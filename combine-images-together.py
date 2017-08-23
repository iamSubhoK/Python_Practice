from PIL import Image #importing pillow

selena = Image.open("668.jpg")
snowden = Image.open("snowden.jpg")

area = (100, 100, 200, 200)
selena.paste(snowden, area)

selena.show()
