import sys, os, pygame, random, math

class Apple:
    def __init__(self, x, y, state,APPLE_SIZE):
        self.x = x
        self.y = y
        self.state = state
        self.size = APPLE_SIZE
        self.rectangle = pygame.rect.Rect(self.x, self.y, APPLE_SIZE, APPLE_SIZE)
        self.ImageOrder = 0
        self.Images = []


    def draw(self, screen):
            self.ImageOrder = (self.ImageOrder + 1) % 9
            screen.blit(self.Images[self.ImageOrder],
                        [self.rectangle[0],
                         self.rectangle[1]])



class FastnerApple(Apple):
        def __init__(self,Apple):
            super().__init__(Apple.x , Apple.y ,Apple.state,Apple.size)
            self.ImageOrder = 0
            self.Images =[]
            for i in range(1, 10):
                self.Images.append(
                    pygame.transform.scale(pygame.image.load("Images/FastnerSnack/Purple_" + str(i) + ".png"),
                                           (self.rectangle[2], self.rectangle[3])))

        def draw(self, screen):
            self.ImageOrder = (self.ImageOrder + 1) % 9
            screen.blit(self.Images[self.ImageOrder],
                        [self.rectangle[0],
                        self.rectangle[1]])


class KillerApple(Apple):
    def __init__(self, Apple):
        super().__init__(Apple.x , Apple.y ,Apple.state,Apple.size)
        self.ImageOrder = 0
        self.Images = []
        for i in range(1, 10):
            self.Images.append(
                pygame.transform.scale(pygame.image.load("Images/KillerSnack/Grey_" + str(i) + ".png"),
                                       (self.rectangle[2], self.rectangle[3])))

    def draw(self, screen):
        self.ImageOrder = (self.ImageOrder + 1) % 9
        screen.blit(self.Images[self.ImageOrder],
                    [self.rectangle[0],
                     self.rectangle[1]])

class OnePointApple(Apple):
    def __init__(self, Apple):
        super().__init__(Apple.x , Apple.y ,Apple.state,Apple.size)
        self.ImageOrder = 0
        self.Images = []
        for i in range(1, 10):
            self.Images.append(
                pygame.transform.scale(pygame.image.load("Images/OnePointSnack/Bronze_" + str(i) + ".png"),
                                       (self.rectangle[2], self.rectangle[3])))

    def draw(self, screen):
        self.ImageOrder = (self.ImageOrder + 1) % 9
        screen.blit(self.Images[self.ImageOrder],
                    [self.rectangle[0],
                     self.rectangle[1]])

class SilverLowerApple(Apple):
    def __init__(self, Apple):
        super().__init__(Apple.x , Apple.y ,Apple.state,Apple.size)
        self.ImageOrder = 0
        self.Images = []
        for i in range(1, 10):
            self.Images.append(
                pygame.transform.scale(pygame.image.load("Images/SilverLower/Silver_" + str(i) + ".png"),
                                       (self.rectangle[2], self.rectangle[3])))

    def draw(self, screen):
        self.ImageOrder = (self.ImageOrder + 1) % 9
        screen.blit(self.Images[self.ImageOrder],
                    [self.rectangle[0],
                     self.rectangle[1]])


class SlowerApple(Apple):
    def __init__(self, Apple):
        super().__init__(Apple.x , Apple.y ,Apple.state,Apple.size)
        self.ImageOrder = 0
        self.Images = []
        for i in range(1, 10):
            self.Images.append(
                pygame.transform.scale(pygame.image.load("Images/SlowerSnack/Green_" + str(i) + ".png"),
                                       (self.rectangle[2], self.rectangle[3])))

    def draw(self, screen):
        self.ImageOrder = (self.ImageOrder + 1) % 9
        screen.blit(self.Images[self.ImageOrder],
                    [self.rectangle[0],
                     self.rectangle[1]])

class ThreePointApple(Apple):
    def __init__(self, Apple):
        super().__init__(Apple.x , Apple.y ,Apple.state,Apple.size)
        self.ImageOrder = 0
        self.Images = []
        for i in range(1, 10):
            self.Images.append(
                pygame.transform.scale(pygame.image.load("Images/ThreePointStack/Gold_" + str(i) + ".png"),
                                       (self.rectangle[2], self.rectangle[3])))

    def draw(self, screen):
        self.ImageOrder = (self.ImageOrder + 1) % 9
        screen.blit(self.Images[self.ImageOrder],
                    [self.rectangle[0],
                     self.rectangle[1]])