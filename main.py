
from pygame import *
from random import randint

window = display.set_mode((1000,600))
display.set_caption('ping pong')
clock = time.Clock()
fps = 80
background = transform.scale(image.load('fone.jpg'),(1000,600))

class GameSprite(sprite.Sprite):
    def __init__(self,rx,ry,player_image,x,y):
        super().__init__()
        self.rx = rx
        self.ry = ry
        self.player_image = player_image
        self.image = transform.scale(image.load(player_image),(rx,ry))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self,rx,ry,player_image,x,y):
        super().__init__(rx,ry,player_image,x,y)
    def move(self,code):
        if code == 'up':
            if self.rect.y > 0:
                self.rect.y -= 4
        if code == 'dw':
            if self.rect.y < 530:
                self.rect.y += 4

rocket_1 = Player(25,200,'rocket.png',100,150)
rocket_2 = Player(25,200,'rocket.png',900,150)
ball = GameSprite(25,25,'ball.png',425,275)
speed_x = 5
speed_y = 5

font.init()
font = font.SysFont('Arial',100)
lost = font.render('Поражение',True,(255,124,124))

game = True
finish = False

while game:
    if not finish:
        window.blit(background,(0,0))
        rocket_1.reset()
        rocket_2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y <= 0 or ball.rect.y >= 575:
            speed_y *= -1
        
        if sprite.collide_rect(rocket_1,ball) or sprite.collide_rect(rocket_2,ball):
            speed_x *= -1

        for e in event.get():
            if e.type == QUIT:
                game = False
        
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w]:
            if rocket_1.rect.y > 0:
                rocket_1.move('up')
        if keys_pressed[K_s]:
            if rocket_1.rect.y < 400:
                rocket_1.move('dw')

        if keys_pressed[K_e]:
            if rocket_2.rect.y > 0:
                rocket_2.move('up')
        if keys_pressed[K_d]:
            if rocket_2.rect.y < 400:
                rocket_2.move('dw')

        if ball.rect.x <= -25 or ball.rect.x >= 1025:   
            finish = True


    if finish:
       window.blit(lost,(200,250))

       for e in event.get():
            if e.type == QUIT:
                game = False

    display.update()
    clock.tick(fps)