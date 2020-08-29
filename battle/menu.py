import pygame
from battle.pokemon_classes import *


class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 1)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


class Menu:
    def __init__(self, window, party_number, ):
        self.buttons = []
        self.WIN = window

        self.pokemon = Pokemon(party_number, "my_pokemon.csv")
        self.moves = []

        for i in range(4):
            self.moves.append(self.pokemon.moves[i])

    def draw(self):
        screen_height = self.WIN.get_height()
        half_screen = self.WIN.get_width() / 2
        width = self.WIN.get_width() / 4
        height = screen_height / 12
        color = (255, 255, 255)

        # Sets up four buttons
        move_one = Button(color, half_screen, screen_height - height*2, width, height, str(self.moves[0]))
        self.buttons.append(move_one)
        move_two = Button(color, half_screen, screen_height - height - 1, width, height, str(self.moves[1]))
        self.buttons.append(move_two)
        move_three = Button(color, half_screen + width, screen_height - height*2, width, height,str(self.moves[2]))
        self.buttons.append(move_three)
        move_four = Button(color, half_screen + width, screen_height - height - 1, width, height,str(self.moves[3]))
        self.buttons.append(move_four)

        for button in self.buttons:
            button.draw(self.WIN)

    def clicked(self, mouse_pos):
        move_number = 0
        for button in self.buttons:
            move_number += 1
            if button.isOver(mouse_pos):
                return int(move_number)
