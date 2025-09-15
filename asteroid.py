import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = ""
        if self.radius >= ASTEROID_MIN_RADIUS:
            color = "red"
        else:
            color = "white"
        pygame.draw.circle(screen, color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("too small")
            return
        rand_angle = random.uniform(20, 50)
        left_split_direction = self.velocity.rotate(-rand_angle)
        right_split_direction = self.velocity.rotate(rand_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        a1, a2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius), Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        a1.velocity = left_split_direction * 1.2
        a2.velocity = right_split_direction * 1.2
