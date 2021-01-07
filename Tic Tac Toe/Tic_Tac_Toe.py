import pygame
pygame.init()

screen_width = 500
screen_height = 500
win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Tic Tac Toe")

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
