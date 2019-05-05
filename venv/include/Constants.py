import  pygame
# Global constant definitions

pygame.font.init()

type = None
menuTimes = 0;
sTime = 0
SPEED = 0.36
SNAKE_SIZE = 9
APPLE_SIZE = 20
SEPARATION = 10
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"UP": 1, "DOWN": 2, "LEFT": 3, "RIGHT": 4}

score_font = pygame.font.Font("fonts/ARCADE.TTF", 38)
score_numb_font = pygame.font.Font("fonts/ARCADE.TTF", 28)
game_over_font = pygame.font.Font("fonts/ARCADE.TTF", 46)
play_again_font = score_numb_font
score_msg = score_font.render("Score:", 1, pygame.Color("green"))
score_msg_size = score_font.size("Score")

def checkCollision(posA, As, posB, Bs):
    # As size of a | Bs size of B
    if (posA.x < posB.x + Bs and posA.x + As > posB.x and posA.y < posB.y + Bs and posA.y + As > posB.y):
        return True
    return False

def checkCollisionw(posA, As, posB, Bs,Bsy):
    # As size of a | Bs size of B
    if (posA.x < posB.x + Bs+ Bsy and posA.x + As > posB.x and posA.y < posB.y + Bs + Bsy and posA.y + As > posB.y):
        return True
    return False

def checkCollisionWall(posA,  posB):
    # As size of a | Bs size of B
    if (posA.x < posB.x  and posA.x  > posB.x and posA.y < posB.y  and posA.y > posB.y):
        return True
    return False





def checkLimits(entity):
    if (entity.x > SCREEN_WIDTH):
        entity.x = SNAKE_SIZE
    if (entity.x < 0):
        entity.x = SCREEN_WIDTH - SNAKE_SIZE
    if (entity.y > SCREEN_HEIGHT):
        entity.y = SNAKE_SIZE
    if (entity.y < 0):
        entity.y = SCREEN_HEIGHT - SNAKE_SIZE
