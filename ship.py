import pygame
class Ship():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("image/ship.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        # 将新的飞船放在底部中间
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.moving_right=False
        self.moving_left=False
    def update(self):
        if self.moving_right:
            self.rect.centerx+= 1
        if self.moving_left:
            self.rect.centerx-= 1
    # 在指定位置绘制飞船
    def blitme(self):
        self.screen.blit(self.image,self.rect)


