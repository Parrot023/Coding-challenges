import pygame

import random


class Bird:

    # Initializer / Instance Attributes
    def __init__(self, x, y, w, h, screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen
        self.jumpforce = 40
        self.gravity = 1.9
        self.info = pygame.display.Info()
        self.sprite = pygame.image.load('flappy bird tra scaled.png')

    def show(self):
        #pygame.draw.rect(self.screen, (255,0,0), (self.x, self.y, self.w, self.h))
        self.screen.blit(self.sprite,(self.x,self.y))

    def update(self):

        self.y += self.gravity

    def jump(self):

        self.y -= self.jumpforce

    def encounter(self, obstacle):

        self.obstacle = obstacle
        self.H2 = self.info.current_h - self.obstacle.h - self.obstacle.gab

        #True if bird touches bottum obstacle
        if self.x + 50 > self.obstacle.x and self.x + 50 < self.obstacle.x + self.obstacle.w:
            if self.y > self.obstacle.y and self.y < self.obstacle.y + self.obstacle.h:
                return 0

        #True if bird touches top obstacle
        if self.x + 50 > self.obstacle.x and self.x + 50 < self.obstacle.x + self.obstacle.w:
            if self.y > self.obstacle.y - self.obstacle.gab - self.H2 and self.y < self.obstacle.y - self.obstacle.gab:
                return 0

        return 1



class Obstacle:

    def __init__(self, x, y, h, w, screen):

        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.screen = screen
        self.speed = 2
        self.count = 0
        self.gab = 100
        self.info = pygame.display.Info()
        self.count = 0

    def show(self):

        pygame.draw.rect(self.screen, (0,255,0), (self.x, self.y, self.w, self.h))

        pygame.draw.rect(self.screen, (0,255,0), (self.x, 0, self.w, self.info.current_h - self.h - self.gab))


    def update(self):

        self.x -= self.speed

        if self.x + self.w < 0:

            self.h = random.randint(100,300)
            self.x = self.info.current_w
            self.y = self.info.current_h - self.h
            self.gab = random.randint(80, 200)
            self.count = self.count + 1
            print("+1")
            return 1

        return 0
