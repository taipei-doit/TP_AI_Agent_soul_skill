# Text and wording

Scope: all types of work. Every piece of text that people will read must follow these rules, including web pages, messages shown by programs, error messages, instructions in Excel and Word tools and the documents they produce, slides, and delivery notes.

### 1. Basic principles

Every word on a web page (titles, explanations, buttons, error messages, delivery notes) should sound like a case officer talking normally: clear, polite, and not exaggerated. Imagine the text printed on a notice at a service counter, or read aloud to a member of the public over the phone.

The tone may be adjusted for the audience: an educational tool for children can be friendly and conversational, and an event promotion page can be a little livelier. Whatever the tone, do not exaggerate, do not use empty words such as 「賦能」 (empower) or 「一鍵搞定」 (done in one click), and state the information (time, place, eligibility, contact information) clearly. When the case officer specifies a design, emoji may be used as decoration but may not replace text.

- Write 「臺北市」 and 「臺灣」, not 「台北市」 and 「台灣」 (use the formal character 臺, not the informal 台). Use agencies' full official names, written in full the first time they appear (「臺北市政府資訊局」, Department of Information Technology, Taipei City Government); afterwards they may be shortened to 「本局」 (this department).
- Address the public as 「您」 (the polite "you"), and refer to your own agency as 「本局」, 「本處」, or 「本府」 (this department / this office / this City Government).
- Follow the agency's custom for dates. Public services may use 「115 年 10 月 12 日」 (ROC calendar year) or 「2026 年 10 月 12 日」 (Western calendar year), but use only one format throughout a website. This refers to the **display** format.
- Date **input** fields: the browser's built-in date picker (`<input type="date">`) only allows Western calendar years, and its display format follows the computer's language settings. Therefore:
  - For forms filled in by the public, when the website uses ROC calendar years, use three numeric fields for year, month, and day (`inputmode="numeric"`), wrapped in `<fieldset>` and `<legend>` to mark them as one date, for example 「出生日期：民國〔　〕年〔　〕月〔　〕日」 (Date of birth: ROC year [ ] month [ ] day [ ]). Check that the date exists before submitting.
  - For date filters the public uses to search, prefer a "month" drop-down or options such as 「本週、本月」 (this week, this month), so the public does not have to type a date.
  - Filters and data entry in admin back offices (for example event times) may use the built-in date or date-time picker, with the field hint stating 「請以西元年選擇」 (please select using the Western calendar year). Search results and lists are still displayed in ROC calendar years.
  - The database always stores Western calendar dates (ISO format, for example 2026-10-12), converting to ROC calendar years only on screen.
- Put one half-width space between numbers or English and Chinese (「保存 3 年」 "kept for 3 years", 「Excel 檔案」 "Excel file").
- Use full-width punctuation: ，。、；：「」（）. Do not use exclamation marks.
- Do not mix Chinese and English. Write 「上傳」 rather than "upload" and 「網址」 rather than "URL" (proper nouns excepted).
- No emoji by default (when the case officer specifies a design, see the explanation above).

### 2. AI-style wording vs. official wording

| Don't write | Write instead |
|---|---|
| 🚀 立即開始！ (🚀 Start now!) | 開始申請 (Start application) |
| 一鍵搞定、輕鬆完成 (Done in one click, finish with ease) | 填寫完成後按「送出」 (When you have filled it in, press "Submit") |
| 讓我們一起打造更美好的城市 (Let's build a better city together) | （刪掉，直接講這頁能做什麼）(Delete it; say directly what this page does) |
| 賦能、無縫接軌、一站式、全方位、生態系 (empower, seamless, one-stop, all-round, ecosystem) | 講具體做了什麼：「線上就能申請，不用到現場」 (Say concretely what was done: "You can apply online without coming in person") |
| 智慧、創新、數位轉型（當形容詞堆疊）(smart, innovative, digital transformation, piled up as adjectives) | 只在正式計畫名稱裡使用 (Use only in official program names) |
| 歡迎使用本系統！我們很高興為您服務 (Welcome to our system! We are happy to serve you) | 本頁提供 ○○ 線上申請。 (This page provides online application for ○○.) |
| 糟糕！出了點問題 😢 (Oops! Something went wrong 😢) | 系統暫時無法處理您的申請，請稍後再試。如持續發生，請洽 ○○（電話 ○○○○）。 (The system cannot process your application right now. Please try again later. If this keeps happening, please contact ○○ (phone ○○○○).) |
| 恭喜您！提交成功 🎉 (Congratulations! Submitted successfully 🎉) | 已收到您的申請，案件編號 ○○○○。本局將於 7 個工作天內回覆。 (We have received your application, case number ○○○○. This department will reply within 7 working days.) |
| 您的隱私對我們非常重要 (Your privacy is very important to us) | 本局依個人資料保護法蒐集您的資料，僅用於 ○○。 (This department collects your data under the Personal Data Protection Act and uses it only for ○○.) |
| 首先……其次……最後…… (First... second... finally...) | 用「一、二、三、」條列 (List with 「一、二、三、」 numbering) |
| 值得注意的是、需要強調的是 (It is worth noting that, it should be emphasized that) | （刪掉，直接講）(Delete it; just say it) |
| 點擊這裡、了解更多 (Click here, learn more) | 下載申請表、查看收費標準 (Download application form, view fee schedule) |
| 提交 (submit, mainland usage) | 送出 |
| 用戶 (user, mainland usage) | 使用者、民眾、申請人 (user, the public, applicant) |
| 帳戶 (account, mainland usage) | 帳號 |
| 默認 (default, mainland usage) | 預設 |
| 信息 (information/message, mainland usage) | 資訊、訊息 |
| 視頻 (video, mainland usage) | 影片 |
| 質量 (quality, mainland usage) | 品質 |
| 優化 (optimize, mainland usage) | 改善、調整 (improve, adjust) |
| 屏幕 (screen, mainland usage) | 螢幕 |
| 鼠標 (mouse, mainland usage) | 滑鼠 |
| 文件（指檔案時）(document, when meaning a file) | 檔案 |
| 登錄（指登入時）(register, when meaning log in) | 登入 |
| 激活 (activate, mainland usage) | 啟用 |

### 3. Examples

Use the following sentences as a reference for tone.

> 本頁提供長青學苑秋季班線上報名。報名期間為 10 月 1 日至 10 月 15 日，每人限報 1 門課程。名額有限，額滿後將依報名順序列為候補，並以電話通知。
>
> (This page provides online registration for the fall term of the Evergreen Academy for seniors. Registration runs from October 1 to October 15, and each person may register for 1 course. Places are limited; once full, applicants will be waitlisted in order of registration and notified by phone.)

> 收到可疑簡訊？先查再點
>
> (Got a suspicious text message? Check before you click)

These sentences are plain and complete, with no piles of adjectives, and readers know what to do next.
