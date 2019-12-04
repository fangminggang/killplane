import sys
import pygame
from pygames.bullet import Bullet


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键下压"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    #按下空格键，把新的子弹放入编组中
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """响应按键弹起"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    """响应鼠标和键盘事件"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        #按键弹起
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)




def update_screen(ai_settings,screen,ship):
    """更新屏幕图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #让最近会自动屏幕可见
    pygame.display.flip()

