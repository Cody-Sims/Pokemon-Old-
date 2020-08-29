import pygame
import os
from battle.menu import *
from battle.classes import *
pygame.font.init()

# Create window
WIDTH, HEIGHT = 1200, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Battler")

# Load Background
TOKYO_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "battle_background001.jpg")), (WIDTH, HEIGHT))



def main():
    run = True
    FPS = 60

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(TOKYO_BACKGROUND, (0, 0))

    counter = 0

    while run:
        #clock.tick(FPS)

        redraw_window()

        counter += 1
        battle = Battle(1, counter)

        # Draws player and enemy screens
        battle.draw(WIN)

        # Creates attack_menu
        party_number = 1
        attack_menu = Menu(WIN, party_number)
        attack_menu.draw()

        # updates display
        pygame.display.update()


        # Checks evente
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:

                # Gets mouse position
                mouse_pos = pygame.mouse.get_pos()

                # Checks if a move has been clicked
                if attack_menu.clicked(mouse_pos):
                    # Calculates health after each round
                    move_number = attack_menu.clicked(mouse_pos) - 1
                    battle.attack(move_number)


def main_menu():
    title_font = pygame.font.SysFont("comicsans", 60)
    run = True
    while run:
        WIN.blit(TOKYO_BACKGROUND, (0, 0))
        title_label = title_font.render("Press the mouse button to begin...", 1, (255, 255, 255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()

