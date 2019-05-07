import sys, os, random, math, Constants
import pygame
from Apple import *
from Wall import *
from Snake import Snake
from Segment import Segment

from Menu import *
import time

pygame.init()
pygame.display.set_caption("Yılan Oyunu v1.0")
pygame.font.init()
random.seed()

# Screen initialization
screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT), pygame.HWSURFACE)
startTime = 0
menuTimer = 0

background_color = pygame.Color(74, 74, 74)
black = pygame.Color(0, 0, 0)

# Clock
gameClock = pygame.time.Clock()
menu = Menu(screen.get_rect())


def Nmaxelements(list1, list2, N):
    final_list = []
    list1 = [int(x) for x in list1]
    list2 = list2

    for i in range(N):
        maxvalin = list1.index(max(list1))

        final_list.append(list2[maxvalin])
        list2.remove(list2[maxvalin])
        final_list.append(list1[maxvalin])
        list1.remove(list1[maxvalin])

    return final_list


def getKEY():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return Constants.KEY["UP"]
            elif event.key == pygame.K_DOWN:
                return Constants.KEY["DOWN"]
            elif event.key == pygame.K_LEFT:
                return Constants.KEY["LEFT"]
            elif event.key == pygame.K_RIGHT:
                return Constants.KEY["RIGHT"]
            elif event.key == pygame.K_z:
                return "exit"
            elif event.key == pygame.K_ESCAPE:
                return "menu"
            elif event.key == pygame.K_y:
                return "yes"
            elif event.key == pygame.K_n:
                return "no"
            elif event.key == pygame.K_m:
                return "save"
        if event.type == pygame.QUIT:
            sys.exit()


def respawnApple(apples, index, sx, sy):
    radius = math.sqrt((
                                   Constants.SCREEN_WIDTH / 2 * Constants.SCREEN_WIDTH / 2 + Constants.SCREEN_HEIGHT / 2 * Constants.SCREEN_HEIGHT / 2)) / 2
    angle = 999
    while (angle > radius):
        angle = random.uniform(0, 800) * math.pi * 2
        x = Constants.SCREEN_WIDTH / 2 + radius * math.cos(angle)
        y = Constants.SCREEN_HEIGHT / 2 + radius * math.sin(angle)
        if (x == sx and y == sy):
            continue

    c = random.randint(1, 7)
    newApple = FastnerApple(Apple(x, y, 1, Constants.APPLE_SIZE))
    if (c == 1):
        newApple = FastnerApple(Apple(x, y, 1, Constants.APPLE_SIZE))
    elif (c == 2):
        newApple = KillerApple(Apple(x, y, 1, Constants.APPLE_SIZE))
        Constants.type = type(newApple)
        a = pygame.time.get_ticks()
        Constants.sTime = a

    elif (c == 3):
        newApple = OnePointApple(Apple(x, y, 1, Constants.APPLE_SIZE))
    elif (c == 4):
        newApple = SilverLowerApple(Apple(x, y, 1, Constants.APPLE_SIZE))
    elif (c == 5):
        newApple = SlowerApple(Apple(x, y, 1, Constants.APPLE_SIZE))
    elif (c == 6):
        newApple = ThreePointApple(Apple(x, y, 1, Constants.APPLE_SIZE))

    apples[index] = newApple


def respawnApples(apples, quantity, sx, sy):
    counter = 0
    del apples[:]
    radius = math.sqrt((
                                   Constants.SCREEN_WIDTH / 2 * Constants.SCREEN_WIDTH / 2 + Constants.SCREEN_HEIGHT / 2 * Constants.SCREEN_HEIGHT / 2)) / 2
    angle = 999
    while (counter < quantity):
        while (angle > radius):
            angle = random.uniform(0, 800) * math.pi * 2
            x = Constants.SCREEN_WIDTH / 2 + radius * math.cos(angle)
            y = Constants.SCREEN_HEIGHT / 2 + radius * math.sin(angle)
            if ((x - Constants.APPLE_SIZE == sx or x + Constants.APPLE_SIZE == sx) and (
                    y - Constants.APPLE_SIZE == sy or y + Constants.APPLE_SIZE == sy) or radius - angle <= 10):
                continue
        apples.append(FastnerApple(Apple(x, y, 1, Constants.APPLE_SIZE)))
        angle = 999
        counter += 1


def endGame(scr):
    Constants.type = None
    Constants.sTime = 0
    Constants.SPEED = 0.36
    Constants.SNAKE_SIZE = 9
    Constants.APPLE_SIZE = 20
    Constants.SEPARATION = 10
    Constants.SCREEN_HEIGHT = 600
    Constants.SCREEN_WIDTH = 800
    Constants.FPS = 25

    message = Constants.game_over_font.render("Game Over", 1, pygame.Color("white"))
    message_play_again = Constants.play_again_font.render("Play Again? Y/N", 1, pygame.Color("green"))
    scr_message_play_again = Constants.play_again_font.render("For Save Your Score Press M", 1, pygame.Color("purple"))
    screen.blit(message, (320, 240))
    screen.blit(message_play_again, (320 + 12, 240 + 40))
    screen.blit(scr_message_play_again, (240, 240 + 80))
    pygame.display.flip()
    pygame.display.update()

    myKEY = getKEY()
    while (myKEY != "exit"):
        if (myKEY == "yes"):
            main()
        elif (myKEY == "no"):
            break
        elif (myKEY == "save"):
            num_lines = sum(1 for line in open('saveFile.txt'))

            if num_lines == 0:
                fileHandle = open('saveFile.txt', "a")
                fileHandle.write("Player" + str(0) + " " + str(scr) + "\r")
                fileHandle.close()
                break
            elif num_lines > 0:
                fileHandle = open('saveFile.txt', "r")
                lineList = fileHandle.readlines()
                fileHandle.close()

                lastline = lineList[len(lineList) - 1]
                index = lastline.find(' ')
                lastPlayerName = lastline[0:index]

                dig = 1
                digc = ''
                for x in lastPlayerName:
                    if x.isdigit():
                        digc += x
                        dig = int(digc)

                fileHandle = open('saveFile.txt', "a")
                fileHandle.write("Player" + str(dig + 1) + " " + str(scr) + "\r")
                fileHandle.close()

                break

        myKEY = getKEY()
        gameClock.tick(Constants.FPS)
    sys.exit()


def drawScore(score):
    score_numb = Constants.score_numb_font.render(str(score), 1, pygame.Color("red"))
    screen.blit(Constants.score_msg, (Constants.SCREEN_WIDTH - Constants.score_msg_size[0] - 60, 10))
    screen.blit(score_numb, (Constants.SCREEN_WIDTH - 45, 14))


def drawGameTime(gameTime):
    game_time = Constants.score_font.render("Time:", 1, pygame.Color("green"))
    game_time_numb = Constants.score_numb_font.render(str(gameTime - menuTimer), 1, pygame.Color("red"))
    screen.blit(game_time, (30, 10))
    screen.blit(game_time_numb, (105, 14))


def drawSave(findomList):
    game_time = Constants.score_font.render("Saved Values:", 1, pygame.Color("green"))

    screen.blit(game_time, (30, 10))

    c = 30
    for x in range(0, len(findomList), 2):
        game_time_numb = Constants.score_numb_font.render(str(findomList[x]), 1, pygame.Color("red"))
        screen.blit(game_time_numb, (300, c))
        game_time_numb = Constants.score_numb_font.render(str(findomList[x + 1]), 1, pygame.Color("red"))
        screen.blit(game_time_numb, (400, c))
        c += 45



    c += 45

    game_time = Constants.score_font.render("Please Click ESC To Return Game", 1, pygame.Color("Yellow"))
    screen.blit(game_time, (200, 500))
    pygame.display.flip()
    pygame.display.update()

    c = getKEY()

    while c != "menu":
        c = getKEY()


def main():
    score = 0

    # wall initialization
    Walls = [Wall(0, 0, 15), Wall(0, 15, 15), Wall(0, 30, 15), Wall(0, 45, 15), Wall(0, 60, 15), Wall(0, 75, 15),
             Wall(0, 90, 15), Wall(0, 105, 15), Wall(0, 120, 15), Wall(0, 135, 15), Wall(0, 150, 15), Wall(0, 165, 15),
             Wall(0, 300, 15), Wall(0, 315, 15), Wall(0, 330, 15), Wall(0, 345, 15), Wall(0, 360, 15), Wall(0, 375, 15),
             Wall(0, 390, 15), Wall(0, 405, 15), Wall(0, 420, 15), Wall(0, 435, 15), Wall(0, 450, 15), Wall(0, 465, 15),

             Wall(785, 0, 15), Wall(785, 15, 15), Wall(785, 30, 15), Wall(785, 45, 15), Wall(785, 60, 15),
             Wall(785, 75, 15),
             Wall(785, 90, 15), Wall(785, 105, 15), Wall(785, 120, 15), Wall(785, 135, 15), Wall(785, 150, 15),
             Wall(785, 165, 15),
             Wall(785, 300, 15), Wall(785, 315, 15), Wall(785, 330, 15), Wall(785, 345, 15), Wall(785, 360, 15),
             Wall(785, 375, 15),
             Wall(785, 390, 15), Wall(785, 405, 15), Wall(785, 420, 15), Wall(785, 435, 15), Wall(785, 450, 15),
             Wall(785, 465, 15),

             Wall(90, 0, 15), Wall(105, 0, 15), Wall(120, 0, 15), Wall(135, 0, 15), Wall(150, 0, 15), Wall(165, 0, 15),
             Wall(180, 0, 15),
             Wall(270, 0, 15), Wall(285, 0, 15), Wall(300, 0, 15), Wall(315, 0, 15), Wall(330, 0, 15), Wall(345, 0, 15),
             Wall(360, 0, 15),
             Wall(450, 0, 15), Wall(465, 0, 15), Wall(480, 0, 15), Wall(495, 0, 15), Wall(510, 0, 15),
             Wall(525, 0, 15), Wall(540, 0, 15),
             Wall(630, 0, 15), Wall(645, 0, 15), Wall(660, 0, 15), Wall(675, 0, 15), Wall(690, 0, 15),
             Wall(705, 0, 15), Wall(720, 0, 15),

             Wall(90, 585, 15), Wall(105, 585, 15), Wall(120, 585, 15), Wall(135, 585, 15), Wall(150, 585, 15),
             Wall(165, 585, 15),
             Wall(180, 585, 15),
             Wall(270, 585, 15), Wall(285, 585, 15), Wall(300, 585, 15), Wall(315, 585, 15), Wall(330, 585, 15),
             Wall(345, 585, 15),
             Wall(360, 585, 15),
             Wall(450, 585, 15), Wall(465, 585, 15), Wall(480, 585, 15), Wall(495, 585, 15), Wall(510, 585, 15),
             Wall(525, 585, 15), Wall(540, 585, 15),
             Wall(630, 585, 15), Wall(645, 585, 15), Wall(660, 585, 15), Wall(675, 585, 15), Wall(690, 585, 15),
             Wall(705, 585, 15), Wall(720, 585, 15)

             ]

    error = None
    Resume = None

    # Snake initialization
    mySnake = Snake(Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 2)
    mySnake.setDirection(Constants.KEY["UP"])
    mySnake.move()
    strb = 3
    start_segments = 3
    while (start_segments > 0):
        mySnake.grow()
        mySnake.move()
        start_segments -= 1

    # Apples initialization
    max_apples = 1
    eaten_apple = False

    apples = [FastnerApple(Apple(random.randint(60, 300), random.randint(60, 300), 1, Constants.APPLE_SIZE))]
    respawnApples(apples, max_apples, mySnake.x, mySnake.y)
    global startTime, menuTimer
    startTime = time.clock()
    endgame = False

    while not endgame:
        gameClock.tick(Constants.FPS)

        # Input
        KEYPress = getKEY()
        if KEYPress == "exit":
            endgame = True
        elif KEYPress == "menu":
            g = menu.runMenu(screen)

            endgame = g
            if (endgame == 'cagır'):
                main()
            if (endgame == 'save'):
                screen.fill(background_color)
                array = []
                nickname = []
                skr = []
                with open("saveFile.txt", "r") as ins:
                    for line in ins:
                        index = line.find(' ')
                        this = line.find('\r')
                        nickname.append(line[0:index])
                        skr.append(line[index:this])

                drawSave(Nmaxelements(skr, nickname, 10))
            drawScore(score)
            c = mySnake.getHead()

            slen = len(mySnake.stack) / 2 - 1

            main2(c.x, c.y, c.direction, apples, slen, score)
        elif (KEYPress == "yes" or KEYPress == "no" or KEYPress == "save"):
            pass
        # Collision check

        Constants.checkLimits(mySnake)
        if (mySnake.checkCrash() == True):
            endGame(score)

        for myApple in apples:
            if (myApple.state == 1):
                if (Constants.checkCollision(mySnake.getHead(), Constants.SNAKE_SIZE, myApple,
                                             Constants.APPLE_SIZE) == True):
                    if (type(myApple) == OnePointApple):
                        mySnake.grow()
                        myApple.state = 0
                        score += 5
                    elif (type(myApple) == FastnerApple):
                        Constants.FPS += 1
                    elif (type(myApple) == KillerApple):
                        endGame(score)
                    elif (type(myApple) == SilverLowerApple):
                        mySnake.remove()

                        if ((len(mySnake.stack) - 1) / 2 < strb):
                            score -= 5
                        if ((len(mySnake.stack) - 1) / 2 <= 0):
                            endGame(score)
                    elif (type(myApple) == SlowerApple):
                        Constants.FPS -= 2
                        if (Constants.FPS <= 25):
                            Constants.FPS = 25
                    elif (type(myApple) == ThreePointApple):
                        mySnake.grow()
                        mySnake.grow()
                        mySnake.grow()
                        score += 15
                    eaten_apple = True

        for wal in Walls:
            if (Constants.checkCollision(mySnake.getHead(), Constants.SNAKE_SIZE, wal, wal.size) == True):
                endGame(score)

        # Position Update
        if (KEYPress):
            mySnake.setDirection(KEYPress)
        mySnake.move()

        if Constants.type == KillerApple and abs(pygame.time.get_ticks() - Constants.sTime) > 5000:
            eaten_apple = False
            Constants.type = None
            respawnApple(apples, 0, mySnake.getHead().x, mySnake.getHead().y)

        # Respawning apples
        if (eaten_apple == True and Constants.type == None):
            eaten_apple = False
            respawnApple(apples, 0, mySnake.getHead().x, mySnake.getHead().y)

        # Drawing
        screen.fill(background_color)
        for wel in Walls:
            wel.draw(screen)

        for myApple in apples:
            if (myApple.state == 1):
                if (type(myApple) == KillerApple):
                    pass
                myApple.draw(screen)

        mySnake.draw(screen)

        drawScore(score)

        gameTime = time.clock() - startTime

        drawGameTime(gameTime - Constants.menuTimes)
        Constants.menuTimes = 0

        pygame.display.flip()
        pygame.display.update()


def main2(snakex, snakey, direction, apley, size, score):
    # wall initialization
    Walls = [Wall(0, 0, 15), Wall(0, 15, 15), Wall(0, 30, 15), Wall(0, 45, 15), Wall(0, 60, 15), Wall(0, 75, 15),
             Wall(0, 90, 15), Wall(0, 105, 15), Wall(0, 120, 15), Wall(0, 135, 15), Wall(0, 150, 15), Wall(0, 165, 15),
             Wall(0, 300, 15), Wall(0, 315, 15), Wall(0, 330, 15), Wall(0, 345, 15), Wall(0, 360, 15), Wall(0, 375, 15),
             Wall(0, 390, 15), Wall(0, 405, 15), Wall(0, 420, 15), Wall(0, 435, 15), Wall(0, 450, 15), Wall(0, 465, 15),

             Wall(785, 0, 15), Wall(785, 15, 15), Wall(785, 30, 15), Wall(785, 45, 15), Wall(785, 60, 15),
             Wall(785, 75, 15),
             Wall(785, 90, 15), Wall(785, 105, 15), Wall(785, 120, 15), Wall(785, 135, 15), Wall(785, 150, 15),
             Wall(785, 165, 15),
             Wall(785, 300, 15), Wall(785, 315, 15), Wall(785, 330, 15), Wall(785, 345, 15), Wall(785, 360, 15),
             Wall(785, 375, 15),
             Wall(785, 390, 15), Wall(785, 405, 15), Wall(785, 420, 15), Wall(785, 435, 15), Wall(785, 450, 15),
             Wall(785, 465, 15),

             Wall(90, 0, 15), Wall(105, 0, 15), Wall(120, 0, 15), Wall(135, 0, 15), Wall(150, 0, 15), Wall(165, 0, 15),
             Wall(180, 0, 15),
             Wall(270, 0, 15), Wall(285, 0, 15), Wall(300, 0, 15), Wall(315, 0, 15), Wall(330, 0, 15), Wall(345, 0, 15),
             Wall(360, 0, 15),
             Wall(450, 0, 15), Wall(465, 0, 15), Wall(480, 0, 15), Wall(495, 0, 15), Wall(510, 0, 15),
             Wall(525, 0, 15), Wall(540, 0, 15),
             Wall(630, 0, 15), Wall(645, 0, 15), Wall(660, 0, 15), Wall(675, 0, 15), Wall(690, 0, 15),
             Wall(705, 0, 15), Wall(720, 0, 15),

             Wall(90, 585, 15), Wall(105, 585, 15), Wall(120, 585, 15), Wall(135, 585, 15), Wall(150, 585, 15),
             Wall(165, 585, 15),
             Wall(180, 585, 15),
             Wall(270, 585, 15), Wall(285, 585, 15), Wall(300, 585, 15), Wall(315, 585, 15), Wall(330, 585, 15),
             Wall(345, 585, 15),
             Wall(360, 585, 15),
             Wall(450, 585, 15), Wall(465, 585, 15), Wall(480, 585, 15), Wall(495, 585, 15), Wall(510, 585, 15),
             Wall(525, 585, 15), Wall(540, 585, 15),
             Wall(630, 585, 15), Wall(645, 585, 15), Wall(660, 585, 15), Wall(675, 585, 15), Wall(690, 585, 15),
             Wall(705, 585, 15), Wall(720, 585, 15)

             ]

    error = None
    Resume = None

    # Snake initialization
    mySnake = Snake(snakex, snakey)
    mySnake.setDirection(direction)
    mySnake.move()
    strb = 3
    start_segments = size
    while (start_segments > 0):
        mySnake.grow()
        mySnake.move()
        start_segments -= 1

    # Apples initialization
    max_apples = 1
    eaten_apple = False

    apples = apley

    global startTime, menuTimer

    endgame = False

    while not endgame:
        gameClock.tick(Constants.FPS)

        # Input
        KEYPress = getKEY()
        if KEYPress == "exit":
            endgame = True
        elif KEYPress == "menu":
            g = menu.runMenu(screen)

            endgame = g
            if (endgame == 'cagır'):
                main()
            if (endgame == 'save'):
                screen.fill(background_color)
                array = []
                nickname = []
                skr = []
                with open("saveFile.txt", "r") as ins:
                    for line in ins:
                        index = line.find(' ')
                        this = line.find('\r')
                        nickname.append(line[0:index])
                        skr.append(line[index:this])

                drawSave(Nmaxelements(skr, nickname, 10))

            drawScore(score)
            c = mySnake.getHead()

            main2(c.x, c.y, c.direction, apples, len(mySnake.stack) / 2 - 1, score)
        elif (KEYPress == "yes" or KEYPress == "no" or KEYPress == "save"):
            pass

        # Collision check

        Constants.checkLimits(mySnake)
        if (mySnake.checkCrash() == True):
            endGame(score)

        for myApple in apples:
            if (myApple.state == 1):
                if (Constants.checkCollision(mySnake.getHead(), Constants.SNAKE_SIZE, myApple,
                                             Constants.APPLE_SIZE) == True):
                    if (type(myApple) == OnePointApple):
                        mySnake.grow()
                        myApple.state = 0
                        score += 5
                    elif (type(myApple) == FastnerApple):
                        Constants.FPS += 1
                    elif (type(myApple) == KillerApple):
                        endGame(score)
                    elif (type(myApple) == SilverLowerApple):
                        mySnake.remove()

                        if ((len(mySnake.stack) - 1) / 2 < strb):
                            score -= 5
                        if ((len(mySnake.stack) - 1) / 2 <= 0):
                            endGame(score)
                    elif (type(myApple) == SlowerApple):
                        Constants.FPS -= 2
                        if (Constants.FPS <= 25):
                            Constants.FPS = 25
                    elif (type(myApple) == ThreePointApple):
                        mySnake.grow()
                        mySnake.grow()
                        mySnake.grow()
                        score += 15
                    eaten_apple = True

        for wal in Walls:
            if (Constants.checkCollision(mySnake.getHead(), Constants.SNAKE_SIZE, wal, wal.size) == True):
                endGame(score)

        # Position Update
        if (KEYPress):
            mySnake.setDirection(KEYPress)
        mySnake.move()

        if Constants.type == KillerApple and abs(pygame.time.get_ticks() - Constants.sTime) > 5000:
            eaten_apple = False
            Constants.type = None
            respawnApple(apples, 0, mySnake.getHead().x, mySnake.getHead().y)

        # Respawning apples
        if (eaten_apple == True and Constants.type == None):
            eaten_apple = False
            respawnApple(apples, 0, mySnake.getHead().x, mySnake.getHead().y)

        # Drawing
        screen.fill(background_color)
        for wel in Walls:
            wel.draw(screen)

        for myApple in apples:
            if (myApple.state == 1):
                if (type(myApple) == KillerApple):
                    pass
                myApple.draw(screen)

        mySnake.draw(screen)

        drawScore(score)

        gameTime = time.clock() - startTime

        drawGameTime(gameTime)

        pygame.display.flip()
        pygame.display.update()


main()