import sys
import fitz  # PyMuPDF
import trafilatura
import requests
import os

def extract_content(target):
    # 如果是本地檔案
    if os.path.exists(target):
        if target.lower().endswith('.pdf'):
            doc = fitz.open(target)
            text = "\n".join([page.get_text() for page in doc])
            return text
        else:
            with open(target, 'r') as f:
                return f.read()
    # 如果是 URL
    elif target.lower().endswith('.pdf'):
        response = requests.get(target)
        temp_pdf = "temp.pdf"
        with open(temp_pdf, 'wb') as f:
            f.write(response.content)
        doc = fitz.open(temp_pdf)
        text = "\n".join([page.get_text() for page in doc])
        os.remove(temp_pdf)
        return text
    else:
        downloaded = requests.get(target).text
        return trafilatura.extract(downloaded)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        content = extract_content(sys.argv[1])
        print(content[:5000])
