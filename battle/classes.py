import math
import random
from battle.sprites import *
from battle.menu import *



class Battle:
    def __init__(self, party_number, pokedex_two):

        # Player's pokemon
        self.pokemon_one = Pokemon(party_number, "my_pokemon.csv")

        # Enemy's Pokemon
        self.pokemon_two = Pokemon(pokedex_two, "pokemon_base_stats.csv")

        self.images = (self.pokemon_two.image("front"), self.pokemon_one.image("back"))

    # Draws sprites for battle
    def draw(self, window):
        # font settings
        font_size = round(window.get_height() / 25)
        text_color = (255, 255, 255)
        font = pygame.font.SysFont('comicsans', font_size)

        # rect settings
        rect_color = (0, 0, 0)
        rect_width = window.get_width() / 5
        rect_height = window.get_height() / 9

        h = window.get_height() / 6

        pygame.draw.rect(window, (123,123,123), ((0, window.get_height() - h), (window.get_width(), h)))

        pygame.draw.rect(window, rect_color, ((0, 0),(rect_width, rect_height)))

        pygame.draw.rect(window, rect_color, ((window.get_width() - rect_width,
                                               window.get_height() - h - rect_height), (rect_width, rect_height)))

        # draw pokemon_two box
        space = 10
        text_one = font.render(self.pokemon_two.name, 1, text_color)
        text_two = font.render(f"Health: {self.pokemon_two.health}", 1, text_color)
        window.blit(text_one, (0 + space, 0 + space))
        window.blit(text_two, (0 + space, text_one.get_height() + space))

        # draw player box
        text_one = font.render(self.pokemon_one.name, 1, text_color)
        text_two = font.render(f"Health: {self.pokemon_one.health}", 1, text_color)
        window.blit(text_one,
                    (window.get_width() - rect_width + space, window.get_height() - rect_height - h + space))
        window.blit(text_two, (window.get_width() - rect_width + space,
                               window.get_height() + text_one.get_height() - rect_height - h + space))

        # draw sprites
        width = 250
        height = 250

        rect = (window.get_width() - width - 10, 50)
        window.blit(pygame.transform.scale(self.images[0], (width, height)), rect)

        rect_two = (50, window.get_height() - h - height)
        window.blit(pygame.transform.scale(self.images[1], (width, height)), rect_two)

    # Calculates health after each turn
    def attack(self, move_number):
        move_name = self.pokemon_one.moves[move_number]
        move = Move(move_name)

        player = self.pokemon_one
        enemy = self.pokemon_two
        print(move)

        print(f"move: {move_name}, Power: {move.power}")

        def stab_damage(pokemon):
            if pokemon.type_one == move.type or pokemon.type_two == move.type:
                return 1.5
            return 1

        def critical_damage():
            if random.randrange(0,100) < 7:
                return 2
            return 1

        def calculate_damage(poke_one, poke_two):
            calculation_one = (2 * poke_one.level + 10) / 250
            calculation_two = poke_one.attack / poke_two.defense
            base = (calculation_one * calculation_two) + 2
            damage = round(base * stab_damage(poke_one) * critical_damage() * (random.randrange(85,100) / 100))
            return damage

        enemy.health -= calculate_damage(player, enemy)
        player.health -= calculate_damage(enemy, player)

        if enemy.health <= 0:
            enemy.health = 0
        if player.health <= 0:
            player.health = 0