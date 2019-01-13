import pygame
import random

pygame.init()

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

font = pygame.font.SysFont(None, 25)
ing = pygame.image.load(r'cr_n.png')
trck = pygame.image.load(r'Track2.png')
background = pygame.image.load(r'Background.png')


def msg_to_screen(msg, color, fnt, width, height):
    screen_txt = fnt.render(msg, True, color)
    gameDisplay.blit(screen_txt, [width, height])


def pause():
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

        msg_to_screen("PAUSED!", green, font1, display_width / 2 - 100, display_height / 2 - 100)
        msg_to_screen("Press C to continue and Q to quit", red, font, display_width / 2 - 150, display_height / 2 + 100)
        pygame.display.update()
        clock.tick(5)


font1 = pygame.font.SysFont(None, 50)


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
    score = 0
    speed_from = 2
    speed_to = 5

    while not gameExit:

        while gameOver is True:
            gameDisplay.blit(background, [0, 0])

            msg_to_screen("GAME OVER, press C to play again or Q to quit", red, font, 10, display_height / 2)
            msg_to_screen("Score " + str(score), red, font1, 100, 200)
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

            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:

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
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        lead_y_2_change = 0

            if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
                if event.type == pygame.KEYDOWN:

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
                        lead_y_1_change = 0

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

        gameDisplay.blit(background, [0, 0])
        gameDisplay.blit(trck, (50, 0))
        gameDisplay.blit(trck, (575, 0))
        gameDisplay.blit(trck, (750, 0))
        gameDisplay.blit(trck, (225, 0))

        pygame.draw.rect(gameDisplay, green, [hurdle_x_3, hurdle_y_3, hurdle_width, hurdle_height])
        pygame.draw.rect(gameDisplay, green, [hurdle_x_4, hurdle_y_4, hurdle_width, hurdle_height])

        pygame.display.update()

        if score > 5:
            speed_from += 1
            speed_to += 1

        hurdle_y_1 += random.randrange(speed_from, speed_to - 2)

        hurdle_y_2 += random.randrange(speed_from + 2, speed_to)
        hurdle_y_3 += random.randrange(speed_from + 2, speed_to)
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

        if hurdle_y_1 > display_height or hurdle_y_2 > display_height or hurdle_y_3 > display_height or hurdle_y_4 > display_height:
            score += 1

        pygame.draw.rect(gameDisplay, pink, [400, 150, 150, 150])
        msg_to_screen("SCORE ", white, font1, 415, 180)
        msg_to_screen(str(score), white, font1, 450, 220)
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()


gameloop()
