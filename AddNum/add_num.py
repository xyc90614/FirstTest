from PIL import Image, ImageDraw, ImageFont

def add_num(num):
	Im = Image.open("lena.bmp")
	x ,y = Im.size
	myfont = ImageFont.truetype('Futura.ttf' ,int(x /3))
	ImageDraw.Draw(Im).text((2*x/3 , 0), str(num) , font = myfont , fill = 'red')
	Im.save('lena_with_num.jpg')

if __name__== '__main__':
	add_num(9)

