import pygame

class Dashboard:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.font = pygame.font.Font(None, 32)

    def draw(self):
        # 显示设施名称
        facility_name = "过山车" if self.game.facility == 0 else "旋转木马"
        name_text = self.font.render(f"当前设施: {facility_name}", True, (0, 0, 0))
        self.screen.blit(name_text, (10, 10))

        # 显示运行状态
        status = "运行中" if self.game.running else "已停止"
        status_text = self.font.render(f"状态: {status}", True, (0, 0, 0))
        self.screen.blit(status_text, (10, 45))

        # 操作提示
        tip_text = self.font.render("←/→切换设施 | 空格启停", True, (0, 0, 0))
        self.screen.blit(tip_text, (10, 80))
