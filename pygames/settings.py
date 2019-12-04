class Settings():
    """存储游戏所有的设置类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_heigth = 1200
        self.screen_width = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 0.3

        ##子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)

