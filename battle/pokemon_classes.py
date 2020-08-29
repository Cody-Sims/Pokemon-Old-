from battle.functions import *


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

        for move in range(4):
            self.moves.append(self.data[self.pokedex_number][move + 10])

        self.pokedex = int(self.data[self.pokedex_number][0])
        self.name = self.data[self.pokedex_number][1]
        self.type_one = self.data[self.pokedex_number][2]
        self.type_two = self.data[self.pokedex_number][3]
        self.level = int(self.data[self.pokedex_number][4])
        self.health = int(self.data[self.pokedex_number][5])
        self.attack = int(self.data[self.pokedex_number][6])
        self.special_attack = int(self.data[self.pokedex_number][7])
        self.defense = int(self.data[self.pokedex_number][8])
        self.special_defense = int(self.data[self.pokedex_number][9])
