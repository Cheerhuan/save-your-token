<div align="center">

# Save Your Token 🦀

![Save Your Token Mascot](crab.png)

**A high-efficiency web, PDF, and Office document analysis tool for Hermes Agent and OpenClaw.**
**專為 Hermes Agent 與 OpenClaw 設計的極致省 Token 文件分析工具。**

**Powered by Microsoft MarkItDown and adaptive extraction algorithms to significantly reduce LLM token consumption.**
**內建 Microsoft MarkItDown 與智慧型自適應解析演算法，自動選擇最節省 Token 的清洗路徑。**

</div>

---

## 📌 Table of Contents | 目錄
- [🌟 Features | 功能特點](#-features-功能特點)
- [🛠 Installation | 安裝指南](#-installation-安裝指南)
- [🚀 Quick Start | 快速開始](#-quick-start-快速開始)
- [⚙️ Advanced Usage | 進階使用](#-advanced-usage-進階使用)
- [🔍 Troubleshooting | 故障排除](#-troubleshooting-故障排除)
- [📜 Changelog | 更新日誌](#-changelog-更新日誌)

---

## 🌟 Features | 功能特點

| Feature | 說明 | Description |
| :--- | :--- | :--- |
| **Smart Extraction** | **智慧萃取** | Adaptive extraction strategy (Trafilatura + MarkItDown) to detect content density. <br> 自動偵測內容密度，在輕量與深度解析間自動切換。 |
| **Batch Processing** | **批量處理** | Convert entire directories of documents with one command. <br> 一鍵轉換整份文件資料夾。 |
| **Cross-Platform** | **跨平台支援** | Fully compatible with both Hermes Agent and OpenClaw. <br> 完美支援 Hermes Agent 與 OpenClaw。 |

---

## 🛠 Installation | 安裝指南

Ensure your environment has Python 3.8+ installed, then install the required dependencies:
確保您的環境已安裝 Python 3.8+，接著安裝必要的依賴套件：

```bash
pip install trafilatura markitdown
```

---

## 🚀 Quick Start | 快速開始

### 1️⃣ Single File Analysis | 單檔分析
```bash
python eco_engine.py <FILE_PATH>
```

### 2️⃣ Batch Conversion | 批量轉換
```bash
python eco_engine.py --batch <INPUT_FOLDER> <OUTPUT_FOLDER>
```

---

## ⚙️ Advanced Usage | 進階使用

| Argument | 說明 | Description |
| :--- | :--- | :--- |
| `--batch` | **啟用批量處理模式** | Enable batch processing mode for directories. |
| `--help` | **顯示指令說明** | Show all available command line options. |

---

## 🔍 Troubleshooting | 故障排除

- **File Read Failure | 檔案讀取失敗**：
  Please check if the page has a firewall or permission issues.
  請檢查該網頁是否有防火牆或權限問題。
- **Slow Parsing | 解析過慢**：
  This may be triggered by MarkItDown's deep mode; please check the source file format.
  這可能是觸發了 MarkItDown 深度模式，建議檢查來源文件格式。

---

## 📜 Changelog | 更新日誌

### v1.2.0
- **Adaptive Parsing | 智慧自適應解析**: Integrated Trafilatura & MarkItDown hybrid strategy to choose the most efficient path based on content density.
  加入 Trafilatura 與 MarkItDown 混合切換策略，根據內容密度自動選擇最高效的解析路徑。
- **Performance Optimization | 優化效能**: Reduced unnecessary resource consumption, further improving token savings.
  減少不必要的資源消耗，Token 節省效果進一步提升。
