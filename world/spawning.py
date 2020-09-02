from battle.classes import *
import random
import math

pokemon_encountered = False


# Spawns a pokemon
class RandomEncounter:
    def __init__(self, mypokemon, window):
        self.pokemon = Pokemon(1, "spawn_rates.csv")
        self.mypokemon = mypokemon
        self.window = window

        # Generates pokemon's level
        self.pokemon.level = random.randrange(self.pokemon.lowest_level, self.pokemon.highest_level)

        # Sets pokemon stats
        self.pokemon.health = math.floor((2 * self.pokemon.health + random.randrange(0, 15)) *
                                         self.pokemon.level / 100 + self.pokemon.level + 10)
        self.pokemon.attack = math.floor(math.floor((2 * self.pokemon.attack + random.randrange(0, 15))
                                                    * self.pokemon.level / 100 + 5))
        self.pokemon.special_attack = math.floor(math.floor((2 * self.pokemon.special_attack +
                                                             random.randrange(0, 15)) * self.pokemon.level / 100 + 5))
        self.pokemon.defense = math.floor(math.floor((2 * self.pokemon.defense + random.randrange(0, 15))
                                                     * self.pokemon.level / 100 + 5))
        self.pokemon.special_defense = math.floor(math.floor((2 * self.pokemon.special_defense +
                                                              random.randrange(0, 15)) * self.pokemon.level / 100 + 5))

        self.pokemon.speed = math.floor(math.floor((2 * self.pokemon.speed + random.randrange(0, 15))
                                                   * self.pokemon.level / 100 + 5))
        self.new_battle = Battle(self.mypokemon, self.pokemon)

    def draw(self):
        self.new_battle.draw(self.window)

    def attack(self, move_number):
        self.new_battle.attack(move_number)

        

