from PIL import Image,ImageFilter

def showImage():
	Im = Image.open('lena.bmp')
	Im.show()

def cropImage(left , right , bottom , top):
	Im = Image.open('lena.bmp')
	box = (left , right , bottom, top)
	imageBox = Im.crop(box)
	imageBox.show()

def Blur():
	Im = Image.open('lena.bmp')
	im2 = Im.filter(ImageFilter.BLUR)
	im2.show()
if __name__ == '__main__':
	cropImage(50 , 50, 250 ,250)
	Blur()
