import pygame
from minigames import lightcycle_game, minecar_game, soar_game, chase_game

# 项目配置列表
projects = [
    {"name": "创极速光轮", "pos": (150, 200), "color": (0, 190, 255), "minigame": lightcycle_game},
    {"name": "七个小矮人矿山车", "pos": (700, 200), "color": (230, 220, 80), "minigame": minecar_game},
    {"name": "翱翔·飞越地平线", "pos": (700, 550), "color": (120, 200, 255), "minigame": soar_game},
    {"name": "热力追踪", "pos": (150, 550), "color": (255, 120, 120), "minigame": chase_game}
]

def launch_project_minigame(screen, project):
    # 黑幕淡入效果
    for alpha in range(0, 180, 12):
        overlay = pygame.Surface(screen.get_size())
        overlay.set_alpha(alpha)
        overlay.fill((30, 30, 30))
        screen.blit(overlay, (0, 0))
        pygame.display.flip()
        pygame.time.wait(8)

    # 启动小游戏
    points = project["minigame"](screen)
    return points
