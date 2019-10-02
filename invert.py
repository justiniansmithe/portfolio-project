
from PIL import Image 
import PIL.ImageOps

image = Image.open("Emilia-Clark.jpg")
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save("Emilia-Clark-inverted.png")
