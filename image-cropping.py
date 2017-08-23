from PIL import Image

img = Image.open("668.jpg")
#cropping
area = (100, 100, 300, 375)
cropped_img = img.crop(area) #instead of area u can pu the dimensns directly

#shows up in the default app
#img.show() #comment this line while u crop or it would execute twice the def app for image
cropped_img.show() #this line would open up the def app for image with the cropped output
