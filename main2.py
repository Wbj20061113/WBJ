import pygame
import sys
from character import Character
from map import Map
from projects import projects, launch_project_minigame
from ui import draw_ui, show_message

# 初始化
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("迪士尼小游戏合集")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# 初始化游戏对象
player = Character(150, 200)
game_map = Map(WIDTH, HEIGHT)
score = 0
project_in_range = None

# 主游戏循环
running = True
while running:
    clock.tick(60)  # 60帧，流畅运行

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE and project_in_range:
                # 启动小游戏
                points = launch_project_minigame(screen, project_in_range)
                if points > 0:
                    show_message(screen, f"{project_in_range['name']} 完成！+{points}分", font, 0.85)
                    score += points

    # 角色移动
    keys = pygame.key.get_pressed()
    player.move(keys, game_map)

    # 检测是否靠近项目点
    project_in_range = None
    for project in projects:
        if abs(player.x - project['pos'][0]) < 40 and abs(player.y - project['pos'][1]) < 40:
            project_in_range = project
            break

    # 绘制画面
    screen.fill((30, 30, 30))
    game_map.draw(screen)
    player.draw(screen)
    draw_ui(screen, font, score)

    # 显示提示文字
    if project_in_range:
        msg = f"按空格体验{project_in_range['name']}"
        show_surf = font.render(msg, True, (255, 255, 255))
        screen.blit(show_surf, (250, 550))

    pygame.display.flip()

pygame.quit()
sys.exit()
