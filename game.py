import pygame
import sys

WIN_SIZE = (480, 500)
WIN_TITLE = "Ping pong"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RECT_SIZE = (80, 13)
SPEED = 25

rect_pos = [WIN_SIZE[0] / 2 - RECT_SIZE[0] / 2, WIN_SIZE[1] - RECT_SIZE[1] * 2]
gameOver = False


def run_game():
    pygame.init()

    screen = pygame.display.set_mode(WIN_SIZE)
    pygame.display.set_caption(WIN_TITLE)

    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rect_pos[0] += SPEED
                elif event.key == pygame.K_LEFT:
                    rect_pos[0] -= SPEED
  
        if rect_pos[0] < 0:
            rect_pos[0] = 0
        elif rect_pos[0] + RECT_SIZE[0] > WIN_SIZE[0]:
            rect_pos[0] = WIN_SIZE[0] - RECT_SIZE[0]

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (tuple(rect_pos), RECT_SIZE))

        pygame.display.update()


run_game()
