# Additional Compression if merged file is too big.

import pymupdf

def target_compression(input_path, output_path):
    doc = pymupdf.open(input_path)
    
    # "Nuclear Option" size reduction:
    # 1. Finds images with resolution > 100 DPI
    # 2. Shrinks them down to 72 DPI
    # 3. Sets JPEG quality to 40 (low but readable)
    doc.rewrite_images(
        dpi_threshold=100, 
        dpi_target=72, 
        quality=40, 
        lossless=False
    )
    
    # Save with 'ez_save' which automatically applies garbage=4 and deflate=True
    doc.ez_save(output_path)
    doc.close()

target_5mb_compression("file.pdf", "compressed_document.pdf")
