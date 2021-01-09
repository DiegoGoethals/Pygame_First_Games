import pygame
pygame.init()

screen_width = 500
screen_height = 480
win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Tutorial")

bg = pygame.image.load('Images/background/bg.jpg')

clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.shootLoop = 0

    def draw(self, win):
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
        char = pygame.image.load('Images/Player/standing.png')

        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.shootLoop == 0:
            if self.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 5:
                bullets.append(Projectile(round(self.x + self.width // 2), round(self.y + self.height // 2), 6, (0, 0, 0), facing))

            self.shootLoop = 1

        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
            self.standing = False
        elif keys[pygame.K_RIGHT] and self.x < 500 - self.width:
            self.x += self.vel
            self.left = False
            self.right = True
            self.standing = False
        else:
            self.standing = True
            self.walkCount = 0
        if not self.isJump:
            # jump mechanic
            if keys[pygame.K_UP]:
                self.isJump = True
        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10


class Projectile:

    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Enemy:
    walkRight = [pygame.image.load('Images/Enemies/R1E.png'), pygame.image.load('Images/Enemies/R2E.png'),
                 pygame.image.load('Images/Enemies/R3E.png'), pygame.image.load('Images/Enemies/R4E.png'),
                 pygame.image.load('Images/Enemies/R5E.png'), pygame.image.load('Images/Enemies/R6E.png'),
                 pygame.image.load('Images/Enemies/R7E.png'), pygame.image.load('Images/Enemies/R8E.png'),
                 pygame.image.load('Images/Enemies/R9E.png'), pygame.image.load('Images/Enemies/R10E.png'),
                 pygame.image.load('Images/Enemies/R11E.png')]
    walkLeft = [pygame.image.load('Images/Enemies/L1E.png'), pygame.image.load('Images/Enemies/L2E.png'),
                pygame.image.load('Images/Enemies/L3E.png'), pygame.image.load('Images/Enemies/L4E.png'),
                pygame.image.load('Images/Enemies/L5E.png'), pygame.image.load('Images/Enemies/L6E.png'),
                pygame.image.load('Images/Enemies/L7E.png'), pygame.image.load('Images/Enemies/L8E.png'),
                pygame.image.load('Images/Enemies/L9E.png'), pygame.image.load('Images/Enemies/L10E.png'),
                pygame.image.load('Images/Enemies/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0

    def hit(self):
        print('hit')
        pass


def redraw_game_window():
    win.blit(bg, (0, 0))
    player.draw(win)
    enemy.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# mainloop
player = Player(0, screen_height - 64, 64, 64)
enemy = Enemy(100, screen_height - 64, 64, 64, 400)
bullets = []
run = True
while run:
    clock.tick(27)

    if player.shootLoop > 0:
        player.shootLoop += 1
    if player.shootLoop > 3:
        player.shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
            if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                enemy.hit()
                bullets.pop(bullets.index(bullet))
        if screen_width > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    player.move()

    redraw_game_window()

pygame.quit()
