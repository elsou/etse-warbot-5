from twitterAPI import api_init
# from instabot import Bot
from storage import txt_to_players, txt_to_mods, txt_to_verbos
import random
from datetime import date
from fotos import crear_tumba

api = api_init()
hoxe = date.today().strftime("%d/%m/%Y")

# --------------------------------------------------------------------------------------------------- #

# Impórtanse os datos gardados
players = txt_to_players()
mods = txt_to_mods()
verbos = txt_to_verbos()

# --------------------------------------------------------------------------------------------------- #

asesino = players[random.randint(0, len(players) - 1)]

victima = players[random.randint(0, len(players) - 1)]

if(victima.pronome == 'o'):
    mod = mods[random.randint(0, len(mods) - 1)].masc
else:
    mod = mods[random.randint(0, len(mods) - 1)].fem
mod = mod.replace('*', '2')

verbo = verbos[random.randint(0, len(verbos) - 1)]
verbo = verbo.replace('*', victima.pronome)

# --------------------------------------------------------------------------------------------------- #

subtexto = f'Falecid{victima.pronome} o ' + hoxe
crear_tumba(victima.nome, 85, subtexto, f'Kills: {victima.kills}', '#1 Posto', 40)

media = api.media_upload("resultado.png")
tweet = f'{hoxe}: {asesino.nome} {verbo} a {victima.nome}{mod}'

#api.update_status(status=tweet, media_ids=[media.media_id])
print(tweet)
print('Tweet publicado')

# bot = Bot()
# bot.login(username = "@etse_warbot", password = "barjaajbar")
# bot.upload_photo('resultado.png')


