(function () {
  const b = document.body;
  const actions = [...document.querySelectorAll('[data-r3-action]')];
  const f = document.querySelector('.r3-feedback');
  const text = document.querySelector('.r3-sentence');
  if (!actions.length) return;
  const split = b.classList.contains('v09');
  const sentence = '把会议里的决定整理成一条清晰行动。';
  let state = 'idle', revision = 0;

  function status(message) {
    f.textContent = b.classList.contains('v08') ? '' : message;
    f.setAttribute('aria-label', message);
    if (b.classList.contains('v08')) {
      actions[0].setAttribute('aria-label', `${actionLabel(0)}；${message}`);
    }
  }

  function selectSentence() {
    const range = document.createRange();
    range.selectNodeContents(text);
    const selection = getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
  }

  async function attemptCopy(atRevision) {
    let message;
    try {
      if (!navigator.clipboard?.writeText) {
        message = '剪贴板不可用 · 精炼句已选择';
      } else {
        await navigator.clipboard.writeText(text.textContent);
        message = '已复制模拟精炼句';
      }
    } catch {
      message = '复制失败 · 精炼句已选择';
    }
    if (revision !== atRevision) return;
    if (message.includes('已选择')) selectSentence();
    status(message);
  }

  function actionLabel(i) {
    if (split) {
      if (i === 0) return state === 'recording' ? '重新开始模拟重录' : '开始模拟重录';
      return state === 'recording' ? '完成模拟录音' : '复制精炼文本';
    }
    return {idle: '开始模拟录音', recording: '完成模拟录音',
      refined: '复制精炼文本', copied: '再次模拟录音'}[state];
  }

  function render() {
    b.classList.toggle('r3-recording', state === 'recording');
    b.classList.toggle('r3-refined', state === 'refined' || state === 'copied');
    actions.forEach((a, i) => {
      a.setAttribute('aria-label', actionLabel(i));
      if (split) {
        a.textContent = i === 0 ? (state === 'recording' ? '重新录音' : '声波重录')
          : (state === 'recording' ? '完成录音' : '一键复制');
      }
      a.setAttribute('aria-pressed', String(state === 'recording' && (!split || i === 0)));
    });
    if (state === 'refined' || state === 'copied') text.textContent ||= sentence;
    if (state === 'idle') status('模拟录音与语音处理');
    else if (state === 'recording') status(split ? '模拟重录中 · 右侧完成录音' : '模拟录音中 · 再次轻触完成');
    else if (state === 'refined') status('模拟精炼完成 · 再次轻触复制');
    else status('正在尝试复制模拟精炼句');
  }

  function transition(kind) {
    revision++;
    if (split && kind === 'rerecord') state = 'recording';
    else if (split) state = state === 'recording' ? 'refined' : 'copied';
    else if (state === 'idle' || state === 'copied') state = 'recording';
    else state = state === 'recording' ? 'refined' : 'copied';
    render();
    if (state === 'copied') void attemptCopy(revision);
  }

  actions.forEach((a, i) => {
    a.addEventListener('click', () => transition(split && i === 0 ? 'rerecord' : 'primary'));
  });
  const previous = document.querySelector('[data-previous]');
  if (previous) previous.addEventListener('click', () => {
    revision++;
    text.textContent = '上一段：下周发布准备。';
    status('已选择上一段模拟录音');
  });
  render();
})();
