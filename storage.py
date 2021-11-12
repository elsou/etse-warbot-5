class Player:
    def __init__(self, nome, pronome, grupo, alianza, kills, forza):
        self.nome = nome
        self.pronome = pronome
        self.grupo = grupo
        self.alianza = alianza
        self.kills = kills
        self.forza = forza

class Mod:
    def __init__(self, masc, fem):
        self.masc = masc
        self.fem = fem


def txt_to_players():
    f = open('nomes.txt', 'r')
    file = f.readlines()
    players = []
    i = 0
    while i < len(file):
        player_str = file[i].split('/')
        players.append(Player(player_str[0], player_str[1],
                              player_str[2], player_str[3],
                              player_str[4], player_str[5]))
        i += 1
    return players

def txt_to_mods():
    f = open('mods.txt', 'r')
    file = f.readlines()
    mods = []
    i = 0
    while i < len(file):
        mod_str = file[i].split('/')
        mods.append(Mod(mod_str[0], mod_str[1]))
        i += 1
    return mods

def txt_to_verbos():
    f = open('verbos.txt', 'r')
    file = f.readlines()
    verbos = []
    i = 0
    while i < len(file):
        verbos.append(file[i].split('/')[0])
        i += 1
    return verbos
