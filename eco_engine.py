import sys
import os
from markitdown import MarkItDown
from pathlib import Path

def process_single(file_path):
    md = MarkItDown()
    result = md.convert(str(file_path))
    return result.text_content

def batch_convert(input_dir, output_dir):
    md = MarkItDown()
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    for file in Path(input_dir).glob("*"):
        if file.is_file():
            try:
                result = md.convert(str(file))
                out_file = output_path / f"{file.stem}.md"
                out_file.write_text(result.text_content, encoding='utf-8')
                print(f"Processed: {file.name}")
            except Exception as e:
                print(f"Failed: {file.name} - {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # 單檔模式
        print(process_single(sys.argv[1])[:5000])
    elif len(sys.argv) == 4 and sys.argv[1] == "--batch":
        # 批量模式: --batch <input_dir> <output_dir>
        batch_convert(sys.argv[2], sys.argv[3])
    else:
        print("用法: eco_engine.py <file> | --batch <input_dir> <output_dir>")
