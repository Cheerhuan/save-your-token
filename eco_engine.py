import sys
import os
from markitdown import MarkItDown
import trafilatura

def get_content_density(text):
    # 簡單的資訊密度估算：文字長度 / (文字長度 + 標點符號密度)
    # 這能幫我們判斷解析出來的是不是一堆垃圾 HTML 或 CSS 雜訊
    if not text: return 0
    return len(text.strip()) / len(text)

def smart_extract(target):
    # 嘗試先用 trafilatura (快、省)
    content = ""
    try:
        if os.path.exists(target):
            with open(target, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = trafilatura.fetch_url(target)
            content = trafilatura.extract(content)
        
        # 若密度太低，表示 trafilatura 解析失敗或雜訊過多，切換到 MarkItDown (深層解析)
        if get_content_density(content) < 0.2:
            print("Content density low, switching to MarkItDown...", file=sys.stderr)
            md = MarkItDown()
            content = md.convert(target).text_content
            
    except Exception as e:
        # 最終防線：使用 MarkItDown
        md = MarkItDown()
        content = md.convert(target).text_content
        
    return content

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        print(smart_extract(target)[:5000])
    else:
        print("用法: eco_engine.py <target>")
