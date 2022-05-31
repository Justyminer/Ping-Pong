from random import randint
from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
gradient = transform.scale(image.load('gradient.png'),(700, 500))
lost = 0
speed_x = 10
speed_y = 10
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_speed,player_x,player_y,width = 60,heigh = 60):
        super().__init__()
        self.image =  transform.scale(image.load(player_image),(width,heigh))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def updatel(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 699:
            self.rect.y += self.speed
    def updater(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 700:
            self.rect.y += self.speed
ball = GameSprite('G.png',10,255,255)
rocket = Player('gradient.png',10,5,300, 20,110)
rocket1 = Player('gradient.png',10,505,300,20,110)
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y <0 or ball.rect.x > 600:
            speed_y =- 1
    



        window.blit(gradient,(0,0))
        ball.reset()
        ball.update()
        rocket.reset()
        rocket1.reset()
        rocket.updatel()
        rocket1.updater()
       
       
    display.update()
    time.delay(50)