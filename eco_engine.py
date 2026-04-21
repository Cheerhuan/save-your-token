import sys
import os
import subprocess
from markitdown import MarkItDown
import trafilatura

def get_content_density(text):
    if not text: return 0
    return len(text.strip()) / len(text)

def firecrawl_scrape(url):
    # 使用 Firecrawl 作為專業備案
    try:
        # 從 .env 或環境變數獲取 Key (這裡假設已載入或手動處理)
        # 為了穩定性，我們直接調用 npx firecrawl
        cmd = [
            "npx", "firecrawl", "scrape", url,
            "--wait-for", "5000",
            "--only-main-content"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
    except Exception as e:
        print(f"Firecrawl failed: {e}", file=sys.stderr)
    return None

def smart_extract(target):
    # 1. 嘗試 trafilatura
    content = ""
    try:
        if os.path.exists(target):
            with open(target, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            # 判斷是否為高防護網站或需要 JS 渲染
            # 如果是政府網站或特定的 SPA，優先考慮 Firecrawl
            if "ndc.gov.tw" in target or "firecrawl" in os.environ.get("PREFER_CRAWLER", ""):
                print("Using Firecrawl for high-security/SPA site...", file=sys.stderr)
                content = firecrawl_scrape(target)
                if content: return content

            content = trafilatura.fetch_url(target)
            content = trafilatura.extract(content)
        
        if get_content_density(content) < 0.2:
            # 2. 切換到 MarkItDown
            print("Content density low, switching to MarkItDown...", file=sys.stderr)
            md = MarkItDown()
            content = md.convert(target).text_content
            
    except Exception as e:
        # 3. 最終防線：Firecrawl (如果之前沒用過)
        if not content and not os.path.exists(target):
            print("Fallback to Firecrawl...", file=sys.stderr)
            content = firecrawl_scrape(target)
        
        if not content:
            md = MarkItDown()
            content = md.convert(target).text_content
        
    return content

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        print(smart_extract(target)[:5000])
    else:
        print("用法: eco_engine.py <target>")
