import pygame
import math
from sys import exit
from time import sleep

# This covers both the players functionality and also the bullets the player can fire.

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player:
    def __init__(self):
        # Init mizer and load sfx into memory
        pygame.mixer.init()

        self.hit_sound = pygame.mixer.Sound('sfx/hit.wav')
        self.explosion_sound = pygame.mixer.Sound('sfx/explosion.wav')
        self.shoot_sound = pygame.mixer.Sound('sfx/shoot.wav')

        self.hit_sound.set_volume(0.09)
        self.explosion_sound.set_volume(0.09)
        self.shoot_sound.set_volume(0.09)

        self.__health: int = 5
        self.__score: int = 0
        self.__angle: float = 0
        self.__position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.__velocity = pygame.Vector2(0, 0)
        self.__bullets = []
        self.__thrust_power = 200
        self.__friction = 0.99
        self.__font = pygame.font.Font(None, 36)  # Font for UI text

    def draw(self, display):
        points = self.__get_triangle_points()
        pygame.draw.polygon(display, (255, 255, 255), points)

        for bullet in self.__bullets:
            bullet.draw(display)

        self.draw_ui(display)

    def update(self, dt: float, keys: list, asteroids):
        # Rotation
        if keys[pygame.K_q]: 
            self.__rotate(-5.0)
        if keys[pygame.K_e]: 
            self.__rotate(5.0)

        # Thrust (pretty important for nice movement)
        # Physics is still annoying btw
        if keys[pygame.K_w]:  
            acceleration = pygame.Vector2(
                math.cos(math.radians(self.__angle)) * self.__thrust_power,
                math.sin(math.radians(self.__angle)) * self.__thrust_power
            )
            self.__velocity += acceleration * dt

        # Apply velocity and friction
        self.__position += self.__velocity * dt
        self.__velocity *= self.__friction

        # Screen wrapping
        self.__handle_screen_wrap()

        # Fire bullets
        if keys[pygame.K_SPACE]:
            self.__fire()

        # Update bullets
        for bullet in self.__bullets:
            bullet.update(dt)

        # Remove bullets that leave screen
        self.__bullets = [b for b in self.__bullets if b.is_on_screen()]

        # Check for collisions
        self.check_collisions(asteroids)

    def check_collisions(self, asteroids):
        for asteroid in asteroids[:]:   # Iterate over a copy of the list
                                        # Check if any bullet hits an asteroid
            for bullet in self.__bullets[:]:  
                if asteroid.collides_with(bullet.position):
                    asteroids.remove(asteroid)
                    self.__bullets.remove(bullet)
                    # +5 points per destroyed asteroid
                    self.__score += 5  
                    self.explosion_sound.play()
                    break

            # Check if the player collides with an asteroid
            # -1 health per collision
            if asteroid.collides_with(self.__position):
                self.__health -= 1  
                asteroids.remove(asteroid)
                self.hit_sound.play()
                if self.__health <= 0:
                    print("Game Over!")
                    exit(0)

    def draw_ui(self, display):
        # Renders the Health/Score UI
        # (why is this in player?)
        health_text = self.__font.render(f"Health: {self.__health}", True, (255, 000, 000))
        score_text = self.__font.render(f"Score: {self.__score}", True, (255, 255, 255))
        display.blit(health_text, (10, 10))
        display.blit(score_text, (10, 40))

    def __handle_screen_wrap(self):
        if self.__position.x < 0:
            self.__position.x = SCREEN_WIDTH
        elif self.__position.x > SCREEN_WIDTH:
            self.__position.x = 0

        if self.__position.y < 0:
            self.__position.y = SCREEN_HEIGHT
        elif self.__position.y > SCREEN_HEIGHT:
            self.__position.y = 0

    def __rotate(self, angle: float):
        self.__angle += angle
    
    def __fire(self):
        MAX_BULLETS = 6
        if len(self.__bullets) < MAX_BULLETS:
            self.shoot_sound.play()
            bullet = Bullet(self.__position, self.__angle)
            self.__bullets.append(bullet)
            sleep(0.011)

    def __get_triangle_points(self):
        size = 20
        angle_rad = math.radians(self.__angle)
        front = pygame.Vector2(
            self.__position.x + math.cos(angle_rad) * size,
            self.__position.y + math.sin(angle_rad) * size
        )
        left = pygame.Vector2(
            self.__position.x + math.cos(angle_rad + 2.5) * size * 0.6,
            self.__position.y + math.sin(angle_rad + 2.5) * size * 0.6
        )
        right = pygame.Vector2(
            self.__position.x + math.cos(angle_rad - 2.5) * size * 0.6,
            self.__position.y + math.sin(angle_rad - 2.5) * size * 0.6
        )
        return [front, left, right]

# The bullet is thankfully far easier than the player
# just some math at the end of the day, yippee!

class Bullet:
    def __init__(self, position, angle):
        self.position = pygame.Vector2(position)
        self.angle = angle
        self.speed = 600
    
    def update(self, dt):
        self.position.x += math.cos(math.radians(self.angle)) * self.speed * dt
        self.position.y += math.sin(math.radians(self.angle)) * self.speed * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), 3)
    
    def is_on_screen(self):
        return 0 <= self.position.x <= 800 and 0 <= self.position.y <= 600