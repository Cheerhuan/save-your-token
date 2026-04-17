# Save Your Token

一個為 Hermes Agent 設計的極致省 Token 網頁內容分析工具。它能自動清洗網頁雜訊，只提取核心內容，幫您省下昂貴的 Token 成本。

## 功能特點
- **極致清洗**：移除廣告、導航欄、Footer 等雜訊。
- **Token 優化**：專為 LLM 傳輸優化，確保只發送核心資訊。
- **簡單安裝**：Hermes 技能化設計。

## 安裝方式
1. 將此倉庫 clone 到您的 `~/.hermes/skills/` 目錄下。
2. 安裝依賴：`pip install trafilatura google-genai`
3. 在您的 Hermes 設定中啟用它。

## 使用方式
直接對您的 Hermes Agent 說：
> 「分析這個頁面: https://example.com」
