# v09 — 晨间纸袋 · Pocketed result deck

Status: Designer-approved R2 Stage 2 pocket-deck handoff; production selection has not been frozen.
Target: desktop/macOS 1280×800, one Scheduled Pulse card with honest layered paper geometry.
Coordinates: VS-002 / CL-002 / X:job-header-pockets / Y:bring-one-paper-forward / Z:opaque-stepped-deck / AppTheme:R2MorningPocket.

## Visual metaphor
Five job papers share a pocket; four retain readable exposed headers while one opens at the front. Set a 1040×636 parent at (120,82), radius 28 and 24px inset. Header 992×40 plus 20px gap leaves a 992×528 pocket. Four rear papers step down by 44px each; the selected front paper begins at y=176 and is 928×336, leaving 16px below. Widths increase 864/880/896/912/928 and are horizontally centered. Every rear header stays 44px tall and unobscured; its hidden body is non-interactive. The front's 24px inset yields an 880px reading width. Use 36px outcome, 20px title, 15px exposed names and 13px schedule/evidence, with 6px tight label spacing. Paper radius is 18, shadow 0 4px 12px at 6% Light / 23% Dark.

## Single P0 focal point
The front paper is 个人数仓晨报, completed 04:01, with a restrained but dominant 36px 5/5 and 阶段通过. Its title appears only in that paper's header. Place one 立即运行 control at the front paper's upper-right reading corner, not on the pocket rim. Five checked folds underneath the number encode the digest's actual passed stages. There is no aggregate health gauge across the whole deck.

## P1/P2 folding
Initial rear-to-front order is Linear @bot 桥接 with 每 1 分钟, 我的 PR with 每 5 分钟, PR 自动审查 with 每 5 分钟, 每日学习推荐 with 每日 04:15, then the selected digest with 每日 04:00. Choose a rear header to bring that same paper forward, repositioning the old front into the vacated layer; never create a second visible title. The front paper's 阶段详情 replaces the large outcome and fold trace with a 168px inset route of ① 个人源采集, ② L2-L3 入仓, ③ Retro-ROI, ④ 学习寻题 and ⑤ Brief 投递 as vertically ordered lines. 查看回执 instead fills that inset with last-completion evidence. The learning front reads 每日 3 题直投 Linear and 3 题, with no five-stage folds. Back papers expose their names, cadence and latest status only.

## Color and surface polarity
Paper roles Light / Dark: desk #F4F0E9 / #161B18; pocket #FFFCF5 / #222C26; front #FFFFFF / #303C33; rear #F1EEE6 / #29342D; ink #2A352C / #F1F4E9; supporting #626C5E / #C0CCB8; commit #4C6542 / #C2DAA9; commit-ink #FFFFFF / #293921; success #2F6A46 / #AAE0B8; failure #AA394B / #FFB4C3; focus #577548 / #DBEFC3. Warm paper and softened forest ink are not permission for low contrast. Rear headers keep supporting text fully readable rather than opacity-dimming an entire paper. Only the front commit and a narrow selected edge use forest color; neutral stepped papers establish depth.

## Liquid Glass optical parameters
The pocket is tactile solid paper, so blur/refraction/chromatic separation are explicitly 0px. Each front surface uses an opaque fill and a 0.5px upper highlight at 8% Light / 6% Dark. Do not add varnish, foils or a refracting overlay to imply depth. Safari renders the measured offsets and shadows unchanged. Reduced Motion keeps the same z-order but relocates papers instantaneously; reduced transparency requires no geometry or palette replacement. This is a spatial folding mechanism, not a swipeable wallet or a drag/reorder feature.

## Inline SVG iconography
Draw a 24×24 open pocket with one rising page corner using 1.6px rounded currentColor strokes. Each header has a small state glyph plus its complete title; the front digest gets a tray-and-check glyph. Stage folds use labelled checkmarks, with 32px-high row targets for details. Entire exposed 44px headers are operable even though the underlying papers overlap. Hidden paper bodies must not trap keyboard focus or announce duplicate content to assistive technology.

## Explicit anti-patterns
Do not flatten the deck into five equal vertical cards, clip rear titles behind the front paper or use duplicate tabs above the stack. Decorative rotations are forbidden because they distort CJK reading and hit areas. No drag handles, fictional wallet balances, history browser or extra jobs. Avoid glass content, high-opacity dark shadows, fake age warnings, in-card theme controls and a global run button detached from the selected paper. Rear papers cannot claim information their hidden bodies do not expose.

## Interaction and states
Boot with aidata-digest frontmost and source records from ../../domain.md at 04:15. A rear-header click brings that original article forward; Tab follows exposed rear headers before the front controls, and Escape closes the front inset. Choosing learning yields its three deliveries, while choosing either PR paper yields its known 04:10 record. Run feedback is printed into the front paper body as 已排队, 运行中, then 刚刚完成 · 耗时 14s; disable that paper's action while busy. If the user changes the front paper mid-run, update the original paper's exposed status, not the new paper. Show 暂无回执 only in an opened missing-evidence inset; failure uses 运行失败 with 立即运行 recovery. Never fill an absent receipt with invented stage timing.

## Stage 2 handoff
main.topology-paper-pocket-deck parents one direct section.content containing header, div[group:paper-pocket] and p[live-status]. The p[live-status] is visually hidden for accessible announcements and consumes no pocket height; visible updates stay on the originating paper. The paper-pocket parents five article[paper] siblings; each article owns header[button:choose-paper plus time plus span:status] and section[paper-body]. The visible body contains output, figure[fold-checks], details[inset-evidence] and div[actions]. Real stacked article siblings and exposed 44px headers are required; merely adding stack-looking class names to an ul is insufficient. Test the five names remain visible exactly once at every reordering, only the front body is focusable, digest expands the five exact stage labels, and learning never presents a digest pipeline. Review actual screenshots for exposed-header occlusion and shadow craft; outline approval does not certify those pixels.
