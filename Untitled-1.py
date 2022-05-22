from pygame import *
from time import time as timer
from random import randint
mixer.init()
font.init()

height = 750
width = 1000
window = display.set_mode((width,height))
display.set_caption('DON`T SKIP LOG')
background = transform.scale(image.load('forest.jpg'),(width,height))


game = True
finish = False

score_1 = 0
score_2 = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, height, width, direction):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.player_speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.height = height
        self.width = width
        self.direction = direction
    def update(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class P1(GameSprite):
    def walk(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.player_speed
        if keys[K_s] and self.rect.y < 600:
            self.rect.y += self.player_speed
        
class P2(GameSprite):
    def walk(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.player_speed
        if keys[K_DOWN] and self.rect.y < 600:
            self.rect.y += self.player_speed

class B(GameSprite):
    pass

bobr_1 = P1('bobr.png', 1, 250, 10, 150, 100, 1)
bobr_2 = P2('bobr_2.png', 900, 250, 10, 150, 100, 1)

while game:
    
    for e in event.get():
            if e.type == QUIT:
                game = False
            elif e.type == KEYDOWN:
                pass
    if finish != True:
        window.blit(background,(0,0))
        bobr_1.update()
        bobr_1.walk()
        bobr_2.update()
        bobr_2.walk()



    clock = time.Clock()
    FPS = 60
    clock.tick(FPS)
    display.update()





