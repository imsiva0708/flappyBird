import pygame
import random

class Ground:
    GROUND_LEVEL = 500

    def __init__(self, win_width):
        self.x = 0
        self.y = Ground.GROUND_LEVEL
        self.rect = pygame.Rect(self.x, self.y,win_width, 5)

    def draw(self,window):
        pygame.draw.rect(window, (255,255,255), self.rect)

class Pipes:
    WIDTH = 15
    OPENING = 100

    def __init__(self,win_width):
        self.x = win_width
        self.bottom_height = random.randint(100,300)
        self.top_height = Ground.GROUND_LEVEL - self.OPENING - self.bottom_height
        self.bottom_rect, self.top_rect = pygame.Rect(0,0,0,0), pygame.Rect(0,0,0,0)
        self.passed = False
        self.off_screen = False

    def draw(self, window):
        self.bottom_rect = pygame.Rect(self.x,Ground.GROUND_LEVEL-self.bottom_height, self.WIDTH,self.bottom_height)
        pygame.draw.rect(window, (255,255,255), self.bottom_rect)
        self.top_rect = pygame.Rect(self.x,0,self.WIDTH,self.top_height)
        pygame.draw.rect(window, (255,255,255), self.top_rect)

    def update(self):
        self.x -= 3 #This effects the speed of the game
        if self.x + Pipes.WIDTH <= 50:
            self.passed = True
        if self.x <= - self.WIDTH:
            self.off_screen = True
    