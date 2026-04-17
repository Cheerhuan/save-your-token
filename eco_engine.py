import sys
from markitdown import MarkItDown

def convert_to_markdown(file_path):
    md = MarkItDown()
    result = md.convert(file_path)
    return result.text_content

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        try:
            content = convert_to_markdown(target)
            print(content[:5000]) # 限制輸出以節省 Token
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("用法: eco_engine.py <file_path>")
