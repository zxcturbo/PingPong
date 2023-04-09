from pygame import *

window = display.set_mode((700,500))
display.set_caption('очень крутое название')
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60,60))
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
        if keys_pressed[K_LEFT] and self.rect.x > 3:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        clock.tick(FPS)
        display.update()