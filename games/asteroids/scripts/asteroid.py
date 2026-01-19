import pygame
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Asteroid:
    def __init__(self, screen_width, screen_height):
        self.position = pygame.Vector2(random.randint(0, screen_width), random.randint(0, screen_height))
        self.velocity = pygame.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))
        self.radius = random.randint(20, 40)    # random asteroid size
        self.speed = random.randint(50, 150)    # pps -> pixels per second
        self.angle = random.uniform(0, 360)     # random direction

    def update(self, dt):
        self.position.x += math.cos(math.radians(self.angle)) * self.speed * dt
        self.position.y += math.sin(math.radians(self.angle)) * self.speed * dt

        # This works a lot better than the old way, and its only 2LoC
        # Huzzah!
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT

    def draw(self, display):
        pygame.draw.circle(display, (200, 200, 200), (int(self.position.x), int(self.position.y)), self.radius)

    def collides_with(self, obj_position):
        return self.position.distance_to(obj_position) < self.radius