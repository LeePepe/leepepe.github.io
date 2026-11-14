(() => {
  const instances = new Map();
  const webkit = !LiquidGlass.supportsSvgBackdropFilter();
  document.documentElement.classList.toggle('webkit', webkit);
  window.RichOptics = {
    instances,
    refresh(root = document) {
      root.querySelectorAll('[data-liquid-glass]').forEach(el => {
        if (!el.getBoundingClientRect().width || !el.getBoundingClientRect().height) return;
        if (instances.has(el)) { instances.get(el).update(); return; }
        const veil = el.querySelector('.caustic-veil');
        const instance = LiquidGlass.attach(el, {
          blur: 1.8, bezel: 24, dispersion: 1.8,
          onUpdate({filterId, mapData}) {
            el.dataset.opticalFilter = filterId;
            if (veil && webkit) veil.style.filter = `url(#${filterId})`;
            el.dataset.mapSize = `${mapData.mapWidth}x${mapData.mapHeight}`;
          }
        });
        instances.set(el, instance);
      });
    }
  };
  addEventListener('DOMContentLoaded', () => RichOptics.refresh());
})();
