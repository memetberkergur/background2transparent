from PIL import Image
from tkinter import filedialog
import sys

def openFile():
	return filedialog.askopenfilename()

def saveAsPath():
	return filedialog.asksaveasfilename(filetypes=[("png dosyasi","*.png")],defaultextension="*.png")
try:
	img = Image.open(openFile())
except (AttributeError):
	sys.exit(0)
	
rgba = img.convert("RGBA")
datas = rgba.getdata()

newData = list()
for item in datas:
	if item[0] == 0 and item[1] == 0 and item[2] == 0: # finding black colour by its RGB value
		# storing a transparent value when we find a black colour
		newData.append((255, 255, 255, 0))
	else:
		newData.append(item) # other colours remain unchanged

rgba.putdata(newData)
width,height = img.width,img.height
img_crop = rgba.crop((1, 0, width-1, height))
savePath = saveAsPath()
img_crop.save(savePath,"PNG")