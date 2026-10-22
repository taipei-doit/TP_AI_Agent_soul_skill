// 表單檢查：錯誤訊息寫在欄位下方，並把焦點移到第一個錯誤欄位。
// 顯示文字一律用 textContent，不使用 innerHTML。

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('apply-form');
  if (!form) return;

  const status = document.getElementById('form-status');
  const submitBtn = form.querySelector('button[type="submit"]');
  let sending = false;

  const rules = {
    name: (v) => (v.trim() ? '' : '請填寫姓名。'),
    phone: (v) => (/^09\d{8}$/.test(v.trim()) ? '' : '手機號碼應為 10 碼數字，例：0912345678。'),
    email: (v) => (!v.trim() || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) ? '' : '電子郵件格式不正確，例：name@example.com。'),
    agree: (_, el) => (el.checked ? '' : '請勾選「我已閱讀上方個人資料蒐集告知」。'),
  };

  function setError(input, message) {
    const err = document.getElementById(input.id + '-err');
    if (message) {
      input.setAttribute('aria-invalid', 'true');
      err.textContent = message;
      err.hidden = false;
    } else {
      input.removeAttribute('aria-invalid');
      err.textContent = '';
      err.hidden = true;
    }
  }

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    if (sending) return;

    let firstInvalid = null;
    for (const [id, check] of Object.entries(rules)) {
      const input = form.elements[id];
      if (!input) continue;
      const message = check(input.value, input);
      setError(input, message);
      if (message && !firstInvalid) firstInvalid = input;
    }

    status.className = 'tp-status';
    if (firstInvalid) {
      status.classList.add('tp-status--error');
      status.textContent = '有欄位需要修正，請依欄位下方說明填寫。';
      firstInvalid.focus();
      return;
    }

    sending = true;
    submitBtn.setAttribute('aria-busy', 'true');
    status.textContent = '資料送出中，請稍候。';

    try {
      // 〔請換成實際的送出程式〕
      // const res = await fetch('/api/apply', { method: 'POST', body: new FormData(form) });
      // if (!res.ok) throw new Error();
      status.classList.add('tp-status--success');
      status.textContent = '已收到您的申請。〔本局將於 7 個工作天內以電話與您聯繫。〕';
      form.reset();
    } catch {
      status.classList.add('tp-status--error');
      status.textContent = '系統暫時無法處理您的申請，請稍後再試。如持續發生，請洽〔聯絡電話〕。';
    } finally {
      sending = false;
      submitBtn.removeAttribute('aria-busy');
    }
  });
});
