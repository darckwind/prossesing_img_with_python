from PIL import Image


img = Image.open('kaos-chan-profile .jpg')
pix = img.load()
print('largo en x',img.size[0]) #obtiene el largo en los ejes x  de la img
print('largo en y',img.size[1]) #obtiene el largo en los ejes y  de la img
print(pix[1,1]) #obtiene los balores en rgb del pixel de la imagen
img.save('alive_parrot.png')
for y in range(0, img.size[1]):
    for x in range(0, img.size[0]):
        if pix[x,y][0]>200 and pix[x,y][1] >200 and pix[x,y][2]>200:
            pix[x, y] = (256, 256, 256)
        else:
            if pix[x,y][0]<30 and pix[x,y][1]<30 and pix[x,y][2]<30:
                pix[x, y] = (0, 0, 0)
            else:
                if pix[x, y][0] > pix[x, y][1]:
                    if pix[x, y][0] > pix[x, y][2]:
                        pix[x, y] = (100, 0, 0)
                else:
                    if pix[x, y][1] > pix[x, y][2]:
                        pix[x, y] = (0, 100, 0)
                    else:
                        pix[x, y] = (0, 0, 100)

img.save('alive_parrot.png')