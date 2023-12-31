class GameStats:

    def __init__(self,ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        # 游戏启动是处于非活动状态
        self.game_active = False

    def reset_stats(self):
        """初始化在游戏运行的时候变化的统计信息"""
        self.ship_left = self.settings.ship_limit