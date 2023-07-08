import pygame
import sys

WIN_SIZE = (480, 500)
WIN_TITLE = "Ping pong"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RECT_SIZE = (80, 13)
RADIUS = 10
SPEED_RECT = 25
FPS = 60

rect_pos = [WIN_SIZE[0] / 2 - RECT_SIZE[0] / 2, WIN_SIZE[1] - RECT_SIZE[1] * 2]
ball_pos = [WIN_SIZE[0] / 2 + RADIUS / 2, WIN_SIZE[1] / 2 - RADIUS * 2]

gameOver = False


def run_game():
    pygame.init()
    speed_x_ball = 3
    speed_y_ball = 3

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
            speed_x_ball = -3
        elif ball_pos[0] - RADIUS < 0:
            speed_x_ball = 3

        if ball_pos[1] + RADIUS > WIN_SIZE[1]:
            speed_y_ball = -3
        elif ball_pos[1] - RADIUS < 0:
            speed_y_ball = 3

        if rect_pos[0] < 0:
            rect_pos[0] = 0
        elif rect_pos[0] + RECT_SIZE[0] > WIN_SIZE[0]:
            rect_pos[0] = WIN_SIZE[0] - RECT_SIZE[0]

        screen.fill(BLACK)

        pygame.draw.rect(screen, WHITE, (tuple(rect_pos), RECT_SIZE))
        pygame.draw.circle(screen, WHITE, tuple(ball_pos), RADIUS)
        clock.tick(FPS)

        pygame.display.flip()


run_game()
