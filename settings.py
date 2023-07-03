class Settings():
    """存储《《外星人之战》》的所有设置的类"""

    def __init__(self):
        """初始化游戏里的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)
        self.speed = 0.5
        self.bullet_speed = 0.2
        self.bullet_width = 15
        self.bullet_height = 25
        self.bullet_color = (0,255,0)
        self.bullet_allowed = 5
        self.alien_speed = 0.1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        self.ship_speed = 0.5
        self.bullet_speed = 0.2
        self.alien_speed = 0.1
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
