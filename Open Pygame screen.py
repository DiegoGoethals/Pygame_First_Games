import pygame
pygame.init()

screen_width = 500
screen_height = 500

win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game Name")

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
