---
name: taipei-gov-dev
description: Development guidelines for Taipei City Government agencies when they ask AI to write programs. Covers tools for processing documents and data such as Excel, Word, PowerPoint, and PDF; web pages; online forms and registration; and systems such as admin back offices. Loads only the guidelines the type of work needs: web page design and bureau logos, government wording, accessibility, personal data, cyber security, checks, and delivery notes. Use these guidelines whenever the user wants to write a program, build a tool, or create or modify a web page, or mentions Taipei City, the Taipei City Government, the City Government, a bureau, an agency, government work, or a case officer.
license: Determined by each agency as needed
compatibility: For AI development tools such as Claude Code, Codex CLI, Gemini CLI, Google Antigravity, GitHub Copilot, and Cursor. Must be used together with soul.md in the same project root directory.
metadata:
  version: "2.0.0"
---

# Taipei City Government AI Development Guidelines

These guidelines aim to make the programs that Taipei City Government staff ask AI to write easy to use, secure, and compliant. This file is the entry point: first determine from the type of work which guidelines to read, then read the parts you need in `references/`. You do not need to read, and should not apply, what you will not use.

## 1. Before you start

(1) **Read soul.md first.** The `soul.md` file in the project root sets out the basic position and legal red lines for AI assisting with government work. No rule in these guidelines may contradict soul.md; if the two conflict, soul.md prevails. If you cannot find soul.md, tell the user first. Do not start work.

(2) **Four basic practices.**

1. **You decide which guidelines apply.** The case officer does not need to know what guidelines exist. An Excel or Word processing tool does not need a website layout, logo, or footer; only a registration website needs the rules on forms, personal data, and accessibility. Decide according to section 2, "Determine the type of work."
2. **You handle the technical issues.** The case officer does not need to know what SQL injection, XSS, or CSRF are. Secure coding is the default; do not ask the case officer whether to do it. When finished, run the applicable checks and report the results truthfully. Anything not tested or not passed must not be described as passing.
3. **No AI look by default, but suitable designs are allowed.** When the case officer has not specified a style, always use the City Government's official style (the default design). Do not use the decorations listed in `references/web-ui.md` section 8, "Styles to avoid," and do not add decorations of your own. When the case officer specifies another style for a business need (for example a promotional event page, a children's educational tool, or an interactive visualization), you may adjust accordingly; gradients, animation, and lively colors are all allowed. You must still follow the accessibility and bureau identity rules and the "never, under any circumstances" items in section 8. What is prohibited is unsuitable design, not any particular CSS effect. Follow `references/writing.md` for text. The tone can be adjusted to the audience, but do not exaggerate or use the empty phrases common in AI writing.
4. **You write clear delivery notes.** The case officer needs to know only four things: whether it works properly, where the data is stored, what the limitations are, and what still needs to be done before others use it for real. Write them according to `references/delivery.md`.

(3) **Strength of wording.** "Must" and "must not" are hard rules. "Should" is the default practice; it may be changed when the case officer explicitly asks, but the change must be stated in the delivery notes. "May" means use as appropriate.

(4) **Order of priority.** The legal red lines in soul.md > the case officer's explicit requirements > the default practices in these guidelines > the AI's own preferences. If the case officer asks to depart from a default practice (for example a different color scheme), do it and note it in the delivery notes. If the request hits a red line (for example showing a full national ID number on screen), do not do it; explain why and offer an alternative.

(5) **Markers.** Rules in `references/` are marked with their source: [Law] is an explicit legal provision, [Gov] is a guideline or rule of the Executive Yuan or the Taipei City Government, and [Rec] is a practice recommended by these guidelines. The original texts of laws, article numbers, and source URLs are in `references/legal-sources.md`.

(6) **Output language.** This is a translation of the Chinese original. Unless the case officer asks otherwise, user-facing text in what you build (web pages, messages, documents) is written in Traditional Chinese as used in Taiwan, following references/writing.md. Talk with the case officer in the language they use.

## 2. Determine the type of work

Before starting, determine which type the work belongs to, then read the corresponding files. One piece of work may belong to several types at once (for example a registration website plus an admin back office); in that case, read the files for all of those types together.

| Type | Examples | Files to read (all in `references/`) |
|---|---|---|
| A. Document and data processing tools | Tidying up Excel lists, merging multiple files, CSV conversion, Word mail merge for certificates or notices, batch updating PowerPoint, extracting text from PDF, generating reports, batch renaming files | `data-tools.md`, `security.md`, `writing.md`, `web-ui.md` section 8, "Styles to avoid," `verification.md`, `delivery.md`; add `privacy.md` when personal data is involved |
| B. Small tool screens for personal or section use | HTML tools opened on your own computer, calculators, form generators | The Type A files, plus `web-ui.md` section 0, "Internal small tools," and `accessibility.md` section 3. A Type A tool built as an HTML tool opened in a browser also counts as Type B |
| C. Public information web pages | Event pages, announcements, application instructions, where the public does not enter any data | `tech-stack.md`, `web-ui.md`, `accessibility.md`, `writing.md`, `security.md`, `verification.md`, `delivery.md`; templates are in `templates/web/` |
| D. Forms, registration, applications | Online registration, feedback, appointments | The Type C files, plus `privacy.md`; add `systems.md` section 7 when places are limited |
| E. Systems | Login, admin back office, file uploads, databases, or shared by multiple agencies | The Type D files, plus `systems.md`; the admin template is in `templates/admin/` |
| F. Systems that use AI themselves | AI customer service, AI summaries, automatic classification of petitions | Based on the types above, plus the risk assessment in soul.md section 5 |

For the five common types of assistant tools below, first determine the type using the table above, then also read the relevant parts of `references/assistants.md`.

| Assistant | Usually | Pay particular attention to |
|---|---|---|
| Government system assistant (reads and fills in government system data for the case officer) | Type A or B | Fill in only, never submit; first confirm the system allows automation; never handle account credentials |
| Records and minutes assistant (turns recordings and meeting materials into draft minutes) | Type A; add Type F when AI summaries are used | Recordings are sensitive data; first confirm where transcription will be done; do not fill in content on your own |
| Data checking assistant (compares documents against rules and lists the results) | Type A | Rules are provided by the case officer; results must be traceable to the source; mark only "possible mismatches" |
| Website inspector (checks links and update status) | Type A | Inspect only websites you are authorized to manage; control request frequency; look only, change nothing |
| Information explainer assistant (organizes information into text or audio-visual content) | Type A or C; add Type F when AI generation is used | Use only verifiable information; review before publishing; label AI-generated content |

Keep the following in mind when deciding.

- Do not apply guidelines that are not needed. Excel and Word processing tools get no logo, footer, or four-color city emblem bar; a small tool used only by yourself needs no accessibility statement or certification mark.
- But the principles of design and wording (see section 1 (2), item 3) apply to all types: use the default design when nothing is specified; when a style is specified, still follow the accessibility rules and the "never, under any circumstances" items.
- When unsure, ask the case officer one simple question (for example, "Will only you use this web page, or will the public use it?"), or go with the more complete type.
- When starting, tell the case officer your judgment in a sentence or two, for example: "This is an Excel tidying tool. It runs on your computer, and the data is not uploaded to the internet. Please do not show me the real file; just give me a sample with fake data."
- When the requirements change (for example, a tool originally for personal use will now be used by the public), reassess the type and read the additional files needed.

## 3. Workflow

(1) **Confirm the requirements.** Ask only about things that affect how the work is done. Ask everything at once, no more than six questions, using multiple choice where possible. Do not ask the case officer technical questions (for example "Which database should we use?" or "Should we guard against XSS?"); you decide those. Do not ask again about anything the case officer has already made clear. If they said only "Make me a registration web page," you may first build a minimum working version using the default approach and list your assumptions in the delivery notes.

Common questions to ask:

1. Who will use it? (only yourself, colleagues in your section, the whole agency, the public)
2. Which agency's business is it? (used to find the logo and fill in contact information; not needed for document and data processing tools)
3. Will it use personal data? Which fields?
4. Where will it be used once done? (your own computer, an internal agency server, a public website)
5. Can software be installed on the computer? (needed for document and data processing tools)
6. Are there existing systems, file formats, or styles it must work with?

(2) **Report what you have read, and explain your judgment and approach.** Before starting, report in the format below so the case officer knows you have read all the guidelines:

```
Work type: [e.g., Type A document and data processing tool]
Read: soul.md, SKILL.md, [references files read per section 2, "Determine the type of work"]
Failed to read: [write "None" if none]
```

Read all the files required for the type in full; do not judge by file name alone or read only the first few paragraphs. If a file cannot be read, say so plainly; never substitute memory or guesswork. After reporting, explain in a sentence or two how you plan to do the work. For Type E (systems), first explain that the agency's IT unit must be involved before going live (see `systems.md` section 1). When the accessibility level needs to be decided, explain the recommended level according to `accessibility.md` section 2.

(3) **Implement.** Write the code according to the guidelines you have read. Use secure coding directly; do not ask the case officer.

(4) **Check.** Run the applicable checks according to `verification.md` and record the results truthfully. Fix any failures first; anything you cannot fix or cannot test must be clearly stated in the delivery notes.

(5) **Deliver.** Write the delivery notes according to `delivery.md`. Technical details (installation, architecture, maintenance) go in the project's README.md for whoever takes over later; do not put them in the delivery notes for the case officer.

## 4. File index

| File | Contents |
|---|---|
| `references/data-tools.md` | How to build tools for processing documents and data such as Excel, CSV, Word, PowerPoint, and PDF |
| `references/tech-stack.md` | Technology choices, databases, and external resources for web pages and systems |
| `references/web-ui.md` | Web page design: colors, fonts, bureau logos, layout, components, footer, styles to avoid |
| `references/accessibility.md` | Determining the accessibility level and how to meet it |
| `references/writing.md` | Text and wording, date formats |
| `references/privacy.md` | Collecting, giving notice about, and handling personal data |
| `references/security.md` | Cyber security: secure coding the AI is responsible for, go-live settings |
| `references/systems.md` | Admin back offices, login, permissions, file uploads, audit logs, limited places, shared platforms |
| `references/verification.md` | Checks required for each type of work, how to report them, pre-delivery checklist |
| `references/delivery.md` | Delivery notes template |
| `references/assistants.md` | Government system assistant, records and minutes assistant, data checking assistant, website inspector, information explainer assistant |
| `references/legal-sources.md` | Sources, article numbers, and verification dates for laws and guidelines |
| `templates/web/` | Public web page templates: `index.html`, `accessibility.html`, `privacy.html`, `assets/tp.css`, `assets/app.js` |
| `templates/admin/` | Admin back-office layout template: `index.html` (shares `templates/web/assets/tp.css`) |
