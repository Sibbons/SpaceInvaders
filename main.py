import pygame
import random
import math

# initialize pygame
pygame.init()


# starting window width, height

class mainParent:
    def __init__(self, x, y, x_change, y_change, imgStr):
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change
        self.img = pygame.image.load(imgStr)

    def draw(self, x, y):
        screen.blit(self.img, (self.x, self.y))





screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
player_img = pygame.image.load('spaceShip.png')

player_X = 370
player_Y = 480
playerX_change = 0
playerY_change = 0



enemy_img = pygame.image.load('redAlien.png')
enemy_X = random.randint(0, 735)
enemy_Y = random.randint(50, 150)
enemyX_change = 2
enemyY_change = 20

bullet_img = pygame.image.load("bullet.png")
bullet_X = 0
bullet_Y = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

score = 0
# Background
background = pygame.image.load("spaceBackground.png")


def player(x, y):
    screen.blit(player_img, (x, y))  # draws image onto window


def enemy(x, y):
    screen.blit(enemy_img, (x, y))  # draws image onto window


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def isCollide(enemX, enemY, bullX, bullY):
    distance = math.sqrt((math.pow(enemX - bullX, 2)) + (math.pow(enemY - bullY, 2)))
    return distance < 27


running = True

while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
            if event.key == pygame.K_SPACE and bullet_state != "fire":
                bullet_X = player_X  # gets current pos of x so bullet doesnt follow ship
                fire_bullet(bullet_X, bullet_Y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    player_X += playerX_change
    if player_X <= 0:
        player_X = 0
    elif player_X >= 736:
        player_X = 736

    enemy_X += enemyX_change
    if enemy_X <= 0:
        enemyX_change = 2
        enemy_Y += enemyY_change
    elif enemy_X >= 736:
        enemyX_change = -2
        enemy_Y += enemyY_change

    if bullet_Y <= -40:
        bullet_Y = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_X, bullet_Y)
        bullet_Y -= bulletY_change

    #collision
    collision = isCollide(enemy_X, enemy_Y, bullet_X, bullet_Y)
    if collision:
        bullet_state = "ready"
        bullet_Y = 480
        score += 1
        print(score)
        enemy_X = random.randint(0, 735)
        enemy_Y = random.randint(50, 150)


    player(player_X, player_Y)
    enemy(enemy_X, enemy_Y)
    pygame.display.update()  # update screen


quit()
