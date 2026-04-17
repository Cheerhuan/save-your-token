# Save Your Token

![Save Your Token Mascot](crab.png)

[English](#english) | [繁體中文](#繁體中文)

---

<a name="english"></a>
## English
A high-efficiency web, PDF, and Office document analysis tool for **Hermes Agent** and **OpenClaw**. 
Powered by **Microsoft MarkItDown** and adaptive extraction algorithms, it generates clean Markdown to significantly reduce LLM token consumption.

### Features
* **Smart Extraction**: Adaptive extraction strategy (Trafilatura + MarkItDown).
* **Batch Processing**: Convert entire directories of documents with one command.
* **Cross-Platform**: Compatible with both Hermes Agent and OpenClaw.

### Installation
確保您的環境已安裝 Python 3.8+，接著安裝必要的依賴套件：
```bash
pip install trafilatura markitdown
```

### Advanced Usage
| 參數 | 說明 |
| :--- | :--- |
| `--batch` | 啟用批量處理模式 |
| `--help` | 顯示所有指令說明 |

### Troubleshooting
* **檔案讀取失敗**：請檢查該網頁是否有防火牆或權限問題。
* **解析過慢**：這可能是觸發了 MarkItDown 深度模式，建議檢查來源文件格式。

---

<a name="繁體中文"></a>
## 繁體中文
這是一款專為 **Hermes Agent** 與 **OpenClaw** 設計的極致省 Token 文件分析工具。
內建 **Microsoft MarkItDown** 與「智慧型自適應解析演算法」，能自動判斷網頁複雜度，選擇最節省 Token 的清洗路徑。

### 功能特點
* **智慧萃取**: 自動偵測內容密度，在輕量與深度解析間切換。
* **批量處理**: 一鍵轉換整份文件資料夾。
* **跨平台支援**: 完美支援 Hermes Agent 與 OpenClaw。

### 快速開始
* **單檔分析**: `python eco_engine.py <檔案路徑>`
* **批量轉換**: `python eco_engine.py --batch <輸入資料夾> <輸出資料夾>`

### 更新日誌 (v1.2.0)
- **智慧自適應解析**: 加入 Trafilatura 與 MarkItDown 混合切換策略，根據內容密度自動選擇最高效的解析路徑。
- **優化效能**: 減少不必要的資源消耗，Token 節省效果進一步提升。
