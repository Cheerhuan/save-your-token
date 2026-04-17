# Save Your Token

![Save Your Token Mascot](crab.png)

[English](#english) | [繁體中文](#繁體中文)

---

<a name="english"></a>
## English
A high-efficiency web and PDF content analysis tool for **Hermes Agent** and **OpenClaw**. 
It cleans up noise and extracts essential content to reduce LLM token costs.

### Installation
* **For Hermes Agent**: 
  Clone this repository to `~/.hermes/skills/save-your-token`
* **For OpenClaw**: 
  Clone this repository to `~/.openclaw/workspace/skills/save-your-token`
* **Common Dependencies**: 
  `pip install pymupdf trafilatura google-genai requests`

---

<a name="繁體中文"></a>
## 繁體中文
這是一款專為 **Hermes Agent** 與 **OpenClaw** 設計的極致省 Token 網頁與 PDF 分析工具。
它能自動過濾網頁雜訊，只提取最有價值的核心內容，幫助您節省 API Token 費用。

### 安裝方式
* **Hermes Agent 使用者**：
  請將本專案 Clone 至 `~/.hermes/skills/save-your-token` 目錄。
* **OpenClaw 使用者**：
  請將本專案 Clone 至 `~/.openclaw/workspace/skills/save-your-token` 目錄。
* **共同依賴**：
  請確保安裝必要套件：`pip install pymupdf trafilatura google-genai requests`

### 使用說明
安裝完成後，系統將自動識別 `save-your-token` 技能。您可直接呼叫並輸入目標網址或檔案路徑。
