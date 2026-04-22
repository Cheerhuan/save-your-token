#!/bin/bash
# save-your-token Skill Installer

set -e # 遇到錯誤立即退出

# 顏色輸出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Save Your Token 技能安裝程序${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# 確定技能的來源目錄 (當前目錄)
SKILL_SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="save-your-token"

# 確定目標安裝目錄
INSTALL_DIR=""
if [ -d "$HOME/.hermes" ]; then
    echo -e "${GREEN}偵測到 Hermes Agent 環境。${NC}"
    INSTALL_DIR="$HOME/.hermes/skills/$SKILL_NAME"
elif [ -d "$HOME/.openclaw" ]; then
    echo -e "${GREEN}偵測到 OpenClaw 環境。${NC}"
    INSTALL_DIR="$HOME/.openclaw/workspace/skills/$SKILL_NAME"
else
    echo -e "${RED}❌ 找不到 Hermes 或 OpenClaw 目錄。請確保您正在支援的 Agent 環境中運行。${NC}"
    exit 1
fi

echo -e "${YELLOW}安裝目錄：${INSTALL_DIR}${NC}"

# 1. 複製技能檔案
echo -e "\n${YELLOW}[1/4] 複製技能檔案...${NC}"
mkdir -p "$INSTALL_DIR"
rsync -av --exclude 'venv/' --exclude '__pycache__/' --exclude '*.log' "$SKILL_SOURCE_DIR/" "$INSTALL_DIR/"
echo -e "${GREEN}✅ 技能檔案複製完成。${NC}"

# 2. 建立並激活 Python 虛擬環境
echo -e "\n${YELLOW}[2/4] 建立並激活 Python 虛擬環境...${NC}"
cd "$INSTALL_DIR"
python3 -m venv venv
source venv/bin/activate

# 安裝核心依賴
echo "安裝 Python 核心依賴..."
pip install --upgrade pip -q
pip install trafilatura markitdown google-genai -q

# 安裝 NotebookLM (如果不存在)
if ! command -v notebooklm &> /dev/null; then
    echo "安裝 NotebookLM CLI (notebooklm-py)..."
    pip install git+https://github.com/teng-lin/notebooklm-py.git -q
else
    echo "NotebookLM CLI 已存在。${NC}"
fi

# 安裝 Playwright (如果需要)
if python3 -c "from playwright.sync_api import sync_playwright" 2>/dev/null; then
    echo "Playwright 依賴已安裝。${NC}"
else
    echo "安裝 Playwright..."
    pip install playwright -q
    python3 -m playwright install chromium
fi

echo -e "${GREEN}✅ Python 依賴安裝完成。${NC}"

# 3. 賦予執行權限
echo -e "\n${YELLOW}[3/4] 賦予腳本執行權限...${NC}"
chmod +x main.py eco_engine.py install.sh
echo -e "${GREEN}✅ 執行權限設定完成。${NC}"

# 4. 配置指導 (針對 NotebookLM 認證)
echo -e "\n${YELLOW}[4/4] 重要：NotebookLM 認證與 API Key 指導${NC}"
echo ""
echo -e "${BLUE}⚡ 為了完全啟用 'save-your-token' 技能，您需要進行以下配置：${NC}"
echo ""
echo -e "${YELLOW}1. NotebookLM 授權 (首次使用必做)：${NC}"
echo -e "   請在您的終端機執行此技能目錄下的登入指令："
echo -e "   ${GREEN}cd ${INSTALL_DIR} && source venv/bin/activate && ./venv/bin/notebooklm login${NC}"
echo -e "   (此步驟會彈出瀏覽器視窗，請完成 Google 登入後，回到終端機按 Enter)"
echo ""
echo -e "${YELLOW}2. API Keys 配置 (如果尚未配置)：${NC}"
echo -e "   請確保以下密鑰已存在於您的 `~/.hermes/.env` (或 `~/.openclaw/.env`) 中："
echo -e "   - ${GREEN}FIRECRAWL_API_KEY${NC}"
echo -e "   - ${GREEN}GOOGLE_API_KEY${NC}"
echo -e "   - ${GREEN}GETNOTE_API_KEY${NC}"
echo -e "   - ${GREEN}GETNOTE_CLIENT_ID${NC}"
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}✅ 'save-your-token' 技能安裝程序完成！${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

deactivate # 退出虛擬環境
