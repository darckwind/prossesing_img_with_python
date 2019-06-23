from PIL import Image

class Imgprocess:
    @staticmethod
    def greenCap():
        print('green cap process')
        img = Image.open('/Users/franciscolagos/PycharmProjects/untitled/satelital_img/satelital_org_img.jpg')
        #print(img.mode)
        img = img.convert("RGBA")

        # carga de imagen
        pix = img.load()

        print('largo en x', img.size[0])  # obtiene el largo en los ejes x  de la img
        print('largo en y', img.size[1])  # obtiene el largo en los ejes y  de la img
        print(pix[1, 1])  # obtiene los balores en rgb del pixel de la imagen
        red = 0;
        blue = 0;
        green = 0;
        banco = 0;
        negro = 0;
        pixeles = img.size[0] * img.size[1]

        for y in range(0, img.size[1]):
            for x in range(0, img.size[0]):
                if pix[x, y][0] > 200 and pix[x, y][1] > 200 and pix[x, y][2] > 200:
                    banco = banco + 1
                    pix[x, y] = (0, 0, 0, 0)
                    # pix[x, y] = (256, 256, 256)
                else:
                    if (pix[x, y][0] < 30 and pix[x, y][1] < 30 and pix[x, y][2] < 30):
                        negro = negro + 1
                        pix[x, y] = (0, 0, 0, 0)
                    else:
                        if pix[x, y][0] > pix[x, y][1] and pix[x, y][0] > pix[x, y][2]:
                            red = red + 1
                            pix[x, y] = (0, 0, 0, 0)
                            # pix[x, y] = (pix[x, y][0], 0, 0)
                        else:
                            if pix[x, y][1] > pix[x, y][2]:
                                if pix[x, y][1] > 90:
                                    pix[x, y] = (0, pix[x, y][1], 0)
                                    green = green + 1
                                else:
                                    pix[x, y] = (0, 0, 0, 0)
                            else:
                                blue = blue + 1
                                pix[x, y] = (0, 0, 0, 0)
                                # pix[x, y] = (0, 0, pix[x, y][2])

        # proceso de guardado de la reconstruccion selectiva de la imagen
        img.save('/Users/franciscolagos/PycharmProjects/untitled/satelital_img_processed/satelital_processed.png')
        # imprecion de los datos de la imagen original
        print('cantidad de banco en la img: ', banco, ' correspondiente a el: ', round((banco * 100) / pixeles, 0), '%')
        print('cantidad de negro en la img: ', negro, ' correspondiente a el: ', round((negro * 100) / pixeles, 0), '%')
        print('cantidad de red en la img: ', red, ' correspondiente a el: ', round((red * 100) / pixeles, 0), '%')
        print('cantidad de green en la img: ', green, ' correspondiente a el: ', round((green * 100) / pixeles, 0), '%')
        print('cantidad de blue en la img: ', blue, ' correspondiente a el: ', round((blue * 100) / pixeles, 0), '%')

    @staticmethod
    def heatMap():
        mayor =0
        menor = 256
        heat = Image.open('/Users/franciscolagos/PycharmProjects/untitled/satelital_img_processed/satelital_processed.png')
        print('fin carga imagen e inicio heat map')
        niceheat = heat.load()
        for alto in range(0, heat.size[0]):
            for ancho in range(0, heat.size[1]):
                if niceheat[alto,ancho][1]>=90 and niceheat[alto,ancho][1]<102:
                    niceheat[alto, ancho] = (0, 0, 256, 30)
                else:
                    if niceheat[alto,ancho][1]>=102 and niceheat[alto,ancho][1]<113:
                        niceheat[alto, ancho] = (0, 256, 0, 30)
                    else:
                        if niceheat[alto,ancho][1]>=112 and niceheat[alto,ancho][1]<124:
                            niceheat[alto, ancho] = (256, 256, 0, 30)
                        else:
                            if niceheat[alto, ancho][1] > 123:
                                niceheat[alto, ancho] = (256, 0, 0, 30)
        heat.save('/Users/franciscolagos/PycharmProjects/untitled/heat_map/heatmap.png')

        #print(mayor,menor,((mayor+menor)/2))

    @staticmethod
    def juntar():
          back = Image.open('/Users/franciscolagos/PycharmProjects/untitled/satelital_img/satelital_org_img.jpg')
          back = back.convert("RGBA")
          front = Image.open('/Users/franciscolagos/PycharmProjects/untitled/heat_map/heatmap.png')
          new_img = Image.blend(back, front, 0.5)
          new_img.save("new.png", "PNG")
