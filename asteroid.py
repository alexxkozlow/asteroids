import pygame
from constants import *
import random

from circleshape import CircleShape


class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        velocity = self.velocity.rotate(angle)
        for _ in range(2):
            asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid.velocity = velocity * 1.2
            velocity = velocity.rotate(-1 * angle)
