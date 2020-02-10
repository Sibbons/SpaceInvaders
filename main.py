import pygame
import random
import math

# initialize pygame
pygame.init()


# starting window width, height

class MainParent:
    def __init__(self, x, y, x_change, y_change, imgStr):
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change
        self.img = pygame.image.load(imgStr)

    def draw(self, x, y):
        screen.blit(self.img, (self.x, self.y))

    def move(self, x_change, y_change):
        self.x += x_change
        self.y += y_change

    def boundaries(self, xChng, yChng):
        if self.x <= 0 or self.x >= 736:
            self.x = ((self.x >= 736) * 736)
            self.x_change *= xChng
            self.y += yChng


class SpaceShip(MainParent):
    def __init__(self, x, y, x_change, y_change, imgStr):
        super().__init__(x, y, x_change, y_change, imgStr)


class Alien(MainParent):
    def __init__(self, x, y, x_change, y_change, imgStr):
        super().__init__(x, y, x_change, y_change, imgStr)


class Bullet(MainParent):
    def __init__(self, x, y, x_change, y_change, imgStr):
        super().__init__(x, y, x_change, y_change, imgStr)
        self.bullet_State = 'ready'

    def reset(self):
        self.bullet_State = "ready"
        self.y = 480

    def bullBoundaries(self):
        if self.y<= -40:
            self.reset()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

ship = SpaceShip(370, 480, 0, 0, 'spaceShip.png')
enemy = Alien(100, 100, 2, 20, 'redAlien.png')
bullet = Bullet(ship.x, 480, 0, 5, 'bullet.png')

# Background
background = pygame.image.load("spaceBackground.png")

running = True

while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.x_change = -1.6
            if event.key == pygame.K_RIGHT:
                ship.x_change = 1.5
            if event.key == pygame.K_SPACE and bullet.bullet_State != 'fire':
                bullet.x = ship.x
                bullet.bullet_State = 'fire'
                bullet.draw(bullet.x, bullet.y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ship.x_change = 0

    ship.move(ship.x_change, ship.y_change)
    enemy.move(enemy.x_change, 0)

    ship.boundaries(1, 0)
    enemy.boundaries(-1, enemy.y_change)

    bullet.bullBoundaries()
    if bullet.bullet_State == 'fire':
        bullet.draw(bullet.x, bullet.y)
        bullet.y -= bullet.y_change

    ship.draw(ship.x, ship.y)
    enemy.draw(enemy.x, enemy.y)

    pygame.display.update()  # update screen

quit()
