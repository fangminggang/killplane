import pygame
from pygame.sprite import  Group
import sys
from pygames.settings import Settings
from pygames.ship import Ship
from pygames import game_functions as gf


def run_game():
    ai_settings = Settings()
    #初始化游戏并创建一个屏幕对象
    pygame.init()

    screen = pygame.display.set_mode((ai_settings.screen_heigth,ai_settings.screen_width))
    #screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('killplane')
    #bg_color = (230,230,230)
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets=Group()

    #开始游戏主循环
    while True:
        #监听键盘和鼠标事件
        # for event in pygame.event.get():
        #     #监听是否为退出游戏操作
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)

        # #每次循环时都重绘屏幕
        # #screen.fill(bg_color)
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # #让最近绘制的屏幕可见,刷新屏幕
        # pygame.display.flip()

run_game()