from PIL import Image

img = Image.open("668.jpg")
print(img.size)
print(img.format)

#shows up in the default app
img.show()
