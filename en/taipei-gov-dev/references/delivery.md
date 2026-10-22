# Delivery notes

Applies to: all work. When finished, explain the work to the case officer in the format in this file.

### 1. Who it is for and how to write it

Delivery notes are written for a case officer who does not know programming. They need to know only four things:

1. Whether it works properly
2. Where the data is stored
3. What the limitations are
4. What still needs to be done before others use it for real

At the end, add a "Note on AI assistance". This is a required disclosure (see part 5 of the template).

How to write:

- Use words the case officer understands. Do not write technical terms such as SQL injection, XSS, CSRF, CSP, or session. When mentioning a security measure, say what it protects ("Others cannot use your account to submit data").
- Technical details (installing packages, program architecture, configuration, maintenance) go in `README.md` in the project folder, for whoever takes over later or for the IT unit. Do not put them in the delivery notes.
- Report check results truthfully according to `verification.md`: write "Confirmed" for things tested and passed, write "Not yet confirmed" with the reason for things not tested, and state problems directly. Do not write "completely secure" or "compliant with all rules."
- Use [Fill in] for information you do not know. Do not make it up.
- Follow `writing.md` for wording.

### 2. Template

Delete items that do not apply to the type of work. Notes for a small tool can be very short and notes for a system will be longer, but always follow the order of these four parts.

```
1. Does it work?
   (1) What was built: [one or two sentences, e.g.: Completed the "Registration List Tidying Tool," which combines the registration Excel files from each session into one and finds people who registered more than once.]
   (2) How to use it:
       [Step by step; every command must be ready to copy and paste, e.g.:
       1. Put the Excel files to be tidied into the "Input" folder.
       2. Double-click "執行整理.bat".
       3. The tidied file will appear in the "Output" folder.]
   (3) What I have confirmed:
       [e.g.:
       1. Tested with fake data: after merging a 100-record list, the record count is correct and all 3 duplicate records were found.
       2. The original files are not modified.]
   (4) What has not yet been confirmed:
       [Write "None" if nothing. e.g.: Not yet tested with files of more than 10,000 records; very large files may take longer.]

2. Where is the data stored?
   [e.g.:
   (1) The tool runs only on your computer, and the data is not uploaded to the internet.
   (2) The tidied file is saved in the "Output" folder and contains people's names and phone numbers. Please store it in the location specified by your agency and delete it according to the retention period after use.]
   [For systems, e.g.:
   (1) Registration data is stored in the system's database file ([location]), currently only on your computer.
   (2) Names and phone numbers on screen are partly masked. Viewing the full data requires entering a reason, and the system keeps a record.
   (3) The data retention period is currently marked [Fill in]. Please confirm it and tell me, and I will set up automatic deletion when it expires.]

3. What are the limitations?
   (1) [Things it cannot do, e.g.: The first row of each file must contain the column names.]
   (2) [Assumptions I made, please confirm, e.g.: The same mobile number is treated as the same person.]
   (3) [Things you need to fill in or confirm, e.g.: The logo was taken from [source URL]; please confirm it is the latest version. The footer address was taken from [source URL]; please confirm it. The purpose of collection and retention period in the personal data notice are currently marked [Fill in].]
   (4) [Differences from the City Government templates; omit if none.]

4. What still needs to be done before others use it for real?
   [Write according to who will use it, e.g.:
   Only you: nothing else is needed.
   Colleagues in your section: have them follow the steps in 1 (2); if the files contain personal data, remind them where to store them.
   The public, or putting it online:
   (1) This system has [login / an admin back office / file uploads / personal data]. Before going live, ask your agency's IT unit to help arrange a server, set up encrypted connections, create backups and test restoring them, and run a vulnerability scan.
   (2) Please run accessibility testing with Freego. I have checked only with automated tools, which does not mean it passes the testing.
   (3) [Things that need applications, e.g.: If you want to switch to TaipeiPASS or City Government single sign-on for login, apply to your IT unit early.]]

5. Note on AI assistance
   (1) This [tool / web page / system] was produced with the help of [AI tool name, model name, and version, written as the tool displays them]. Please check and revise it yourself, and have your supervisor review it before use.
   (2) Under the Taipei City Government Guidelines for the Use of Artificial Intelligence, compare the code with similarity comparison software before public release. Parts identical or similar to open source software must comply with its license terms; parts identical or similar to third-party software must be substantially revised by hand or regenerated.
```

### 3. Key points for each type of work

| Type | Under "Does it work?" write | Under "Where is the data stored?" write | Under "Before use for real" write |
|---|---|---|---|
| A. Document and data processing tools | How to run it; record count check results | Whether data stays only on the local computer; where output files are saved | How colleagues should use it; how to keep files containing personal data |
| B. Small tool screens | How to open it | Whether data stays only on the local computer; whether it is stored in the browser | Same as A |
| C. Public information web pages | How to open a preview; check results | Whether any data is collected (usually none) | Uploading to the agency's web server; accessibility testing |
| D. Forms, registration, applications | How to test the registration flow | Where registration data is stored and for how long | Server, encrypted connections, accessibility testing, items to fill in for the personal data notice |
| E. Systems | How to start it; how to create the first administrator account | Where the database is, who can see what, audit logs | IT unit assessment, backups, vulnerability scanning, applying for the login method |

### 4. README.md (for whoever takes over)

Web pages and systems that store data (`tech-stack.md` Tier 2 and above), and tools that need installation, must have a `README.md` in the project folder, written for whoever maintains it later or for the IT unit. It covers:

- Technologies and packages used (with versions)
- How to install, start, stop, and update
- Configuration files and environment variables
- Where data is stored and how to back it up and restore it
- Account and permission design
- Known limitations and to-do items
