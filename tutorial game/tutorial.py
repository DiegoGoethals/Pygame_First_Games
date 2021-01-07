import pygame
pygame.init()

screen_width = 500
screen_height = 480
win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Tic Tac Toe")

walkRight = [pygame.image.load('Images/Player/R1.png'), pygame.image.load('Images/Player/R2.png'),
             pygame.image.load('Images/Player/R3.png'), pygame.image.load('Images/Player/R4.png'),
             pygame.image.load('Images/Player/R5.png'), pygame.image.load('Images/Player/R6.png'),
             pygame.image.load('Images/Player/R7.png'), pygame.image.load('Images/Player/R8.png'),
             pygame.image.load('Images/Player/R9.png')]
walkLeft = [pygame.image.load('Images/Player/L1.png'), pygame.image.load('Images/Player/L2.png'),
            pygame.image.load('Images/Player/L3.png'), pygame.image.load('Images/Player/L4.png'),
            pygame.image.load('Images/Player/L5.png'), pygame.image.load('Images/Player/L6.png'),
            pygame.image.load('Images/Player/L7.png'), pygame.image.load('Images/Player/L8.png'),
            pygame.image.load('Images/Player/L9.png')]
bg = pygame.image.load('Images/background/bg.jpg')
char = pygame.image.load('Images/Player/standing.png')

clock = pygame.time.Clock()

x = 0
y = 416
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0


def redraw_game_window():
    global walkCount
    win.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
    pygame.display.update()


# mainloop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0
    if not isJump:
        # jump mechanic
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redraw_game_window()

pygame.quit()
