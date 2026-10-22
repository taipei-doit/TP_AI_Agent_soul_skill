# Technology choices

Scope: when building a web page or system. For data processing tools, see `data-tools.md`.

**1. Choose technology to fit the need, and no more.** There are no restrictions on technology. Node.js, build tools, front-end frameworks, and databases may all be used. What matters is choosing "the simplest approach that meets the need." The simpler it is, the easier it is for the case officer to understand and modify, and the easier it is for whoever takes over later to maintain. In SKILL.md section 3, "Workflow," step (2), where you "explain your judgment and approach," state which tier you chose and why.

| Tier | Suitable needs | Recommended approach |
|---|---|---|
| Tier 1: static pages | Event information, announcements, application instructions, forms that submit to an existing system | HTML, CSS, and a little plain JavaScript. No tools need to be installed; open it directly in a browser to see the page, and the case officer can edit the text themselves |
| Tier 2: storing data | Online registration, the public looking up their own data, feedback, simple case registration | Add a back-end program and a database. The back end may use Python (FastAPI, Flask, Django), Node.js (Express, etc.), or a language the agency already uses (PHP, Java, .NET, etc.) |
| Tier 3: complex systems | Admin back offices, multiple roles and permissions, dashboards, many interactive screens, file uploads | Back end and database as in Tier 2. Pages may be generated on the server (for example Flask or Django templates); use frameworks such as React or Vue with build tools only when there is a lot of interaction. Tier 3 does not necessarily mean using a front-end framework. Also follow `systems.md` |

Consider the following in order when choosing:

1. **The agency's existing platforms and technology**: give priority to the languages, databases, and servers the agency's IT unit already uses. Once the system is built, someone must be able to take over its maintenance, and that matters more than how new the technology is.
2. **Whether the case officer can maintain it**: if the case officer can only edit text, stay at Tier 1 where possible; with IT colleagues' support, go higher.
3. **What the features really need**: a simple public form does not call for a framework. Conversely, a system with a back office and multiple permission levels should not be patched together from plain HTML.

**2. Databases.**

- During development and trial, you may start with SQLite (the whole database is a single file, with nothing extra to install), so the case officer can try it right away.
- For production, use a database such as PostgreSQL, MySQL, or SQL Server as planned by the agency's IT unit. The program should access data through an ORM or a database abstraction layer, so that changing the database later does not require major changes.
- Database connection strings, usernames, and passwords go in environment variables or configuration files, never in the code, and configuration files must not be put in version control.
- For other database rules, see `systems.md` section 9.

**3. Rules for every tier.** When using a framework or component library, still follow the visual, wording, accessibility, and security rules in these guidelines. The CSS variables in `tp.css` can be used directly in frameworks such as React and Vue. When using component libraries such as Mantine or Bootstrap, change the colors, fonts, and corner radius to the settings in these guidelines, and remove gradients, large shadows, animation, and other styles the default design does not use (`web-ui.md` section 8).

**4. File structure (Tier 1 static pages).** Start by copying the templates from `templates/web/`. Tiers 2 and 3 follow the conventions of the framework used, but should still have the two pages for the accessibility statement and the privacy policy (for internal back offices, a "Data protection notice" instead; see `systems.md` section 2), plus a README.md for whoever takes over.

```
project-folder/
├── index.html          Home page
├── accessibility.html  Accessibility statement
├── privacy.html        Privacy and personal data protection policy
├── assets/
│   ├── tp.css          Shared styles
│   ├── app.js          Shared script (not needed if there is no interaction)
│   ├── logo.svg        Bureau logo (from the agency's official website; see `web-ui.md` section 4)
│   └── favicon.ico
└── README.md           How to modify and how to deploy
```

**5. External resources.**

- You must not load tracking code, ad code, or plug-ins of unknown origin.
- Fonts, icons, and libraries should be downloaded into your own `assets/` folder (self-hosted) rather than linked from an external CDN.
- If a CDN must be used, you must pin the version number and add the `integrity` (SRI) attribute.
- When choosing packages, confirm that the chosen version has no publicly known security vulnerabilities, and prefer the latest official patched release. Some packages publish patched releases only on their official website, not on npm or PyPI, so follow the official instructions.
- Before choosing a package, confirm that it is not a "product endangering national cyber security." When unsure, ask the case officer to check with the agency's Chief Information Security Officer or IT unit.

**6. Language.** `<html lang="zh-Hant-TW">`. If there is an English version, make separate English pages with `lang="en"`.
