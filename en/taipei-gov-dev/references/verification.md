# Checks and reporting

Applies to: all work. When finished, run the applicable checks in this file and report truthfully.

> Markers: [Law] an explicit legal provision; [Gov] a guideline or rule of the Executive Yuan or the Taipei City Government; [Rec] a practice recommended by these guidelines. For the original texts of laws and their sources, see `legal-sources.md`.

### 1. Principles

1. **Security is the default, not an option.** Input validation, parameterized queries, output escaping, permission checks, and CSRF protection are built in as you write the code. Do not ask the case officer about them, and do not explain the technical terms to the case officer. [Rec]
2. **Test for real when finished.** Run every check that can be run in your environment. Do not look only at the code and say "it should be fine." [Rec]
3. **Report truthfully.** Each check can have only one of the following four results:
   - **Passed**: actually tested, and the result is as expected.
   - **Failed**: actually tested, and the result is not as expected. Fix it and test again first; if it cannot be fixed, state the problem and its impact.
   - **Not tested**: not tested, with the reason stated (for example "requires the production server to test" or "requires the IT unit's scanning tool").
   - **Not applicable**: the work has no such feature, with the reason stated.
4. **You must not overstate.** [Gov]
   - You must not describe untested or failed items as passed.
   - You must not use summary claims such as "secure," "compliant," "meets legal requirements," or "passed accessibility testing." Say instead what was done and what was tested, for example "Checked accessibility with an automated tool, 0 issues; not yet submitted for Freego testing."
   - Results from automated checking tools (for example axe-core) are not the same as passing the Ministry of Digital Affairs accessibility testing or obtaining a certification mark. Security tests you run yourself are not the same as a vulnerability scan or penetration test.
5. **Test only with fake data.** Do not test with real data about members of the public. [Gov]

### 2. Checks for each type of work

For work types, see SKILL.md section 2, "Determine the type of work." When a piece of work belongs to several types, run the checks for each type.

| Type | Minimum checks |
|---|---|
| A. Document and data processing tools | Actually run it once with fake data or a sample file; confirm the original files were not modified; error messages are in plain language. Excel, CSV: record count check (read, written, excluded); feed in problem data (blank rows, numbers starting with 0, dates, full-width and half-width characters, duplicates) and confirm it is handled correctly. Word, PowerPoint, PDF: output files open normally; layout, fonts, and page numbers are intact; the number of merged documents matches the number of records in the list; files for outside release have had tracked changes, comments, speaker notes, and author information removed |
| B. Small tool screens | The Type A checks; no error messages when opened in a browser; fully operable with the keyboard alone; still usable with the network disconnected (if it claims not to use the network) |
| C. Public information web pages | No errors in the browser console; no horizontal scroll bar at desktop (1280px and above) or mobile (390px) widths; no horizontal scroll bar at 200% zoom (or 640px width); the first Tab stop is "Skip to main content"; text contrast meets the target level; run an automated accessibility check (for example axe-core) when a tool is available; all links open correctly |
| D. Forms, registration, applications | The Type C checks; on blank submission or format errors, the error messages are correct and focus moves to the first field in error; clicking Submit repeatedly creates only one record; all six items of the personal data notice are present; the back end also validates formats |
| E. Systems | The Type D checks; the admin back office cannot be entered without logging in; when an account with role A directly calls a function of role B or of another agency, the back end blocks it; submissions without a CSRF token are rejected; failed logins trigger lockout; the old session is invalid after logout; with limited places, many people competing for the last place at the same time does not cause overbooking; with uploads, disallowed file types, files with changed extensions, and oversized files are all blocked; CSV exports are protected against formula injection |
| F. Systems that use AI themselves | Check according to the types above, and also confirm that the screen tells people they are using AI and offers a way to reach a human |

Checks that cannot be done (for example no browser available for testing, or the production server is needed) are marked "Not tested" with the reason, and listed in the delivery notes under "What still needs to be done before others use it for real?"

When the test environment differs from the environment the case officer actually uses (for example you tested with Chromium on Linux and the case officer uses Edge on Windows), report the functional test results truthfully as "Passed," add a separate item "Operation in the case officer's actual environment" as "Not tested," and ask the case officer to try it once with fake data first.

### 3. Pre-delivery checklist

Copy the applicable sections of the checklist below into your reply and mark each item.

- `[x]` Done and checked
- `[ ]` Not yet done (fix it first, or state the reason in the delivery notes)
- `[—]` Not applicable, with the reason in parentheses after it, for example "[—] File upload rules (this system has no upload feature)"

When an entire section does not apply (for example an Excel tool has no web screen), one line is enough: "[Screens and identity] Not applicable: this tool has no web screen." Within an applicable section, do not force a check mark on an individual item that does not apply, and do not simply delete it.

```
[Document and data processing tools] (Types A, B)
[ ] Did not read the content of real files; developed with column names, fake data, or sample files; the program that processes real data is run by the case officer personally
[ ] Data is processed locally and not uploaded to external services
[ ] Original files are not modified; output goes to new files without overwriting existing files
[ ] Screen and logs show only counts, not personal data
[ ] After processing, a record count check is shown, and problem records are output to a separate list
[ ] Excel pitfalls handled: leading zeros, dates, merged cells, full-width and half-width characters, etc.
[ ] Word and PowerPoint output keeps the original formatting; files for outside release have had tracked changes, comments, speaker notes, and author information removed
[ ] Error messages are in plain language; text shown by the program has no emoji, exclamation marks, or common AI phrases
[ ] Screens and produced documents and slides: default design when nothing is specified; when a style is specified, it follows web-ui.md section 8 (2) and (3)

[Screens and identity] (Types C, D, E)
[ ] The header has the bureau logo (official file, not distorted or recolored, alt text is the agency's full official name, links back to the home page); if not found, only the agency's full official name in text is shown and the case officer has been asked to provide the logo
[ ] The logo's source URL is stated in the delivery notes
[ ] The footer has the agency name, address, phone number, privacy policy, and accessibility statement (admin back offices follow systems.md section 2)
[ ] Complies with web-ui.md section 8, "Styles to avoid": the default design has none of the listed styles; a specified design is stated in the delivery notes
[ ] With the default design: no emoji, gradients, frosted glass, large rounded corners, or unnecessary animation

[Text and style] (all types)
[ ] Does not violate any "never, under any circumstances" item in web-ui.md section 8 (3)
[ ] AI-generated images, if used, are labeled and meet the conditions in web-ui.md section 8 (4)
[ ] Uses 「臺北市」, not 「台北市」
[ ] Buttons are verbs; error messages explain how to fix the problem
[ ] No marketing tone, exclamation marks, Mainland China terms, or unnecessary English
[ ] Unknown content is marked 〔請填入〕 (to be filled in), not made up

[Accessibility (target level: ____)] (Type B checks only the first five items; Types C, D, E check all)
[ ] html lang="zh-Hant-TW"
[ ] One h1 per page, with no skipped heading levels
[ ] Every field has a label
[ ] All operations can be completed with the keyboard alone, with a visible focus outline
[ ] Information is not conveyed by color alone
[ ] Has "Skip to main content" and the U/C/Z access key anchors (導盲磚)
[ ] All images have alt text
[ ] Text contrast meets the target level (AA 4.5:1 / AAA 7:1; the palette in these guidelines meets it; custom colors must be measured)
[ ] No horizontal scroll bar at 200% zoom (check with 200% browser zoom, or by setting the window width to 640px)
[ ] Does not display an accessibility certification mark that has not been obtained

[Personal data and security] (all types)
[ ] Forms that collect personal data have the six notice items beside them
[ ] Only necessary fields are collected
[ ] Personal data on screen is masked
[ ] All test data is fake
[ ] No passwords, keys, or connection strings in the code
[ ] User input is displayed with textContent; the database is accessed with parameterized queries
[ ] No inline script/style, so CSP can be applied
[ ] External resources are self-hosted, or pinned to a version with SRI
[ ] No tracking code

[Complex systems] (Type E)
[ ] The case officer has been told that the IT unit must be involved before going live
[ ] The admin back-office layout is separate from the public pages and still uses no prohibited styles
[ ] Every back-end API checks permissions, not just hiding front-end buttons
[ ] Login code is a separate module; no hard-coded default account or password; passwords are hashed with bcrypt/scrypt/Argon2
[ ] File uploads have a file type allowlist, content checks, size limits, random file names, and are stored outside the web root
[ ] Irreversible operations such as deletion have a confirmation step
[ ] There are audit logs, with no passwords or full personal data in them
[ ] Exports have permission controls; CSV is protected against formula injection
[ ] Forms have CSRF protection; the server-side session is invalidated after logout
[ ] Login lockout, idle timeout, and password length are configured; public lookup features limit failed attempts
[ ] Features with limited places: the back end controls places with transactions, one-time tokens prevent duplicate submission, and a unique index blocks duplicate registration, all tested for real
[ ] Reminded to create backups and test restoring them before going live

[Delivery] (all types)
[ ] Check results are recorded truthfully as "Passed / Failed / Not tested / Not applicable"; nothing untested is reported as passed
[ ] Delivery notes (delivery.md) are attached
[ ] States that the program was produced with AI assistance, with the AI tool, model name, and version
[ ] Reminded the case officer to compare the code with similarity comparison software (City Government AI guidelines, Annex 5)
```
