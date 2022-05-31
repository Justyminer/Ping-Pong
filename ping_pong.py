from random import randint
from pygame import *
font.init()
window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
gradient = transform.scale(image.load('gradient.png'),(700, 500))
font0 = font.Font(None,23)

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
        if keys_pressed[K_s] and self.rect.y <390:
            self.rect.y += self.speed
    def updater(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 390:
            self.rect.y += self.speed
ball = GameSprite('G.png',10,255,255)
rocket = Player('gradient.png',10,5,300, 20,110)
rocket1 = Player('gradient.png',10,675,300,20,110)

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(gradient,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y <0 or ball.rect.y > 440:
            speed_y *= -1
        if sprite.collide_rect(rocket,ball) or sprite.collide_rect(rocket1,ball):
            speed_x *= -1

        if ball.rect.x >= 640 :
            finish = True
            los = font0.render('1LOSE',True,(255, 215, 0))
            window.blit(los,(350,350))
            
        if ball.rect.x <= 0:
            finish = True
            los = font0.render('2LOSE',True,(255, 215, 0))
            window.blit(los,(350,350))
        ball.reset()
        ball.update()
        rocket.reset()
        rocket1.reset()
        rocket.updatel()
        rocket1.updater()
        
       
       
    display.update()
    time.delay(50)
