#!/usr/bin/env python3
# Leonardo José Zanotti
# https://github.com/LeonardoZanotti/PyPlanet

import math
import sys
from typing import Type

import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Planet simulation")
BLACK = 0, 0, 0


class Planet:
    AU = 149.6e9  # Astronomical Unities
    G = 6.67428e-11
    SCALE = 250 / AU    # 1 AU = 100 pixels
    TIMESTEP = 3600 * 24    # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color;
        self.mass = mass

        self.sun = False
        self.distance_to_sun = 0
        self.orbit = []

        self.x_vel = 0
        self.y_vel = 0


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        SCREEN.fill(BLACK)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()


main()
