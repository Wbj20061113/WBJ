import pygame
from projects import projects

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # 地图路径
        self.paths = [
            ((150, 200), (700, 200)),
            ((150, 200), (150, 550)),
            ((700, 200), (700, 550)),
            ((150, 550), (700, 550)),
            ((400, 200), (400, 550)),
        ]

    def draw(self, screen):
        # 画路径
        for a, b in self.paths:
            pygame.draw.line(screen, (180, 180, 180), a, b, 3)
        # 画项目点
        for p in projects:
            pygame.draw.circle(screen, p['color'], p['pos'], 20)
            font = pygame.font.Font(None, 24)
            text = font.render(p['name'], True, (255, 255, 255))
            text_rect = text.get_rect(center=(p['pos'][0], p['pos'][1] + 35))
            screen.blit(text, text_rect)
