import docx
import sys

try:
    doc = docx.Document(r"d:\Andy\CeylonTrailsbyAndy\docs\Tour Group Feedback Summary Re.docx")
    fullText = []
    for para in doc.paragraphs:
        if para.text.strip():
            fullText.append(para.text)
    
    with open("docx_output.txt", "w", encoding="utf-8") as f:
        f.write('\n'.join(fullText))
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
