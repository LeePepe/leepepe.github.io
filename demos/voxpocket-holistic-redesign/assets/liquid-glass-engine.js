/*!
 * Apple Liquid Glass — Pure Offline Optical Refraction Engine (v1.0)
 * Zero dependencies · Works directly on file:// · Supports Chromium backdrop-filter
 * and Cross-Browser DOM Lens mode.
 *
 * Synthesizes verified primary techniques from:
 *   - kube.io (Snell's law + Convex Squircle surface profile)
 *   - VII-Cae/hyalite v0.5.0 (Widened-radius SDF direction field, B-channel signed
 *     caustic shade + Fresnel rim, alpha-1 pre-dispersion pin, slope folding)
 *   - samasante/liquid-glass & 0kzh/glisse (Symmetric RGB dispersion, neutral 128 flood)
 *   - rdev/liquid-glass-react (Pointer glint tracking & Fresnel mask border)
 */
(function (root) {
  "use strict";

  const SVG_NS = "http://www.w3.org/2000/svg";
  const XLINK_NS = "http://www.w3.org/1999/xlink";

  const DEFAULTS = {
    bezel: 32,          // Width of curved refractive bezel in px
    thickness: 48,      // Virtual glass slab thickness in px
    ior: 1.5,           // Index of refraction (crown glass = 1.5)
    scaleRatio: 1.0,    // Multiplier on physical max displacement
    slope: 2.2,         // Max displacement decay slope (>1 enables liquid rim folding)
    shape: "squircle",  // 'squircle' | 'circle' | 'lip'
    blur: 1.8,          // Center pre-blur stdDeviation in px (keep <= 4px for crisp refraction)
    dispersion: 1.8,    // Symmetric chromatic aberration separation in px (0 = single pass)
    shade: 0.42,        // Caustic & Fresnel transmission darkening at rim (0..2)
    rim: 1.65,          // In-filter Fresnel specular rim intensity (0..4)
    edgeW: 8,           // Absolute width in px of rim light/shade band
    saturate: 1.45,     // Color saturation boost in the refracted glass
    lightAngle: -135,   // Light source angle in degrees (0 = top, -135 = top-left)
    interactive: true,  // Track pointer position for specular glint & angle
    selfMode: false     // If true, applies `filter: url(#id)` instead of `backdrop-filter`
  };

  const CHANNEL_ONLY = {
    R: "1 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 1 0",
    G: "0 0 0 0 0  0 1 0 0 0  0 0 0 0 0  0 0 0 1 0",
    B: "0 0 0 0 0  0 0 0 0 0  0 0 1 0 0  0 0 0 1 0"
  };

  let svgHost = null;
  let filterSeq = 0;
  let forceSupport = null;
  const instances = new Map(); // HTMLElement -> InstanceState
  const mapCache = new Map();  // key -> { dataUrl, maxDisp, width, height, radii, profile }

  /**
   * Reliable engine check for SVG `backdrop-filter: url(#id)`.
   * Note: `CSS.supports('backdrop-filter', 'url(#x)')` is a false positive in Safari/Firefox,
   * and passing `url(#id)` to Safari drops the entire `backdrop-filter` (losing blur).
   */
  function supportsSvgBackdropFilter() {
    if (forceSupport !== null) return forceSupport;
    if (typeof navigator === "undefined") return false;
    const ua = navigator.userAgent || "";
    const hasUAData = navigator.userAgentData != null;
    const isBlink =
      hasUAData ||
      (/\b(?:Chrome|Chromium|Edg)\//.test(ua) &&
        !/\b(?:CriOS|EdgiOS|FxiOS|OPiOS)\b/.test(ua) &&
        !/iPhone|iPad|iPod/.test(ua));
    return isBlink;
  }

  function ensureSvgHost() {
    if (svgHost && svgHost.isConnected) return svgHost;
    svgHost = document.createElementNS(SVG_NS, "svg");
    svgHost.setAttribute("aria-hidden", "true");
    svgHost.setAttribute("width", "0");
    svgHost.setAttribute("height", "0");
    // Must NEVER be display:none or Chromium ignores the <filter> definitions
    svgHost.style.cssText =
      "position:absolute;top:0;left:0;width:0;height:0;overflow:hidden;pointer-events:none;z-index:-1";
    const defs = document.createElementNS(SVG_NS, "defs");
    defs.id = "lg-svg-defs";
    svgHost.appendChild(defs);
    document.body.appendChild(svgHost);
    return svgHost;
  }

  function svgEl(tag, attrs) {
    const el = document.createElementNS(SVG_NS, tag);
    for (const [k, v] of Object.entries(attrs || {})) {
      el.setAttribute(k, String(v));
    }
    return el;
  }

  /* ------------------------------------------------------------------------
   * Optical Physics & Surface Equations
   * --------------------------------------------------------------------- */

  // Quarter circle: H_c(t) = sqrt(1 - (1 - t)^2)
  const heightCircle = (t) => Math.sqrt(Math.max(0, 1 - (1 - t) * (1 - t)));

  // Apple Convex Squircle: H_s(t) = (1 - (1 - t)^4)^(1/4)
  const heightSquircle = (t) =>
    Math.pow(Math.max(0, 1 - Math.pow(1 - t, 4)), 0.25);

  // Switch Lip (raised outer rim + shallow inner concave dip):
  const heightLip = (t) =>
    heightCircle(t) + 0.3 * Math.pow(Math.sin(Math.PI * t), 2) * Math.cos(Math.PI * t);

  function getSurfaceFn(shape) {
    if (shape === "circle") return heightCircle;
    if (shape === "lip") return heightLip;
    return heightSquircle;
  }

  // Unpolarized Fresnel reflectance for air (n1=1) -> glass (n2=ior)
  function fresnelReflectance(alpha, ior) {
    const a = Math.abs(alpha);
    const sinBeta = Math.sin(a) / ior;
    if (sinBeta >= 1) return 1;
    if (a < 1e-4) {
      const r0 = (1 - ior) / (1 + ior);
      return r0 * r0;
    }
    const beta = Math.asin(sinBeta);
    const rs = Math.sin(a - beta) / Math.sin(a + beta);
    const rp = Math.tan(a - beta) / Math.tan(a + beta);
    return Math.min(1, 0.5 * (rs * rs + rp * rp));
  }

  // Snell's Law Ray Refraction at distance `d` from outer edge (0 <= d <= B)
  function sampleBezelRay(d, B, thickness, ior, H) {
    const x = Math.min(1, Math.max(0, d / B));
    const eps = 1e-3;
    const x1 = Math.min(1, x + eps);
    const x0 = Math.max(0, x - eps);
    const deriv = (H(x1) - H(x0)) / (x1 - x0);
    const alpha = Math.atan(deriv); // Surface slope angle
    const beta =
      Math.sign(alpha) *
      Math.asin(Math.min(1, Math.sin(Math.abs(alpha)) / ior));
    const remainingHeight = thickness + B * heightCircle(x);
    const disp = remainingHeight * Math.tan(alpha - beta);
    return { disp, alpha };
  }

  // Rounded rectangle Signed Distance Function (negative inside) with per-corner radii [tl, tr, br, bl]
  function makeRoundedRectSDF(W, H, radii) {
    const cx = W / 2;
    const cy = H / 2;
    return (px, py) => {
      const dx = px - cx;
      const dy = py - cy;
      const R =
        dx < 0 ? (dy < 0 ? radii[0] : radii[3]) : dy < 0 ? radii[1] : radii[2];
      const qx = Math.abs(dx) - (W / 2 - R);
      const qy = Math.abs(dy) - (H / 2 - R);
      const ox = Math.max(qx, 0);
      const oy = Math.max(qy, 0);
      return Math.min(Math.max(qx, qy), 0) + Math.hypot(ox, oy) - R;
    };
  }

  // Parse element's 4 corner radii with CSS adjacent-corner overlap scaling
  function readElementRadii(el, W, H) {
    const cs = getComputedStyle(el);
    const parseOne = (val) => {
      const token = String(val).trim().split(/\s+/)[0] || "0";
      const num = parseFloat(token);
      if (!Number.isFinite(num)) return 0;
      return Math.max(0, token.endsWith("%") ? (num / 100) * Math.min(W, H) : num);
    };
    const r = [
      cs.borderTopLeftRadius,
      cs.borderTopRightRadius,
      cs.borderBottomRightRadius,
      cs.borderBottomLeftRadius
    ].map(parseOne);

    let scaleFactor = 1;
    const edges = [
      [W, r[0] + r[1]],
      [H, r[1] + r[2]],
      [W, r[2] + r[3]],
      [H, r[3] + r[0]]
    ];
    for (const [len, sum] of edges) {
      if (sum > len && sum > 0) {
        scaleFactor = Math.min(scaleFactor, len / sum);
      }
    }
    return scaleFactor < 1 ? r.map((v) => v * scaleFactor) : r;
  }

  /* ------------------------------------------------------------------------
   * Displacement & Specular/Caustic Map Generator (R=dx, G=dy, B=signed Rim)
   * --------------------------------------------------------------------- */

  function generateOpticalMap(W, H, radii, opts) {
    const cacheKey = [
      W,
      H,
      radii.map((r) => r.toFixed(1)).join(","),
      opts.bezel,
      opts.thickness,
      opts.ior,
      opts.slope,
      opts.shape,
      opts.shade,
      opts.rim,
      opts.edgeW,
      opts.lightAngle
    ].join("|");

    if (mapCache.has(cacheKey)) {
      return mapCache.get(cacheKey);
    }

    const shortSide = Math.min(W, H);
    const B = Math.max(2, Math.min(opts.bezel, Math.floor(shortSide / 2) - 1));
    const Hfn = getSurfaceFn(opts.shape);

    // 1. Precompute 1D radial displacement & signed edge lighting LUT along bezel [0..B]
    const STEP = 0.25;
    const N = Math.ceil(B / STEP);
    const dispLut = new Float64Array(N + 1);
    dispLut[N] = 0;

    for (let i = N - 1; i >= 0; i--) {
      const raw = sampleBezelRay(i * STEP, B, opts.thickness, opts.ior, Hfn).disp;
      dispLut[i] = Math.min(raw, dispLut[i + 1] + opts.slope * STEP);
    }

    const maxDisp = Math.max(...Array.from(dispLut, Math.abs), 1e-4);

    const edgeLut = new Float64Array(N + 1);
    const causticGainLut = new Float64Array(N + 1);
    const ABSORB_RATIO = 0.5 / 0.46;
    const GLOW_RATIO = 0.4 / 1.76;
    const SPEC_EXPONENT = 42;

    for (let i = 0; i <= N; i++) {
      const d = i * STEP;
      const ray = sampleBezelRay(d, B, opts.thickness, opts.ior, Hfn);
      // Caustic energy density ratio in sRGB (^1/2.2)
      const linearGain = Math.max(
        0.02,
        1 + (dispLut[Math.min(N, i + 1)] - dispLut[i]) / STEP
      );
      const srgbGain = Math.pow(linearGain, 1 / 2.2);
      causticGainLut[i] = srgbGain;

      const windowEnv = Math.exp((-2.5 * d) / Math.max(1, opts.edgeW));
      const slopeSin = Math.max(0, Math.sin(ray.alpha));
      const fresnel = fresnelReflectance(ray.alpha, opts.ior);

      const specularAdd =
        fresnel * opts.rim * GLOW_RATIO +
        Math.pow(slopeSin, SPEC_EXPONENT) * opts.rim;
      const shadeSub =
        (1 - srgbGain) * opts.shade + fresnel * opts.shade * ABSORB_RATIO;

      edgeLut[i] = (specularAdd - shadeSub) * windowEnv;
    }

    const sampleLut = (lut, d) => {
      const f = Math.min(N - 1e-6, Math.max(0, d) / STEP);
      const idx = Math.floor(f);
      const frac = f - idx;
      return lut[idx] * (1 - frac) + lut[idx + 1] * frac;
    };

    // 2. Build 2D SDF & Widened-Radius Direction Field (prevents corner ridges & circle cross-seams)
    const sdf = makeRoundedRectSDF(W, H, radii);
    const maxDirRadius = shortSide / 2 - 0.5;
    const sdfDir = makeRoundedRectSDF(
      W,
      H,
      radii.map((r) => Math.min(r + B, maxDirRadius))
    );

    const MAX_PIXELS = 260000;
    const resScale = Math.min(1, Math.sqrt(MAX_PIXELS / Math.max(1, W * H)));
    const MW = Math.max(4, Math.round(W * resScale));
    const MH = Math.max(4, Math.round(H * resScale));

    const canvas = document.createElement("canvas");
    canvas.width = MW;
    canvas.height = MH;
    const ctx = canvas.getContext("2d");
    const imgData = ctx.createImageData(MW, MH);
    const data = imgData.data;

    const lightRad = (opts.lightAngle * Math.PI) / 180;
    const Lx = Math.sin(lightRad);
    const Ly = -Math.cos(lightRad);

    let curDisp = 0;
    let curEdge = 0;

    const directionalEdge = (nx, ny) => {
      if (curEdge <= 0) return curEdge; // Caustic shade applies all around
      const dot = nx * Lx + ny * Ly;
      // Primary light side (0.80) + opposite secondary internal bounce (0.32)
      return curEdge * (Math.max(0, dot) * 0.8 + Math.max(0, -dot) * 0.32);
    };

    const writePixel = (x, y, inX, inY, litVal) => {
      const idx = (y * MW + x) * 4;
      // R = X inward displacement (128 = neutral)
      data[idx] = Math.round(
        Math.max(0, Math.min(255, 128 + (inX * curDisp / maxDisp) * 127))
      );
      // G = Y inward displacement (128 = neutral)
      data[idx + 1] = Math.round(
        Math.max(0, Math.min(255, 128 + (inY * curDisp / maxDisp) * 127))
      );
      // B = Signed edge profile (128 = neutral, <128 shade, >128 Fresnel glint)
      data[idx + 2] = Math.round(
        Math.max(0, Math.min(255, 128 + litVal * 127))
      );
      data[idx + 3] = 255;
    };

    const isSymmetric =
      radii[0] === radii[1] && radii[1] === radii[2] && radii[2] === radii[3];
    const limitX = isSymmetric ? Math.ceil(MW / 2) : MW;
    const limitY = isSymmetric ? Math.ceil(MH / 2) : MH;
    const eps = 0.5;

    for (let y = 0; y < limitY; y++) {
      for (let x = 0; x < limitX; x++) {
        const px = (x + 0.5) / resScale;
        const py = (y + 0.5) / resScale;
        const depth = -sdf(px, py);

        let nx = 0;
        let ny = 0;
        curDisp = 0;
        curEdge = 0;

        if (depth > -1 && depth < B) {
          const clampedDepth = Math.max(0, depth);
          // Smooth 1px anti-aliasing feather right at the outer contour
          const aa = depth < 0 ? Math.max(0, 1 + depth) : 1;
          curDisp = sampleLut(dispLut, clampedDepth) * aa;
          curEdge = sampleLut(edgeLut, clampedDepth) * aa;

          nx = (sdfDir(px + eps, py) - sdfDir(px - eps, py)) / (2 * eps);
          ny = (sdfDir(px, py + eps) - sdfDir(px, py - eps)) / (2 * eps);
          const len = Math.hypot(nx, ny) || 1;
          nx /= len;
          ny /= len;
        }

        // Inward sampling: negate outward normal (-nx, -ny)
        writePixel(x, y, -nx, -ny, directionalEdge(nx, ny));

        if (isSymmetric) {
          const mx = MW - 1 - x;
          const my = MH - 1 - y;
          if (mx !== x) writePixel(mx, y, nx, -ny, directionalEdge(-nx, ny));
          if (my !== y) writePixel(x, my, -nx, ny, directionalEdge(nx, -ny));
          if (mx !== x && my !== y) {
            writePixel(mx, my, nx, ny, directionalEdge(-nx, -ny));
          }
        }
      }
    }

    ctx.putImageData(imgData, 0, 0);
    const result = {
      dataUrl: canvas.toDataURL("image/png"),
      maxDisp,
      width: W,
      height: H,
      mapWidth: MW,
      mapHeight: MH,
      bezel: B,
      radii: radii.slice(),
      profile: {
        step: STEP,
        disp: Array.from(dispLut),
        edge: Array.from(edgeLut),
        causticGain: Array.from(causticGainLut)
      }
    };

    if (mapCache.size > 32) {
      const oldestKey = mapCache.keys().next().value;
      mapCache.delete(oldestKey);
    }
    mapCache.set(cacheKey, result);
    return result;
  }

  /* ------------------------------------------------------------------------
   * SVG Filter Graph Builder
   * --------------------------------------------------------------------- */

  function buildSvgFilterElement(filterId, mapData, opts) {
    const filter = svgEl("filter", {
      id: filterId,
      filterUnits: "objectBoundingBox",
      primitiveUnits: "userSpaceOnUse",
      x: "0",
      y: "0",
      width: "1",
      height: "1",
      "color-interpolation-filters": "sRGB"
    });

    // 1. Neutral 128 grey backdrop to prevent dark/warped edge fringes
    filter.appendChild(
      svgEl("feFlood", {
        "flood-color": "rgb(128,128,128)",
        "flood-opacity": "1",
        result: "neutralBg"
      })
    );

    // 2. Load baked Snell Squircle RGBA map
    const feImg = svgEl("feImage", {
      preserveAspectRatio: "none",
      result: "rawMap"
    });
    feImg.setAttribute("href", mapData.dataUrl);
    feImg.setAttributeNS(XLINK_NS, "xlink:href", mapData.dataUrl);
    filter.appendChild(feImg);

    filter.appendChild(
      svgEl("feComposite", {
        in: "rawMap",
        in2: "neutralBg",
        operator: "over",
        result: "map"
      })
    );

    const baseScale = 2 * mapData.maxDisp * (opts.scaleRatio ?? 1.0);

    // 3. Pre-blur + Alpha-1 Pin (prevents 3x premultiplied white hairline at box boundary)
    let sourceNode = "SourceGraphic";
    if (opts.blur > 0) {
      filter.appendChild(
        svgEl("feGaussianBlur", {
          in: "SourceGraphic",
          stdDeviation: String(opts.blur),
          result: "blurredRaw"
        })
      );
      if (!opts.selfMode) {
        filter.appendChild(
          svgEl("feColorMatrix", {
            in: "blurredRaw",
            type: "matrix",
            values: "1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 0 1",
            result: "blurredOpaque"
          })
        );
        sourceNode = "blurredOpaque";
      } else {
        sourceNode = "blurredRaw";
      }
    }

    // 4. Optical Refraction + Symmetric 3-Channel Chromatic Aberration
    if (opts.dispersion > 0 && !opts.selfMode) {
      const deltaScale = 2 * opts.dispersion;
      const scales = {
        R: baseScale - deltaScale,
        G: baseScale,
        B: baseScale + deltaScale
      };
      for (const ch of ["R", "G", "B"]) {
        filter.appendChild(
          svgEl("feDisplacementMap", {
            in: sourceNode,
            in2: "map",
            scale: scales[ch].toFixed(2),
            xChannelSelector: "R",
            yChannelSelector: "G",
            result: `disp_${ch}`
          })
        );
        filter.appendChild(
          svgEl("feColorMatrix", {
            in: `disp_${ch}`,
            type: "matrix",
            values: CHANNEL_ONLY[ch],
            result: `ch_${ch}`
          })
        );
      }
      filter.appendChild(
        svgEl("feComposite", {
          in: "ch_R",
          in2: "ch_G",
          operator: "arithmetic",
          k1: "0",
          k2: "1",
          k3: "1",
          k4: "0",
          result: "ch_RG"
        })
      );
      filter.appendChild(
        svgEl("feComposite", {
          in: "ch_RG",
          in2: "ch_B",
          operator: "arithmetic",
          k1: "0",
          k2: "1",
          k3: "1",
          k4: "0",
          result: "refracted"
        })
      );
    } else {
      filter.appendChild(
        svgEl("feDisplacementMap", {
          in: sourceNode,
          in2: "map",
          scale: baseScale.toFixed(2),
          xChannelSelector: "R",
          yChannelSelector: "G",
          result: "refracted"
        })
      );
    }

    // 5. Saturation Boost
    let currentResult = "refracted";
    if (opts.saturate && opts.saturate !== 1) {
      filter.appendChild(
        svgEl("feColorMatrix", {
          in: currentResult,
          type: "saturate",
          values: String(opts.saturate),
          result: "saturated"
        })
      );
      currentResult = "saturated";
    }

    // 6. Blue-Channel Caustic & Fresnel Transmission Shade (values < 128 multiply down)
    if (opts.shade > 0 && !opts.selfMode) {
      filter.appendChild(
        svgEl("feColorMatrix", {
          in: "map",
          type: "matrix",
          values: "0 0 1 0 0  0 0 1 0 0  0 0 1 0 0  0 0 0 0 1",
          result: "edgeBlueRGB"
        })
      );
      const shadeTransfer = svgEl("feComponentTransfer", {
        in: "edgeBlueRGB",
        result: "shadeMask"
      });
      for (const ch of ["R", "G", "B"]) {
        shadeTransfer.appendChild(
          svgEl(`feFunc${ch}`, { type: "table", tableValues: "0 1 1" })
        );
      }
      filter.appendChild(shadeTransfer);
      filter.appendChild(
        svgEl("feBlend", {
          in: currentResult,
          in2: "shadeMask",
          mode: "multiply",
          result: "shaded"
        })
      );
      currentResult = "shaded";
    }

    // 7. Blue-Channel Fresnel Specular Rim Glint (values > 128 add white highlight)
    if (opts.rim > 0 && !opts.selfMode) {
      filter.appendChild(
        svgEl("feColorMatrix", {
          in: "map",
          type: "matrix",
          values: "0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 1 0 0",
          result: "rimAlpha"
        })
      );
      const rimTransfer = svgEl("feComponentTransfer", {
        in: "rimAlpha",
        result: "rimHighlight"
      });
      rimTransfer.appendChild(
        svgEl("feFuncA", { type: "table", tableValues: "0 0 1" })
      );
      filter.appendChild(rimTransfer);
      filter.appendChild(
        svgEl("feComposite", {
          in: "rimHighlight",
          in2: currentResult,
          operator: "over",
          result: "finalGlass"
        })
      );
    }

    return filter;
  }

  /* ------------------------------------------------------------------------
   * DOM Attachment, ResizeObserver & Interactive Pointer Tracking
   * --------------------------------------------------------------------- */

  function updateElementGlass(el) {
    const state = instances.get(el);
    if (!state) return;

    const W = Math.round(el.offsetWidth || el.getBoundingClientRect().width);
    const H = Math.round(el.offsetHeight || el.getBoundingClientRect().height);
    if (W < 4 || H < 4) return;

    const opts = state.opts;
    const radii = readElementRadii(el, W, H);
    const mapData = generateOpticalMap(W, H, radii, opts);
    state.lastMap = mapData;

    const hostDefs = ensureSvgHost().querySelector("#lg-svg-defs");
    if (state.filterEl) {
      state.filterEl.remove();
    }

    // Bump filter ID on every update so WebKit/Blink never serve stale cached filter output
    const filterId = `lg-opt-filter-${++filterSeq}`;
    const filterEl = buildSvgFilterElement(filterId, mapData, opts);
    hostDefs.appendChild(filterEl);
    state.filterEl = filterEl;
    state.filterId = filterId;

    if (opts.selfMode) {
      el.style.filter = `url(#${filterId})`;
      el.setAttribute("data-lg-refractive", "true");
    } else if (supportsSvgBackdropFilter()) {
      const filterChain = `url(#${filterId}) brightness(var(--lg-brightness, 104%)) contrast(var(--lg-contrast, 104%))`;
      el.style.setProperty("--lg-backdrop-filter", filterChain);
      el.setAttribute("data-lg-refractive", "true");
    } else {
      el.style.removeProperty("--lg-backdrop-filter");
      el.setAttribute("data-lg-refractive", "false");
    }

    if (typeof opts.onUpdate === "function") {
      opts.onUpdate({
        filterId,
        mapData,
        options: opts,
        supported: supportsSvgBackdropFilter()
      });
    }
  }

  function setupPointerTracking(el) {
    const onMove = (e) => {
      const rect = el.getBoundingClientRect();
      if (!rect.width || !rect.height) return;
      const xPct = ((e.clientX - rect.left) / rect.width) * 100;
      const yPct = ((e.clientY - rect.top) / rect.height) * 100;
      el.style.setProperty("--lg-mouse-x", `${xPct.toFixed(1)}%`);
      el.style.setProperty("--lg-mouse-y", `${yPct.toFixed(1)}%`);

      // Subtle dynamic tilt of the Fresnel specular angle toward the pointer
      const dx = (e.clientX - (rect.left + rect.width / 2)) / (rect.width / 2);
      const dy = (e.clientY - (rect.top + rect.height / 2)) / (rect.height / 2);
      const dynamicAngle = 135 + dx * 18 - dy * 12;
      el.style.setProperty("--lg-angle", `${dynamicAngle.toFixed(1)}deg`);
    };
    el.addEventListener("pointermove", onMove, { passive: true });
    return () => el.removeEventListener("pointermove", onMove);
  }

  function attach(el, userOpts = {}) {
    if (!el) return null;
    if (instances.has(el)) {
      detach(el);
    }

    const opts = Object.assign({}, DEFAULTS, userOpts);
    const state = {
      el,
      opts,
      filterId: null,
      filterEl: null,
      lastMap: null,
      cleanupPointer: null,
      resizeObserver: null
    };
    instances.set(el, state);

    if (opts.interactive) {
      state.cleanupPointer = setupPointerTracking(el);
    }

    let rafId = 0;
    state.resizeObserver = new ResizeObserver(() => {
      cancelAnimationFrame(rafId);
      rafId = requestAnimationFrame(() => updateElementGlass(el));
    });
    state.resizeObserver.observe(el);

    updateElementGlass(el);
    return {
      update(newOpts = {}) {
        Object.assign(state.opts, newOpts);
        updateElementGlass(el);
      },
      getState() {
        return state;
      },
      destroy() {
        detach(el);
      }
    };
  }

  function detach(el) {
    const state = instances.get(el);
    if (!state) return;
    if (state.resizeObserver) state.resizeObserver.disconnect();
    if (state.cleanupPointer) state.cleanupPointer();
    if (state.filterEl) state.filterEl.remove();
    el.style.removeProperty("--lg-backdrop-filter");
    el.style.removeProperty("filter");
    el.removeAttribute("data-lg-refractive");
    instances.delete(el);
  }

  function attachAll(selector = "[data-liquid-glass]", opts = {}) {
    const nodes = document.querySelectorAll(selector);
    return Array.from(nodes).map((node) => attach(node, opts));
  }

  /**
   * Exports a 100% self-contained, zero-JS HTML + CSS + inline SVG snippet
   * with the element's baked PNG Data URI displacement map embedded directly.
   */
  function exportStandaloneSnippet(el) {
    const state = instances.get(el);
    if (!state || !state.filterEl || !state.lastMap) return "";
    const cloneFilter = state.filterEl.cloneNode(true);
    cloneFilter.id = "apple-liquid-glass-filter";
    const { width, height, radii } = state.lastMap;
    const radiusPx = Math.round(radii[0] || 28);

    return `<!-- Apple Liquid Glass — Standalone Zero-JS HTML + CSS + Inline SVG Snippet
     Baked for ${width}x${height}px (radius ${radiusPx}px). -->
<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" aria-hidden="true"
     style="position:absolute;width:0;height:0;overflow:hidden;pointer-events:none">
  <defs>
    ${cloneFilter.outerHTML}
  </defs>
</svg>

<div class="lg-surface" style="width:${width}px;height:${height}px;--lg-radius:${radiusPx}px;--lg-backdrop-filter:url(#apple-liquid-glass-filter) brightness(104%) contrast(104%);">
  <!-- Your content here -->
</div>`;
  }

  root.LiquidGlass = {
    DEFAULTS,
    attach,
    detach,
    attachAll,
    supportsSvgBackdropFilter,
    force(val) {
      forceSupport = val === null ? null : Boolean(val);
      for (const el of instances.keys()) updateElementGlass(el);
      return supportsSvgBackdropFilter();
    },
    generateOpticalMap,
    exportStandaloneSnippet
  };
})(typeof window !== "undefined" ? window : globalThis);
