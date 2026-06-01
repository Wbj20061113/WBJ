import pygame

def draw_ui(screen, font, score):
    score_text = font.render(f"总分: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def show_message(screen, text, font, duration):
    msg_surf = font.render(text, True, (255, 255, 255))
    msg_rect = msg_surf.get_rect(center=(400, 300))
    screen.blit(msg_surf, msg_rect)
    pygame.display.flip()
    pygame.time.wait(int(duration * 1000))
