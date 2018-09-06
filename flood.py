from PIL import Image

img = Image.open("maze2.jpg")

w,h = img.size

fillcolor = (0,70,160)
bordercolor = (0,0,0)
emptycolor = (255,255,255)

boundary = []
newboundary = []

def fill(x,y):
	global boundary
	for dy in range(-1, 2):
		for dx in range(-1, 2):
			nx = x+dx
			ny = y+dy
			if nx < 0 or nx > w-1 or ny < 0 or ny > h-1:
				continue
			
			coords = (nx,ny)
			
			p = img.getpixel(coords)
			if p[:3] == emptycolor:
				img.putpixel(coords, fillcolor)
				newboundary.append(coords)

start = (0,0)
img.putpixel(start, fillcolor)
boundary.append(start)

for i in range(5300):
	print(i)
	
	fillcolor = ((fillcolor[0]+1)%256,(fillcolor[1]+1)%256,(fillcolor[2]+1)%256)

	for point in boundary:
		x,y = point
		fill(x,y)
		
	boundary = newboundary
	newboundary = []
	
	if i%20==0:
		img.save("anim/%i.jpg" % i)
