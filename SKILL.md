---
name: taipei-gov-dev
description: 臺北市政府各機關開發網頁、網站、線上表單、查詢服務、內部管理系統時使用的開發規範與頁面範本。內容包括市府風格的版面、配色、字型、局處 Logo 用法、公務用語、無障礙等級判斷（A／AA／AAA）、個資告知、資安設定，以及交付前的檢核清單。只要使用者要建立或修改任何網頁、表單、後臺、儀表板、前端畫面，或提到臺北市、北市府、市府、局處、機關、公務系統、承辦，就應使用本規範。
license: 由各機關依需要自行決定
compatibility: 適用 Claude Code、Codex CLI、Gemini CLI、Google Antigravity、GitHub Copilot、Cursor 等 AI 開發工具。須搭配同一專案根目錄的 soul.md 使用。
metadata:
  version: "1.0.0"
---

# 臺北市政府網頁開發規範

本規範說明臺北市政府各機關請 AI 開發程式時，畫面應該長什麼樣子、文字應該怎麼寫、程式應該注意什麼。目的是讓各局處做出來的網頁風格一致、民眾好用，也符合無障礙、個資與資安的要求。

## 壹、開始之前

一、**先讀 soul.md。** 專案根目錄的 `soul.md` 規定了 AI 協助公務的基本立場與法規紅線。本規範每一條都不能違反 soul.md；兩者衝突時，以 soul.md 為準。如果找不到或讀不到 soul.md，請先告訴使用者，不要直接開工。

二、**本規範的強弱用語。**

- 「必須」「不得」：硬性規定，不能自行調整。
- 「應」：預設做法。使用者明確要求時可以改，但要在交付說明寫清楚改了什麼。
- 「可」：選擇性做法，視情況採用。

三、**優先順序。** 遇到衝突時，依下列順序處理：

1. soul.md 的法規紅線（個資、機密、資安、著作權、無障礙最低標準）
2. 承辦人（使用者）的明確需求
3. 本規範的預設風格與技術選擇
4. AI 自己的偏好

承辦人要求的做法偏離本規範（例如想換配色），照做，並在交付說明註明。承辦人要求的做法碰到 soul.md 紅線（例如要把民眾身分證字號直接顯示在畫面上），不要照做，說明原因，並提出可行的替代做法。

四、**風格與彈性。** 本規範的設計方向是「公文的莊重，加上捷運指標的清晰」。這並不是要求每個機關的網站都長得一模一樣；各機關有自己的業務特性和識別，只要守住本規範的原則，細節可以調整。

## 貳、工作流程

每件工作都依下列五個步驟進行。

### 一、確認需求

開工前先弄清楚下面幾件事。使用者已經講過的就不要再問；沒講的，一次問完，最多六題，盡量用選擇題，讓不熟程式的同仁也答得出來。

1. 這個網頁給誰用？（民眾、市府同仁，或兩者都有）
2. 是哪個機關的業務？（用來找 Logo、填寫頁尾聯絡資訊）
3. 會不會蒐集或顯示個人資料？會的話，有哪些欄位？
4. 做好之後放在哪裡？（只在自己電腦試用、機關內部主機、對外公開網站）
5. 需不需要登入、管理後臺、檔案上傳？（有的話，依本規範「玖、複雜系統」辦理）
6. 有沒有一定要配合的既有系統或樣式？

使用者只說了一句「幫我做一個報名網頁」時，可以先依本規範的預設值做出最小可用版本，並在交付說明列出你做了哪些假設，請承辦人確認。

### 二、判斷功能複雜度與無障礙目標

依頁面功能判斷要做到哪個無障礙等級（詳見本規範「陸、無障礙」），把判斷結果和理由告訴承辦人，承辦人同意後再開工。

功能越單純，越容易做到 AAA。不要一律只做 AA，也不要硬把複雜系統拉到 AAA。

### 三、規劃

用幾句話說明打算怎麼做：會有哪幾頁、每頁放什麼、用什麼技術、資料存在哪裡。功能單純的話，這一步可以和第一步合併。

### 四、實作

依本規範的版面、元件、用語、無障礙、資安規定撰寫程式。

### 五、自我檢核與交付

完成後，依本規範「拾壹、交付前檢核清單」逐項檢查，沒過的先改好再交。交付時附上「拾貳、交付說明」，用承辦人看得懂的話說明。

## 參、技術預設

一、**依需求選技術，夠用就好。** 技術沒有限制，Node.js、建置工具、前端框架、資料庫都可以用，重點是選「能滿足需求的最簡單做法」。越簡單，承辦人越容易看懂、修改，之後接手的人也越好維護。在工作流程的「規劃」步驟，要說明選用哪一級及理由。

| 級別 | 適合的需求 | 建議做法 |
|---|---|---|
| 第一級：靜態頁面 | 活動說明、公告、申請須知、表單送到既有系統 | HTML、CSS、少量原生 JavaScript。不需要安裝任何工具，用瀏覽器直接打開就能看到畫面，承辦人自己也能改文字 |
| 第二級：要存資料 | 線上報名、民眾查詢本人資料、意見回饋、簡單的案件登記 | 加上後端程式與資料庫。後端可用 Python（FastAPI、Flask、Django）、Node.js（Express 等）或機關既有的語言（PHP、Java、.NET 等） |
| 第三級：複雜系統 | 管理後臺、多種角色權限、儀表板、大量互動畫面、檔案上傳 | 後端與資料庫同第二級。畫面可以由伺服器產生（例如 Flask、Django 的樣板），互動很多時才用 React、Vue 等框架與建置工具。第三級不代表一定要用前端框架。另須遵守本規範「玖、複雜系統」 |

選擇時依下列順序考量：

1. **機關已有的平臺和技術**：機關資訊單位已經在用的語言、資料庫、主機，優先配合。系統做好之後要有人能接手維護，這比技術新不新重要。
2. **承辦人能不能自己維護**：承辦人只會改文字的，盡量停在第一級；有資訊同仁支援的，再往上。
3. **功能真正需要什麼**：只是要讓民眾填表，不需要為此架一套框架；反過來，有後臺、有多種權限的系統，也不要硬用純 HTML 拼湊。

二、**資料庫。**

- 開發和試用階段，可以先用 SQLite（一個檔案就是一個資料庫，不用另外安裝），承辦人馬上就能試用。
- 正式上線時，依機關資訊單位的規劃使用 PostgreSQL、MySQL、SQL Server 等資料庫。程式應透過 ORM 或資料庫抽象層存取資料，日後更換資料庫時才不用大改。
- 資料庫連線字串、帳號密碼放在環境變數或設定檔，不得寫在程式碼裡，設定檔也不得放進版本控制。
- 其他資料庫規定見「玖、九」。

三、**不論哪一級，都要遵守的事。** 使用框架或元件庫時，仍要遵守本規範的視覺、用語、無障礙、資安規定。`tp.css` 的 CSS 變數可以直接沿用到 React、Vue 等框架；使用 Mantine、Bootstrap 這類元件庫時，要把配色、字型、圓角改成本規範的設定，並移除漸層、大陰影、動畫等「伍、不要做的樣式」。

四、**檔案結構（第一級靜態頁面）。** 第二、三級依所用框架的慣例安排，但仍應有無障礙聲明、隱私權政策兩頁（內部後臺改為「資料保護說明」，見「玖、二」），以及給接手者看的 README.md。

```
專案資料夾/
├── index.html          首頁
├── accessibility.html  無障礙聲明
├── privacy.html        隱私權及個人資料保護政策
├── assets/
│   ├── tp.css          共用樣式
│   ├── app.js          共用程式（沒有互動就不用）
│   ├── logo.svg        局處 Logo（從機關官網取得，見「肆、四」）
│   └── favicon.ico
└── README.md           說明怎麼修改、怎麼上線
```

五、**外部資源。**

- 不得載入追蹤碼、廣告碼、來路不明的外掛。
- 字型、圖示、函式庫，應下載後放在自己的 `assets/` 資料夾裡（自架），不要直接連外部 CDN。
- 真的要用 CDN 時，必須鎖定版本號，並加上 `integrity`（SRI）屬性。
- 選用套件前，先確認不是「危害國家資通安全產品」。不確定時，請承辦人向機關資安長或資訊單位確認。

六、**語系。** `<html lang="zh-Hant-TW">`。有英文版時另做英文頁，`lang="en"`。

## 肆、視覺規範

### 一、設計方向

市府網站不是商業產品頁，不需要吸睛，要的是**讓人一眼看懂、放心使用**。

- 像公文：機關銜名、明確的標題、條列式說明，用「一、二、三、」編號。
- 像捷運指標：重要的事情放大、放前面，一頁只做一件主要的事。
- 色彩克制：大面積是白底黑字，主色只用在按鈕、連結、標題。
- 少裝飾：用細線分段，不用卡片陰影、漸層、動畫來撐場面。

### 二、配色

下面是預設配色，文字顏色的對比度都已經算過。機關有自己的代表色時可以替換，但**必須重新計算對比度**，不得低於本規範「陸、無障礙」要求的數值。

| 用途 | 變數名稱 | 色碼 | 對白底對比 | 說明 |
|---|---|---|---|---|
| 主色 | `--tp-primary` | `#0F5C86` | 7.25 : 1 | 按鈕、連結、焦點框 |
| 主色（深） | `--tp-primary-dark` | `#094463` | 10.40 : 1 | 按鈕滑過、淺色底上的連結 |
| 主色（淺） | `--tp-primary-tint` | `#E9F2F7` | — | 只當底色，不當文字色 |
| 標題墨色 | `--tp-ink` | `#16324A` | 13.21 : 1 | h1、h2、條次編號 |
| 內文 | `--tp-text` | `#212529` | 15.43 : 1 | 一般文字 |
| 次要文字 | `--tp-text-muted` | `#495057` | 8.18 : 1 | 說明、頁尾、日期 |
| 頁面底色 | `--tp-bg` | `#FAFBFC` | — | 偏紙感的白 |
| 內容底色 | `--tp-surface` | `#FFFFFF` | — | 表單、表格 |
| 提示帶底色 | `--tp-band` | `#F1F6FA` | — | 重點提示區塊 |
| 分隔線 | `--tp-border` | `#DEE2E6` | — | 只當裝飾線 |
| 輸入框框線 | `--tp-border-input` | `#6C757D` | 4.69 : 1 | 欄位外框（須 3:1 以上） |
| 錯誤 | `--tp-danger` | `#A61E1E` | 7.43 : 1 | 錯誤訊息 |
| 成功 | `--tp-success` | `#14532D` | 9.11 : 1 | 成功訊息 |
| 注意 | `--tp-warning` | `#6F3404` | 9.68 : 1 | 注意事項 |
| 資訊 | `--tp-info` | `#0B3A66` | 11.59 : 1 | 一般提示 |

**市徽四色**：紅 `#C64B4B`、黃 `#DFA92E`、綠 `#2F9464`、藍 `#2B6CB0`。這四色只能用在標題下方一條 4px 高的細色條，整頁只出現一次，作為市府的識別記號。不得拿來當大面積底色、按鈕色或文字色。

注意：主色 `#0F5C86` 放在淺色底（`#F1F6FA`、`#E9F2F7`）上，對比會掉到 7:1 以下。要做 AAA 的頁面，淺色底上的連結和文字請改用 `--tp-primary-dark`。

### 三、字型

```css
--tp-font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC",
                "PingFang TC", "Microsoft JhengHei", Arial, sans-serif;
--tp-font-serif: "Noto Serif TC", "PMingLiU", "MingLiU", serif;
```

- 內文用黑體（系統字型），不需要另外下載。
- 頁面大標（h1）和段落標題（h2）可用明體，表現公文的正式感。明體預設使用電腦內建的字型；要統一效果時，可把 Noto Serif TC 粗體（700）下載後放在 `assets/` 自架。
- 字重只用 400（內文）、600（強調）、700（標題）三種。
- 內文字級 16px 以上，行高 1.8 左右。
- 不要用 Inter、Poppins、Montserrat 這類西文字型當主字型，中文顯示會跳回系統字，看起來像外國產品套上中文。

### 四、局處 Logo

每個網站的頁首左上角都要放**該局處自己的 Logo**，讓民眾一看就知道是哪個機關的服務。

**取得方式**

1. 由 AI 到該機關的官方網站找 Logo，不用麻煩承辦人準備。臺北市各局處官網多半是 `機關英文簡稱.gov.taipei`，例如資訊局 `doit.gov.taipei`、民政局 `ca.gov.taipei`；不確定網址時，可從臺北市政府全球資訊網（`www.gov.taipei`）的機關列表找到連結。
2. 官網頁首的 Logo 可能是 `<img>`，也可能是 CSS 背景圖，兩處都要看。找到後確認圖上是**該局處自己的標誌**，不要誤抓頁尾的承包廠商 Logo、合作單位 Logo、活動橫幅。把原檔下載到 `assets/`，SVG 優先，其次是夠大的 PNG（高度至少 80px，顯示在高解析度螢幕上才不會糊）。
3. 在交付說明寫明 Logo 的來源網址，請承辦人看一眼確認是正確、最新的版本。
4. 有下列情形之一，就算「找不到局處 Logo」：
   - 連不上網路，或官網上找不到 Logo 圖檔。
   - 官網用的是臺北市政府的標誌或市徽，不是局處專屬的標誌。
   - 無法確定找到的圖是不是正式的局處標誌。

   這時**不放 Logo**，頁首只用文字寫機關全銜（例如「臺北市政府社會局」），也不得拿市府標誌、市徽或其他圖代替。並明確告訴承辦人：

   > 我在社會局官網上沒有找到局處專屬的 Logo，所以頁首先只放機關名稱文字。如果貴局有正式的 Logo 檔，請提供給我，我再換上去。

**使用規定**

- 必須使用機關的正式檔案。不得自己畫、用 AI 生成、描圖重繪，也不得用相似的圖示代替。
- 不得改顏色、拉長壓扁、裁切、旋轉，也不得加陰影、外框、光暈或動畫。
- 顯示高度約 30 至 40px，寬度依原比例自動縮放。Logo 四周要留空間，不要和文字、邊框貼在一起。
- 圖片的 `alt` 寫機關全銜，例如 `alt="臺北市政府資訊局"`。
- Logo 外面包一層連結，連回這個網站的首頁。
- 深色底上要放 Logo 時，使用機關提供的反白版本；沒有反白版本就不要放在深色底上。

**臺北市市徽**

- 市徽依《臺北市市徽市旗設置自治條例》使用，主管機關是民政局。不得擅自更改樣式，不得用在商業或不莊重的地方。
- 網頁上建議只把市徽做成瀏覽器分頁的小圖示（favicon），頁首用局處 Logo 就好。
- 市徽檔案應使用民政局或市府官網提供的正式檔案，不得重繪。

### 五、版面

```
┌─────────────────────────────────────────┐
│ 頁首：局處 Logo ＋ 服務名稱      主選單 │  高約 72px，白底，底部一條細線
├─────────────────────────────────────────┤
│ 路徑：首頁／目前頁面                     │
│                                          │
│ 臺北市政府〇〇局          ← 銜名，小字   │
│ 頁面大標                  ← h1，明體     │
│ ▬▬▬▬                     ← 市徽四色條   │
│ 一兩句話說明這頁可以做什麼               │
│ [ 主要按鈕 ]                             │
│                                          │
│ 段落標題                  ← h2，明體     │
│ ───────────────────                      │
│ 一、……                                   │
│ 二、……                                   │
├─────────────────────────────────────────┤
│ 頁尾：機關資訊、政策連結、無障礙標章     │
└─────────────────────────────────────────┘
```

- 內容區寬度：以閱讀為主的頁面，最大寬度約 40em（一行約 40 個中文字）；表格、儀表板可放寬到 72em。
- 區塊之間的距離約 48 至 56px，段落之間 16px。
- 手機版（寬度 640px 以下）改單欄，按鈕寬度可撐滿。
- 頁首固定在上方時，螢幕可視高度小於 480px（例如手機橫放）要取消固定，免得頁首占去太多畫面。

### 六、元件

**按鈕**

- 按鈕分四種：
  - 主要按鈕（`.tp-btn--primary`）：主色實心、白字。用在這個畫面最主要的那一個動作。
  - 次要按鈕（`.tp-btn--secondary`）：白底、主色外框。用在其他動作。
  - 危險按鈕（`.tp-btn--danger`）：白底、紅色外框紅字。用在退件、駁回、刪除、停用等不利於民眾或不可復原的動作；在確認對話框裡的最後確認鈕，改用紅色實心（`.tp-btn--danger-solid`）。
  - 文字連結：用在「回上一頁」「取消並返回」這類離開畫面的動作。
- 尺寸：所有按鈕高度至少 44px；主要按鈕建議 48px。圓角 8px，粗體（700）。
- 對外頁面：一個畫面只放一個主要按鈕，民眾才不會猶豫。
- 管理後臺：同一個區塊只放一個主要按鈕。例如列表頁的「查詢」和「新增案件」分屬篩選區與標題區，可以各自是主要按鈕；審核區有「核准」「候補」「補件」「退件」幾個並列決定時，最常用的一個用主要按鈕，其他用次要按鈕，不利於民眾的用危險按鈕，並且和其他按鈕隔開一點距離，避免誤按。
- 按鈕文字用動詞，講清楚按了會怎樣：「送出申請」「查詢」「下載申請表」。
- 圖示可以放在文字左邊，但不能只有圖示沒有文字。
- 送出中不要把按鈕設成 `disabled`（焦點會跑掉），改加 `aria-busy="true"`，並用程式擋住重複送出。

**表單欄位**

- 欄位名稱（`<label>`）放在欄位上方，必填寫「（必填）」，不要只用紅色星號。
- `placeholder` 只放範例（例如「例：0912-345-678」），不能拿來代替欄位名稱。
- 欄位下方可放一行說明，用 `aria-describedby` 連結。
- 錯誤訊息放在欄位正下方，寫清楚哪裡錯、要怎麼填，並把游標移回該欄位。
  - 好的寫法：「手機號碼應為 10 碼數字，例：0912345678」
  - 不好的寫法：「格式錯誤」「Invalid input」
- 欄位高度 44px，框線用 `--tp-border-input`，圓角 8px。

**重點提示區（提示帶）**

淺色底（`--tp-band`）加左側 3px 墨色直線，用來放「收到可疑連結？先查再點」這類需要特別注意的事項。一頁最多一兩個。

**條文式清單**

說明事項、注意事項、承諾事項，用「一、二、三、」編號，編號用明體加墨色。這是公文慣用的格式，比項目符號正式，也方便引用（「請參考第二點」）。

**表格**

- 一定要有 `<caption>`（表格標題）和 `<th scope="col">`。
- 不要用表格排版面。
- 手機上表格太寬時，外層加水平捲動，不要把字縮小。

**訊息提示**

送出結果、查詢結果放在一個常駐的 `<div role="status" aria-live="polite">` 裡，讓報讀軟體能唸出來。錯誤用 `--tp-danger`、成功用 `--tp-success`，並加上文字（「送出成功」「送出失敗」），不能只靠顏色區分。

**路徑（麵包屑）**

`<nav aria-label="路徑連結列">`，分隔符號用「／」，最後一項加 `aria-current="page"`。只有一頁的網站可省略。

**外部連結**

另開新視窗的連結，加上 `target="_blank" rel="noopener"`，並在 `title` 註明「[另開新視窗]」。

**圖示**

需要圖示時，用單色線條的 SVG（例如 Tabler Icons，MIT 授權），下載後放在專案裡。顏色用 `currentColor` 跟著文字走，線寬 1.75 至 2，大小 18 至 24px。圖示旁邊有文字時加 `aria-hidden="true"`；單獨當按鈕時要加 `aria-label`。

### 七、頁尾

頁尾放在 `<main>` 外面。一般機關網頁應放下列項目：

1. 機關全銜（可放 Logo）
2. 地址
3. 電話與服務時間（可加註「臺北市民當家熱線 1999」）
4. 隱私權及個人資料保護政策（連結）
5. 資訊安全政策（連結）
6. 政府網站資料開放宣告（連結）
7. 無障礙聲明（連結）
8. 無障礙標章（**取得之後**才放，見「陸、六」）
9. 最後更新日期
10. 臺北市政府全球資訊網（連結）

功能很單純的小工具，頁尾可以精簡，但**機關名稱、聯絡方式、隱私權政策、無障礙聲明**這四項不能省。內部管理後臺的頁尾另依「玖、二」的「後臺頁尾」辦理。

機關的地址、電話，應從機關官網的頁尾抄錄，和找 Logo 一樣，不用請承辦人另外提供；抄錄後在交付說明請承辦人確認。

## 伍、不要做的樣式

AI 做網頁很容易套出同一種版型：藍紫漸層、滿版 emoji、毛玻璃卡片、置中大標配三欄功能卡。這種畫面一看就知道是 AI 做的，放在市府網站上不莊重，很多也過不了無障礙檢測。下列樣式**不得使用**：

| 不要這樣做 | 原因 | 改成 |
|---|---|---|
| 藍紫、紫粉、彩虹漸層（背景、按鈕、文字） | 不是市府色系；漸層上的文字對比不穩定 | 白底加單一主色 |
| emoji 當圖示、標題裝飾、清單符號（🚀✨📌✅） | 各平臺長相不同；報讀軟體會唸出「火箭」；不莊重 | 單色線條 SVG，或不用圖示 |
| 毛玻璃、半透明卡片 | 對比無法控制，舊電腦跑起來卡 | 白底實色 |
| 霓虹光暈、多層大陰影 | 搶視線，看起來像遊戲或廣告 | 細線分段，頂多一層淡陰影 |
| 滑鼠移過去整張卡片浮起、捲動視差、進場動畫 | 分散注意力，前庭敏感的使用者會不舒服 | 不加動畫；真的要加，須尊重 `prefers-reduced-motion` |
| 16px 以上的大圓角、膠囊形狀的卡片 | 商業 App 的語彙 | 統一 8px |
| 置中超大標語、三欄功能卡、「已服務 10,000+ 人」、使用者好評區 | 新創公司產品頁的套路，政府網站不需要推銷 | 銜名、大標、說明、一個主要按鈕 |
| 深色科技風背景、純黑底、淺灰小字 | 對比不足，長輩看不清楚 | 白底深色字 |
| 只有圖示沒有文字的按鈕、拿 placeholder 當欄位名稱 | 看不懂、報讀軟體唸不出來 | 圖示加文字，label 放上方 |
| AI 生成的插畫或人物、圖庫的商務人士照片 | 和業務無關，也有著作權疑慮 | 用業務實景照片，或不放圖 |
| 把字做成圖片 | 無法放大、無法報讀、無法翻譯 | 用真的文字 |
| 重繪市徽或局處 Logo、改色、加特效 | 違反識別使用規定 | 用正式檔案原樣放置 |

## 陸、無障礙

### 一、法源

《身心障礙者權益保障法》第 52 條之 2 規定：「各級政府及其附屬機關（構）、學校所建置之網站，應通過第一優先等級以上之無障礙檢測，並取得認證標章。」檢測依據是數位發展部公告的《網站無障礙規範》，分 A、AA、AAA 三個等級。現行版參照 WCAG 2.1；115 年 5 月 29 日修正的新版自 115 年 11 月 30 日生效，新增 WCAG 2.2 的準則，例如焦點不得被固定頁首等元素遮住（2.4.11）、點選目標要夠大（2.5.8）、登入不得只靠記憶或解謎驗證（3.3.8）。新開發的網站請直接依新版設計。法定最低要求是第一優先等級（A），實務上新建或改版的網站多以 AA 為目標，本規範也以 AA 為底線。

### 二、依功能判斷目標等級

功能越單純，越容易做到 AAA。開工前，AI 必須依下表判斷，並把結果告訴承辦人確認。

| 功能程度 | 典型例子 | 目標等級 |
|---|---|---|
| 單純 | 純資訊頁、公告頁、1 至 3 個欄位的單一表單、查詢單一結果 | **AAA** |
| 中等 | 多步驟申請表單、查詢加列表加分頁、篩選排序、需要登入的後臺 | **至少 AA**，下面列的 AAA 項目能做的盡量做 |
| 複雜 | 地圖、互動圖表、即時更新的資料、影音、拖拉操作、嵌入第三方服務 | **AA 為底線**，列出做不到 AAA 的項目和替代方案 |

告訴承辦人時，可參考下列說法：

> 這個網頁只有一個查詢欄位和一個結果區，屬於功能單純的頁面，建議以 AAA 為目標。預計要做到的重點是：文字對比 7:1 以上、不設操作時間限制、錯誤訊息會說明正確格式。如果之後要加地圖，會再重新評估。請問是否同意？

網站之後加了新功能（例如加上地圖），要重新判斷一次。

### 三、每個等級都要做的事

- `<html lang="zh-Hant-TW">`。
- 頁面第一個可以用鍵盤移到的元素是「跳到主要內容」連結。
- 導盲磚：頁首、主要內容、頁尾開頭各放一個 `:::` 連結，分別設 `accesskey="U"`（上方）、`"C"`（中央）、`"Z"`（下方）。平時隱藏，用鍵盤移到時才出現。
- 用 `<header>`、`<nav>`、`<main>`、`<footer>` 標出區塊；`<footer>` 不放在 `<main>` 裡面。
- 每頁只有一個 `<h1>`，標題層級不跳號（h1 下面是 h2，不要直接跳 h3）。
- 有意義的圖片寫 `alt`；純裝飾的圖片寫 `alt=""`。
- 每個欄位都有對應的 `<label>`。
- 全部功能只用鍵盤也能操作，而且看得到目前焦點在哪裡（焦點框：3px 主色外框，`outline-offset: 2px`）。按鈕、連結、欄位等可以操作的元素，不得用 `outline: none` 把焦點框拿掉。唯一的例外是 `tabindex="-1"` 的跳轉目標（例如 `<main>`），它只是讓「跳到主要內容」有地方落腳，使用者不會操作它，可以不顯示焦點框。
- 不能只靠顏色傳達資訊。
- 動態出現的結果放在 `role="status"` 區塊裡。

### 四、AAA 要多做的事

目標是 AAA 的頁面，除了上面的基本項目，還要做到：

- 一般文字對比 7:1 以上，大字（24px 以上，或 18.66px 以上粗體）4.5:1 以上。
- 一行不超過 40em，行高至少 1.5，段落間距至少行高的 1.5 倍，不用左右對齊。
- 文字放大到 200% 時不會出現左右捲軸。
- 不用圖片呈現文字（Logo 除外）。
- 不設操作時間限制、不自動更新、不自動輪播。
- 沒有閃爍內容。
- 有路徑（麵包屑）讓使用者知道自己在哪裡。
- 單看連結文字就知道會連到哪裡，不要用「點此」「更多」。
- 用標題把內容分段。
- 可以點的地方至少 44×44px。
- 少用專有名詞和縮寫；一定要用時，第一次出現就解釋。文字寫到國中生看得懂的程度。
- 欄位旁邊提供範例和說明。
- 送出前可以檢查、修改；送出後可以撤回或更正。

### 五、做不到 AAA 時的替代方案

| 功能 | 難以達成的項目 | 替代做法 |
|---|---|---|
| 影片 | 手語翻譯、延伸口述影像 | 至少提供字幕和逐字稿 |
| 地圖 | 只能用滑鼠點選 | 另外提供地址或行政區的文字查詢，結果也用清單列出 |
| 圖表 | 看不到圖的人無法理解 | 圖表下方提供同一份資料的表格 |
| 即時更新 | 內容自己跳動 | 提供「暫停更新」或改成按鈕手動更新 |
| 登入逾時 | 不設逾時 | 逾時前提醒，並可一鍵延長 |
| 法規條文 | 閱讀程度太高 | 條文旁附白話摘要 |

### 六、無障礙標章與聲明

- 每個網站都要有一頁「無障礙聲明」，說明適用範圍、快速鍵（U／C／Z）、鍵盤操作方式、聯絡方式。
- 無障礙標章由機關向數位發展部申請：先用 Freego 檢測工具自我檢測，再上網登錄申請，經人工檢測通過後核發，效期 3 年。申請人必須是機關，不能由廠商代為申請。
- **網站還沒取得標章前，不得放標章圖示。** 取得後依核發規格放置（圖檔尺寸不可更動），連結到數位發展部的標章資料頁，`alt` 寫明等級，例如「通過AAA無障礙網頁檢測」。
- AI 不能替機關宣稱已通過檢測，只能說「依 ○○ 等級設計，建議送 Freego 檢測」。

## 柒、文字與用語

### 一、基本原則

網頁上的每一個字（標題、說明、按鈕、錯誤訊息、交付說明）都要像**承辦人平常講話**：清楚、客氣、不誇張。想像這段話是要印在臨櫃的告示上，或在電話裡唸給民眾聽。

- 用「臺北市」「臺灣」，不用「台北市」「台灣」。機關名稱用全銜，第一次出現時寫完整（「臺北市政府資訊局」），後面可簡稱「本局」。
- 稱呼民眾用「您」，稱呼自己機關用「本局」「本處」「本府」。
- 日期依機關習慣，對外服務可用「115 年 10 月 12 日」或「2026 年 10 月 12 日」，同一個網站統一一種。這是指**顯示**的格式。
- 日期**輸入**欄位：瀏覽器內建的日期選擇器（`<input type="date">`）只能選西元年，顯示格式又跟著電腦的語言設定走，所以：
  - 給民眾填寫的表單，網站用民國年時，改用「年、月、日」三個數字欄位（`inputmode="numeric"`），外層用 `<fieldset>` 和 `<legend>` 標出這是一個日期，例如「出生日期：民國〔　〕年〔　〕月〔　〕日」。送出前檢查日期是否存在。
  - 民眾用來查詢的日期篩選，優先改用「月份」下拉選單或「本週、本月」這類選項，避免讓民眾輸入日期。
  - 管理後臺的篩選條件與資料輸入（例如活動時間），可以使用內建的日期或日期時間選擇器，欄位說明寫明「請以西元年選擇」；查詢結果與列表仍以民國年顯示。
  - 資料庫一律存西元日期（ISO 格式，例如 2026-10-12），只在畫面上轉換成民國年。
- 數字、英文和中文之間留一個半形空格（「保存 3 年」「Excel 檔案」）。
- 標點用全形：，。、；：「」（）。不用驚嘆號。
- 不要中英夾雜。「上傳」不寫 upload，「網址」不寫 URL（專有名詞例外）。
- 不用 emoji。

### 二、AI 常用語與公務用語對照

| 不要寫 | 改成 |
|---|---|
| 🚀 立即開始！ | 開始申請 |
| 一鍵搞定、輕鬆完成 | 填寫完成後按「送出」 |
| 讓我們一起打造更美好的城市 | （刪掉，直接講這頁能做什麼） |
| 賦能、無縫接軌、一站式、全方位、生態系 | 講具體做了什麼：「線上就能申請，不用到現場」 |
| 智慧、創新、數位轉型（當形容詞堆疊） | 只在正式計畫名稱裡使用 |
| 歡迎使用本系統！我們很高興為您服務 | 本頁提供 ○○ 線上申請。 |
| 糟糕！出了點問題 😢 | 系統暫時無法處理您的申請，請稍後再試。如持續發生，請洽 ○○（電話 ○○○○）。 |
| 恭喜您！提交成功 🎉 | 已收到您的申請，案件編號 ○○○○。本局將於 7 個工作天內回覆。 |
| 您的隱私對我們非常重要 | 本局依個人資料保護法蒐集您的資料，僅用於 ○○。 |
| 首先……其次……最後…… | 用「一、二、三、」條列 |
| 值得注意的是、需要強調的是 | （刪掉，直接講） |
| 點擊這裡、了解更多 | 下載申請表、查看收費標準 |
| 提交 | 送出 |
| 用戶 | 使用者、民眾、申請人 |
| 帳戶 | 帳號 |
| 默認 | 預設 |
| 信息 | 資訊、訊息 |
| 視頻 | 影片 |
| 質量 | 品質 |
| 優化 | 改善、調整 |
| 屏幕 | 螢幕 |
| 鼠標 | 滑鼠 |
| 文件（指檔案時） | 檔案 |
| 登錄（指登入時） | 登入 |
| 激活 | 啟用 |

### 三、範例

語氣可參考下列例句。

> 本頁提供長青學苑秋季班線上報名。報名期間為 10 月 1 日至 10 月 15 日，每人限報 1 門課程。名額有限，額滿後將依報名順序列為候補，並以電話通知。

> 收到可疑簡訊？先查再點

句子平實、資訊完整、沒有形容詞堆疊，民眾讀完就知道該怎麼做。

## 捌、個人資料與資訊安全

法規依據和原則寫在 soul.md，這裡只寫程式上怎麼做。

### 一、蒐集個人資料的表單

- 只蒐集辦這件事真正需要的欄位。用不到的不要問（例如報名講座不需要身分證字號）。
- 表單上方或送出按鈕旁邊，必須直接放個資告知事項，不能只靠頁尾連結。告知事項依《個人資料保護法》第 8 條，要寫明：
  1. 蒐集機關名稱
  2. 蒐集目的
  3. 個人資料類別
  4. 利用的期間、地區、對象及方式
  5. 當事人可以行使的權利（查詢、閱覽、複製、補充更正、停止蒐集處理利用、刪除）及方式
  6. 不提供資料對權益的影響
- 告知事項的內容要具體，不能只寫「依相關法令使用」。不知道蒐集目的或保存期限時，用 `〔請填入〕` 標出來，在交付說明請承辦人補上，不要自己編。
- 有特種個人資料（病歷、醫療、基因、性生活、健康檢查、犯罪前科）時，先停下來告訴承辦人，確認有法律依據再做。

### 二、程式寫法

- 畫面上顯示個資時預設遮蔽，例如「王○明」「A12****789」「0912-***-678」。
- 個資不得寫進前端程式、瀏覽器的 localStorage、網址參數、log 檔。
- 測試資料一律用假資料（「王小明」「0912-345-678」），不得用真實民眾資料。
- 密碼、金鑰、資料庫連線字串不得寫在程式碼裡，改用環境變數，並把 `.env` 加進 `.gitignore`。
- 使用者輸入的內容一律當作不可信任：
  - 顯示到畫面時用 `textContent`，不得用 `innerHTML` 拼接。
  - 資料庫查詢用參數化查詢，不得字串拼接 SQL。
  - 前端和後端都要檢查格式。
- 錯誤頁不得顯示程式錯誤細節（堆疊資訊、資料庫訊息）。
- 不使用追蹤性 Cookie。需要 Cookie 時，設定 `Secure`、`HttpOnly`、`SameSite=Lax`。

### 三、上線設定

部署到正式主機時，應設定下列 HTTP 標頭（由機關資訊單位或主機管理者協助設定，交付說明要提醒）：

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: strict-origin-when-cross-origin
```

為了能套用上面這組 CSP，程式裡不要寫 inline `<script>` 和 `style="..."`，一律放在獨立的 `.js`、`.css` 檔。

其他提醒：

- 全站使用 HTTPS。
- 對外公開的系統，上線前應做弱點掃描；依機關的資通安全責任等級，可能還需要滲透測試。請承辦人洽機關資訊單位。
- 有管理後臺的，必須有登入和權限控管，不能只靠「網址不公開」。
- 保留必要的存取紀錄（時間、來源 IP、操作），寫明保存期限。

## 玖、複雜系統：管理後臺、登入、檔案上傳

前面各章以「給民眾看的頁面」為主。有管理後臺、登入、檔案上傳、資料庫的系統，風險和使用情境都不一樣，除了前面的規定，還要遵守本章。

### 一、開工前先說明：這類系統須有資訊單位參與

系統一旦有下列任何一項，就**必須**在開工前告訴承辦人，上線前要請機關資訊單位參與，不能自己做完就放上網路：

- 需要登入（帳號密碼、臺北通、市府單一簽入等）
- 有管理後臺，可以新增、修改、刪除資料
- 民眾或同仁可以上傳檔案
- 資料存在資料庫，而且含有個人資料
- 會寄信、發簡訊、串接其他機關的系統

可以這樣說明：

> 這個系統有後臺管理和檔案上傳，屬於資通系統，上線前需要經過機關資訊單位評估防護等級、做弱點掃描，並安排主機與備份。我可以先把程式做出來讓您試用，但請先不要自行放到對外網路上，建議現在就和資訊單位聯繫。

這類系統屬於「參、一」的第二或第三級。選擇技術前，應先問承辦人機關是否已有既定的平臺或主機，有的話優先配合；沒有的話，依「參、一」選擇，並把架構寫在交付說明裡，讓資訊單位評估。

### 二、兩種畫面，兩種版型

同一個系統裡，給民眾看的頁面和給同仁用的後臺，版型應該不同，但共用同一組配色與元件。

| | 對外頁面 | 管理後臺 |
|---|---|---|
| 使用者 | 民眾，偶爾使用 | 同仁，每天長時間使用 |
| 目標 | 一看就懂、放心 | 找得快、改得快、不出錯 |
| 版寬 | 約 40em 單欄 | 撐滿畫面，最大約 90em |
| 導覽 | 頁首簡單選單 | 左側功能選單（手機改成可收合） |
| 標題 | 明體大標、市徽四色條 | 黑體（`<body class="tp-admin">`），不放四色條 |
| 內容 | 條文式說明、一個主要按鈕 | 表格、篩選條件、批次操作 |
| 字級 | 內文 16px 以上 | 內文 15 至 16px，表格可到 14px |
| 無障礙目標 | 依功能判斷（多為 AAA 或 AA） | 至少 AA |

後臺仍然**不得**使用「伍、不要做的樣式」列出的任何樣式。後臺的頁首放局處 Logo（找不到時放機關全銜文字）與系統名稱，並清楚標示「管理系統」，避免同仁和對外網站搞混。

**後臺版面**

```
┌──────────────────────────────────────────────────┐
│ 局處 Logo ＋ 〇〇管理系統          王小明（承辦人）登出 │
├────────────┬─────────────────────────────────────┤
│ 案件管理   │ 案件管理／案件列表                    │
│ 檔案管理   │ 案件列表                    [新增案件] │
│ 帳號管理   │ ┌篩選：狀態▼  日期起迄  關鍵字 [查詢]┐ │
│ 操作紀錄   │ ├────────────────────────────────┤ │
│            │ │ 表格（可排序、分頁）              │ │
│            │ └────────────────────────────────┘ │
└────────────┴─────────────────────────────────────┘
```

**手機上的後臺頁首**

手機寬度（640px 以下）時，頁首只保留一行：局處 Logo（或機關全銜文字）和系統名稱，太長時系統名稱可縮短或換行在 Logo 下方。使用者姓名、登出、功能選單一律收進「選單」按鈕裡（`aria-expanded` 標示開合），不要全部擠在頁首。

**後臺頁尾**

內部後臺的頁尾放在 `<main>` 外面，只要放：

1. 機關全銜
2. 系統問題的聯絡窗口（單位、分機或信箱）
3. 系統版本或最後更新日期
4. 無障礙聲明（連結）
5. 系統處理個人資料時，放「資料保護說明」（連結）

對外頁面頁尾要求的地址、資料開放宣告、全球資訊網連結，後臺可以省略。「資料保護說明」是寫給同仁看的，說明系統裡有哪些個人資料、誰可以看、保存多久、存取會留下紀錄、外洩時找誰通報；不需要照抄對外隱私權政策的六項告知。

**後臺登入頁**

還沒登入的頁面（登入、忘記密碼、首次登入改密碼）沒有左側選單，用單欄置中版型（寬約 28em），頁首放局處 Logo 與系統名稱並標示「管理系統」，標題用黑體，不放四色條。

**後臺元件規定**

- **表格**：要有 `<caption>`、欄位標題、分頁與每頁筆數；可排序的欄位標題要是按鈕，並用 `aria-sort` 標示目前排序。資料多時用伺服器端分頁，不要一次全部載入。
- **篩選**：篩選條件放在表格上方，按「查詢」才套用，不要每打一個字就重新查詢。
- **需要確認的操作**：下列動作必須先跳出確認對話框，寫清楚會對哪一筆資料做什麼、會有什麼結果：
  - 影響民眾權益的決定：核准、駁回、退件、錄取、列入候補、通知補件。
  - 會通知民眾的動作：寄信、發簡訊、公告。
  - 不可復原的動作：刪除、批次修改、匯入覆蓋。

  寫法例如「確定退回案件 1150012（王○明，國畫山水）嗎？退件後將以簡訊通知申請人。」能做成「停用」或「移到回收區」，就不要真的刪除。
- **理由欄位**：不利於民眾的決定（駁回、退件、通知補件）必須填寫理由才能送出，欄位說明要提醒「這段文字會通知申請人」。核准、錄取這類有利的決定，可以讓承辦人選填備註。
- **批次操作**：先勾選，再選動作，執行前顯示「將對 12 筆資料執行停用」。
- **狀態**：用文字加顏色表示（「已結案」「處理中」「退件」），不能只用色點。
- **對話框**：使用原生 `<dialog>` 元素。開啟時焦點移進對話框：需要填寫理由的，焦點放在理由欄位；只需要確認的，焦點放在「取消」，避免按 Enter 就誤送出。按 Esc 可關閉，關閉後焦點回到原本的按鈕。按鈕排列為「取消」在前、確認鈕在後，確認鈕的文字寫出動作（「確定退件」，不寫「確定」）。注意：對話框若放在 `<form>` 裡面，對話框關閉時，其中標了 `required` 的欄位仍會被瀏覽器檢查，擋住整張表單送出。對話框應有自己獨立的 `<form method="dialog">` 或獨立的送出表單。需要確認的動作，在沒有 JavaScript 時也要能運作（例如改成先到一個確認頁）。
- **登入逾時**：逾時前 2 分鐘提醒，並可一鍵延長，避免同仁打到一半的資料不見。

### 三、登入與權限

不要讓登入方式拖住開發進度。臺北通、市府單一簽入這類串接都要另外申請，開通前沒辦法測試，所以分兩個階段處理：

**開發與試用階段**

- 先用系統自己的帳號密碼登入，讓承辦人可以馬上試用、確認功能。
- 登入的程式要獨立寫成一個模組，其他功能只透過這個模組取得「目前是誰、是什麼角色」。之後換成其他登入方式時，只要改這個模組，不用動到整個系統。
- 自己做的帳號密碼仍要做到基本安全：
  - 密碼用 bcrypt、scrypt 或 Argon2 雜湊後儲存，不得明文或可逆加密。
  - 連續輸入錯誤要暫時鎖定。沒有機關規定時，預設連續錯 5 次鎖定 15 分鐘。鎖定應以「帳號加來源 IP」計算，或改用逐次拉長等待時間，避免有心人故意輸錯把別人的帳號鎖住。
  - 密碼至少 12 個字元，不強制定期更換，但要擋掉常見的弱密碼（例如 `12345678`、`password`）。
  - 閒置 30 分鐘自動登出，逾時前 2 分鐘提醒並可一鍵延長（見「玖、二」）。
  - 以上是預設值；機關資通安全規定另有要求時，依機關規定。
  - 不得寫死 `admin／admin` 這類預設帳號密碼；初始管理者帳號由啟動指令或設定檔建立，首次登入強制變更密碼。

**正式上線階段（建議）**

- 民眾登入：建議評估串接臺北通（TaipeiPASS）。
- 市府同仁登入：建議評估使用機關或市府既有的單一簽入。
- 管理者帳號建議加上多因素驗證。
- 這些都需要申請與開通，交付說明應提醒承辦人及早洽機關資訊單位或臺北市政府資訊局，和開發同時進行。AI 不得自行假設串接規格；不知道的地方用〔待確認〕標示。
- 最後要不要串接、用哪一種，由機關依系統性質決定。沒有串接時，正式上線也要做到「開發與試用階段」所列的基本安全要求。

- **權限**：
  - 至少區分「一般承辦」「管理者」兩種角色，依最小權限原則給權限。
  - 每一個後端 API 都必須檢查「這個人有沒有權限做這件事」，不能只把前端按鈕藏起來。
  - 不能只靠網址不公開來保護後臺。
  - 承辦人只能看到自己業務範圍的資料時，查詢條件要在後端強制加上，不能交給前端篩選。
- **Session**：Cookie 設 `Secure`、`HttpOnly`、`SameSite=Lax`；登出要讓伺服器端的 session 失效；表單送出要有 CSRF 防護。
  - 試用階段在本機用 `http://127.0.0.1` 或 `http://localhost` 開啟時，瀏覽器允許 `Secure` Cookie，可以正常登入。同事用區網 IP（例如 `http://192.168.x.x`）連進來會無法登入，這是正常的安全行為。不要為了方便而關掉 `Secure`，請在 README 說明只能用本機網址試用，或請資訊單位架設有 HTTPS 的測試主機。
- **民眾查詢功能**：讓民眾用「編號加手機號碼」這類資料查詢或取消的功能，要限制失敗次數。沒有機關規定時，預設同一來源 IP 15 分鐘內最多失敗 10 次，避免被人亂猜編號。

### 四、檔案上傳

檔案上傳是最常被拿來攻擊的功能之一，下列規定**必須**全部做到：

1. **限制檔案類型**：只接受業務需要的類型（例如 PDF、JPG、PNG），用白名單。不能只看副檔名，後端要檢查檔案實際內容（magic number）。一律拒絕 `.exe`、`.js`、`.html`、`.svg`、`.php` 等可以執行或內含程式碼的檔案。
2. **限制大小與數量**：設定單檔上限與總量上限（例如單檔 10MB、一次最多 5 個），前端提示、後端強制。
3. **重新命名**：存檔時用系統產生的隨機名稱，不要沿用使用者上傳的檔名（原檔名另存在資料庫）。
4. **存放位置**：存在網站根目錄以外的地方，或物件儲存空間，不能讓人直接用網址開啟或執行。下載時由程式檢查權限後再傳送，並設定 `Content-Disposition: attachment` 與正確的 `Content-Type`。
5. **病毒掃描**：對外開放上傳的系統，應經過防毒掃描後才讓承辦人開啟。請承辦人洽資訊單位提供掃描機制。
6. **個資**：上傳的檔案常含身分證影本、診斷證明等個資。要寫明保存期限，到期自動刪除；後臺顯示時只給有權限的人看。
7. **圖片**：民眾上傳的圖片，要移除 EXIF 資訊（裡面可能有拍攝地點）。
8. **紀錄**：記下誰在什麼時候上傳、下載、刪除了哪個檔案。

上傳欄位本身也要符合無障礙：

- 使用原生 `<input type="file">`，搭配 `<label>`。
- 欄位說明寫明接受的類型與大小（「可上傳 PDF、JPG、PNG，單檔 10MB 以內，最多 5 個」）。
- 上傳後列出已選擇的檔名，每個檔案旁邊有可用鍵盤操作的「移除」按鈕。
- 上傳進度與結果放在 `role="status"` 區塊裡。
- 拖放上傳可以做，但必須同時保留按鈕選檔的方式。

### 五、操作紀錄

後臺系統必須留下操作紀錄，出問題時才查得到是誰、什麼時候、做了什麼：

- 記錄登入、登出、登入失敗、新增、修改、刪除、匯出、權限變更、檔案下載。
- 每筆紀錄包含：時間、帳號、來源 IP、動作、對象（例如案件編號）。
- 紀錄裡不寫密碼，也不寫完整個資（記「修改了案件 1150012 的電話欄位」，不記新的電話號碼）。
- 一般使用者不能修改或刪除紀錄。
- 保存期限依機關規定，沒有規定時請承辦人洽資訊單位，不要自己訂。

### 六、匯出與報表

- 匯出功能要有權限控管，並記錄在操作紀錄裡。
- 匯出的個資欄位預設遮蔽，需要完整資料時要有理由並經授權。
- 匯出 CSV 時，儲存格開頭是 `=`、`+`、`-`、`@` 的內容，要在前面加上單引號，避免用 Excel 打開時被當成公式執行。
- 圖表要同時提供資料表格（見「陸、五」）。

### 七、名額與重複送出

報名、預約、申請這類有名額的系統，最常出事的是**超收**和**重複報名**。前端擋重複點擊不夠，後端必須做到：

- 名額檢查和寫入要在同一個資料庫交易裡完成，並鎖定該活動的資料列（或用條件式更新，例如「目前人數小於名額才加一」），避免很多人同時搶最後一個名額時超收。
- 每份表單帶一個一次性代碼，同一個代碼重複送出只建立一筆，並回到同一個結果頁。
- 依業務規則加上資料庫唯一索引，例如「同一活動、同一手機號碼只能報名一次」，讓程式疏漏時資料庫還能再擋一次。
- 表單送出成功後，轉到結果頁（Post/Redirect/Get），使用者按重新整理時不會再送一次。
- 交付前要實測：多人同時搶最後一個名額、連按送出、同一資料重複報名。

### 八、多機關共用的平臺

一個平臺給很多局處共用（例如全市活動報名、共用預約系統）時：

- **頁首與頁尾**：放負責維運的機關（例如資訊局）的 Logo 與聯絡資料，頁尾註明「本網站由臺北市政府〇〇局維護」。
- **各頁內容**：每個活動或服務頁面清楚寫出主辦機關與洽詢方式，讓民眾知道有問題要找誰。
- **個資告知**：蒐集機關寫主辦該活動的機關，告知事項依主辦機關填寫的內容自動帶入；另外註明網站由哪個機關維運。若主辦機關與維運機關之間有委託處理個資的關係，具體寫法請承辦人洽機關法制或個資窗口確認。
- **權限**：各機關只能看到、管理自己的資料，查詢條件在後端強制加上（見「玖、三」）。
- **頁面上的機關資料**：主辦機關的地址、電話若要顯示，由各機關承辦人在後臺填寫，或由 AI 從各機關官網抄錄並標示來源；不知道時用〔請填入〕，不要編。

### 九、資料庫

- 一律使用參數化查詢或 ORM，不得字串拼接 SQL。
- 資料庫帳號只給程式需要的權限，不用最高權限帳號連線。
- 個資欄位依需要加密儲存。
- 交付說明要提醒：正式上線前要建立備份機制，並實際測試還原。

### 十、交付時要多寫的事

交付說明的「上線前還要做的事」，除了一般項目，還要列出：

- 需要資訊單位協助的項目：主機、HTTPS、防毒掃描、備份、弱點掃描；如果要串接臺北通或單一簽入，也要及早申請。
- 系統用到的帳號、角色與權限設計。
- 資料保存期限與刪除方式，標示哪些需要承辦人確認。
- 如何啟動系統、如何更新，寫給之後接手維護的人。

## 拾、頁面範本

以下是可以直接使用的完整範本（對外頁面）。管理後臺沿用同一份 `tp.css`，版型依「玖、二」：`<body class="tp-admin">`，內容外層用 `.tp-admin-layout`，左側選單用 `.tp-sidenav`，登入頁用 `.tp-login`；另有分頁 `.tp-pagination`、確認對話框 `.tp-dialog`、單選複選群組 `.tp-fieldset`／`.tp-choice`、危險按鈕 `.tp-btn--danger` 可直接使用。〔 〕內是要換成實際內容的地方。

### 一、index.html

```html
<!doctype html>
<html lang="zh-Hant-TW">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>〔服務名稱〕｜臺北市政府〔機關〕</title>
  <meta name="description" content="〔一句話說明這個網站可以做什麼〕">
  <link rel="icon" href="assets/favicon.ico">
  <link rel="stylesheet" href="assets/tp.css">
  <script src="assets/app.js" defer></script>
</head>
<body>
  <a class="tp-skip" href="#main">跳到主要內容</a>

  <header class="tp-header" id="top">
    <a class="tp-accesskey" href="#top" accesskey="U" title="上方功能區塊">:::</a>
    <div class="tp-header__inner">
      <a class="tp-brand" href="./">
        <!-- Logo 從機關官網取得局處專屬標誌的原檔。找不到時（含只有市府標誌的情形），
             刪除這行 img，改成 <span class="tp-brand__org">臺北市政府〔機關〕</span>，
             並請承辦人提供 Logo 檔（見「肆、四」）。 -->
        <img src="assets/logo.svg" alt="臺北市政府〔機關〕" height="40">
        <span class="tp-brand__name">〔服務名稱〕</span>
      </a>
      <nav class="tp-nav" aria-label="主要功能選單">
        <ul>
          <li><a href="./">首頁</a></li>
          <li><a href="〔頁面〕.html">〔功能〕</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="tp-main" id="main" tabindex="-1">
    <a class="tp-accesskey" href="#main" accesskey="C" title="中央內容區塊">:::</a>

    <section class="tp-hero">
      <p class="tp-eyebrow">臺北市政府〔機關〕</p>
      <h1>〔頁面大標〕</h1>
      <div class="tp-stripe" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
      <p class="tp-lead">〔用一兩句話說明這頁可以做什麼、要準備什麼〕</p>
      <p><a class="tp-btn tp-btn--primary" href="#apply">〔動詞，例：開始申請〕</a></p>
    </section>

    <section class="tp-section" aria-labelledby="notice-title">
      <h2 id="notice-title">〔段落標題，例：申請須知〕</h2>
      <ol class="tp-clauses">
        <li><span class="tp-clauses__no">一、</span>〔說明〕</li>
        <li><span class="tp-clauses__no">二、</span>〔說明〕</li>
        <li><span class="tp-clauses__no">三、</span>〔說明〕</li>
      </ol>
    </section>

    <aside class="tp-band" aria-labelledby="band-title">
      <p class="tp-band__title" id="band-title">〔重點提示標題〕</p>
      <p>〔提示內容〕</p>
    </aside>

    <section class="tp-section" id="apply" aria-labelledby="apply-title">
      <h2 id="apply-title">〔表單標題〕</h2>

      <div class="tp-privacy">
        <p class="tp-privacy__title">個人資料蒐集告知</p>
        <ol class="tp-clauses tp-clauses--small">
          <li><span class="tp-clauses__no">一、</span>蒐集機關：臺北市政府〔機關〕。</li>
          <li><span class="tp-clauses__no">二、</span>蒐集目的：〔請填入，例：辦理○○活動報名及通知〕。</li>
          <li><span class="tp-clauses__no">三、</span>個人資料類別：姓名、聯絡電話、電子郵件。</li>
          <li><span class="tp-clauses__no">四、</span>利用期間、地區、對象及方式：〔請填入，例：活動結束後 6 個月內，於本〔局／處〕業務範圍內，以電話或電子郵件通知〕；期滿後刪除。</li>
          <li><span class="tp-clauses__no">五、</span>您可以依個人資料保護法第 3 條，向本〔局／處〕請求查詢、閱覽、製給複製本、補充或更正、停止蒐集處理利用或刪除。聯絡方式：〔電話〕。</li>
          <li><span class="tp-clauses__no">六、</span>您可以自由選擇是否提供資料；未提供必填欄位時，將無法完成〔報名〕。</li>
        </ol>
      </div>

      <form class="tp-form" id="apply-form" novalidate>
        <div class="tp-field">
          <label for="name">姓名（必填）</label>
          <input id="name" name="name" type="text" autocomplete="name" required
                 aria-describedby="name-err">
          <p class="tp-field__error" id="name-err" hidden></p>
        </div>

        <div class="tp-field">
          <label for="phone">手機號碼（必填）</label>
          <input id="phone" name="phone" type="tel" inputmode="numeric" autocomplete="tel"
                 required pattern="09[0-9]{8}" aria-describedby="phone-hint phone-err">
          <p class="tp-field__hint" id="phone-hint">10 碼數字，例：0912345678</p>
          <p class="tp-field__error" id="phone-err" hidden></p>
        </div>

        <div class="tp-field">
          <label for="email">電子郵件</label>
          <input id="email" name="email" type="email" autocomplete="email"
                 aria-describedby="email-hint email-err">
          <p class="tp-field__hint" id="email-hint">選填，用來寄送通知，例：name@example.com</p>
          <p class="tp-field__error" id="email-err" hidden></p>
        </div>

        <div class="tp-field tp-field--check">
          <input id="agree" name="agree" type="checkbox" required aria-describedby="agree-err">
          <label for="agree">我已閱讀上方個人資料蒐集告知（必填）</label>
          <p class="tp-field__error" id="agree-err" hidden></p>
        </div>

        <button class="tp-btn tp-btn--primary" type="submit">送出申請</button>
      </form>

      <div class="tp-status" id="form-status" role="status" aria-live="polite"></div>
    </section>
  </main>

  <footer class="tp-footer" id="footer">
    <a class="tp-accesskey" href="#footer" accesskey="Z" title="下方功能區塊">:::</a>
    <div class="tp-footer__inner">
      <p class="tp-footer__org">臺北市政府〔機關〕</p>
      <p>地址：〔郵遞區號〕臺北市〔地址〕</p>
      <p>電話：〔02-XXXX-XXXX〕（服務時間：週一至週五 8:30–17:30）　臺北市民當家熱線 1999</p>
      <ul class="tp-footer__links">
        <li><a href="privacy.html">隱私權及個人資料保護政策</a></li>
        <li><a href="〔資訊安全政策網址〕">資訊安全政策</a></li>
        <li><a href="〔政府網站資料開放宣告網址〕">政府網站資料開放宣告</a></li>
        <li><a href="accessibility.html">無障礙聲明</a></li>
        <li><a href="https://www.gov.taipei" target="_blank" rel="noopener" title="[另開新視窗]臺北市政府全球資訊網">臺北市政府全球資訊網</a></li>
      </ul>
      <p class="tp-footer__meta">最後更新：〔115 年 10 月 12 日〕</p>
      <!-- 取得無障礙標章後才放：
      <a href="〔數位發展部標章資料頁網址〕" target="_blank" rel="noopener" title="[另開新視窗]無障礙標章資料">
        <img src="assets/accessibility-aaa.png" width="88" height="31" alt="通過AAA無障礙網頁檢測">
      </a>
      -->
    </div>
  </footer>
</body>
</html>
```

### 二、assets/tp.css

```css
/* 臺北市政府網頁共用樣式
   機關可替換主色，但須重新確認文字對比度。 */

:root {
  --tp-primary: #0F5C86;
  --tp-primary-dark: #094463;
  --tp-primary-tint: #E9F2F7;
  --tp-ink: #16324A;
  --tp-text: #212529;
  --tp-text-muted: #495057;
  --tp-bg: #FAFBFC;
  --tp-surface: #FFFFFF;
  --tp-band: #F1F6FA;
  --tp-border: #DEE2E6;
  --tp-border-input: #6C757D;
  --tp-danger: #A61E1E;
  --tp-success: #14532D;
  --tp-warning: #6F3404;
  --tp-info: #0B3A66;

  /* 市徽四色：只用在 .tp-stripe */
  --tp-emblem-red: #C64B4B;
  --tp-emblem-yellow: #DFA92E;
  --tp-emblem-green: #2F9464;
  --tp-emblem-blue: #2B6CB0;

  --tp-font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC",
                  "PingFang TC", "Microsoft JhengHei", Arial, sans-serif;
  --tp-font-serif: "Noto Serif TC", "PMingLiU", "MingLiU", serif;

  --tp-radius: 8px;
  --tp-measure: 40em;
  --tp-measure-wide: 72em;
  --tp-header-h: 72px;
  --tp-focus: 3px solid var(--tp-primary);
}

*, *::before, *::after { box-sizing: border-box; }

html {
  font-size: 100%;
  /* 固定頁首不可遮住跳轉目標與焦點欄位 */
  scroll-padding-top: calc(var(--tp-header-h) + 16px);
}

body {
  margin: 0;
  background: var(--tp-bg);
  color: var(--tp-text);
  font-family: var(--tp-font-sans);
  font-size: 1rem;
  line-height: 1.8;
}

a { color: var(--tp-primary); text-underline-offset: 3px; }
a:hover { color: var(--tp-primary-dark); }

:focus-visible {
  outline: var(--tp-focus);
  outline-offset: 2px;
}

h1, h2, h3 { color: var(--tp-ink); line-height: 1.35; margin: 0; }
h1, h2 { font-family: var(--tp-font-serif); font-weight: 700; }
/* 管理後臺：<body class="tp-admin">，標題改用黑體 */
.tp-admin h1, .tp-admin h2 { font-family: var(--tp-font-sans); letter-spacing: 0; }
.tp-admin h1 { font-size: 1.75rem; }
.tp-admin h2 { font-size: 1.25rem; }
h1 { font-size: clamp(2rem, 5.5vw, 3rem); letter-spacing: 2px; }
h2 { font-size: 1.45rem; }
h3 { font-size: 1.15rem; font-weight: 600; }

p { margin: 0 0 1rem; }

/* 跳到主要內容、導盲磚：平時隱藏，鍵盤聚焦時出現 */
/* 只給報讀軟體讀的文字（例如隱藏的欄位名稱），畫面上不顯示 */
.tp-visually-hidden {
  position: absolute !important;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.tp-skip,
.tp-accesskey {
  position: absolute;
  left: -9999px;
  top: 0;
  z-index: 2000;
  padding: 6px 12px;
  background: #FFFFFF;
  color: var(--tp-ink);
  font-weight: 700;
  text-decoration: none;
  border: 2px solid var(--tp-primary);
  border-radius: 4px;
}
.tp-skip:focus,
.tp-accesskey:focus { left: 8px; top: 8px; }

/* 頁首 */
.tp-header {
  position: sticky;
  top: 0;
  z-index: 100;
  min-height: var(--tp-header-h);
  background: var(--tp-surface);
  border-bottom: 2px solid var(--tp-border);
}
.tp-header__inner {
  max-width: var(--tp-measure-wide);
  margin: 0 auto;
  padding: 12px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px 24px;
}
.tp-brand {
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--tp-ink);
  text-decoration: none;
}
.tp-brand img { height: clamp(30px, 5.5vw, 40px); width: auto; }
.tp-brand__name { font-weight: 700; font-size: 1.1rem; }
.tp-brand__org { font-weight: 700; font-size: 1rem; letter-spacing: 1px; }
.tp-nav ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 4px 20px; }
.tp-nav a {
  display: inline-block;
  min-height: 44px;
  padding: 10px 0;
  color: var(--tp-text);
  font-weight: 600;
  text-decoration: none;
}
.tp-nav a:hover,
.tp-nav a[aria-current="page"] { color: var(--tp-primary); text-decoration: underline; }

/* 可視高度太矮時取消固定頁首 */
@media (max-height: 480px) {
  .tp-header { position: static; }
}

/* 主要內容 */
.tp-main {
  max-width: var(--tp-measure);
  margin: 0 auto;
  padding: 32px 20px 56px;
}
.tp-main--wide { max-width: var(--tp-measure-wide); }
/* 例外：main 是 tabindex="-1" 的跳轉目標，不是可操作的元素 */
.tp-main:focus { outline: none; }

.tp-hero { margin-bottom: 56px; }
.tp-eyebrow {
  margin: 0 0 12px;
  font-size: 0.875rem;
  font-weight: 600;
  letter-spacing: 4px;
  color: var(--tp-text-muted);
}
.tp-hero h1 { margin-bottom: 16px; }
.tp-lead { font-size: 1.0625rem; line-height: 1.9; }

/* 市徽四色條：整頁只出現一次 */
.tp-stripe {
  display: flex;
  width: 168px;
  height: 4px;
  margin: 0 0 20px;
  border-radius: 2px;
  overflow: hidden;
}
.tp-stripe i { flex: 1; }
.tp-stripe i:nth-child(1) { background: var(--tp-emblem-red); }
.tp-stripe i:nth-child(2) { background: var(--tp-emblem-yellow); }
.tp-stripe i:nth-child(3) { background: var(--tp-emblem-green); }
.tp-stripe i:nth-child(4) { background: var(--tp-emblem-blue); }

/* 段落 */
.tp-section { margin-bottom: 56px; }
.tp-section > h2 {
  padding-bottom: 12px;
  margin-bottom: 20px;
  border-bottom: 1px solid var(--tp-border);
}

/* 條文式清單 */
.tp-clauses { list-style: none; margin: 0; padding: 0; }
.tp-clauses li {
  display: flex;
  gap: 4px;
  margin-bottom: 12px;
  line-height: 1.9;
}
.tp-clauses__no {
  flex: none;
  font-family: var(--tp-font-serif);
  font-weight: 700;
  color: var(--tp-ink);
}
.tp-clauses--small li { font-size: 0.9375rem; margin-bottom: 6px; }

/* 重點提示帶 */
.tp-band {
  margin: 0 0 56px;
  padding: 24px 28px;
  background: var(--tp-band);
  border-left: 3px solid var(--tp-ink);
  border-radius: 0 var(--tp-radius) var(--tp-radius) 0;
}
.tp-band a { color: var(--tp-primary-dark); }
.tp-band__title {
  margin-bottom: 6px;
  font-family: var(--tp-font-serif);
  font-size: 1.125rem;
  font-weight: 700;
  color: var(--tp-ink);
}
.tp-band p:last-child { margin-bottom: 0; }

/* 個資告知 */
.tp-privacy {
  margin-bottom: 24px;
  padding: 20px 24px;
  background: var(--tp-surface);
  border: 1px solid var(--tp-border);
  border-radius: var(--tp-radius);
}
.tp-privacy__title { font-weight: 700; color: var(--tp-ink); margin-bottom: 8px; }

/* 按鈕 */
.tp-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 48px;
  padding: 10px 24px;
  border: 2px solid var(--tp-primary);
  border-radius: var(--tp-radius);
  font: inherit;
  font-weight: 700;
  text-decoration: none;
  cursor: pointer;
}
.tp-btn--primary { background: var(--tp-primary); color: #FFFFFF; }
.tp-btn--primary:hover { background: var(--tp-primary-dark); border-color: var(--tp-primary-dark); color: #FFFFFF; }
.tp-btn--secondary { background: var(--tp-surface); color: var(--tp-primary); }
.tp-btn--secondary:hover { background: var(--tp-primary-tint); color: var(--tp-primary-dark); }
.tp-btn--danger { background: var(--tp-surface); color: var(--tp-danger); border-color: var(--tp-danger); }
.tp-btn--danger:hover { background: #FFFFFF; color: #7F1D1D; border-color: #7F1D1D; }
.tp-btn--danger-solid { background: var(--tp-danger); color: #FFFFFF; border-color: var(--tp-danger); }
.tp-btn--danger-solid:hover { background: #7F1D1D; border-color: #7F1D1D; color: #FFFFFF; }
.tp-btn--small { min-height: 44px; padding: 6px 14px; }
.tp-btn svg { width: 20px; height: 20px; flex: none; }

/* 表單 */
.tp-form { display: grid; gap: 20px; }
.tp-field label { display: block; margin-bottom: 6px; font-weight: 600; }
.tp-field input[type="text"],
.tp-field input[type="tel"],
.tp-field input[type="email"],
.tp-field input[type="number"],
.tp-field input[type="date"],
.tp-field input[type="datetime-local"],
.tp-field input[type="time"],
.tp-field input[type="month"],
.tp-field input[type="password"],
.tp-field input[type="search"],
.tp-field input[type="url"],
.tp-field select,
.tp-field textarea {
  width: 100%;
  min-height: 44px;
  padding: 8px 12px;
  border: 1px solid var(--tp-border-input);
  border-radius: var(--tp-radius);
  background: var(--tp-surface);
  color: var(--tp-text);
  font: inherit;
}
.tp-field textarea { min-height: 120px; }
.tp-field [aria-invalid="true"] { border: 2px solid var(--tp-danger); }
.tp-field__hint { margin: 6px 0 0; font-size: 0.9375rem; color: var(--tp-text-muted); }
.tp-field__error { margin: 6px 0 0; font-weight: 600; color: var(--tp-danger); }
.tp-field--check { display: flex; flex-wrap: wrap; align-items: flex-start; gap: 10px; }
.tp-field--check input { width: 24px; height: 24px; margin: 4px 0 0; flex: none; }
.tp-field--check label { flex: 1; margin: 0; font-weight: 400; }
.tp-field--check .tp-field__error { flex-basis: 100%; }

/* 單選、複選群組：外層用 fieldset＋legend */
.tp-fieldset { border: 0; margin: 0; padding: 0; }
.tp-fieldset legend { font-weight: 600; margin-bottom: 6px; padding: 0; }
.tp-choice { display: flex; align-items: flex-start; gap: 10px; min-height: 44px; padding: 8px 0; }
.tp-choice input { width: 24px; height: 24px; margin: 2px 0 0; flex: none; }
.tp-choice label { margin: 0; font-weight: 400; }

/* 結果訊息 */
.tp-status:empty { display: none; }
.tp-status {
  margin-top: 20px;
  padding: 16px 20px;
  border-left: 3px solid var(--tp-info);
  background: var(--tp-band);
  color: var(--tp-info);
  font-weight: 600;
}
.tp-status--success { border-color: var(--tp-success); color: var(--tp-success); }
.tp-status--error { border-color: var(--tp-danger); color: var(--tp-danger); }

/* 表格 */
.tp-table-wrap { overflow-x: auto; margin-bottom: 24px; }
.tp-table { width: 100%; border-collapse: collapse; background: var(--tp-surface); }
.tp-table caption { text-align: left; font-weight: 700; color: var(--tp-ink); padding-bottom: 8px; }
.tp-table th,
.tp-table td { padding: 10px 12px; border-bottom: 1px solid var(--tp-border); text-align: left; vertical-align: top; }
.tp-table th { background: var(--tp-primary-tint); color: var(--tp-ink); font-weight: 700; }

/* 分頁 */
.tp-pagination ul { list-style: none; margin: 24px 0; padding: 0; display: flex; flex-wrap: wrap; gap: 8px; }
.tp-pagination a,
.tp-pagination span {
  display: inline-flex; align-items: center; justify-content: center;
  min-width: 44px; min-height: 44px; padding: 0 12px;
  border: 1px solid var(--tp-border-input); border-radius: var(--tp-radius);
  text-decoration: none; color: var(--tp-primary); background: var(--tp-surface);
}
.tp-pagination [aria-current="page"] { background: var(--tp-primary); border-color: var(--tp-primary); color: #FFFFFF; font-weight: 700; }

/* 確認對話框（原生 dialog） */
.tp-dialog {
  width: min(32em, calc(100vw - 32px));
  padding: 24px;
  border: 1px solid var(--tp-border);
  border-radius: var(--tp-radius);
  background: var(--tp-surface);
  color: var(--tp-text);
  box-shadow: 0 2px 12px rgba(0, 0, 0, .12);
}
.tp-dialog::backdrop { background: rgba(22, 50, 74, .45); }
.tp-dialog h2 { font-family: var(--tp-font-sans); font-size: 1.25rem; margin-bottom: 12px; }
.tp-dialog__actions { display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 12px; margin-top: 20px; }

/* 管理後臺版面：<body class="tp-admin">，內容外層 .tp-admin-layout */
.tp-admin-layout { display: grid; grid-template-columns: 14rem minmax(0, 1fr); gap: 32px; max-width: 90em; margin: 0 auto; padding: 24px 20px 56px; }
.tp-admin-layout .tp-main { max-width: none; margin: 0; padding: 0; }
.tp-sidenav ul { list-style: none; margin: 0; padding: 0; }
.tp-sidenav a {
  display: block; min-height: 44px; padding: 10px 14px;
  border-left: 3px solid transparent; border-radius: 0 var(--tp-radius) var(--tp-radius) 0;
  color: var(--tp-text); font-weight: 600; text-decoration: none;
}
.tp-sidenav a:hover { background: var(--tp-band); color: var(--tp-primary-dark); }
.tp-sidenav a[aria-current="page"] { border-left-color: var(--tp-primary); background: var(--tp-primary-tint); color: var(--tp-primary-dark); }
.tp-sidenav__group { margin: 20px 0 6px; padding-left: 14px; font-size: 0.875rem; font-weight: 700; color: var(--tp-text-muted); }

/* 後臺登入頁：單欄置中 */
.tp-login { max-width: 28em; margin: 48px auto; padding: 0 20px; }

/* 路徑 */
.tp-crumbs ol { list-style: none; margin: 0 0 24px; padding: 0; display: flex; flex-wrap: wrap; font-size: 0.9375rem; }
.tp-crumbs li + li::before { content: "／"; padding: 0 6px; color: var(--tp-text-muted); }

/* 頁尾 */
.tp-footer {
  border-top: 1px solid var(--tp-border);
  background: var(--tp-surface);
  font-size: 0.9375rem;
  color: var(--tp-text-muted);
}
.tp-footer__inner { max-width: var(--tp-measure-wide); margin: 0 auto; padding: 32px 20px 40px; }
.tp-footer__inner p { margin-bottom: 6px; }
.tp-footer__org { font-weight: 700; color: var(--tp-ink); }
.tp-footer__links { list-style: none; margin: 16px 0; padding: 0; display: flex; flex-wrap: wrap; gap: 4px 20px; }
.tp-footer__links a { color: var(--tp-primary); display: inline-block; padding: 10px 0; }
.tp-footer__meta { margin-top: 12px; }

/* 手機版 */
@media (max-width: 640px) {
  /* 後臺左側選單改到內容上方，由「選單」按鈕開合 */
  .tp-admin-layout { grid-template-columns: 1fr; gap: 16px; }
  /* 手機上頁首會換行變高，改為隨頁面捲動 */
  .tp-header { position: static; }
  html { scroll-padding-top: 16px; }
  .tp-main { padding-top: 24px; }
  .tp-btn { width: 100%; }
  .tp-band { padding: 20px; }
}

/* 使用者設定減少動態效果時，關閉所有動畫與轉場 */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation: none !important;
    transition: none !important;
    scroll-behavior: auto !important;
  }
}

@media print {
  .tp-header, .tp-footer, .tp-skip, .tp-accesskey, .tp-btn { display: none; }
  body { background: #FFFFFF; }
}
```

### 三、assets/app.js

```js
// 表單檢查：錯誤訊息寫在欄位下方，並把焦點移到第一個錯誤欄位。
// 顯示文字一律用 textContent，不使用 innerHTML。

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('apply-form');
  if (!form) return;

  const status = document.getElementById('form-status');
  const submitBtn = form.querySelector('button[type="submit"]');
  let sending = false;

  const rules = {
    name: (v) => (v.trim() ? '' : '請填寫姓名。'),
    phone: (v) => (/^09\d{8}$/.test(v.trim()) ? '' : '手機號碼應為 10 碼數字，例：0912345678。'),
    email: (v) => (!v.trim() || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) ? '' : '電子郵件格式不正確，例：name@example.com。'),
    agree: (_, el) => (el.checked ? '' : '請勾選「我已閱讀上方個人資料蒐集告知」。'),
  };

  function setError(input, message) {
    const err = document.getElementById(input.id + '-err');
    if (message) {
      input.setAttribute('aria-invalid', 'true');
      err.textContent = message;
      err.hidden = false;
    } else {
      input.removeAttribute('aria-invalid');
      err.textContent = '';
      err.hidden = true;
    }
  }

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    if (sending) return;

    let firstInvalid = null;
    for (const [id, check] of Object.entries(rules)) {
      const input = form.elements[id];
      if (!input) continue;
      const message = check(input.value, input);
      setError(input, message);
      if (message && !firstInvalid) firstInvalid = input;
    }

    status.className = 'tp-status';
    if (firstInvalid) {
      status.classList.add('tp-status--error');
      status.textContent = '有欄位需要修正，請依欄位下方說明填寫。';
      firstInvalid.focus();
      return;
    }

    sending = true;
    submitBtn.setAttribute('aria-busy', 'true');
    status.textContent = '資料送出中，請稍候。';

    try {
      // 〔請換成實際的送出程式〕
      // const res = await fetch('/api/apply', { method: 'POST', body: new FormData(form) });
      // if (!res.ok) throw new Error();
      status.classList.add('tp-status--success');
      status.textContent = '已收到您的申請。〔本局將於 7 個工作天內以電話與您聯繫。〕';
      form.reset();
    } catch {
      status.classList.add('tp-status--error');
      status.textContent = '系統暫時無法處理您的申請，請稍後再試。如持續發生，請洽〔聯絡電話〕。';
    } finally {
      sending = false;
      submitBtn.removeAttribute('aria-busy');
    }
  });
});
```

### 四、其他必要頁面

**accessibility.html（無障礙聲明）** 應包含：

1. 本網站依《網站無障礙規範》〔AA／AAA〕等級設計。
2. 快速鍵說明：Alt+U 上方功能區塊、Alt+C 中央內容區塊、Alt+Z 下方功能區塊（Mac 為 Control+Option+按鍵）。
3. 鍵盤操作：Tab 移到下一個項目、Shift+Tab 回上一個、Enter 執行。
4. 適用範圍與尚未符合的項目（如果有）。
5. 意見回饋的聯絡方式。

**privacy.html（隱私權及個人資料保護政策）** 應包含：蒐集哪些資料、做什麼用、保存多久、是否使用 Cookie、當事人權利與行使方式、聯絡窗口。內容不知道的地方用〔請填入〕標示，不要自己編。

## 拾壹、交付前檢核清單

完成後，把下面這份清單複製到回覆裡，逐項標示。沒過的項目先修正，再重新檢查一次。

標示方式：

- `[x]` 已做到
- `[ ]` 還沒做到（要先修正，或在交付說明寫明原因）
- `[—]` 不適用，後面用括號寫原因，例如「[—] 檔案上傳規定（本系統沒有上傳功能）」「[—] 後端權限檢查（本次只做畫面樣本，列入上線前待辦）」

不適用的項目不要硬打勾，也不要直接刪掉。

```
【畫面與識別】
[ ] 頁首有局處 Logo（正式檔案、未變形改色，alt 為機關全銜，連回首頁）；找不到時只放機關全銜文字，並已請承辦人提供
[ ] Logo 來源網址已寫在交付說明
[ ] 頁尾有機關名稱、地址、電話、隱私權政策、無障礙聲明
[ ] 沒有使用「伍、不要做的樣式」列出的任何樣式
[ ] 沒有 emoji、漸層、毛玻璃、大圓角、不必要的動畫

【文字】
[ ] 用語是「臺北市」不是「台北市」
[ ] 按鈕是動詞，錯誤訊息有說明怎麼改
[ ] 沒有行銷口吻、驚嘆號、中國大陸用語、不必要的英文
[ ] 不知道的內容用〔請填入〕標出，沒有自己編

【無障礙（目標等級：____）】
[ ] html lang="zh-Hant-TW"
[ ] 有「跳到主要內容」與 U／C／Z 導盲磚
[ ] 每頁一個 h1，標題層級沒有跳號
[ ] 圖片都有 alt
[ ] 每個欄位都有 label
[ ] 只用鍵盤可以完成所有操作，看得到焦點框
[ ] 文字對比符合目標等級（AA 4.5:1／AAA 7:1；沿用本規範色票即符合，自訂顏色要用對比檢查工具實測）
[ ] 不靠顏色單獨傳達資訊
[ ] 放大到 200% 沒有左右捲軸（可用瀏覽器縮放 200%，或把視窗寬度設為 640px 檢查）
[ ] 沒有放未取得的無障礙標章

【個資與資安】
[ ] 蒐集個資的表單旁有六項告知事項
[ ] 只蒐集必要欄位
[ ] 畫面上的個資有遮蔽
[ ] 測試資料都是假資料
[ ] 程式碼裡沒有密碼、金鑰、連線字串
[ ] 使用者輸入用 textContent 顯示、用參數化查詢存取資料庫
[ ] 沒有 inline script／style，可以套用 CSP
[ ] 外部資源已自架，或已鎖定版本並加 SRI
[ ] 沒有追蹤碼

【複雜系統（有登入、後臺、上傳、資料庫才需檢查）】
[ ] 已告知承辦人上線前須請資訊單位參與
[ ] 後臺版型與對外頁面分開，仍未使用禁用樣式
[ ] 每個後端 API 都有檢查權限，不只隱藏前端按鈕
[ ] 登入程式獨立成模組；沒有寫死的預設帳號密碼；密碼以 bcrypt／scrypt／Argon2 雜湊
[ ] 檔案上傳有類型白名單、內容檢查、大小限制、隨機檔名、存放於網站根目錄外
[ ] 刪除等不可復原操作有確認步驟
[ ] 有操作紀錄，紀錄中沒有密碼與完整個資
[ ] 匯出有權限控管，CSV 已防範公式注入
[ ] 表單有 CSRF 防護；登出後伺服器端 session 失效
[ ] 登入鎖定、閒置逾時、密碼長度已設定；民眾查詢功能有限制失敗次數
[ ] 有名額的功能：後端以交易控制名額、一次性代碼防重複送出、唯一索引擋重複報名，並已實測
[ ] 已提醒上線前建立備份並實測還原

【交付】
[ ] 附上交付說明
[ ] 標明本程式由 AI 協助產出，並寫明 AI 工具、模型名稱與版本
[ ] 提醒承辦人以近似度比對軟體比對程式碼（市府 AI 作業指引附件五）
```

## 拾貳、交付說明

交付時，用下面的格式向承辦人說明。少用技術術語；非用不可時，在括號裡補充白話解釋。

```
一、完成內容
　　〔用兩三句話說明做了什麼，例：完成「○○講座線上報名」網頁，共 3 頁：報名頁、無障礙聲明、隱私權政策。〕

二、怎麼打開來看
　　〔第一級靜態頁面，例：用滑鼠雙擊資料夾裡的 index.html，就會用瀏覽器打開。〕
　　〔第二、三級系統，寫出完整步驟，例：
　　　（一）安裝 Python 3.12（下載網址）。
　　　（二）在資料夾裡執行安裝指令：〔指令〕。
　　　（三）建立第一個管理者帳號：〔指令〕。
　　　（四）啟動：〔指令〕，再用瀏覽器打開 http://127.0.0.1:5000/。
　　　（五）關閉：在終端機按 Ctrl＋C。
　　　每個指令都要能直接複製貼上；需要資訊單位協助的步驟要寫明。〕

三、我做的假設（請確認）
　　（一）〔例：報名欄位只放姓名、手機、電子郵件。〕
　　（二）〔例：無障礙目標等級訂為 AAA，理由是頁面只有一個表單。〕

四、需要您補上或確認的地方
　　（一）Logo 取自〔來源網址〕，請確認是最新版本。
　　（二）頁尾地址、電話取自〔來源網址〕，請確認。
　　（三）個資告知的蒐集目的、保存期限，目前標示〔請填入〕。

五、和市府範本不同的地方
　　〔沒有就寫「無」。有的話說明哪裡不同、為什麼。〕

六、上線前還要做的事
　　（一）請機關資訊單位設定 HTTPS 與安全標頭。
　　（二）建議先用 Freego 做無障礙檢測。
　　（三）對外公開前請做弱點掃描。

七、提醒
　　（一）本程式由〔AI 工具名稱、模型名稱與版本〕協助產出，內容與功能請承辦人親自檢查、修改，送主管審閱後再上線使用。
　　（二）依臺北市政府使用人工智慧作業指引，對外公開前請以近似度比對軟體比對程式碼；與開源軟體相同或近似的部分須遵守其授權條款，與第三方軟體相同或近似的部分，須以人工大幅修改或重新產生。
```
