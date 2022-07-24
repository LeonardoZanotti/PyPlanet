#!/usr/bin/env python3
# Leonardo José Zanotti
# https://github.com/LeonardoZanotti/PyPlanet

import math
import sys

import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Planet simulation")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 71, 81)
WHITE_YELLOW = (233, 233, 200)

FONT = pygame.font.SysFont("comicsans", 16)


class Star:
    AU = 149.6e9  # Astronomical Unities
    G = 6.67428e-11
    SCALE = 250 / AU  # 1 AU = 100 pixels
    TIMESTEP = 3600  # 1 hour

    def update_position(self, planets):
        total_fx = total_fy = 0

        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))


class Planet(Star):
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.sun = False
        self.distance_to_sun = 0
        self.orbit = []

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, screen):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                px, py = point
                px = px * self.SCALE + WIDTH / 2
                py = py * self.SCALE + HEIGHT / 2
                updated_points.append((px, py))
            pygame.draw.lines(screen, self.color, False, updated_points, 2)

        pygame.draw.circle(screen, self.color, (x, y), self.radius)

        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun / 1000, 1)} km", 1, WHITE)
            screen.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))

    def attraction(self, other):
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y


class Moon(Star):
    def __init__(self, planet, x, y, radius, color, mass):
        self.planet = planet
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.distance_to_planet = 0
        self.orbit = []

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, screen):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                px, py = point
                px = px * self.SCALE + WIDTH / 2
                py = py * self.SCALE + HEIGHT / 2
                updated_points.append((px, py))
            pygame.draw.lines(screen, self.color, False, updated_points, 2)

        pygame.draw.circle(screen, self.color, (x, y), self.radius)

        distance_text = FONT.render(f"{round(self.distance_to_planet / 1000, 1)} km", 1, WHITE)
        screen.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))

    def attraction(self, other):
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other == self.planet:
            self.distance_to_planet = distance

        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y


def main():
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10 ** 30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9741 * 10 ** 24)
    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10 ** 23)
    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.3 * 10 ** 23)
    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10 ** 24)

    earth.y_vel = 29.783 * 1000
    mars.y_vel = 24.077 * 1000
    mercury.y_vel = -47.4 * 1000
    venus.y_vel = 35.02 * 1000

    earth_moon = Moon(earth, -1.00256 * Moon.AU, 0, 4.35968, WHITE_YELLOW, 7.3477 * 10 ** 22)

    earth_moon.y_vel = 30.783 * 1000  # earth velocity plus moon velocity (so the moon goes with the earth around
    # the sun and also goes around the earth)

    planets = [sun, earth, mars, mercury, venus]
    moons = [earth_moon]

    while 1:
        clock.tick(60)
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for planet in planets:
            planet.update_position(planets)
            planet.draw(SCREEN)

        for moon in moons:
            moon.update_position(planets)
            moon.draw(SCREEN)

        pygame.display.update()


if __name__ == '__main__':
    main()
