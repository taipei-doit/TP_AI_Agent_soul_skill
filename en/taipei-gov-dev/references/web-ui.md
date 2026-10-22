# Web page design guidelines

Scope: web pages that other people will see (public websites, registration pages, admin back offices). For small tools used only on your own computer, the short rules in section 0, "Internal small tools," are enough.

> Markers: [Law] an explicit legal provision; [Gov] a guideline or rule of the Executive Yuan or the Taipei City Government; [Rec] a practice recommended by these guidelines. For the original texts of laws and their sources, see `legal-sources.md`.

### 0. Internal small tools

Small tools used only by you or colleagues in your section on your own computers (work type B) do not need the full set of website rules. They only need to meet the following: [Rec]

- Link `templates/web/assets/tp.css` and use its colors and fonts. Do not design new ones.
- Use the City Government's official style by default, following the default design in section 8, "Styles to avoid," and do not add decoration of your own. When the case officer asks for another style, follow section 8 (2) and (3).
- Do not use wording typical of AI. Phrases such as 「一鍵搞定」 (done in one click), 「輕鬆完成」 (finish with ease), 「賦能」 (empower), 「無縫接軌」 (seamless), 「🚀 開始使用」 (🚀 Get started), and 「糟糕！出了點問題」 (Oops! Something went wrong) must not appear. Replace them with official wording using the table in `writing.md` section 2. Button labels are verbs (「開始整理」 "Start sorting", 「下載結果」 "Download results"), and error messages explain in plain language what to do.
- Put the tool's name and a sentence or two about its purpose at the top of the page.
- No bureau logo, footer, four-color city emblem bar, accessibility statement, or accessibility mark is needed.
- Meet the basic accessibility items in `accessibility.md` section 3.
- If the tool will later be offered to the public, follow all rules in this file.

### 1. Design direction

A City Government website is not a commercial product page. It does not need to catch the eye. It needs to be understood at a glance and used with confidence.

- Like an official document: the agency's name, a clear title, and itemized explanations numbered 「一、二、三、」 (1, 2, 3).
- Like MRT signage: important things are larger and come first, and each page does one main thing.
- Restrained color: large areas are black text on white, and the primary color is used only for buttons, links, and headings.
- Little decoration: separate sections with thin lines, not card shadows, gradients, or animation.

### 2. Colors

Below is the default palette. Contrast ratios for all text colors have already been calculated. An agency with its own signature color may substitute it, but must recalculate the contrast ratio, which must not fall below the values required in `accessibility.md`.

| Use | Variable name | Color code | Contrast on white | Notes |
|---|---|---|---|---|
| Primary | `--tp-primary` | `#0F5C86` | 7.25 : 1 | Buttons, links, focus outlines |
| Primary (dark) | `--tp-primary-dark` | `#094463` | 10.40 : 1 | Button hover, links on light backgrounds |
| Primary (tint) | `--tp-primary-tint` | `#E9F2F7` | — | Background only, never text |
| Heading ink | `--tp-ink` | `#16324A` | 13.21 : 1 | h1, h2, item numbers |
| Body text | `--tp-text` | `#212529` | 15.43 : 1 | Regular text |
| Secondary text | `--tp-text-muted` | `#495057` | 8.18 : 1 | Notes, footer, dates |
| Page background | `--tp-bg` | `#FAFBFC` | — | A paper-like white |
| Content background | `--tp-surface` | `#FFFFFF` | — | Forms, tables |
| Notice band background | `--tp-band` | `#F1F6FA` | — | Key notice blocks |
| Divider | `--tp-border` | `#DEE2E6` | — | Decorative lines only |
| Input border | `--tp-border-input` | `#6C757D` | 4.69 : 1 | Field outlines (must be 3:1 or higher) |
| Error | `--tp-danger` | `#A61E1E` | 7.43 : 1 | Error messages |
| Success | `--tp-success` | `#14532D` | 9.11 : 1 | Success messages |
| Caution | `--tp-warning` | `#6F3404` | 9.68 : 1 | Points to note |
| Information | `--tp-info` | `#0B3A66` | 11.59 : 1 | General notices |

**The four city emblem colors**: red `#C64B4B`, yellow `#DFA92E`, green `#2F9464`, blue `#2B6CB0`. These four colors may only be used in one thin 4px bar under the title, appearing once per page, as the City Government's identifying mark. They must not be used for large background areas, buttons, or text.

Note: on light backgrounds (`#F1F6FA`, `#E9F2F7`), the primary color `#0F5C86` drops below 7:1 contrast. For AAA pages, use `--tp-primary-dark` for links and text on light backgrounds.

### 3. Fonts

```css
--tp-font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC",
                "PingFang TC", "Microsoft JhengHei", Arial, sans-serif;
--tp-font-serif: "Noto Serif TC", "PMingLiU", "MingLiU", serif;
```

- Body text uses a sans-serif (system fonts), with nothing extra to download.
- The page title (h1) and section headings (h2) may use a serif (Ming) typeface to convey the formality of an official document. By default the serif uses fonts built into the computer. For a consistent look, you may download Noto Serif TC Bold (700) and self-host it in `assets/`.
- Use only three font weights: 400 (body), 600 (emphasis), 700 (headings).
- Body text is 16px or larger, with a line height of about 1.8.
- Do not use Latin fonts such as Inter, Poppins, or Montserrat as the main font. Chinese text falls back to the system font, and the page looks like a foreign product with Chinese pasted on.

### 4. Bureau logo

Every website places the bureau's own logo at the top left of the header, so the public can tell at a glance which agency provides the service.

**How to obtain it**

1. The AI finds the logo on the agency's official website, so the case officer does not have to prepare it. Most Taipei City bureau websites are at `<agency English abbreviation>.gov.taipei`, for example the Department of Information Technology at `doit.gov.taipei` and the Department of Civil Affairs at `ca.gov.taipei`. If you are not sure of the address, find the link in the agency list on the Taipei City Government portal (`www.gov.taipei`).
2. The logo in the website header may be an `<img>` or a CSS background image, so check both. Once found, confirm that the image is the bureau's own mark. Do not mistakenly take a contractor's logo from the footer, a partner's logo, or an event banner. Download the original file to `assets/`, preferring SVG, then a sufficiently large PNG (at least 80px high, so it does not blur on high-resolution screens).
3. State the logo's source URL in the delivery notes and ask the case officer to check that it is the correct, current version.
4. Any of the following counts as "bureau logo not found":
   - There is no network connection, or no logo image can be found on the official website.
   - The official website uses the Taipei City Government mark or the city emblem, not a mark specific to the bureau.
   - You cannot be sure the image you found is the bureau's official mark.

   In that case, **do not place a logo**. The header shows only the agency's full official name in text (for example 「臺北市政府社會局」, Department of Social Welfare, Taipei City Government), and you must not substitute the City Government mark, the city emblem, or any other image. Tell the case officer clearly:

   > I could not find a logo specific to the Department of Social Welfare on its official website, so for now the header shows only the agency name in text. If your department has an official logo file, please send it to me and I will put it in.

**Rules of use**

- You must use the agency's official file. You must not draw it yourself, generate it with AI, trace and redraw it, or substitute a similar icon.
- You must not change its colors, stretch or squash it, crop it, or rotate it, or add shadows, outlines, glows, or animation.
- Display it at about 30 to 40px high, with width scaling to the original proportions. Leave space around the logo; do not let it touch text or borders.
- The image's `alt` is the agency's full official name, for example `alt="臺北市政府資訊局"`.
- Wrap the logo in a link back to the website's home page.
- To place the logo on a dark background, use the reversed (white) version provided by the agency. If there is no reversed version, do not place it on a dark background.

**Taipei City emblem**

- [Law] The city emblem is used in accordance with the Taipei City Emblem and Flag Ordinance (臺北市市徽市旗設置自治條例); the competent authority is the Department of Civil Affairs. Its design must not be altered without authorization, and it must not be used in commercial or undignified settings.
- On web pages, we recommend using the city emblem only as the browser tab icon (favicon). The header uses the bureau logo.
- You should use the official emblem file provided by the Department of Civil Affairs or the City Government website. It must not be redrawn.

### 5. Layout

```
┌──────────────────────────────────────────────────┐
│ Header: bureau logo + service name     Main menu │  about 72px high, white, thin bottom line
├──────────────────────────────────────────────────┤
│ Breadcrumb: Home / Current page                  │
│                                                  │
│ Taipei City ___ Dept.     ← agency name, small   │
│ Page title                ← h1, serif            │
│ ▬▬▬▬                      ← emblem color bar     │
│ One or two sentences on what this page does      │
│ [ Primary button ]                               │
│                                                  │
│ Section heading           ← h2, serif            │
│ ───────────────────                              │
│ 一、……                                           │
│ 二、……                                           │
├──────────────────────────────────────────────────┤
│ Footer: agency info, policy links, access. mark  │
└──────────────────────────────────────────────────┘
```

- Content width: for reading-oriented pages, a maximum of about 40em (about 40 Chinese characters per line). Tables and dashboards may widen to 72em.
- Space between blocks is about 48 to 56px; space between paragraphs is 16px.
- On mobile (640px wide or less), switch to a single column; buttons may span the full width.
- If the header is fixed to the top, remove the fixed position when the visible screen height is under 480px (for example a phone held sideways), so the header does not take up too much of the screen.

### 6. Components

**Buttons**

- There are four kinds of buttons:
  - Primary button (`.tp-btn--primary`): solid primary color, white text. Used for the single most important action on the screen.
  - Secondary button (`.tp-btn--secondary`): white background, primary-color outline. Used for other actions.
  - Danger button (`.tp-btn--danger`): white background, red outline and red text. Used for actions that are unfavorable to the public or cannot be undone, such as returning, rejecting, deleting, or deactivating. For the final confirm button in a confirmation dialog, use solid red (`.tp-btn--danger-solid`).
  - Text link: used for actions that leave the screen, such as 「回上一頁」 (Back) or 「取消並返回」 (Cancel and return).
- Size: all buttons are at least 44px high; 48px is recommended for primary buttons. Corner radius 8px, bold (700).
- Public pages: only one primary button per screen, so the public does not hesitate.
- Admin back offices: only one primary button per block. For example, on a list page, 「查詢」 (Search) and 「新增案件」 (New case) belong to the filter area and the title area respectively, so each may be a primary button. When a review area has several side-by-side decisions such as 「核准」 (Approve), 「候補」 (Waitlist), 「補件」 (Request more documents), and 「退件」 (Return), the most common one is the primary button, the others are secondary buttons, and those unfavorable to the public are danger buttons, set a little apart from the other buttons to prevent mistaken clicks.
- Button labels are verbs that say clearly what happens when pressed: 「送出申請」 (Submit application), 「查詢」 (Search), 「下載申請表」 (Download application form).
- An icon may go to the left of the text, but never an icon without text.
- While submitting, do not set the button to `disabled` (focus will be lost). Add `aria-busy="true"` instead, and block repeated submissions in code.

**Form fields**

- Put the field name (`<label>`) above the field. Mark required fields with 「（必填）」 (required); do not rely on a red asterisk alone.
- `placeholder` holds only an example (for example 「例：0912-345-678」, "e.g. 0912-345-678") and must not replace the field name.
- A one-line hint may go under the field, linked with `aria-describedby`.
- Put the error message directly under the field, say clearly what is wrong and how to fill it in, and move the cursor back to that field.
  - Good: 「手機號碼應為 10 碼數字，例：0912345678」 (A mobile number should be 10 digits, e.g. 0912345678)
  - Bad: 「格式錯誤」 (Format error), 「Invalid input」
- Field height 44px, border `--tp-border-input`, corner radius 8px.

**Key notice area (notice band)**

A light background (`--tp-band`) with a 3px ink-colored line on the left, for items that need special attention, such as 「收到可疑連結？先查再點」 (Got a suspicious link? Check before you click). At most one or two per page.

**Numbered item lists**

For explanations, points to note, and commitments, number items 「一、二、三、」, with the numbers in serif and ink color. This is the customary format of official documents. It is more formal than bullets and easy to cite (「請參考第二點」, "please see item 2").

**Tables**

- Always include a `<caption>` (table title) and `<th scope="col">`.
- Do not use tables for layout.
- When a table is too wide on mobile, wrap it in horizontal scrolling; do not shrink the text.

**Status messages**

Put submission and search results in a persistent `<div role="status" aria-live="polite">` so screen readers can read them aloud. Use `--tp-danger` for errors and `--tp-success` for success, and add text (「送出成功」 "Submitted successfully", 「送出失敗」 "Submission failed"); do not rely on color alone.

**Breadcrumbs**

`<nav aria-label="路徑連結列">`, with 「／」 as the separator, and `aria-current="page"` on the last item. A single-page site may omit it.

**External links**

For links that open in a new window, add `target="_blank" rel="noopener"` and note 「[另開新視窗]」 (opens in a new window) in `title`.

**Icons**

When icons are needed, use single-color line SVGs (for example Tabler Icons, MIT license), downloaded into the project. Use `currentColor` so the color follows the text, stroke width 1.75 to 2, size 18 to 24px. When an icon sits next to text, add `aria-hidden="true"`; when it stands alone as a button, add `aria-label`.

### 7. Footer

The footer goes outside `<main>`. A typical agency web page should include the following:

1. The agency's full official name (logo optional)
2. Address
3. Phone number and service hours (may add 「臺北市民當家熱線 1999」, the Taipei 1999 Citizen Hotline)
4. Privacy and personal data protection policy (link)
5. Information security policy (link)
6. Government website open data declaration (link)
7. Accessibility statement (link)
8. Accessibility mark (placed only after it is obtained; see `accessibility.md` section 6)
9. Last updated date
10. Taipei City Government portal (link)

For very simple tools the footer may be shortened, but these four items must not be left out: agency name, contact information, privacy policy, and accessibility statement. Footers for internal admin back offices follow "Back-office footer" in `systems.md` section 2.

The agency's address and phone number should be copied from the footer of its official website. As with the logo, there is no need to ask the case officer to provide them; after copying, ask the case officer to confirm them in the delivery notes.


### 8. Styles to avoid

This section applies to all types of work, including documents and slides produced by Excel, Word, and PowerPoint processing tools, internal small tools, public websites, and admin back offices.

What is prohibited is inappropriate design, not any particular CSS effect in itself, so there are four cases to consider.

(1) **Default design**: when the case officer has not specified a style, always use the City Government's official style, do not use the styles listed in the table below, and do not add decoration of your own to make things look nice. Formal business screens such as admin back offices, announcements, applications, and searches all use the default design.

(2) **Design specified by the case officer**: when the case officer specifies another style for business needs (such as event promotion pages, festival events, educational tools for children, or interactive visualizations), or when the thing being built itself calls for a livelier form (for example, the case officer wants a small game, a promotional event page, or teaching material for children, even without naming a style), the gradients, animation, livelier colors, and illustrations in the table below may be used, provided the following are met:

1. Contrast between text and background still meets the target accessibility level. Text on a gradient or image needs its own background color to keep contrast high enough.
2. Animation that plays continuously or repeatedly can be paused. Animation that plays only when triggered and ends within a second or two (for example a card flip) can be turned off. All animation respects the user's "reduce motion" setting (`prefers-reduced-motion`), and content must not flash.
3. Emoji and icons are decoration only (add `aria-hidden="true"`) and may not replace text.
4. The bureau logo and city emblem are used according to section 4, "Bureau logo."
5. In the "Differences from the City Government templates" part of the delivery notes, state which designs were used and why. If the case officer did not state a style explicitly, list it as an assumption for the case officer to confirm.

(3) **Never, under any circumstances**:

1. Redrawing, recoloring, or distorting the city emblem or a bureau logo.
2. Using AI-generated images to pass as real photos or real people.
3. Rendering text as images (except logos).
4. Insufficient text contrast, flashing content, or autoplay that cannot be stopped.
5. Buttons with only an icon and no text.
6. Fake figures or fake testimonials unrelated to the service (for example 「已服務 10,000+ 人」 "10,000+ people served" or 「使用者好評」 "user reviews").

(4) **AI-generated images**: the default design does not add AI-generated images on its own initiative. When the case officer specifies a design or asks for images, illustrations, diagrams, decorative images, and icons may be AI-generated (including SVG illustrations you draw with code), subject to the following conditions:

1. **Label them clearly.** Note 「本頁插圖由 AI 生成」 (Illustrations on this page were generated by AI) next to the image or at the bottom of the page. For public release, state in the delivery notes which AI service was used. [Gov] Transparency, City Government AI guidelines
2. **Do not pass them off as real.** Do not depict real events, places, or event scenes in a realistic photo style. Do not generate identifiable real people (officials, celebrities, members of the public).
3. **Content must be correct.** Diagrams for health education, traffic, disaster prevention, or step-by-step instructions mislead the public if drawn wrong, so ask the case officer or the business unit to confirm the content.
4. **No AI-generated text.** AI-generated images often contain typos or garbled characters. When an image needs text, overlay real text on the web page.
5. **No infringement.** Do not ask for the style of a particular artist, anime character, or brand. The terms of the AI service used must allow official or public use. Images generated entirely by AI are in principle not protected by copyright, and the agency may not be able to assert rights over them, so commission a designer for important identity elements such as key visuals and mascots. [Gov] Taiwan Intellectual Property Office (TIPO) (經濟部智慧財產局) letter dated April 1, 2025 (ROC year 114)
6. **No bias.** Do not show people only in stereotypes of a single gender, age, or ethnic group. [Law] Article 4 of the Artificial Intelligence Basic Act (人工智慧基本法), fairness and non-discrimination
7. **Keep sensitive data out.** When generating images, do not put personal data or non-public official information in the prompt, and do not upload photos of real people for AI to modify. [Gov]
8. **The city emblem and bureau logos must not be AI-generated or modified** (see section 4, "Bureau logo").
9. Meaningful images get `alt` text; purely decorative images get `alt=""`.

AI-made web pages tend to fall into the same template: blue-purple gradients, emoji everywhere, frosted-glass cards, a large centered headline with three feature cards. If this gets built when the case officer did not ask for it, anyone can tell AI made it. It looks undignified on a City Government website, and much of it fails accessibility testing. The table below lists styles that the default design does not use:

| Don't do this | Reason | Do this instead |
|---|---|---|
| Blue-purple, purple-pink, or rainbow gradients (backgrounds, buttons, text) | Not City Government colors; text contrast on gradients is unstable | White background with a single primary color |
| Emoji as icons, heading decoration, or list bullets (🚀✨📌✅) | They look different on each platform; screen readers read out "rocket"; undignified | Single-color line SVG, or no icon |
| Frosted-glass or semi-transparent cards | Contrast cannot be controlled, and they slow down older computers | Solid white background |
| Neon glows, multiple large shadows | Draw attention and look like a game or an ad | Thin divider lines, at most one light shadow |
| Whole cards lifting on hover, scroll parallax, entrance animations | Distracting, and uncomfortable for users with vestibular sensitivity | No animation; if truly needed, respect `prefers-reduced-motion` |
| Corner radius of 16px or more, pill-shaped cards | The vocabulary of commercial apps | Use 8px throughout |
| Huge centered slogan, three feature cards, 「已服務 10,000+ 人」 ("10,000+ people served"), user review section | The startup product page formula; government websites have nothing to sell | Agency name, title, explanation, one primary button |
| Dark tech-style backgrounds, pure black backgrounds, small light gray text | Insufficient contrast; older people cannot read it | Dark text on white |
| Icon-only buttons, placeholder used as field name | Hard to understand, and screen readers cannot read them | Icon plus text, label above the field |
| Decorative illustrations unrelated to the service, stock photos of business people | Unrelated to the service, just filling space | Real photos of the service, or no image; for illustrations, follow (4) |
| Text rendered as images | Cannot be enlarged, read aloud, or translated | Use real text |
| Redrawn, recolored, or effect-laden city emblem or bureau logo | Violates the rules for using identity marks | Place the official file as is |


### 9. Other required pages (templates in `templates/web/`)

**accessibility.html (accessibility statement)** should include:

1. This website is designed to level [AA/AAA] of the Website Accessibility Guidelines (網站無障礙規範).
2. Access keys: Alt+U for the top function area, Alt+C for the central content area, Alt+Z for the bottom function area (on Mac, Control+Option+key).
3. Keyboard use: Tab moves to the next item, Shift+Tab goes back to the previous one, Enter activates.
4. Scope, and items not yet compliant (if any).
5. Contact information for feedback.

**privacy.html (privacy and personal data protection policy)** should include: what data is collected, what it is used for, how long it is kept, whether cookies are used, the rights of data subjects and how to exercise them, and a contact point. Where you do not know the content, mark it with 〔請填入〕 (to be filled in); do not make it up.

### 10. Template files

Files in `templates/` can be copied directly into a project. Replace the contents of 〔 〕 with the actual content:

| File | Purpose |
|---|---|
| `templates/web/index.html` | Public page: header, title, numbered explanations, notice band, registration form (with personal data notice), footer |
| `templates/web/accessibility.html` | Accessibility statement |
| `templates/web/privacy.html` | Privacy and personal data protection policy |
| `templates/web/assets/tp.css` | Shared styles, used for public pages, back offices, and internal small tools alike |
| `templates/web/assets/app.js` | Form validation (error messages, focus movement, preventing repeated submission) |
| `templates/admin/index.html` | Admin back-office layout: left menu, filters, table, pagination, confirmation dialog |

When modifying `tp.css`, change only the color variables; changing the primary color requires recalculating contrast. Special designs specified by the case officer go in the project's own stylesheet; do not change `tp.css`.
