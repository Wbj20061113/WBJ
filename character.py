# 角色控制与绘制
import pygame

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.color = (240, 80, 80)
        self.radius = 20

    def move(self, keys, park_map):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = self.speed
        # 限制在地图内
        nx, ny = self.x + dx, self.y + dy
        if 100 <= nx <= 800 and 150 <= ny <= 600:
            self.x, self.y = nx, ny

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y - 10), 5) # 眼睛
        pygame.draw.circle(screen, (0,0,0), (self.x, self.y - 10), 2)