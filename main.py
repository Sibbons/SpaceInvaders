import pygame
import random
import math

# initialize pygame
pygame.init()


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
        self.bad = True

    def setImage(self):
        imgstr = ''
        if self.bad:
            imgstr = './images/redAlien.png'
        else:
            imgstr = './images/greenAlien.png'
        self.img = pygame.image.load(imgstr)


class Bullet(MainParent):
    def __init__(self, x, y, x_change, y_change, imgStr):
        super().__init__(x, y, x_change, y_change, imgStr)
        self.bullet_State = 'ready'

    def reset(self):
        self.bullet_State = "ready"
        self.y = 480

    def bullBoundaries(self):
        if self.y <= -40:
            self.reset()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

ship = SpaceShip(370, 480, 0, 0, './images/spaceShip.png')
enemies = []
# enemy = Alien(50, random.randint(50, 200), 2, 20, './images/redAlien.png')
bullet = Bullet(ship.x, 480, 0, 5, './images/bullet.png')

for i in range(3):
    enemy = Alien(random.randint(10, 550), random.randint(50, 200), random.randint(4, 4), random.randint(5, 15),
                  './images/redAlien.png')
    enemies.append(enemy)
    print(f'{i}, x = {enemy.x},y = {enemy.y}')
# Background
background = pygame.image.load("./images/spaceBackground.png")
gameOver = pygame.image.load('./images/gameOver.jpg')
running = True
win = False
score = 0


def isCollision(alien, missel):
    distance = math.sqrt((math.pow(alien.x - missel.x, 2)) + (math.pow(alien.y - missel.y, 2)))
    return distance < 27


def allGreen(aliens):
    for alien in aliens:
        if alien.bad:
            return False
    return True


while running and not win:
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
    ship.boundaries(1, 0)
    bullet.bullBoundaries()

    # Collision
    for enemy in enemies:
        collision = isCollision(enemy, bullet)
        if collision:
            bullet.reset()
            score += enemy.bad
            enemy.y = random.randint(200, 400)
            enemy.bad = not enemy.bad
            enemy.setImage()
            print(score)
        enemy.move(enemy.x_change, 0)
        enemy.draw(enemy.x, enemy.y)
        enemy.boundaries(-1, enemy.y_change)

        if enemy.y >= 420 and not enemy.bad:
            win = not enemy.bad
            enemy.y = 1000
        elif enemy.y >= 420 and enemy.bad:
            running = False
    win = allGreen(enemies)
    if bullet.bullet_State == 'fire':
        bullet.draw(bullet.x, bullet.y)
        bullet.y -= bullet.y_change

    ship.draw(ship.x, ship.y)

    pygame.display.update()  # update screen
if not win:
    screen.blit(gameOver, (0, 0))
    pygame.display.update()
