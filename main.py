import os
import sys
from pdf_utils import extract_pdf_pages

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <folder_path>")
        return

    folder_path = sys.argv[1]

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    pdf_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))

    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        extract_pdf_pages(pdf_path)

if __name__ == "__main__":
    main()
