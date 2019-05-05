import sys, os, pygame, random, math

class Wall:

    def __init__(self, x, y,WALL_SIZE):
        self.x = x
        self.y = y

        self.size = WALL_SIZE
        self.rectangle = pygame.rect.Rect(self.x, self.y, WALL_SIZE, WALL_SIZE)


        img = pygame.image.load("Images/wll.png")
        self.Image = pygame.transform.scale(img, (WALL_SIZE, WALL_SIZE))

    def draw(self, screen):

            screen.blit(self.Image,
                        [self.rectangle[0],
                         self.rectangle[1]])

