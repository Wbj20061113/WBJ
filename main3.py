import pygame
from game import DisneyParkGame
from dashboard import Dashboard

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("迪士尼游乐设施模拟器")

    # 初始化游戏和仪表盘
    game = DisneyParkGame(screen)
    dashboard = Dashboard(screen, game)

    while True:
        # 运行游戏逻辑
        game.run_frame()
        # 绘制仪表盘
        dashboard.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()
