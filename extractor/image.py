import fitz
import PIL.Image as pil
import io

def script(pdf):
    pdf = fitz.open(str(pdf))
    counter = 1
    for i in range(2):
        page = pdf[i]
        images  = page.get_images()
        for image in images:
            imgdict = pdf.extract_image(image[0])
            data = imgdict["image"]
            img = pil.open(io.BytesIO(data))
            extension = imgdict["ext"]
            img.save(open(f"image{counter}.{extension}", "wb"))
            counter += 1