# Personal data

Scope: when a program collects, reads, displays, exports, or stores personal data.

> Markers: [Law] an explicit legal provision; [Gov] a guideline or rule of the Executive Yuan or the Taipei City Government; [Rec] a practice recommended by these guidelines. For the original texts of laws and their sources, see `legal-sources.md`.

The legal principles are in soul.md and the original sources are in `legal-sources.md`. This file covers only how to handle personal data in code.

### 1. Forms that collect personal data

- Collect only the fields truly needed for the task. Do not ask for what you will not use (for example, registering for a lecture does not require a national ID number). [Law] Article 5 of the Personal Data Protection Act (個人資料保護法); data minimization principle in Article 4 of the Artificial Intelligence Basic Act (人工智慧基本法)
- The personal data notice must be placed directly above the form or next to the submit button; a footer link alone is not enough. Under Article 8 of the Personal Data Protection Act, the notice must state: [Law]
  1. The name of the collecting agency
  2. The purpose of collection
  3. The categories of personal data
  4. The period, area, recipients, and manner of use
  5. The rights the data subject may exercise (inquiry, review, copies, supplementing or correcting, stopping collection, processing, or use, and deletion) and how to exercise them
  6. The effect on the person's rights and interests of not providing the data
- The notice must be specific; writing only 「依相關法令使用」 (used in accordance with applicable laws) is not enough. If you do not know the purpose of collection or the retention period, mark it with `〔請填入〕` (to be filled in) and ask the case officer to fill it in via the delivery notes. Do not make it up.
- When sensitive personal data is involved (medical records, medical treatment, genetics, sex life, health examinations, criminal records), stop first, tell the case officer, and proceed only after confirming there is a legal basis. [Law] Article 6 of the Personal Data Protection Act; [Gov] entering it into AI without consent is an absolutely prohibited item under the City Government guidelines
- A government agency must collect personal data for a specific purpose, within the scope necessary to perform its statutory duties or with the data subject's consent, and its use must not go beyond the original purpose. When unsure, ask the case officer to confirm the legal basis. [Law] Articles 15 and 16 of the Personal Data Protection Act

### 2. Files that contain personal data

- If Excel, Word, or other files provided by the case officer contain real personal data, do not read their contents. Develop using a sample with fake data instead (see `data-tools.md` section 1). [Gov] Point 4 of the Executive Yuan Guidelines for the Use of Generative AI by Government Agencies (行政院及所屬機關（構）使用生成式 AI 參考指引)
- When structured data containing personal data is to be opened up or analyzed across agencies, it must first be de-identified in accordance with the Taipei City Government SOP for the Personal Data De-identification Platform (臺北市政府個資去識別化平臺標準作業流程) (processing and verification are done by different staff; data that directly identifies a person is encrypted or deleted). [Gov]
- Mask personal data on screens, in exported files, and in log files by default. When full data is needed, require permission, a stated reason, and a record (see `systems.md` section 6). [Rec]
