import pygame
from game import Game
from AI import AI


SIZE_X = 1000
SIZE_Y = 600


def main():
    pygame.font.init()
    pygame.init()
    pygame.display.set_caption('Simulation')

    screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
    clock = pygame.time.Clock()

    game = Game(SIZE_X, SIZE_Y)
    quit_game = False

    while not quit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True

        foreground = pygame.Surface((SIZE_X, SIZE_Y), pygame.SCRALPHA)
        foreground.fill(pygame.Color('black'))


if __name__ == '__main__':
    main()
