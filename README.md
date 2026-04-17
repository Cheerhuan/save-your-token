# Save Your Token

![Save Your Token Mascot](crab.png)

[English](#english) | [繁體中文](#繁體中文)

---

<a name="english"></a>
## English
A high-efficiency web and PDF content analysis tool for Hermes Agent. 
It cleans up noise (ads, navbars) and extracts essential content to reduce LLM token costs.

### Features
* **Smart Extraction**: Uses `trafilatura` for clean text.
* **Token Optimization**: Minimizes LLM cost.
* **Cross-Platform**: Supports both Hermes Agent and OpenClaw.

### Installation
1. Clone to `~/.hermes/skills/` or OpenClaw workspace.
2. Install dependencies: `pip install pymupdf trafilatura google-genai requests`

---

<a name="繁體中文"></a>
## 繁體中文
這是一款為 Hermes Agent 與 OpenClaw 設計的極致省 Token 網頁與 PDF 分析工具。
它能自動過濾網頁雜訊，只提取最有價值的核心內容，節省 API 費用。

### 功能特點
* **極致清洗**：移除無效雜訊。
* **Token 優化**：專為 LLM 傳輸優化。
* **跨平台支援**：同時支援 Hermes Agent 與 OpenClaw。

### 安裝方式
1. 將此倉庫 clone 到您的 `~/.hermes/skills/` 目錄。
2. 安裝依賴：`pip install pymupdf trafilatura google-genai requests`
