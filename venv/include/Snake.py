import sys, os, pygame, random, math
from Segment import Segment
import Constants












class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = Constants.KEY["UP"]
        self.stack = []

        self.stack.append(self)

        blackBox = Segment(self.x, self.y + Constants.SEPARATION)
        blackBox.direction = Constants.KEY["UP"]
        blackBox.color = "NULL"
        self.stack.append(blackBox)

    def move(self):
        last_element = len(self.stack) - 1
        while (last_element != 0):
            self.stack[last_element].direction = self.stack[last_element - 1].direction
            self.stack[last_element].x = self.stack[last_element - 1].x
            self.stack[last_element].y = self.stack[last_element - 1].y
            last_element -= 1
        if (len(self.stack) < 2):
            last_segment = self
        else:
            last_segment = self.stack.pop(last_element)
        last_segment.direction = self.stack[0].direction
        if (self.stack[0].direction == Constants.KEY["UP"]):
            last_segment.y = self.stack[0].y - (Constants.SPEED * Constants.FPS)
        elif (self.stack[0].direction == Constants.KEY["DOWN"]):
            last_segment.y = self.stack[0].y + (Constants.SPEED * Constants.FPS)
        elif (self.stack[0].direction == Constants.KEY["LEFT"]):
            last_segment.x = self.stack[0].x - (Constants.SPEED * Constants.FPS)
        elif (self.stack[0].direction == Constants.KEY["RIGHT"]):
            last_segment.x = self.stack[0].x + (Constants.SPEED * Constants.FPS)
        self.stack.insert(0, last_segment)

    def getHead(self):
        return (self.stack[0])
    def remove(self):
        last_element = len(self.stack) - 1
        self.stack.remove(self.stack[last_element])
        self.stack.remove(self.stack[last_element-1])

    def grow(self):
        last_element = len(self.stack) - 1
        self.stack[last_element].direction = self.stack[last_element].direction
        if (self.stack[last_element].direction == Constants.KEY["UP"]):
            newSegment = Segment(self.stack[last_element].x, self.stack[last_element].y - Constants.SNAKE_SIZE)
            blackBox = Segment(newSegment.x, newSegment.y - Constants.SEPARATION)

        elif (self.stack[last_element].direction == Constants.KEY["DOWN"]):
            newSegment = Segment(self.stack[last_element].x, self.stack[last_element].y + Constants.SNAKE_SIZE)
            blackBox = Segment(newSegment.x, newSegment.y + Constants.SEPARATION)

        elif (self.stack[last_element].direction == Constants.KEY["LEFT"]):
            newSegment = Segment(self.stack[last_element].x - Constants.SNAKE_SIZE, self.stack[last_element].y)
            blackBox = Segment(newSegment.x - Constants.SEPARATION, newSegment.y)

        elif (self.stack[last_element].direction == Constants.KEY["RIGHT"]):
            newSegment = Segment(self.stack[last_element].x + Constants.SNAKE_SIZE, self.stack[last_element].y)
            blackBox = Segment(newSegment.x + Constants.SEPARATION, newSegment.y)

        blackBox.color = "NULL"
        self.stack.append(newSegment)
        self.stack.append(blackBox)

    def iterateSegments(self, delta):
        pass

    def setDirection(self, direction):
         # if (self.direction == Constants.KEY["RIGHT"] and direction == Constants.KEY["LEFT"] or self.direction == Constants.KEY[
         #     "LEFT"] and direction == Constants.KEY["RIGHT"]):
         #     pass
         # elif (self.direction == Constants.KEY["UP"] and direction == Constants.KEY["DOWN"] or self.direction == Constants.KEY["DOWN"] and direction ==
         #       Constants.KEY["UP"]):
         #     pass
         # else:
        self.direction = direction

    def get_rect(self):
        rect = (self.x, self.y)
        return rect

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def checkCrash(self):
        counter = 1
        while (counter < len(self.stack) - 1):
            if (Constants.checkCollision(self.stack[0], Constants.SNAKE_SIZE, self.stack[counter], Constants.SNAKE_SIZE) and self.stack[
                counter].color != "NULL"):
                return True
            counter += 1
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.color.Color("yellow"),
                         (self.stack[0].x, self.stack[0].y, Constants.SNAKE_SIZE, Constants.SNAKE_SIZE), 0)
        counter = 1
        while (counter < len(self.stack)):
            if (self.stack[counter].color == "NULL"):
                counter += 1
                continue
            pygame.draw.rect(screen, pygame.color.Color("white"),
                             (self.stack[counter].x, self.stack[counter].y, Constants.SNAKE_SIZE, Constants.SNAKE_SIZE), 0)
            counter += 1
