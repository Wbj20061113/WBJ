# UI 辅助函数和积分提示气泡
import pygame

def draw_ui(screen, font, score):
    pygame.draw.rect(screen, (30, 30, 60), (10, 10, 220, 46), border_radius=12)
    txt = font.render(f"积分 Score: {score}", True, (225,225,240))
    screen.blit(txt, (24, 23))

def show_message(screen, msg, font, pos_ratio=0.7):
    text = font.render(msg, True, (200,48,48))
    x = screen.get_width() // 2 - text.get_width() // 2
    y = int(screen.get_height() * pos_ratio)
    box = pygame.Surface((text.get_width()+32, 40), pygame.SRCALPHA)
    box.fill((250,250,255,220))
    pygame.draw.rect(box, (200, 80, 80,210), box.get_rect(), 2, border_radius=10)
    box.blit(text, (16, 10))
    screen.blit(box, (x-16, y))
    pygame.display.update()
    pygame.time.wait(1000)