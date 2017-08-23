from PIL import Image

selena = Image.open("668.jpg")
#print(selena.mode) #to check the image mode
r, g, b = selena.split()

r.show()
g.show()
b.show()

