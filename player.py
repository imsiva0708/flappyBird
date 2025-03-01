import random
import pygame
import config
from components import Pipes


class Player:
    def __init__(self):
        # BIRD
        self.x = 50
        self.y = 200
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.colour = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.vel = 0
        self.flap = False
        self.alive = True

        # AI
        self.decision = None

    def draw(self, window):
        pygame.draw.rect(window, self.colour, self.rect)

    def ground_collision(self, ground):
        return pygame.Rect.colliderect(self.rect, ground)

    def sky_collision(self):
        return bool(self.rect.y < 30)

    def pipe_collision(self):
        p: Pipes
        for p in config.pipes:
            return pygame.Rect.colliderect(self.rect, p.top_rect) or pygame.Rect.colliderect(self.rect, p.bottom_rect)

    def update(self, ground):
        if not (self.ground_collision(ground) or self.pipe_collision()):
            # Apply adaptive gravity
            if self.vel < 5:  
                self.vel += 0.35  # Slow increase when rising
            else:
                self.vel += 0.5  # Faster increase when falling
            
            self.rect.y += self.vel
        else:
            self.alive = False
            self.flap = False
            self.vel = 0

    def bird_flap(self):
        if not self.sky_collision():  # Allow multiple flaps
            self.vel = -6.5  # Reduce jump strength slightly for better control


    # AI Related Function
    def think(self):
        self.decision = random.uniform(0, 1)
        print(self.decision)
        if self.decision > 0.73:
            self.bird_flap()