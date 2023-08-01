
import fitz
import io
from PIL import Image
  

file = "file.pdf"

pdf_file = fitz.open(file)
  
for page_index in range(len(pdf_file)):

    page = pdf_file[page_index]
    image_list = page.get_images()

    if image_list:
        print(
            f"image found ! ")
    else:
        print("[!] No images found on page", page_index)
    for image_index, img in enumerate(page.get_images(), start=1):

        xref = img[0]
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]


        image = Image.open(io.BytesIO(image_bytes))
        image.save(f"out.png")