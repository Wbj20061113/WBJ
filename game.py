import pygame
import math

class DisneyParkGame:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        # 设施状态
        self.facility = 0  # 0:过山车 1:旋转木马
        self.running = False
        
        # 过山车数据
        self.car_x = 100
        self.car_y = 320
        
        # 旋转木马数据
        self.center = (400, 280)
        self.angle = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.running = not self.running
                if event.key == pygame.K_LEFT:
                    self.facility = 0
                    self.running = False
                if event.key == pygame.K_RIGHT:
                    self.facility = 1
                    self.running = False

    def update(self):
        if self.running:
            if self.facility == 0:
                # 过山车移动
                self.car_x += 3
                if self.car_x > 700:
                    self.car_x = 80
            else:
                # 旋转木马转动
                self.angle += 2

    def draw(self):
        self.screen.fill((130, 200, 255))  # 蓝天背景

        if self.facility == 0:
            # 过山车轨道和车厢
            pygame.draw.arc(self.screen, (80, 40, 20), (80, 250, 620, 180), 3.14, 0, 6)
            pygame.draw.rect(self.screen, (180, 30, 30), (self.car_x, self.car_y, 35, 22))
        else:
            # 旋转木马底座和木马
            cx, cy = self.center
            pygame.draw.circle(self.screen, (139, 90, 43), (cx, cy), 110, 5)
            for i in range(4):
                rad = math.radians(self.angle + i * 90)
                x = cx + math.cos(rad) * 75
                y = cy + math.sin(rad) * 75
                pygame.draw.line(self.screen, (60, 30, 20), (cx, cy), (x, y), 3)
                pygame.draw.ellipse(self.screen, (255, 60, 120), (x-15, y-18, 30, 36))

    def run_frame(self):
        self.handle_events()
        self.update()
        self.draw()
        pygame.display.flip()
        self.clock.tick(self.fps)
