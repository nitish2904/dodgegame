import pygame
import random

pygame.init()
pygame.mixer.init()

display_width = 1000
display_height = 700
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('DODGE')
pygame.display.update()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 155, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
pink = (255, 128, 128)
FPS = 30

clock = pygame.time.Clock()
crash = pygame.mixer.Sound("mario_bross_dies.wav")
star_sound = pygame.mixer.Sound("mario.wav")
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
ing = pygame.image.load(r'crab.png')
trck = pygame.image.load(r'track2.png')
background = pygame.image.load(r'back.jpg')
star = pygame.image.load('star.gif')


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def msg_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def pause():
    pygame.mixer.music.stop()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.blit(background, [0, 0])

        msg_to_screen("PAUSED!", green, -50, "large")
        msg_to_screen("Press C to continue and Q to quit", red, 50, "medium")
        pygame.display.update()
        clock.tick(5)


def gameloop():
    gameExit = False
    gameOver = False
    lead_y_1_change = 0
    lead_y_2_change = 0
    lead_x_change = 176
    lead_x_1 = 93
    lead_x_2 = 620
    lead_y_1 = display_height - 30
    lead_y_2 = display_height - 30

    c = 0
    hurdle_x_1 = 100
    hurdle_x_2 = 275
    hurdle_x_3 = 625
    hurdle_x_4 = 800
    hurdle_width = 50
    hurdle_height = 10
    hurdle_y_1 = random.randrange(0, display_height * (1 / 4))
    hurdle_y_2 = random.randrange(0, display_height * (1 / 4))
    hurdle_y_3 = random.randrange(0, display_height * (1 / 4))
    hurdle_y_4 = random.randrange(0, display_height * (1 / 4))
    score_1 = 0
    score_2 = 0
    speed_from = 2
    speed_to = 5
    y_1 = random.randrange(200, 600)
    y_2 = random.randrange(200, 600)
    y_3 = random.randrange(200, 600)
    y_4 = random.randrange(200, 600)
    while not gameExit:

        while gameOver is True:
            gameDisplay.fill(white)
            gameDisplay.blit(background, [0, 0])
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(crash)
            if score_1 > score_2:
                msg_to_screen("Player 1 WINS !", white, -50, "large")
            elif score_1 < score_2:
                msg_to_screen("Player 2 WINS !", white, -50, "large")
            else:
                msg_to_screen("DRAW!", white, -50, "large")
            msg_to_screen("press C to play again or Q to quit", white, 100, "small")
            msg_to_screen("Player 1 Score " + str(score_1), white, 150, "medium")
            msg_to_screen("Player 2 Score " + str(score_2), white, 200, "medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and c < 1:
                    lead_x_2 += lead_x_change
                    c += 1
                if event.key == pygame.K_LEFT and c > 0:
                    lead_x_2 -= lead_x_change
                    c -= 1
                if event.key == pygame.K_UP:
                    lead_y_2_change = -10
                if event.key == pygame.K_DOWN:
                    lead_y_2_change = 10

                if event.key == pygame.K_d and c < 1:
                    lead_x_1 += lead_x_change
                    c += 1
                if event.key == pygame.K_a and c > 0:
                    lead_x_1 -= lead_x_change
                    c -= 1
                if event.key == pygame.K_w:
                    lead_y_1_change = -10
                if event.key == pygame.K_s:
                    lead_y_1_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        lead_y_1_change = 0
                else:

                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        lead_y_2_change = 0

                if event.key == pygame.K_p:
                    pause()

        lead_y_1 += lead_y_1_change

        lead_y_2 += lead_y_2_change

        if hurdle_y_1 > display_height:
            hurdle_y_1 = random.randrange(0, display_height * (1 / 4))
        if hurdle_y_2 > display_height:
            hurdle_y_2 = random.randrange(0, display_height * (1 / 4))
        if hurdle_y_3 > display_height:
            hurdle_y_3 = random.randrange(0, display_height * (1 / 4))
        if hurdle_y_4 > display_height:
            hurdle_y_4 = random.randrange(0, display_height * (1 / 4))
        gameDisplay.fill(white)
        gameDisplay.blit(background, [0, 0])
        gameDisplay.blit(trck, (50, 0))
        gameDisplay.blit(trck, (575, 0))
        gameDisplay.blit(trck, (750, 0))
        gameDisplay.blit(trck, (225, 0))

        pygame.draw.rect(gameDisplay, green, [hurdle_x_3, hurdle_y_3, hurdle_width, hurdle_height])
        pygame.draw.rect(gameDisplay, green, [hurdle_x_4, hurdle_y_4, hurdle_width, hurdle_height])

        pygame.display.update()

        if score_1 > 5 or score_2 > 5:
            speed_from += 1
            speed_to += 1

        hurdle_y_1 += random.randrange(speed_from, speed_to - 2)

        hurdle_y_2 += random.randrange(speed_from + 2, speed_to)
        hurdle_y_3 += random.randrange(speed_from, speed_to - 2)
        hurdle_y_4 += random.randrange(speed_from + 2, speed_to)

        gameDisplay.blit(ing, (lead_x_1, lead_y_1))
        gameDisplay.blit(ing, (lead_x_2, lead_y_2))
        pygame.draw.rect(gameDisplay, green, [hurdle_x_1, hurdle_y_1, hurdle_width, hurdle_height])
        pygame.draw.rect(gameDisplay, green, [hurdle_x_2, hurdle_y_2, hurdle_width, hurdle_height])

        pygame.display.update()
        if hurdle_y_1 >= lead_y_1 - 15 and hurdle_y_1 <= lead_y_1 + 15 and hurdle_x_1 >= lead_x_1 - 30 and hurdle_x_1 <= lead_x_1 + 30:
            gameOver = True

        if hurdle_y_3 >= lead_y_2 - 15 and hurdle_y_3 <= lead_y_2 + 15 and hurdle_x_3 >= lead_x_2 - 30 and hurdle_x_3 <= lead_x_2 + 30:
            gameOver = True

        if hurdle_y_4 >= lead_y_2 - 15 and hurdle_y_4 <= lead_y_2 + 15 and hurdle_x_4 >= lead_x_2 - 30 and hurdle_x_4 <= lead_x_2 + 30:
            gameOver = True

        if hurdle_y_2 >= lead_y_1 - 15 and hurdle_y_2 <= lead_y_1 + 15 and hurdle_x_2 >= lead_x_1 - 30 and hurdle_x_2 <= lead_x_1 + 30:
            gameOver = True
        if lead_y_1 <= 0 or lead_y_2 <= 0:
            gameOver = True

        if hurdle_y_1 > display_height or hurdle_y_2 > display_height:
            score_1 += 1
        elif hurdle_y_3 > display_height or hurdle_y_4 > display_height:
            score_2 += 1

        if y_1 + 30 > lead_y_1 > y_1 - 30 and 110 > lead_x_1 > 70:
            pygame.mixer.Sound.play(star_sound)
            score_1 += 1
            y_1 = random.randrange(200, 600)
        if y_2 + 30 > lead_y_1 > y_2 - 30 and 285 > lead_x_1 > 245:
            pygame.mixer.Sound.play(star_sound)
            y_2 = random.randrange(200, 600)
            score_1 += 1
        if y_3 + 30 > lead_y_2 > y_3 - 30 and 630 > lead_x_2 > 590:
            pygame.mixer.Sound.play(star_sound)
            y_3 = random.randrange(200, 600)
            score_2 += 1
        if y_4 + 30 > lead_y_2 > y_4 - 30 and 805 > lead_x_2 > 765:
            pygame.mixer.Sound.play(star_sound)
            y_4 = random.randrange(200, 600)
            score_2 += 1

        gameDisplay.blit(star, (90, y_1))
        gameDisplay.blit(star, (265, y_2))
        gameDisplay.blit(star, (610, y_3))
        gameDisplay.blit(star, (785, y_4))

        pygame.draw.rect(gameDisplay, pink, [430, 170, 120, 150])
        msg_to_screen("Player 1 ", white, -150, "small")
        msg_to_screen("SCORE ", white, -100, "small")
        msg_to_screen(str(score_1), white, -50, "small")

        pygame.draw.rect(gameDisplay, pink, [430, 470, 120, 150])
        msg_to_screen("Player 2 ", white, +150, "small")
        msg_to_screen("SCORE ", white, +170, "small")
        msg_to_screen(str(score_2), white, +200, "small")
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()


gameloop()
