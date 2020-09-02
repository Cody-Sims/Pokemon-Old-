from battle.functions import *
from battle.sprites import *
import math


class Move:
    def __init__(self, name):
        self.name = name
        self.file_name = "moves.csv"
        self.move = search_string_in_file(self.file_name, self.name)
        self.move_name = self.move[0][0]
        self.type = self.move[0][1]
        self.category = self.move[0][2]
        self.power = int(self.move[0][3])
        self.accuracy = int(self.move[0][4])
        self.description = self.move[0][7]


class Pokemon:
    def __init__(self, pokedex_number, file_name):
        self.pokedex_number = pokedex_number
        self.data = create_data(file_name)
        self.moves = []

        for move_number in range(4):
            if self.data[self.pokedex_number][move_number + 11] != "None":
                self.moves.append(self.data[self.pokedex_number][move_number + 11])

        self.pokedex = int(self.data[self.pokedex_number][0])
        self.name = self.data[self.pokedex_number][1]
        self.type_one = self.data[self.pokedex_number][2]
        self.type_two = self.data[self.pokedex_number][3]
        self.level = self.data[self.pokedex_number][4]
        self.health = int(self.data[self.pokedex_number][5])
        self.attack = int(self.data[self.pokedex_number][6])
        self.special_attack = int(self.data[self.pokedex_number][7])
        self.defense = int(self.data[self.pokedex_number][8])
        self.special_defense = int(self.data[self.pokedex_number][9])
        self.speed = int(self.data[self.pokedex_number][10])

        if self.level == "None":
            self.lowest_level = int(self.data[self.pokedex_number][15])
            self.highest_level = int(self.data[self.pokedex_number][16])
        else:
            self.level = int(self.level)

    def image(self, image_type):
        if image_type == 'front':
            pokemon = SpriteSheet('sprite_sheet_front.png')
        elif image_type == 'back':
            pokemon = SpriteSheet("sprite_sheet_back.png")

        poke_x = int(self.pokedex - 1) % 31 * 96
        poke_row = math.floor((self.pokedex - 1) / 33)
        poke_y = int(poke_row * 95)
        pokemon_rect = (poke_x, poke_y + 10, 100, 95)

        return pokemon.image_at(pokemon_rect, colorkey=(143, 165, 151))


class PartyPokemon:
    def __init__(self):
        self.one = Pokemon(1, "my_pokemon.csv")
