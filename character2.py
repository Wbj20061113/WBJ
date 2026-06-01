import pygame

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8  # 调高速度，移动更流畅
        self.color = (240, 80, 80)
        self.radius = 20

    def move(self, keys, park_map=None):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = self.speed

        self.x += dx
        self.y += dy

        # 边界限制，防止角色跑出窗口
        self.x = max(self.radius, min(800 - self.radius, self.x))
        self.y = max(self.radius, min(600 - self.radius, self.y))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
