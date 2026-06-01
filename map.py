# 地图和项目点位
import pygame
from projects import projects

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # 项目布局点位
        self.paths = [
            ((150, 200), (700, 200)),
            ((150, 200), (150, 550)),
            ((700, 200), (700, 550)),
            ((150, 550), (700, 550)),
            ((400, 200), (400, 550)), # 中轴
            ]
        self.start_x = 120
        self.start_y = 180

    def draw(self, screen):
        # 画路径
        for a, b in self.paths:
            pygame.draw.line(screen, (180, 180, 140), a, b, 14)
        # 画项目点
        for p in projects:
            pygame.draw.circle(screen, p['color'], p['pos'], 28)
            font = pygame.font.Font(None, 28)
            text = font.render(p['name'], True, (0, 32, 90))
            screen.blit(text, (p['pos'][0] - text.get_width()//2, p['pos'][1]-40))