# Complex systems: admin back offices, login, file uploads, databases

Scope: systems with login, an admin back office, file uploads, a database, or shared use by many people.

> Markers: [Law] an explicit legal provision; [Gov] a guideline or rule of the Executive Yuan or the Taipei City Government; [Rec] a practice recommended by these guidelines. For the original texts of laws and their sources, see `legal-sources.md`.

Systems with an admin back office, login, file uploads, or a database have different risks and use cases from simple web pages. In addition to the rules in `web-ui.md`, `privacy.md`, and `security.md`, they must follow this file.

### 1. Explain before starting: these systems need the IT unit's involvement

If a system has any of the following, you must tell the case officer before starting work that the agency's IT unit has to be involved before it goes live, and that it cannot simply be put on the internet once you finish it: [Gov] Taipei City Government Cyber Security Management Rules (臺北市政府資通安全管理規定)

- It requires login (username and password, TaipeiPASS (臺北通), City Government single sign-on, etc.)
- It has an admin back office where data can be added, changed, or deleted
- Members of the public or colleagues can upload files
- Data is stored in a database and includes personal data
- It sends email or text messages, or connects to other agencies' systems

You may explain it like this:

> This system has a back office and file uploads, so it counts as an information and communication system. Before it goes live, the agency's IT unit needs to assess its protection level, run a vulnerability scan, and arrange the server and backups. I can build the program first so you can try it, but please do not put it on the public internet yourself for now. I recommend contacting the IT unit now.

These systems fall under Tier 2 or Tier 3 in `tech-stack.md` section 1. Before choosing technology, you should first ask the case officer whether the agency already has an established platform or server, and if so, give it priority. If not, choose according to `tech-stack.md` section 1, and describe the architecture in the delivery notes so the IT unit can assess it.

### 2. Two kinds of screens, two layouts

In the same system, pages for the public and the back office for colleagues should have different layouts, but share the same colors and components.

| | Public pages | Admin back office |
|---|---|---|
| Users | The public, occasional use | Colleagues, long daily use |
| Goal | Understood at a glance, used with confidence | Find fast, edit fast, no mistakes |
| Width | About 40em, single column | Full screen, maximum about 90em |
| Navigation | Simple menu in the header | Function menu on the left (collapsible on mobile) |
| Titles | Large serif title, four-color city emblem bar | Sans-serif (`<body class="tp-admin">`), no four-color bar |
| Content | Numbered explanations, one primary button | Tables, filters, batch actions |
| Font size | Body text 16px or larger | Body text 15 to 16px; tables may go down to 14px |
| Accessibility target | Decided by functionality (mostly AAA or AA) | At least AA |

The back office is a formal business screen. It uses the default design and does not use the styles listed in `web-ui.md` section 8, "Styles to avoid." The back-office header shows the bureau logo (or the agency's full official name in text if no logo is found) and the system name, and is clearly labeled 「管理系統」 (management system) so colleagues do not confuse it with the public website.

**Back-office layout**

```
┌──────────────────────────────────────────────────────────┐
│ Bureau logo + ___ Admin System    Wang (officer) Log out │
├────────────┬─────────────────────────────────────────────┤
│ Cases      │ Cases / Case list                           │
│ Files      │ Case list                        [New case] │
│ Accounts   │ ┌Filter: Status▼  Dates  Keyword  [Search]┐ │
│ Audit log  │ ├─────────────────────────────────────────┤ │
│            │ │ Table (sortable, paginated)             │ │
│            │ └─────────────────────────────────────────┘ │
└────────────┴─────────────────────────────────────────────┘
```

**Back-office header on mobile**

At mobile width (640px or less), the header keeps only one line: the bureau logo (or the agency's full official name in text) and the system name. A long system name may be shortened or wrap below the logo. The user's name, log out, and the function menu all go inside a 「選單」 (Menu) button (with `aria-expanded` indicating open or closed); do not cram everything into the header.

**Back-office footer**

The footer of an internal back office goes outside `<main>` and only needs:

1. The agency's full official name
2. A contact point for system problems (unit, extension, or email)
3. System version or last updated date
4. Accessibility statement (link)
5. When the system processes personal data, a 「資料保護說明」 (data protection notice) (link)

The address, open data declaration, and portal link required in public page footers may be omitted in the back office. The data protection notice is written for colleagues. It explains what personal data the system holds, who can see it, how long it is kept, that access is logged, and whom to notify in case of a leak. It does not need to copy the six notice items of the public privacy policy.

**Back-office login page**

Pages before login (login, forgot password, change password on first login) have no left menu and use a single centered column (about 28em wide). The header shows the bureau logo and system name, labeled 「管理系統」 (management system); the title uses sans-serif, with no four-color bar.

**Back-office component rules**

- **Tables**: include a `<caption>`, column headers, pagination, and rows per page. Sortable column headers are buttons, with `aria-sort` indicating the current sort. With large amounts of data, use server-side pagination instead of loading everything at once.
- **Filters**: put filters above the table and apply them only when 「查詢」 (Search) is pressed; do not re-run the search on every keystroke.
- **Actions that need confirmation**: the following actions must first open a confirmation dialog stating clearly what will be done to which record and what the result will be. Decisions affecting the public's rights and interests must take effect only after the case officer confirms them, and must not be decided automatically by the program. [Gov] absolutely prohibited items in the City Government AI guidelines; [Rec] the confirmation dialog approach
  - Decisions affecting the public's rights and interests: approve, reject, return, admit, waitlist, request more documents.
  - Actions that notify the public: sending email, sending text messages, posting announcements.
  - Actions that cannot be undone: deleting, batch editing, import with overwrite.

  For example: 「確定退回案件 1150012（王○明，國畫山水）嗎？退件後將以簡訊通知申請人。」 (Return case 1150012 (王○明, Chinese landscape painting)? The applicant will be notified by text message after the return.) If it can be done as "deactivate" or "move to recycle bin," do not actually delete.
- **Reason field**: decisions unfavorable to the public (reject, return, request more documents) cannot be submitted without a reason, and the field hint should note 「這段文字會通知申請人」 (this text will be sent to the applicant). For favorable decisions such as approve or admit, the case officer may optionally add a note.
- **Batch actions**: select first, then choose the action, and before running it show 「將對 12 筆資料執行停用」 (Deactivate will be applied to 12 records).
- **Status**: show status with text plus color (「已結案」 "Closed", 「處理中」 "In progress", 「退件」 "Returned"); never a colored dot alone.
- **Dialogs**: use the native `<dialog>` element. When it opens, move focus into the dialog: if a reason must be entered, put focus on the reason field; if only confirmation is needed, put focus on 「取消」 (Cancel), so pressing Enter does not submit by mistake. Esc closes it, and focus returns to the original button after closing. Order the buttons with 「取消」 (Cancel) first and the confirm button after it, and the confirm button's label names the action (「確定退件」 "Confirm return," not 「確定」 "OK"). Note: if the dialog is inside a `<form>`, fields marked `required` in it are still checked by the browser when the dialog is closed, which blocks the whole form from submitting. The dialog should have its own separate `<form method="dialog">` or its own separate submit form. Actions that need confirmation must also work without JavaScript (for example by going to a confirmation page first).
- **Login timeout**: warn 2 minutes before timeout and allow extending with one button press, so colleagues do not lose data they are halfway through entering.

### 3. Login and permissions

Do not let the login method hold up development. Integrations such as TaipeiPASS and City Government single sign-on require separate applications and cannot be tested until enabled, so handle them in two stages:

**Development and trial stage**

- Start with the system's own username and password login, so the case officer can try it right away and confirm the features.
- Write the login code as a separate module. Other features get "who this is and what role they have" only through this module. When switching to another login method later, only this module needs to change, not the whole system.
- Your own username and password login must still meet basic security:
  - Store passwords hashed with bcrypt, scrypt, or Argon2; never in plain text or with reversible encryption.
  - Lock temporarily after repeated wrong entries. Without an agency rule, the default is a 15-minute lock after 5 consecutive failures. Count lockouts by "account plus source IP," or use progressively longer waits instead, so that no one can lock others out of their accounts by entering wrong passwords on purpose.
  - Passwords are at least 12 characters. Do not force periodic changes, but block common weak passwords (for example `12345678`, `password`).
  - Log out automatically after 30 minutes of inactivity, warn 2 minutes before timeout, and allow extending with one button press (see section 2 of this file).
  - These are defaults; when the agency's cyber security rules require otherwise, follow the agency's rules.
  - You must not hard-code default credentials such as `admin／admin`. Create the initial administrator account through a startup command or configuration file, and force a password change on first login.

**Production stage (recommended)**

- Public login: we recommend assessing integration with TaipeiPASS.
- City Government staff login: we recommend assessing the agency's or the City Government's existing single sign-on.
- We recommend adding multi-factor authentication to administrator accounts.
- All of these require application and enabling. The delivery notes should remind the case officer to contact the agency's IT unit or the Department of Information Technology of the Taipei City Government early, in parallel with development. The AI must not assume integration specifications on its own; mark unknowns with 〔待確認〕 (to be confirmed).
- Whether to integrate, and which method to use, is decided by the agency according to the nature of the system. Without integration, production must still meet the basic security requirements listed under "Development and trial stage."

- **Permissions**:
  - Distinguish at least two roles, "regular case officer" and "administrator," and grant permissions on the principle of least privilege.
  - Every back-end API must check "whether this person has permission to do this"; hiding front-end buttons is not enough.
  - Do not protect the back office only by keeping its URL private.
  - When case officers may see only data within their own area of work, enforce the query conditions on the back end; do not leave filtering to the front end.
- **Session**: set cookies to `Secure`, `HttpOnly`, `SameSite=Lax`; logging out must invalidate the server-side session; form submissions must have CSRF protection.
  - During the trial stage, when opened locally at `http://127.0.0.1` or `http://localhost`, browsers allow `Secure` cookies and login works normally. Colleagues connecting through a LAN IP (for example `http://192.168.x.x`) cannot log in; this is normal security behavior. Do not turn off `Secure` for convenience. Explain in the README that the trial only works at the local address, or ask the IT unit to set up a test server with HTTPS.
- **Public lookup features**: features that let the public look up or cancel using data such as "reference number plus mobile number" must limit failed attempts. Without an agency rule, the default is at most 10 failures from the same source IP within 15 minutes, to prevent people from guessing reference numbers.

### 4. File uploads

File upload is one of the features most often used for attacks. **All** of the following rules must be met:

1. **Limit file types**: accept only the types the business needs (for example PDF, JPG, PNG), using an allowlist. Do not look only at the file extension; the back end must check the file's actual content (magic number). Always reject files that can be executed or contain code, such as `.exe`, `.js`, `.html`, `.svg`, and `.php`.
2. **Limit size and number**: set a per-file limit and a total limit (for example 10MB per file, at most 5 at a time), shown on the front end and enforced on the back end.
3. **Rename**: save files under a random name generated by the system rather than the file name the user uploaded (store the original name separately in the database).
4. **Storage location**: store files outside the website's root directory or in object storage, so they cannot be opened or executed directly by URL. For downloads, the program checks permissions before sending the file, and sets `Content-Disposition: attachment` and the correct `Content-Type`.
5. **Virus scanning**: in systems open to public uploads, files should pass an antivirus scan before the case officer opens them. Ask the case officer to have the IT unit provide a scanning mechanism.
6. **Personal data**: uploaded files often contain personal data such as copies of ID cards or medical certificates. State the retention period and delete files automatically when it expires; in the back office, show them only to people with permission.
7. **Images**: remove EXIF data from images uploaded by the public (it may contain the location where the photo was taken).
8. **Logging**: record who uploaded, downloaded, or deleted which file and when.

The upload field itself must also be accessible:

- Use the native `<input type="file">` with a `<label>`.
- The field hint states the accepted types and size (「可上傳 PDF、JPG、PNG，單檔 10MB 以內，最多 5 個」 "PDF, JPG, or PNG, up to 10MB each, at most 5 files").
- After uploading, list the selected file names, with a keyboard-operable 「移除」 (Remove) button next to each file.
- Put upload progress and results in a `role="status"` region.
- Drag-and-drop upload may be offered, but the button for choosing files must also be kept.

### 5. Audit logs [Rec]

Back-office systems must keep audit logs, so that when something goes wrong you can find out who did what and when:

- Log logins, logouts, failed logins, additions, changes, deletions, exports, permission changes, and file downloads.
- Each record includes: time, account, source IP, action, and target (for example the case number).
- Do not write passwords or full personal data in the logs (record "changed the phone field of case 1150012," not the new phone number).
- Regular users cannot change or delete log records.
- The retention period follows agency rules. If there is no rule, ask the case officer to consult the IT unit; do not set one yourself.

### 6. Exports and reports

- Export functions must have access control and be recorded in the audit log.
- Personal data fields in exports are masked by default. Full data requires a reason and authorization.
- When exporting CSV, add a single quote before cell contents that start with `=`, `+`, `-`, or `@`, so they are not run as formulas when opened in Excel. When exporting `.xlsx`, write cells as text type.
- Charts must also be provided as data tables (see `accessibility.md` section 5).

### 7. Limited places and duplicate submissions

In systems with limited places, such as registrations, bookings, and applications, the most common problems are overbooking and duplicate registration. Blocking repeated clicks on the front end is not enough; the back end must:

- Check capacity and write the record within the same database transaction, locking the event's row (or use a conditional update, such as "add one only if the current count is below capacity"), to prevent overbooking when many people compete for the last place at the same time.
- Include a one-time token in each form. Repeated submissions with the same token create only one record and return the same result page.
- Add unique database indexes according to the business rules, for example "one registration per mobile number per event," so the database catches what the program misses.
- After a successful submission, redirect to a result page (Post/Redirect/Get), so refreshing the page does not submit again.
- Test before delivery: many people competing for the last place at once, pressing submit repeatedly, and registering the same data twice.

### 8. Platforms shared by multiple agencies

When one platform is shared by many bureaus (for example citywide event registration or a shared booking system):

- **Header and footer**: show the logo and contact information of the agency responsible for operating it (for example the Department of Information Technology), and note in the footer 「本網站由臺北市政府〇〇局維護」 (This website is maintained by the ___ Department, Taipei City Government).
- **Page content**: each event or service page states clearly the organizing agency and how to make inquiries, so the public knows whom to contact with questions.
- **Personal data notice**: the collecting agency is the agency organizing the event, and the notice content is filled in automatically from what the organizing agency entered. Also note which agency operates the website. If there is an outsourced processing relationship for personal data between the organizing agency and the operating agency, ask the case officer to confirm the exact wording with the agency's legal affairs or personal data contact.
- **Permissions**: each agency can see and manage only its own data, with query conditions enforced on the back end (see section 3 of this file).
- **Agency information on pages**: if the organizing agency's address and phone number are displayed, each agency's case officer enters them in the back office, or the AI copies them from each agency's official website and notes the source. When unknown, use 〔請填入〕 (to be filled in); do not make it up.

### 9. Databases

- Always use parameterized queries or an ORM; never build SQL by string concatenation.
- Give the database account only the permissions the program needs; do not connect with the highest-privilege account.
- Encrypt personal data fields in storage as needed.
- The delivery notes should remind the case officer to set up a backup mechanism before going live and to actually test restoring from it.

### 10. Extra items for delivery

In part 4 of the delivery notes template (`delivery.md` section 2), "What still needs to be done before others use it for real?", list the following in addition to the usual items:

- Items that need the IT unit's help: server, HTTPS, antivirus scanning, backups, vulnerability scanning; if integrating with TaipeiPASS or single sign-on, apply early as well.
- The accounts, roles, and permission design used by the system.
- Data retention periods and deletion methods, noting which need the case officer's confirmation.
- How to start and how to update the system, written for whoever maintains it later.
