# 上海迪士尼游玩模拟游戏主入口
import pygame
import sys
from map import Map
from character import Character
from projects import projects, launch_project_minigame
from ui import draw_ui, show_message

pygame.init()
WIDTH, HEIGHT = 900, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("上海迪士尼游玩模拟游戏")
clock = pygame.time.Clock()

# 初始化地图和角色
park_map = Map(WIDTH, HEIGHT)
player = Character(park_map.start_x, park_map.start_y)

score = 0
current_message = ""
font = pygame.font.Font(None, 32)
project_in_range = None
bgm = pygame.mixer.Sound("resources/bgm.ogg")
bgm.play(-1)

while True:
    screen.fill((220, 240, 250))
    park_map.draw(screen)
    project_in_range = None

    # 检查是否靠近项目
    for project in projects:
        px, py = project['pos']
        if abs(player.x - px) < 40 and abs(player.y - py) < 40:
            project_in_range = project
            break

    # 事件响应
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(), sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(), sys.exit()
            elif event.key == pygame.K_SPACE and project_in_range:
                # 启动小游戏
                points = launch_project_minigame(screen, project_in_range)
                if points > 0:
                    show_message(screen, f"{project_in_range['name']} 完成！+{points}分", font)
                score += points

    # 角色移动
    keys = pygame.key.get_pressed()
    player.move(keys, park_map)

    # 绘制角色和UI
    player.draw(screen)
    draw_ui(screen, font, score)
    if project_in_range:
        msg = f"按空格体验“{project_in_range['name']}”"
        show_message(screen, msg, font, 0.85)
    pygame.display.flip()
    clock.tick(60)
    