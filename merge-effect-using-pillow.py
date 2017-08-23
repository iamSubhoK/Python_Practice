from PIL import Image

selena = Image.open("668.jpg")
r, g, b = selena.split()
new_img = Image.merge('RGB', (r, g, b)) #mode and bands

new_img.show()
