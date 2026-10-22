# Taipei City Government AI Development Guidelines

[正體中文](../README.md) | [English](../en/README.md) | [日本語](../ja/README.md)

Use this guideline package whenever you ask an AI tool to write a program for you. Whether you need a small tool for tidying up Excel files or processing Word documents, or a registration website or management system, the result will be easy to use, secure, and in line with the rules on AI use.

The quickest way needs no installation. Paste the sentence below into your AI development tool, then go on to describe what you want to build.

```
Please read the README at https://github.com/taipei-doit/TP_AI_Agent_soul_skill/tree/main/en , follow "Instructions for AI" to read all the guidelines, then build the following according to the guidelines: (describe what you want)
```

If you want the guidelines applied automatically every time, see "Installation steps" below.

---

## Instructions for AI

> This section is written for AI development tools. Case officers can skip it.

If you are an AI and have been asked to "read this README and build according to the guidelines," reading this README alone is not enough. The README is an installation guide for case officers; the guidelines themselves are in other files. Before you start, complete the following steps in order.

1. **Get the guideline files.** If you can run commands, first download the whole project (`git clone` this repo, or download the ZIP and extract it), then read the local files. If you cannot download it, read the raw version of each file listed below, one at a time. To do this, replace `github.com/<account>/<project>` in the URL with `raw.githubusercontent.com/<account>/<project>/main/`, followed by the file path. For example: `https://raw.githubusercontent.com/taipei-doit/TP_AI_Agent_soul_skill/main/en/soul.md`.

2. **You must read the two files below**, in full, every time.

   1. `en/soul.md`: the basic position and legal red lines for assisting Taipei City Government staff. It takes precedence over all other rules.
   2. `en/taipei-gov-dev/SKILL.md`: the entry point to the guidelines. Use its section 2, "Determine the type of work," to decide which type this work belongs to.

3. **Read the files in `en/taipei-gov-dev/references/` according to the type of work.** The type table in SKILL.md lists the files to read for each type. Read these files in full as well; do not judge by file name alone or read only the first few paragraphs. The files you may need are listed below.

| File | When to read it |
|---|---|
| `en/taipei-gov-dev/references/data-tools.md` | Tools for processing documents and data such as Excel, Word, PowerPoint, and PDF |
| `en/taipei-gov-dev/references/tech-stack.md` | Web pages and systems |
| `en/taipei-gov-dev/references/web-ui.md` | When there is a user interface (section 8, "Styles to avoid," applies to all types) |
| `en/taipei-gov-dev/references/accessibility.md` | When there is a user interface |
| `en/taipei-gov-dev/references/writing.md` | All types |
| `en/taipei-gov-dev/references/privacy.md` | When personal data is involved |
| `en/taipei-gov-dev/references/security.md` | All types |
| `en/taipei-gov-dev/references/systems.md` | When there is login, an admin back office, uploads, a database, or limited places |
| `en/taipei-gov-dev/references/verification.md` | All types (checks after completion) |
| `en/taipei-gov-dev/references/delivery.md` | All types (delivery notes) |
| `en/taipei-gov-dev/references/assistants.md` | Government system assistant, records and minutes assistant, data checking assistant, website inspector, information explainer assistant |
| `en/taipei-gov-dev/references/legal-sources.md` | When you need to cite the original text of laws |
| Files under `en/taipei-gov-dev/templates/web/` | Public web pages and internal small tools (shared stylesheet `assets/tp.css`) |
| Files under `en/taipei-gov-dev/templates/admin/` | Admin back offices |

4. **Report before you start**, so the case officer can confirm that you have read everything:

```
Work type: [e.g., Type C public information page; case officer requested a lively design]
Read: en/soul.md, en/taipei-gov-dev/SKILL.md, [files read for this type]
Failed to read: [write "None" if none]
```

If even one required file cannot be read, tell the case officer plainly. Do not substitute memory or guesswork for the content of the guidelines.

5. **Once everything is read, start working.** Follow section 3, "Workflow," in SKILL.md. Ask only questions that affect how the work is done. Do not ask again about anything the case officer has already made clear. Start with the default approach and build a working version first.

---

## What is this?

Many AI tools today (for example Claude Code, OpenAI Codex, Gemini CLI, Google Antigravity, and GitHub Copilot) can help write programs. You just say, in your own words, "Make me a tool that combines the registration Excel files from each session into one" or "Make me an event registration web page," and it writes the program.

But the results look different every time. They often have blue-purple gradients and lots of emoji, which do not look right on a government website. The AI also does not know which rules government agencies must follow.

This guideline package is a set of "work rules for the AI." Put it in your folder, and the AI will read it before starting work. The AI will then:

- Decide on its own which rules apply. An Excel tool will not be forced into a website layout; a registration website will get personal data notices, accessibility, and other required features.
- Handle the technical side itself, writing code that protects against data leaks and hacking. You do not need to understand the technical terms.
- Check its own work when finished, and tell you honestly what has been tested and what has not. It will not describe something untested as problem-free.
- Explain in plain language at delivery: whether it works, where the data is stored, what the limitations are, and what still needs to be done before others use it.
- Make the screens and text match the Taipei City Government style, without blue-purple gradients, emoji, or other common AI looks.
- Follow the Artificial Intelligence Basic Act (人工智慧基本法) and the AI use rules of the Executive Yuan and the Taipei City Government.

## What files are included?

| File | Purpose | In plain terms |
|---|---|---|
| `soul.md` | The AI's basic position and legal red lines | Tells the AI, "You are working for the City Government. These are things you must never do." |
| `taipei-gov-dev` folder | Development guidelines and templates | Tells the AI "what to do for each type of work, how to check it, and how to explain it." It contains the entry file `SKILL.md`, guidelines by topic (the `references` folder), and web page templates (the `templates` folder). |
| `README.md` | Installation guide | The document you are reading now |

You do not need to understand the contents of `soul.md` or the `taipei-gov-dev` folder. They are written for the AI. You are welcome to open them if you are curious.

---

## What you need before you start

1. **A computer** (Windows or Mac)
2. **An AI development tool** that is already installed and working, for example Claude Code, OpenAI Codex, Gemini CLI, Google Antigravity, VS Code with GitHub Copilot, or Cursor.

Note that the ChatGPT, Gemini, and Claude chat websites in your browser cannot create files on your computer, so this guide does not apply to them. You need a development tool like those above, which works inside a folder on your computer.

If you do not have an AI development tool yet, first ask your agency's IT unit which tools the agency allows and which account to use when applying. Under Taipei City Government rules, accounts for external AI services should be registered with your City Government work email.

---

## Installation steps

### Step 1: Download the guideline package

1. Open this address: https://github.com/taipei-doit/TP_AI_Agent_soul_skill (no login needed)
2. Find the green "Code" button and click it
3. Choose "Download ZIP" at the bottom
4. When the download finishes, find `TP_AI_Agent_soul_skill-main` in your "Downloads" folder. Windows usually does not show the `.zip` at the end; the icon is a folder with a zipper.
5. Right-click the file and choose "Extract All" (Windows), or double-click it (Mac)

A folder appears after extraction. If it contains another folder with the same name, open that one too. Then open the `en` folder, where you will see two files, `soul.md` and `README.md`, and a `taipei-gov-dev` folder. Windows may show only `soul` and `README` without the `.md`. This is normal.

### Step 2: Create your working folder

Create a new folder for each new web page or system.

1. Right-click on the desktop (or wherever you usually work) and choose "New" → "Folder" (on a Mac, "New Folder")
2. Give it a name you will recognize, for example `lecture-signup`
3. Copy the `soul.md` file and the **entire** `taipei-gov-dev` folder from the `en` folder you just downloaded into this folder

Your folder now contains these two items:

```
lecture-signup
  soul.md
  taipei-gov-dev (folder)
```

### Step 3: Have the AI tool work in this folder

The AI development tool has to "enter" your folder before it can read the guidelines and create files there. Follow the table below for the tool you use:

| AI tool | How to do it |
|---|---|
| Claude Code (desktop app) | Open the app. Where you start a new conversation, choose a folder and select "lecture-signup" |
| VS Code + GitHub Copilot | Open VS Code, click "File" → "Open Folder" at the top, and select "lecture-signup". Then open the Copilot chat window and, in the mode menu below the input box, change "Ask" to "Agent" (only Agent mode can create files for you) |
| Cursor | Open Cursor, click "Open Folder," and select "lecture-signup" |
| Google Antigravity | Open Antigravity, click "Open Folder," and select "lecture-signup" |
| Claude Code, Codex, Gemini CLI (terminal versions) | See the instructions below |

**Using the terminal versions**

The "terminal" is a black or white text window where you operate the computer by typing.

- Windows: open the Start menu, search for "PowerShell," and open it.
- Mac: open "Applications" → "Utilities" → "Terminal."

Once it is open:

1. Type `cd` and press the space bar once.
2. Drag the "lecture-signup" folder into the window with your mouse. The folder's location appears automatically. Press Enter.
3. Depending on your tool, type `claude`, `codex`, or `gemini` and press Enter.

(If you are using the Windows "Command Prompt" rather than PowerShell, and the folder is not on the C drive, type `cd /d` in step 1 instead.)

### Step 4: Ask the AI to finish the setup

Next, each AI tool needs a few configuration files (small settings files that tell it where to look) so it can find these two items. Some of them go in hidden folders, and doing this by hand is error-prone, so just ask the AI to do it.

1. Copy all of the text in the box below (on the GitHub web page, there is a copy button at the top right of the box), paste it to the AI, and press Enter to send:

```
Please set up the "Taipei City Government AI Development Guidelines" in this folder. Follow the steps below and make no other changes.

Step 1: Create the folder .claude/skills/ and move the entire taipei-gov-dev folder (including all files and subfolders in it) into it, so that it becomes .claude/skills/taipei-gov-dev/.

Step 2: Leave soul.md where it is. Do not move it.

Step 3: Create AGENTS.md. Its content is the text between "===BEGIN===" and "===END===" below, not including those two lines:
===BEGIN===
# Project guidelines

This project is used by Taipei City Government staff. Before starting any work, you must read the following two files in full and follow them throughout the work:

- soul.md: the basic position and legal red lines for AI assisting with government work. It takes precedence over all other rules.
- .claude/skills/taipei-gov-dev/SKILL.md: the entry point to the Taipei City Government development guidelines. Follow its instructions to determine the type of work, then read the guideline files you need.

Even if the tool you use does not support Skills, open and read the SKILL.md file above directly.
Before starting work, list the type of work and the files you have read.
If you cannot read these two files, tell the user first. Do not start development.
===END===

Step 4: Create CLAUDE.md. Its content is the two lines between "===BEGIN===" and "===END===" below, not including the markers:
===BEGIN===
@AGENTS.md
@soul.md
===END===

Step 5: Create GEMINI.md with exactly the same content as CLAUDE.md.

Step 6: Create .github/copilot-instructions.md with exactly the same content as AGENTS.md.

Step 7: Create .agents/rules/taipei-gov.md. Its content is the text between "===BEGIN===" and "===END===" below, not including the markers:
===BEGIN===
---
trigger: always_on
description: Taipei City Government AI development guidelines
---
@[soul.md](../../soul.md)

Before developing any web page or program, you must read @../../.claude/skills/taipei-gov-dev/SKILL.md in full and follow its rules.
===END===

When finished, list the paths of all files in this folder (including hidden files), one per line, so I can check them.
```

2. Before making changes, the AI may ask for your permission, for example "Do you want to create AGENTS.md?" Choose the first option, "Yes." If you choose "Yes, and don't ask again," a `settings.local.json` file may appear in the `.claude` folder. This is also normal.
3. When finished, the AI will list the files. Its list may look a little different from the one below (for example, with `./` in front of each path). As long as all of the following appear, the setup is correct. The `taipei-gov-dev` folder will contain other files too, but you do not need to check each one.

```
soul.md
AGENTS.md
CLAUDE.md
GEMINI.md
.claude/skills/taipei-gov-dev/SKILL.md
.github/copilot-instructions.md
.agents/rules/taipei-gov.md
```

Folders whose names begin with "." are hidden folders. File Explorer and Finder do not show them by default. This is normal and does not mean the AI skipped them. To see them: in Windows File Explorer, click "View" → "Show" → check "Hidden items" at the top; on a Mac, press Command + Shift + period in Finder.

### Step 5: Confirm that the AI has read the guidelines

First close the AI tool and open it again so that it reloads the settings:

- Desktop apps: close the app, open it again, and choose the same folder.
- Terminal versions: type `/exit` and press Enter (or just close the window), then follow Step 3 again to enter the folder and start the AI.

Then ask it:

```
In three points, what rules must you follow when developing programs in this project?
```

If the AI's answer mentions things like "Taipei City Government," "personal data," "accessibility," "classified documents," or "bureau logo," the setup worked.

If the answer is vague, or does not mention the Taipei City Government at all, see "Frequently asked questions" below.

---

## Asking the AI to build something

Once setup is done, you can simply tell the AI in your own words what you want. The more specific you are, the closer the result will be to what you need. It helps to say which agency you are with, what you want to build, where the data comes from, and who will use it.

### Five common types of assistants

Below are five types of tools commonly used at the City Government. Each comes with a sample request that you can adapt to your own work.

**1. Government system assistant**: handles repetitive reading and filling-in of data in a government system for the case officer. The case officer checks the entries and submits them personally.

```
I am a case officer at the XX Bureau, Taipei City Government. Every week I have to enter
subsidy application data from Excel, one record at a time, into the application form of the XX business system, about 80 records.
I want a tool that fills in the fields for me. I will check each record and click Submit myself.
```

The AI will only fill in data for you; it will not submit on your behalf. Before starting, it will also ask you to confirm with the system's administrators that the system allows automated operation. You log in to the system yourself; the AI will not ask for your password.

**2. Records and minutes assistant**: organizes source material such as recordings and meeting documents into issues and conclusions, and prepares draft minutes or summaries from a template for the case officer to revise and review.

```
I am a case officer at the XX Bureau, Taipei City Government. Our monthly section meetings have audio recordings and slides.
I want a tool that turns them into draft minutes, following our section's minutes template (Word).
The meetings do not involve classified information.
```

Recordings contain the voices and remarks of attendees, so the AI will first confirm with you where the transcription will be done (for example, a transcription tool that runs on your computer without an internet connection). It will not send recordings directly to an outside service. Inaudible parts will be marked, not filled in by guesswork.

**3. Data checking assistant**: reads and compiles document data, compares it item by item against specified rules or reference data, and lists the results for the case officer to confirm.

```
I am a case officer at the XX Bureau, Taipei City Government. Every month a contractor sends payment request documents (an Excel breakdown and PDF invoices).
I need to check whether the items, quantities, and amounts match the contract, and list any mismatches for me to confirm.
```

The AI will first ask you to explain the comparison rules. The results will state the file, row, and field, and will mark only "possible mismatches." Whether to return the documents is your decision.

**4. Website inspector**: checks whether a website is working normally, whether content is up to date, and whether links work, and compiles the results and suggested improvements for the responsible staff to confirm and fix.

```
I am a case officer at the XX Bureau, Taipei City Government. Our bureau's website has more than 300 pages.
I want to check once a week for broken links and pages that have not been updated in over a year, and compile a report.
```

The AI will inspect only websites belonging to your own agency, and will space out its checks so it does not overload the site. The tool only checks; it does not change anything. Fixes are made by you or the website administrator.

**5. Information explainer assistant**: gathers and organizes information of various kinds and turns it into text or audio-visual content for reference. When needed, the content can also be published on websites, social media, and other channels.

```
I am a case officer at the XX Bureau, Taipei City Government. I want to turn our bureau's latest announcements and press releases
into short explanations for older readers and draft Facebook posts. I will review them and publish them myself.
```

The AI uses only public, verifiable information and cites a source for each paragraph. It will not publish automatically, and AI-generated content will be labeled. Please have your supervisor review the content before publishing.

### Other examples

**Organizing an Excel list**

```
I am a case officer at the Department of Social Welfare, Taipei City Government. The registration list for each session is a separate Excel file.
I want a tool that combines all sessions into one file and finds people who registered more than once.
I cannot install software on my computer myself.
```

The AI will ask you for the column names and a few sample rows with fake data. **Please do not show the real list to the AI.** Once the AI has written the tool based on that format, you run the tool on the real files yourself, and the data never leaves your computer.

**Event registration web page**

```
I am a case officer at the Department of Social Welfare, Taipei City Government. I need an online registration page for the "Evergreen Academy Fall Term" (classes for seniors).
People need to enter their name, mobile number, and the course they want (choose one of calligraphy, tai chi, or smartphone basics).
The registration data is used only to send class notices and will be deleted 3 months after the program ends.
```

**Promotional mini game**

```
I am a case officer at the XX Bureau, Taipei City Government. I want to make a tarot card mini game to promote our bureau's XX services.
The screens can be a bit lively. After playing, people will see the key points of the service and how to apply.
```

### Before starting and after completion

Before starting, the AI will tell you the "work type" and which guideline files it has "read." It may then ask a few questions, such as "Who will use this tool?" or "Will it use personal data?" Just answer truthfully. If you do not know, say so; the AI will use the default approach first and then ask you to confirm.

When finished, the AI will provide "delivery notes" telling you four things: whether it works properly, where the data is stored, what the limitations are, and what still needs to be done before others use it for real. **Be sure to read these notes in full**, especially anything marked [Fill in] (〔請填入〕 in Chinese text) or "not yet confirmed."

---

## Advanced: apply the guidelines automatically to every new folder

If you often start new projects and do not want to repeat Steps 2 to 4 each time, you can install the guidelines in your computer's "global settings" so that they apply in any folder.

So far this is confirmed to work only with Claude Code. Paste the following into Claude Code:

```
Please install the taipei-gov-dev folder and soul.md in this folder into my computer's global settings:
1. Copy the entire taipei-gov-dev folder to ~/.claude/skills/taipei-gov-dev/
2. Copy soul.md to ~/.claude/taipei-gov-soul.md
3. Add this line at the end of ~/.claude/CLAUDE.md: @~/.claude/taipei-gov-soul.md
   (If ~/.claude/CLAUDE.md does not exist, create it.)
When finished, tell me the full path of each file.
```

For other AI tools, it is safer to set up each folder separately.

---

## Frequently asked questions

**Q: The AI seems to have started after reading only the README, without following the guidelines.**

A: An AI that follows the guidelines lists the "work type" and the files it has "read" before starting. If it did not, or if "read" lists only the README, tell it directly:

```
Please follow "Instructions for AI" in the README: read soul.md, taipei-gov-dev/SKILL.md, and the references files needed for this work in full, list the files you have read, and then start again.
```

**Q: The AI does not seem to follow the guidelines. The result is still blue-purple.**

A: Try the following in order:

1. Close the AI tool and open it again.
2. Tell it directly: "Please read soul.md and .claude/skills/taipei-gov-dev/SKILL.md first, then redo the work according to their rules."
3. Check that all the files from Step 4 were created (ask the AI to list all files, including hidden files).
4. If you use Claude Code, make sure it is updated to the latest version.

**Q: My AI tool is not on the list above. Can I use it?**

A: Most likely yes. Most AI development tools read `AGENTS.md` automatically. If, after setup, it cannot answer the confirmation question in Step 5, paste this sentence at the start of each new conversation: "Please read AGENTS.md first, and follow its instructions to read soul.md and SKILL.md."

**Q: The AI says it cannot find our agency's logo.**

A: The AI first looks on the agency's official website. If it cannot find the logo, it uses the agency's name in text instead. You can save the logo image from the header of the agency's website, put it in the folder, and tell the AI: "The logo file is logo.png. Please use it."

**Q: The AI refuses to build a feature I asked for, saying it violates the rules.**

A: This means the guidelines are working. The AI will explain why and will usually suggest an alternative. Common examples:

- Asking it to process a file marked classified → under the rules, classified documents cannot be processed with AI
- Asking it to have "the system decide automatically and notify people that they are not eligible" → a human review step must be added
- Asking it to show a full national ID number on screen → part of the number must be masked

If you believe your request has a legal basis and should be allowed, please consult your agency's legal affairs unit or IT unit.

**Q: The AI asked me "Should accessibility be AA or AAA?" and I do not know how to answer.**

A: Just say "Go with your recommendation." The AI will decide based on what the page does: for simple pages (for example, a page with only one form) it recommends the highest level, AAA; for complex pages (for example, with a map) it aims for at least AA.

**Q: The AI is done. Can I put it online right away?**

A: **No.** First:

1. Try it out yourself and confirm that it works and the text is correct.
2. Read the AI's delivery notes in full and fill in everything marked [Fill in] (〔請填入〕).
3. Hand it to your agency's IT unit, who will help set up the server, HTTPS, security testing, and accessibility testing before it goes live.

**Q: Can I give the AI real data from the public so it can test the program?**

A: **No.** Under Executive Yuan and Taipei City Government rules, personal data must not be provided to external AI services. Test with fake data, for example "王小明" (a placeholder name) and "0912-345-678." The AI will also use fake data on its own.

**Q: Does the file name have to be `SKILL.md`? Can I change it to lowercase?**

A: Please keep `SKILL.md` (all uppercase). Claude Code recognizes only this file name. Keep `soul.md` in lowercase.

**Q: What should I do when the guidelines are updated?**

A: Download again from Step 1. Overwrite the old `soul.md` with the new one. Put the new `taipei-gov-dev` folder at the top level of your project folder first, then ask the AI: "Please delete the .claude/skills/taipei-gov-dev folder and replace it by moving the new taipei-gov-dev folder from the top level into its place."

---

## Notes for agency IT units

- The Skill uses the Agent Skills format. In the folder `taipei-gov-dev/`, `SKILL.md` (YAML frontmatter, with `name` set to `taipei-gov-dev`) is the entry point. Based on the type of work (document and data processing tools, small tools, public web pages, forms, systems, and systems with AI features), it directs the AI to read the guidelines it needs in `references/`. Templates are in `templates/`. The AI loads only what it needs; it does not apply website rules when building an Excel tool.
- Rules in `references/` are marked [Law], [Gov], or [Rec], meaning an explicit legal provision, an Executive Yuan or City Government rule, or a recommendation of these guidelines, respectively. Article numbers, document numbers, and source URLs are collected in `references/legal-sources.md`.
- Keep only one copy of the whole folder, at `.claude/skills/taipei-gov-dev/`. Claude Code, VS Code Copilot, and Cursor load the Skill from this location. Codex CLI and Gemini CLI do not scan `.claude/skills/`; instead, `AGENTS.md` and `GEMINI.md` tell them to read the files directly. We do not also copy it to `.agents/skills/`. A second copy would make VS Code see two Skills with the same name, and the two copies could drift apart during updates.
- The `@` import syntax in `CLAUDE.md` and `GEMINI.md` is understood only by Claude Code and Gemini CLI. GitHub Copilot also reads these two files but sees only text, which causes no errors; it gets the full instructions from `AGENTS.md` and `.github/copilot-instructions.md`.
- Google Antigravity reads `AGENTS.md`, `GEMINI.md`, and `.agents/rules/*.md`, but loads Skills only from `.agents/skills/`, and `@soul.md` in `GEMINI.md` becomes just a file path, not loaded content. For this reason we create `.agents/rules/taipei-gov.md` (`trigger: always_on`), which embeds the full text of soul.md with `@[soul.md](../../soul.md)` and points to SKILL.md by path. Antigravity limits a single rule file to 24 KB (counted after embedding). If you add to soul.md later, keep it under this limit.
- Most other tools not listed (for example Windsurf, Cline, and JetBrains AI Assistant) support `AGENTS.md`. If one does not, type "Please read AGENTS.md first, and follow its instructions to read soul.md and SKILL.md" at the start of each conversation.
- `soul.md` is loaded at the start of every conversation through the `@` import syntax in `CLAUDE.md` and `GEMINI.md`; Codex, Copilot, and Cursor are told to read it by `AGENTS.md`. A Skill is loaded only when the AI judges it relevant, so the legal red lines are kept in `soul.md`, which is read in every conversation.
- Codex CLI reads `AGENTS.md` up to a default limit of 32 KiB, so `AGENTS.md` contains only pointers. Do not paste the full text of the two files into it.
- If your agency has its own brand color, logo rules, or internal security rules, you can add a section titled "Supplementary rules of this agency" to the relevant file in `taipei-gov-dev/references/` (for example `web-ui.md` or `security.md`) or at the end of `soul.md`. After changing the primary color, recalculate the text contrast ratios.

## References

- Artificial Intelligence Basic Act
- Executive Yuan Guidelines for the Use of Generative AI by Government Agencies (行政院及所屬機關（構）使用生成式 AI 參考指引)
- Taipei City Government Guidelines for the Use of Artificial Intelligence (臺北市政府使用人工智慧作業指引)
- Ministry of Digital Affairs AI Risk Classification Framework (數位發展部人工智慧風險分類框架)
- Ministry of Digital Affairs Website Accessibility Guidelines (數位發展部網站無障礙規範)
- Personal Data Protection Act (個人資料保護法), Cyber Security Management Act (資通安全管理法), Copyright Act (著作權法)
