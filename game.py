import pygame
import sys

WIN_SIZE = (480, 500)
WIN_TITLE = "Ping pong"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RECT_SIZE = (80, 13)
RADIUS = 10
SPEED_RECT = 25
SPEED_X_BALL = 4
SPEED_Y_BALL = 3
FPS = 60

rect_pos = [WIN_SIZE[0] / 2 - RECT_SIZE[0] / 2, WIN_SIZE[1] - RECT_SIZE[1] * 2]
ball_pos = [WIN_SIZE[0] / 2 + RADIUS / 2, WIN_SIZE[1] / 2 - RADIUS * 2]

def run_game():
    gameOver = False
    
    pygame.init()
    speed_x_ball = SPEED_X_BALL
    speed_y_ball = SPEED_Y_BALL

    screen = pygame.display.set_mode(WIN_SIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption(WIN_TITLE)

    while not gameOver:
        keys = pygame.key.get_pressed()
        ball_pos[0] += speed_x_ball
        ball_pos[1] += speed_y_ball

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if keys[pygame.K_a]:
                rect_pos[0] -= SPEED_RECT
            elif keys[pygame.K_d]:
                rect_pos[0] += SPEED_RECT

        if ball_pos[0] + RADIUS > WIN_SIZE[0]:
            speed_x_ball = -SPEED_X_BALL
        elif ball_pos[0] - RADIUS < 0:
            speed_x_ball = SPEED_X_BALL

        if ball_pos[1] + RADIUS > WIN_SIZE[1]:
            print("Game over")
            gameOver = True
        elif ball_pos[1] - RADIUS < 0:
            speed_y_ball = SPEED_Y_BALL

        if rect_pos[0] < 0:
            rect_pos[0] = 0
        elif rect_pos[0] + RECT_SIZE[0] > WIN_SIZE[0]:
            rect_pos[0] = WIN_SIZE[0] - RECT_SIZE[0]

        if (ball_pos[1] + RADIUS >= rect_pos[1]) and (
            ball_pos[0] + RADIUS >= rect_pos[0]
            and ball_pos[0] + RADIUS <= rect_pos[0] + 80
        ):
            speed_y_ball = -SPEED_Y_BALL

        screen.fill(BLACK)

        pygame.draw.rect(screen, WHITE, (tuple(rect_pos), RECT_SIZE))
        pygame.draw.circle(screen, WHITE, tuple(ball_pos), RADIUS)
        clock.tick(FPS)

        pygame.display.flip()


run_game()
