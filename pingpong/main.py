from pygame import *

window = display.set_mode((700,500))
display.set_caption('очень крутое название')
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (600,100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__(player_image, player_speed, player_x, player_y)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 410:
            self.rect.y += self.speed


class Player2(GameSprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__(player_image, player_speed, player_x, player_y)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 410:
            self.rect.y += self.speed


background = transform.scale(image.load('fon.jpg'), (700,500))

game = True
finish = False

player1 = Player("palka.png", 10, 345, 200)
player2 = Player2("palka.png", 10, -250, 200)


font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN!', True, (255,215,0))
lose = font.render("YOU LOSE!", True, (255,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        player1.reset()
        player1.update()

        player2.reset()
        player2.update()

    clock.tick(FPS)
    display.update()
