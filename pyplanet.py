#!/usr/bin/env python3
# Leonardo José Zanotti
# https://github.com/LeonardoZanotti/PyPlanet

import math
import sys
import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode(SIZE)
BLACK = 0, 0, 0


def main():
    run = True

    pygame.display.set_caption("Planet simulation")

    while run:
        SCREEN.fill(BLACK)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()


main()

