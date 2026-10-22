# Accessibility

Scope: all web pages. Internal small tools only need section 3, "What every level must do."

> Markers: [Law] an explicit legal provision; [Gov] a guideline or rule of the Executive Yuan or the Taipei City Government; [Rec] a practice recommended by these guidelines. For the original texts of laws and their sources, see `legal-sources.md`.

### 1. Legal basis

[Law] Article 52-2 of the People with Disabilities Rights Protection Act (身心障礙者權益保障法) provides: "Websites established by government agencies at all levels and their affiliated agencies (institutions) and schools shall pass accessibility testing at the first priority level or above and obtain a certification mark." Testing is based on the Website Accessibility Guidelines (網站無障礙規範) published by the Ministry of Digital Affairs, which have three levels: A, AA, and AAA. The current version follows WCAG 2.1. A new version amended on May 29, 2026 (ROC year 115) takes effect on November 30, 2026 (ROC year 115), adding WCAG 2.2 criteria, including: focus is not hidden by elements such as a fixed header (2.4.11), click targets are large enough (2.5.8), and login does not rely only on memory or puzzles (3.3.8). Design newly developed websites to the new version from the start. The legal minimum is the first priority level (A). In practice, most new or redesigned websites aim for AA, and these guidelines also set AA as the baseline.

### 2. Choosing the target level by functionality

The simpler the functionality, the easier it is to reach AAA. Before starting work, the AI must decide using the table below and tell the case officer the result for confirmation.

| Functionality | Typical examples | Target level |
|---|---|---|
| Simple | Information-only pages, announcement pages, a single form with 1 to 3 fields, a search returning a single result | **AAA** |
| Moderate | Multi-step application forms, search plus list plus pagination, filtering and sorting, back offices that require login | **At least AA**, doing as many of the AAA items listed below as possible |
| Complex | Maps, interactive charts, real-time data, audio and video, drag-and-drop, embedded third-party services | **AA as the baseline**, listing the AAA items that cannot be met and the alternatives |

When telling the case officer, you may use wording like this:

> This page has only one search field and one results area, so it is a simple page, and I recommend aiming for AAA. The main points I plan to meet are: text contrast of 7:1 or higher, no time limits on use, and error messages that explain the correct format. If a map is added later, I will reassess. Do you agree?

If the website later gains new features (for example a map), decide again.

### 3. What every level must do

- `<html lang="zh-Hant-TW">`.
- The first keyboard-focusable element on the page is a "Skip to main content" link.
- Access key anchors: place one `:::` link at the start of the header, the main content, and the footer, with `accesskey="U"` (top), `"C"` (center), and `"Z"` (bottom) respectively. They are hidden normally and appear only when reached by keyboard.
- Mark regions with `<header>`, `<nav>`, `<main>`, and `<footer>`; do not put `<footer>` inside `<main>`.
- Only one `<h1>` per page, and heading levels do not skip (h1 is followed by h2, not directly by h3).
- Meaningful images get `alt` text; purely decorative images get `alt=""`.
- Every field has a matching `<label>`.
- All functions can be operated by keyboard alone, and the current focus is visible (focus outline: 3px primary-color outline, `outline-offset: 2px`). You must not remove the focus outline with `outline: none` on operable elements such as buttons, links, and fields. The only exception is a skip target with `tabindex="-1"` (for example `<main>`). It exists only as a landing point for "Skip to main content"; users do not operate it, so it may go without a focus outline.
- Do not convey information by color alone.
- Put dynamically appearing results in a `role="status"` region.

For small tools used only by yourself or your section (type B in SKILL.md), the access key anchors and the footer (`<footer>`) may be omitted, and "Skip to main content" may also be omitted when the page is short. All other items must be met.

### 4. Additional requirements for AAA

Pages targeting AAA must also meet the following:

- Contrast of 7:1 or higher for regular text, and 4.5:1 or higher for large text (24px or larger, or 18.66px or larger in bold).
- Lines no longer than 40em, line height at least 1.5, paragraph spacing at least 1.5 times the line height, and no justified text.
- No horizontal scroll bar when text is enlarged to 200%.
- No text presented as images (except logos).
- No time limits on use, no automatic refresh, no automatic carousels.
- No flashing content.
- A breadcrumb trail so users know where they are.
- Link text alone says where the link goes; do not use 「點此」 (click here) or 「更多」 (more).
- Divide content with headings.
- Clickable areas are at least 44×44px.
- Use few technical terms and abbreviations; when one must be used, explain it the first time it appears. Write so that a junior high school student can understand it.
- Provide examples and hints next to fields.
- Users can check and edit before submitting, and can withdraw or correct after submitting.

### 5. Alternatives when AAA cannot be met

| Feature | Hard-to-meet item | Alternative |
|---|---|---|
| Video | Sign language interpretation, extended audio description | Provide at least captions and a transcript |
| Map | Can only be operated by mouse | Also provide a text search by address or district, and list the results |
| Chart | People who cannot see it cannot understand it | Provide a table of the same data below the chart |
| Real-time updates | Content moves on its own | Provide "Pause updates," or switch to a button for manual refresh |
| Login timeout | No timeout | Warn before timing out, and allow extending with one button press |
| Legal text | Reading level too high | Add a plain-language summary beside the provisions |

### 6. Accessibility mark and statement

- Every website must have an "Accessibility statement" page describing its scope, access keys (U/C/Z), keyboard operation, and contact information.
- The agency applies to the Ministry of Digital Affairs for the accessibility mark: first self-test with the Freego testing tool, then register and apply online. The mark is issued after passing manual testing and is valid for 3 years. The applicant must be the agency; a contractor may not apply on its behalf.
- **The mark's image must not be displayed before the website has obtained the mark.** After obtaining it, place it according to the issued specifications (the image size must not be changed), link it to the mark's information page at the Ministry of Digital Affairs, and state the level in `alt`, for example 「通過AAA無障礙網頁檢測」 (Passed AAA web accessibility testing).
- The AI may not claim on the agency's behalf that testing has been passed. It may only say "designed to level ○○; we recommend submitting it for Freego testing."
