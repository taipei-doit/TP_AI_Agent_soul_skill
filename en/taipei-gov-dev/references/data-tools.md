# Document and data processing tools

Applies to: tools that process files such as Excel, CSV, Word, PowerPoint, and PDF, for example tidying up lists, merging multiple files, batch printing official documents or certificates, extracting text from slides or documents, converting formats, generating reports, and batch renaming files. These tools run on the case officer's computer and do not need the website rules on layout, logo, or footer. When built as an HTML tool opened in a browser, the screen also follows Type B in SKILL.md.

> Markers: [Law] an explicit legal provision; [Gov] a guideline or rule of the Executive Yuan or the Taipei City Government; [Rec] a practice recommended by these guidelines. For the original texts of laws and their sources, see `legal-sources.md`.

### 1. Protect the data first, then write the program

First distinguish between the two situations below.

| | AI reads the data | A program processes the data locally |
|---|---|---|
| What it is | You (the AI) open or preview a file, or see content printed while a program runs | The program you wrote is run by the case officer on their own computer and reads the real files |
| Where the data goes | To the AI service | Stays on the case officer's computer |
| Is real data allowed? | **Not allowed** when it contains personal data or unpublished government information (exceptions below) | **Allowed**; this is exactly what these tools are for |

In other words, the program reading real Excel or Word files is normal, and you write it to read local files as usual. What is not allowed is letting the content of real data reach the AI.

1. **You do not read the content of real files.** Excel files from case officers often contain people's names, phone numbers, and national ID numbers; Word and PowerPoint files often contain draft memos and letters, meeting materials, and unpublished policy content. As soon as you read such content, the data has in effect been sent to the AI service, which violates Point 4 of the Executive Yuan generative AI guidelines (do not provide information that must be kept confidential, personal information, or information not approved for public release) and the City Government guidelines. [Gov]
   - Excel, CSV: ask the case officer for the column names (the first row) and 3 to 5 sample rows changed to fake data.
   - Word, PowerPoint, PDF: ask the case officer for a sample file with the content replaced by fake text but with the original layout and formatting kept, or for a written description of the layout (for example, "Page 1 is the title; from page 2 on, each page has one table with 4 columns").
   - You can say: "To protect people's data and government information, please do not show me the real files. Please save a copy with the content replaced by fake data, keeping the format the same. I will write the program to match that format, and then you can run the program on the real files."
   - If the case officer has already put real files in the folder, do not open or preview them, including sheet names and file summaries. File names may contain personal data, so do not list them either. If you need to know how many files there are and what they are called, ask the case officer to tell you and to save a sample version.
   - If a file name or content is marked 「密」 or 「機密」 (classified), or the file is clearly a classified document, stop work according to soul.md section 3 (1). Generative AI must not be used to produce classified documents. [Gov]
2. **The case officer runs the program that processes real data.** You run and test only with fake data. If you (the AI tool) ran the program on real files, you would see the data in the program's output and error messages, which again sends the data to the AI. At delivery, explain clearly how the case officer can run it personally. [Gov]
3. **A program processing real data must meet three conditions.** It runs on the case officer's own work computer or in an environment approved by the agency; the data is not uploaded to any external service; and the output files are handled according to section 6, "Keeping output files." [Gov]
4. **Exception.** When using an AI environment built by the City Government or not connected to outside networks, the AI may process real data by classification level according to agency rules. [Gov] City Government AI guidelines, absolutely prohibited items, item 1

5. **Data stays on the case officer's computer.** The tool processes data locally and must not upload it to online conversion sites, cloud spreadsheets, or any external service. [Gov]
6. **Do not modify the original files.** Read the original file and write the output to a new file. Add 「_整理後」 ("organized") and the date to the new file name, for example `報名名單_整理後_1151019.xlsx` or `簡報_更新後_1151019.pptx`. If the output file already exists, add a sequence number rather than overwriting it. For HTML tools that save files through a browser download, let the browser add a number to files with the same name, and state this in the delivery notes. [Rec]
7. **Do not show personal data on screen or in logs.** Messages while the program runs show only counts and results (「共讀取 1,203 筆，輸出 1,198 筆，5 筆有問題」, "1,203 records read, 1,198 written, 5 with problems"). Do not print names or phone numbers on screen or in log files. [Rec]

### 2. Choosing an approach

First ask the case officer, "Can you install software on your computer yourself?" Then choose from the table below:

| Situation | Recommended approach | Notes |
|---|---|---|
| Cannot install software | Built-in Excel features (formulas, Power Query), or an HTML tool opened in a browser | The HTML tool must run locally without an internet connection; any libraries it uses must be kept in the tool's folder, with no connections to external websites |
| Can install Python, or the agency already has a Python environment | A Python program (openpyxl or pandas for Excel; python-docx for Word; python-pptx for PowerPoint; pypdf or similar for PDF) | Include a simple way to run it (a `.bat` file that runs with a double-click on Windows, or one clearly stated command line) |
| Only need to repeat the same task in Word or Excel | Built-in Office features (Word mail merge, styles, Excel formulas); use macros only when necessary | Macros may be blocked by agency security settings; ask the case officer to confirm whether the agency allows them before using them |
| The agency's IT unit has designated a tool | Follow agency rules | |

Whichever approach you choose, make sure the case officer can use it without knowing how to program.

- Make it as simple as possible to run, for example double-clicking an executable, dragging a file into a window, or pasting one command line.
- Put settings to be entered (for example file locations or column names) at the top of the program or in a separate configuration file, with comments in Chinese explaining them.
- Error messages should say in plain language what the problem is and how to fix it (「找不到『手機號碼』這一欄，請確認 Excel 第一列的欄位名稱」, "Cannot find the 'mobile number' column. Please check the column names in the first row of the Excel file"). Do not show raw program error messages.
- When there is a screen, or when documents or slides are produced, use the default design if nothing is specified, and do not add decorations such as gradient backgrounds or emoji yourself. When the case officer specifies another style, follow `web-ui.md` section 8 (2) and (3). Produced documents keep the format of the original file or the agency template.
- All text the program displays (prompts, progress, completion messages, error messages) follows `writing.md`: no emoji or exclamation marks, and none of the phrases common in AI writing such as 「一鍵搞定」 ("done in one click"), 「輕鬆完成」 ("done with ease"), or 「處理完成 🎉」 ("processing complete 🎉"). For example, on completion write 「已整理完成，共輸出 1,198 筆，檔案存在『輸出』資料夾」 ("Done. 1,198 records written; the file is in the 'Output' folder").

### 3. Common Excel pitfalls

Handle the following in the program; do not ask the case officer to deal with them:

- Leading zeros disappearing from national ID numbers, phone numbers, and postal codes: always read these as text.
- Dates turning into numbers (for example 46310): convert them back to dates. Decide between ROC calendar years and Western calendar years based on the column content, and state in the delivery notes how this was decided.
- Merged cells, blank rows, and extra header rows: handle these before calculating.
- Full-width and half-width characters, leading and trailing spaces, and variant forms of the same character (臺／台): normalize before comparing.
- The same person appearing more than once: decide according to the rule the case officer specifies (for example, "the same mobile number means the same person"). Do not decide on your own.
- Output CSV files must display Chinese correctly in Excel: use UTF-8 encoding with a BOM.
- Prevent formulas from running: when writing CSV, add a single quote in front of cell content that begins with `=`, `+`, `-`, `@` (or a tab or line break). When writing `.xlsx`, always write cells as "text" type, so they will not be treated as formulas and no single quote is needed (an added quote would show in the cell).

### 4. Common Word, PowerPoint, and PDF pitfalls

- **Keep the original formatting.** When modifying a document, keep the original file's styles, fonts, headers and footers, page numbers, and layout. Do not apply new styles. Official documents follow the agency's official document format and fonts (for example 標楷體, DFKai-SB); use the template if there is one.
- **Old formats**: ask the case officer to save `.doc` and `.ppt` files as `.docx` and `.pptx` first. The program does not process old formats directly.
- **Hidden information travels with the file.** Tracked changes and comments in Word, speaker notes and hidden slides in PowerPoint, and author and revision information inside files may contain content that should not be released. When producing files to be provided outside the agency, remove this information by default and remind the case officer in the delivery notes to check.
- **Mail merge**: for example, producing one certificate or notice per person from a list. Each file name must be identifiable (for example by adding a serial number), but must not contain full personal data (for example a national ID number). After producing the files, show the total count so the case officer can check that it matches the number of records in the list.
- **Tables and charts**: tables in Word and PowerPoint often have merged cells, and chart data may be hidden in an embedded Excel file. Check the structure before modifying, and make sure the file opens normally afterward.
- **PDF**: a scanned PDF is an image with no text to extract. It needs optical character recognition (OCR), and OCR results must always be checked by a person. Do not upload PDFs to online conversion or OCR sites.
- **Fonts**: when a produced file is opened on another computer, different fonts may break the layout. Prefer Chinese fonts built into Windows; if a specific font is needed, state it in the delivery notes.

### 5. Results must be verifiable

The case officer must be able to confirm that the tool has not miscalculated:

- After processing, show a count check: how many records were read, written, excluded, and found with problems.
- Write problem or excluded records to a separate list with the reason (for example 「第 15 列：手機號碼只有 9 碼」, "Row 15: mobile number has only 9 digits") so the case officer can confirm them manually.
- When there are totals or statistics, state the calculation method in the delivery notes and recommend that the case officer spot-check a few records manually.
- For document tools (mail merge, reformatting, text extraction), ask the case officer to open several output files and confirm that the layout, fonts, and content are correct.

### 6. Keeping output files

If output files contain personal data, the delivery notes must remind the case officer to:

- Store them in the location specified by the agency, not on the desktop, a USB drive, or a personal cloud drive.
- Delete them according to the retention period after use, including intermediate temporary files.
- Encrypt them or use an official file transfer method according to agency rules when sending them to others.
