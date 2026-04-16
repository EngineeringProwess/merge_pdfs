import os 
import pypdf

def merge_pdfs(output_filename):
    merger = pypdf.PdfWriter()

    pdf_files = [f for f in os.listdir() if f.endswith(".pdf")]
    pdf_files.sort()

    for pdf in pdf_files:
        print(f"Adding: {pdf}")
        merger.append(pdf)

    merger.write(output_filename)
    merger.close()
    print(f"Successfully merged into {output_filename}")

if __name__ == "__main__":
    merge_pdfs("merged_output.pdf")
