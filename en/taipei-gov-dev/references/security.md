# Cyber security

Scope: all programs.

> Markers: [Law] an explicit legal provision; [Gov] a guideline or rule of the Executive Yuan or the Taipei City Government; [Rec] a practice recommended by these guidelines. For the original texts of laws and their sources, see `legal-sources.md`.

### 1. These are your responsibility; do not ask the case officer

The case officer does not need to know the names of attack techniques, and should not be the one to decide whether to defend against them. The following practices are the default; build them in as you write the code: [Rec]

| What to prevent | Plain explanation (for when you need to explain to the case officer) | What you do |
|---|---|---|
| SQL injection | Someone types special text into a field to view or delete data in the database | Parameterized queries or an ORM |
| XSS (cross-site scripting) | Someone types code into a field and hijacks the accounts of other people who view the page | Escape on output; use `textContent` on the front end; turn on auto-escaping in the template engine |
| CSRF (cross-site request forgery) | Another website secretly submits data using your logged-in identity | Include a CSRF token in forms; set `SameSite` on cookies |
| Authorization bypass | Anyone who knows the URL can see data they should not see | Check identity and permissions in every back-end function |
| Password leaks | Passwords are exposed directly if the database is stolen | Store password hashes (see `systems.md` section 3) |
| Secrets in code | If the code leaks, passwords and keys leak with it | Use environment variables or configuration files, kept out of version control |
| File upload attacks | A disguised program file is uploaded and run on the server | Follow `systems.md` section 4 |
| Spreadsheet formula injection | Formulas in an exported file run automatically when opened in Excel | CSV: add a single quote when a cell starts with `=`, `+`, `-`, or `@`; `.xlsx`: write as text type |
| Packages of unknown origin | A package may contain a backdoor or be a product that endangers national cyber security | Follow `tech-stack.md` section 5; [Law] Article 11 of the Cyber Security Management Act (資通安全管理法) |

When done, test according to `verification.md` and report truthfully. When explaining to the case officer, use the plain language in the middle column, not the terms on the left.

### 2. Coding practices

- Mask personal data on screen by default, for example 「王○明」, 「A12****789」, 「0912-***-678」. [Rec]
- Personal data must not be written into front-end code, the browser's localStorage, URL parameters, or log files. [Rec]
- Always use fake data for testing (「王小明」, 「0912-345-678」); never use real data from members of the public. [Gov]
- Passwords, keys, and database connection strings must not be written in the code. Use environment variables, and add `.env` to `.gitignore`.
- Treat all user input as untrusted:
  - When displaying it on screen, use `textContent`; you must not concatenate with `innerHTML`.
  - Use parameterized queries for the database; you must not build SQL by string concatenation.
  - Validate formats on both the front end and the back end.
- Error pages must not show program error details (stack traces, database messages).
- Do not use tracking cookies. When cookies are needed, set `Secure`, `HttpOnly`, and `SameSite=Lax`.

### 3. Go-live settings

When deploying to the production server, you should set the following HTTP headers (the agency's IT unit or server administrator can help; mention this in the delivery notes):

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: strict-origin-when-cross-origin
```

So that the CSP above can be applied, do not write inline `<script>` or `style="..."` in the code. Always put scripts and styles in separate `.js` and `.css` files.

Other reminders:

- Use HTTPS across the whole site.
- Public-facing systems should have a vulnerability scan before going live, and depending on the agency's cyber security responsibility level, a penetration test may also be needed. Ask the case officer to consult the agency's IT unit. [Gov] System development and outsourcing follow the Taipei City Government Cyber Security Management Rules (臺北市政府資通安全管理規定).
- A system with an admin back office must have login and access control; do not rely only on "the URL is not public."
- Keep necessary access logs (time, source IP, action), and state the retention period.
