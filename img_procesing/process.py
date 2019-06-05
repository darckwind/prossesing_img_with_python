from PIL import Image


img = Image.open('/Users/franciscolagos/PycharmProjects/untitled/satelital_img/caca.jpeg')
pix = img.load()
print('largo en x',img.size[0]) #obtiene el largo en los ejes x  de la img
print('largo en y',img.size[1]) #obtiene el largo en los ejes y  de la img
print(pix[1,1]) #obtiene los balores en rgb del pixel de la imagen
red=0;
blue=0;
green=0;
banco=0;
negro=0;
pixeles =img.size[0]*img.size[1]

for y in range(0, img.size[1]):
    for x in range(0, img.size[0]):
        if pix[x,y][0]>200 and pix[x,y][1] >200 and pix[x,y][2]>200:
            banco=banco+1
            pix[x, y] = (256, 256, 256)
        else:
            if (pix[x,y][0]<30 and pix[x,y][1]<30 and pix[x,y][2]<30):
                negro =negro+1
                pix[x, y] = (0, 0, 0)
            else:
                if  pix[x, y][0] > pix[x, y][1] and pix[x, y][0] > pix[x, y][2]:
                    red=red+1
                    pix[x, y] = (0, 0, 0)
                else:
                    if pix[x, y][1] > pix[x, y][2]:
                        green=green+1
                        pix[x, y] = (0, pix[x, y][1], 0)
                    else:
                        blue=blue+1
                        pix[x, y] = (0, 0, pix[x, y][2])

img.save('/Users/franciscolagos/PycharmProjects/untitled/satelital_img_processed/satelital_processed.png')
print('cantidad de banco en la img: ',banco,' correspondiente a el: ',round((banco*100)/pixeles,0),'%')
print('cantidad de negro en la img: ',negro,' correspondiente a el: ',round((negro*100)/pixeles,0),'%')
print('cantidad de red en la img: ',red,' correspondiente a el: ',round((red*100)/pixeles,0),'%')
print('cantidad de green en la img: ',green,' correspondiente a el: ',round((green*100)/pixeles,0),'%')
print('cantidad de blue en la img: ',blue,' correspondiente a el: ',round((blue*100)/pixeles,0),'%')