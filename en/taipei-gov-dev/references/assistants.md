# Common assistant tools

This file applies to five types of tools: government system assistants, records and minutes assistants, data checking assistants, website inspectors, and information explainer assistants. First determine the type according to SKILL.md section 2, "Determine the type of work," read the files required for that type, and then read the relevant parts of this file.

> Markers: [Law] an explicit legal provision; [Gov] a guideline or rule of the Executive Yuan or the Taipei City Government; [Rec] a practice recommended by these guidelines. For the original texts of laws and their sources, see `legal-sources.md`.

### 1. Common principles

1. **The tool makes drafts; people make decisions.** Filled-in forms, organized minutes, comparison results, inspection reports, and explainer content are all drafts for the case officer to confirm. Submitting, publishing, or making a decision is always done personally by the case officer or the responsible staff. [Gov] Executive Yuan generative AI guidelines, Points 2 and 5; absolutely prohibited items in the City Government AI guidelines
2. **When the tool itself uses AI** (for example AI summarization, transcription, comparison, or rewriting), it counts as Type F in SKILL.md, and the risk must be assessed according to soul.md section 5. If data will be sent to an AI service, decide whether that is allowed according to `data-tools.md` section 1. [Gov]
3. **State that AI was used.** Content released to the public must disclose the vendor, model name, and version of the AI used. Content drafted by generative AI must state which AI drafted it, must be personally checked and revised by the case officer, and may be published only after a supervisor has reviewed it. [Gov] City Government AI guidelines, Part VI, 1 (5) and Part VI, 2 (4)
4. **Stop when in doubt.** If you run into data you do not understand, a field you cannot find, or a screen that differs from what you expected, stop and list the problem for the case officer. Do not guess, and do not force your way through. [Rec]

### 2. Government system assistant

Handles repetitive reading and filling-in of data in a government system for the case officer, who checks the entries and submits them personally.

- **Fill in only; never submit.** After filling data into a form, the tool stops. The case officer checks each record and clicks "Submit" personally. [Gov]
- **First confirm that automation is allowed.** Before starting, ask the case officer to confirm with the system's administering unit or the agency's IT unit that the system allows automated operation by a program. Some systems prohibit automation under cyber security rules. [Gov] Taipei City Government Cyber Security Management Rules (臺北市政府資通安全管理規定)
- **Do not touch account credentials or authentication.** The tool takes over only after the case officer has logged in personally. Do not write account names or passwords in code or configuration files, and do not bypass CAPTCHAs, multi-factor authentication, or any other security mechanism. [Rec]
- **Go slowly and keep records.** Leave an interval between records; do not run many operations in a short time and overload the system. Record the result of each record (success, failure, reason) so the case officer can check it. [Rec]
- **Try it in a test environment or with fake data first.** If the system has a test environment, work there first. If not, first try one or two records already confirmed to be correct; once the case officer has checked them and found no problems, process the rest. [Rec]
- When the data source is Excel, follow `data-tools.md`: you do not read the content of real data, and the case officer runs the program personally.

### 3. Records and minutes assistant

Organizes source material such as recordings and meeting documents into issues and conclusions, and prepares draft minutes or summaries from a template for the case officer to revise and review.

- **Recordings are sensitive data.** Recordings contain the voices and remarks of attendees and may be personal data or unpublished government information. Generative AI must not be used for classified meetings. [Gov] Executive Yuan generative AI guidelines, Points 3 and 4
- **Confirm first where transcription and summarization will be done.** Transcribing or summarizing with an external AI service means sending out the recording and its content, so it must be a service approved by the agency. When personal data or unpublished information is involved, use a transcription tool that runs on the case officer's computer without an internet connection, or an AI environment built by the City Government, instead. [Gov]
- **Give notice before recording.** Remind the case officer that if a meeting will be recorded, attendees should be told in advance. [Rec]
- **Do not fill in content.** Minutes contain only what is in the source material. Mark inaudible or uncertain parts as "〔聽不清楚，約 00:12:30〕" ([inaudible, around 00:12:30]), and mark an uncertain speaker as "〔發言人待確認〕" ([speaker to be confirmed]). Do not speculate. [Rec]
- **Produce output from the template.** Follow the format of the minutes template (Word) provided by the agency, keeping the template's existing styles and fonts (`data-tools.md` section 4). Mark both the file name and the content as 「草稿」 (draft). [Rec]
- **Resolutions must be checked by a person.** In the delivery notes, remind the case officer to check each resolution, action item, responsible unit, and deadline one by one. [Rec]

### 4. Data checking assistant

Reads and compiles document data, compares it item by item against specified rules or reference data, and lists the results for the case officer to confirm.

- **Rules must be written clearly.** Comparison rules (for example, "the invoice amount must equal the contract unit price times the quantity") are provided by the case officer, written at the top of the program or in a configuration file, and listed in the delivery notes. If a rule is unclear, ask the case officer; do not make one up yourself. [Rec]
- **Every result must be traceable to its source.** Results must state the file, the page or row, and the field, so the case officer can go back and check. [Rec]
- **Write "possible mismatch," not conclusions.** The tool only marks places that may have a problem. Whether to return documents, deduct payment, or request corrections is the case officer's decision. [Gov] Absolutely prohibited items in the City Government AI guidelines (no scoring or dispositions without human review)
- **Text recognition must be checked by a person.** Text recognized from scans or photos may contain errors. Comparison results must note "obtained by text recognition; please check against the original." [Rec]
- Handle files according to `data-tools.md`.

### 5. Website inspector

Checks whether a website is working normally, whether content is up to date, and whether links work, and compiles the results and suggested improvements for the responsible staff to confirm and fix.

- **Inspect only websites you are authorized to manage.** By default, check only the website of the case officer's own agency. Before checking another agency's website or an external website, get that party's consent first. [Rec]
- **Do not overload the website.** Send at most 1 to 2 requests per second and avoid peak office hours; follow the website's `robots.txt`; state the inspection tool's name and contact information in the request headers. [Rec]
- **Look only; change nothing.** Do not log in, submit forms, or attempt any attack or vulnerability scan. Vulnerability scanning is done by the security unit following its procedures; it is not the inspection tool's job. [Gov] Taipei City Government Cyber Security Management Rules
- **Do not modify the website automatically.** Compile the inspection results into a report (page URL, problem found, suggested fix) for the responsible staff to confirm and fix themselves. [Rec]
- **You may also check accessibility along the way**, but state that these are results from an automated tool and do not mean the site has passed formal accessibility testing (`verification.md` section 1).

### 6. Information explainer assistant

Gathers and organizes information of various kinds and turns it into text or audio-visual content for reference. When needed, the content can also be published on websites, social media, and other channels.

- **Use only public, verifiable information.** Attach a source URL to each section of content. Dates, figures, amounts, and eligibility conditions follow the original text; you must not make them up or calculate them yourself. [Gov] Executive Yuan generative AI guidelines, Points 2 and 5
- **Review before publishing.** The case officer checks and revises the content, and it is published only after a supervisor has reviewed it. Content involving people's rights and obligations (for example subsidy eligibility or application deadlines) is high risk and must be checked word for word against the original. [Gov] City Government AI guidelines
- **The tool does not publish automatically.** Producing drafts is enough; the case officer posts them to the website or social media personally. Social media account passwords are not written in the program. [Rec]
- **Label AI-generated audio and video.** AI-generated voice, video, and images must be clearly labeled. You must not imitate a real person's voice or likeness (unless the person has consented), and must not pass off AI images as real photos. For the conditions on using AI-generated images, see `web-ui.md` section 8 (4). [Gov] City Government AI guidelines, transparency
- **Have the business unit review specialized content.** For specialized content such as health education, law, subsidy eligibility, and disaster prevention, base it only on public information from the competent authority, and in the delivery notes remind the case officer to have the business unit confirm that it is correct and still reflects the current rules. If a business web page is only a table of contents, read the agency's own subpages it links to; do not add content yourself. [Rec]
- **Materials must be licensed.** Confirm the license for any images, music, or video used, and credit the source. [Law] Copyright Act (著作權法)
- **Adjust the writing to the audience.** Write according to `writing.md`. Versions for older people, new immigrants, or children should use shorter sentences and fewer technical terms.
