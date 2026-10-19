// 管理後臺共用程式：手機選單開合、確認對話框。
// 顯示文字一律用 textContent，不使用 innerHTML。

document.addEventListener('DOMContentLoaded', () => {
  // 手機選單：使用者資訊、登出與左側功能選單一起開合
  document.documentElement.classList.add('js');
  const toggle = document.querySelector('.tp-menu-toggle');
  if (toggle) {
    const panels = toggle.getAttribute('aria-controls').split(' ')
      .map((id) => document.getElementById(id)).filter(Boolean);
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      panels.forEach((el) => el.classList.toggle('is-open', !open));
    });
  }

  // 確認對話框：開啟時焦點放在第一個必填欄位，沒有就放在「取消」；關閉後焦點回到原按鈕
  document.querySelectorAll('[data-dialog]').forEach((opener) => {
    opener.addEventListener('click', () => {
      const dialog = document.getElementById(opener.dataset.dialog);
      if (!dialog || typeof dialog.showModal !== 'function') return;
      const target = dialog.querySelector('[data-dialog-target]');
      if (target) target.textContent = opener.dataset.target || '';
      dialog.showModal();
      const first = dialog.querySelector('[required]') || dialog.querySelector('[data-dialog-close]');
      if (first) first.focus();
      dialog.addEventListener('close', () => opener.focus(), { once: true });
    });
  });

  document.querySelectorAll('[data-dialog-close]').forEach((btn) => {
    btn.addEventListener('click', () => btn.closest('dialog').close());
  });
});
