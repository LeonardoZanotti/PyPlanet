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
WHITE = 255, 255, 255
YELLOW = 255, 255, 0


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

    def draw(self, screen):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(screen, self.color, (x, y), self.radius)


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    planets = [sun]

    while 1:
        clock.tick(60)
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for planet in planets:
            planet.draw(SCREEN)

        pygame.display.update()


main()
