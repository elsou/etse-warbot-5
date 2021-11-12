from PIL import Image, ImageFont, ImageDraw

# Crea a imaxe da tumba co nome da víctima
def crear_tumba(nome, big_size, subtexto, kills, posto, small_size):
    tumba = Image.open("tumba.png").convert("RGBA")
    logo = Image.open("warbot_logo3.png")
    texto_img = Image.new('RGBA', tumba.size, (255, 255, 255, 0))

    edicion = ImageDraw.Draw(texto_img)

    fonte = ImageFont.truetype('Futura Bold font.ttf', big_size)
    add_text(fonte, nome, (tumba.size[0] // 2 - ancho(nome, edicion, fonte) // 2, 250), edicion)

    fonte = ImageFont.truetype('Futura Bold font.ttf', small_size)
    add_text(fonte, kills, (tumba.size[0] / 2 - ancho(kills, edicion, fonte) + 160, 420), edicion)
    add_text(fonte, subtexto, (tumba.size[0] / 2 - ancho(subtexto, edicion, fonte) / 2, 355), edicion)
    add_text(fonte, posto, (tumba.size[0] / 2 - 175, 420), edicion)

    edicion_final = Image.alpha_composite(tumba, texto_img)
    edicion_final = Image.alpha_composite(edicion_final, logo)

    edicion_final.save("resultado.png")
    #edicion_final.show()


def add_text(font, text, pos, img):
    fonte = font
    ancho_texto = img.textsize(text, font=fonte)[0]
    ancho_texto = img.textsize(text, font=fonte)[0]
    img.text(pos, text, fill=(50, 50, 50, 110), font=fonte)


def ancho(text, img, font):
    fonte = font
    w = img.textsize(text, font=fonte)[0]
    return w
