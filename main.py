# ---------------------------------------------------------------------------------------------------#

from twitterAPI import api_init
from PIL import Image, ImageFont, ImageDraw
import random
from datetime import date

api = api_init()

today = date.today()
data = today.strftime("%d/%m/%Y")


# ---------------------------------------------------------------------------------------------------#

class Player:
    def __init__(self, nome, pronome, alianza, kills):
        self.nome = nome
        self.pronome = pronome
        self.alianza = alianza
        self.kills = kills


# ---------------------------------------------------------------------------------------------------#

f = open('nomes.txt', 'r')
file = f.readlines()
players = []
i = 0
while i < len(file):
    player_str = file[i].split('/')
    players.append(Player(player_str[0], player_str[1], player_str[2], player_str[3]))
    i += 1

# ---------------------------------------------------------------------------------------------------#

# Crea a imaxe da tumba co nome da víctima
def crear_tumba(nome, text_size, subtexto, sub_size):
    tumba = Image.open("tumba.png").convert("RGBA")
    texto_img = Image.new('RGBA', tumba.size, (255, 255, 255, 0))

    nome_edicion = ImageDraw.Draw(texto_img)
    fonte = ImageFont.truetype('Futura Bold font.ttf', text_size)
    ancho_texto = nome_edicion.textsize(nome, font=fonte)[0]
    nome_edicion.text((tumba.size[0] / 2 - ancho_texto / 2, 80), nome, fill=(50, 50, 50, 110), font=fonte)

    data_edicion = ImageDraw.Draw(texto_img)
    fonte = ImageFont.truetype('Futura Bold font.ttf', sub_size)
    ancho_texto = data_edicion.textsize(subtexto, font=fonte)[0]
    data_edicion.text((tumba.size[0] / 2 - ancho_texto / 2, 185), subtexto, fill=(50, 50, 50, 110), font=fonte)
    edicion_final = Image.alpha_composite(tumba, texto_img)
    edicion_final.save("resultado.png")

# ---------------------------------------------------------------------------------------------------#

asesino = players[random.randint(0, len(players) - 1)]
victima = players[random.randint(0, len(players) - 1)]

subtexto = f'Falecid{victima.pronome} o ' + data
crear_tumba(victima.nome, 85, subtexto, 40)

media = api.media_upload("resultado.png")
tweet = f'{data}: {asesino.nome} decapitou a {victima.nome} pero iso é trivial'

api.update_status(status=tweet, media_ids=[media.media_id])
print('Tweet publicado')
