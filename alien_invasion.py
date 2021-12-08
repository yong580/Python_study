import sys
import pygame
from setting import Settings
from ship import Ship
import game_function as gf
def run_game():
    #初始化游戏创建个屏幕对象
    pygame.init()
    alien_setting  = Settings()
    # 窗口也是一个对象
    screen=pygame.display.set_mode((alien_setting.width,alien_setting.height))
    pygame.display.set_caption("Alien Invasion")
    bg_color=alien_setting.bg_color
    # 此处只是创建一个对象
    ship = Ship(screen)
#游戏主循环，包括监测事件和更新屏幕
    while True:
    #更新屏幕显示
        gf.check_events(ship)
        ship.update()
        gf.update_screen(alien_setting, screen,ship)
        print("hello")
run_game()
