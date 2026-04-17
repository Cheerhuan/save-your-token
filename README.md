![Save Your Token Mascot](https://raw.githubusercontent.com/Cheerhuan/save-your-token/main/crab.png)

![Save Your Token Mascot](crab.png)

[English](#english) | [繁體中文](#繁體中文)

# Save Your Token

[English](#english) | [繁體中文](#繁體中文)

<a name="english"></a>
## English
A high-efficiency web and PDF content analysis tool designed for Hermes Agent. It automatically cleans up noise (ads, navbars, etc.) from websites and extracts essential content to significantly reduce LLM token costs.

### Features
- **Smart Extraction**: Cleans noise from websites using `trafilatura`.
- **Token Optimization**: Extracts core content to save on LLM inference costs.
- **Cross-Platform**: Compatible with both Hermes Agent and OpenClaw.

### Installation
1. Clone this repository to your `~/.hermes/skills/` or OpenClaw workspace.
2. Install dependencies: `pip install pymupdf trafilatura google-genai requests`

---

<a name="繁體中文"></a>
## 繁體中文
這是一款為 Hermes Agent 與 OpenClaw 設計的極致省 Token 網頁與 PDF 分析工具。它能自動過濾網頁雜訊（如廣告、導航欄），只提取最有價值的核心內容，幫您省下昂貴的 Token 成本。

### 功能特點
- **極致清洗**：移除無效雜訊，只留下純淨文字。
- **Token 優化**：專為 LLM 傳輸優化，節省您的 API 費用。
- **跨平台支援**：完美支援 Hermes Agent 與 OpenClaw。

### 安裝方式
1. 將此倉庫 clone 到您的 `~/.hermes/skills/` 目錄。
2. 安裝依賴：`pip install pymupdf trafilatura google-genai requests`
