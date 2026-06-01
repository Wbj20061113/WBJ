import pygame
import random

# 1. 创极速光轮 - 躲避障碍
def lightcycle_game(screen):
    clock = pygame.time.Clock()
    score = 0
    player_x, player_y = 100, 300
    player_speed = 6
    obstacles = []
    game_running = True

    while game_running:
        screen.fill((20, 20, 60))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_y > 50:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < 550:
            player_y += player_speed

        # 生成障碍物
        if random.randint(0, 60) < 3:
            obstacles.append([800, random.randint(50, 550), 30, 30])

        # 移动障碍物并碰撞检测
        for obs in obstacles:
            obs[0] -= 5
            pygame.draw.rect(screen, (255, 100, 100), obs)
            if (player_x < obs[0] + obs[2] and player_x + 20 > obs[0] and
                player_y < obs[1] + obs[3] and player_y + 20 > obs[1]):
                game_running = False

        obstacles = [obs for obs in obstacles if obs[0] > -30]
        pygame.draw.circle(screen, (0, 190, 255), (player_x, player_y), 20)
        score += 1
        font = pygame.font.Font(None, 36)
        screen.blit(font.render(f"分数: {score}", True, (255,255,255)), (10,10))
        pygame.display.flip()
        clock.tick(60)
    return score

# 2. 七个小矮人矿山车 - 收集金币
def minecar_game(screen):
    clock = pygame.time.Clock()
    score = 0
    player_x, player_y = 400, 500
    player_speed = 7
    coins = []
    game_running = True

    while game_running:
        screen.fill((60, 40, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < 750:
            player_x += player_speed

        # 生成金币
        if random.randint(0, 40) < 3:
            coins.append([random.randint(50, 750), -20])

        # 移动金币并收集
        for coin in coins:
            coin[1] += 4
            pygame.draw.circle(screen, (255, 215, 0), coin, 15)
            if abs(player_x - coin[0]) < 30 and abs(player_y - coin[1]) < 30:
                coins.remove(coin)
                score += 10
            if coin[1] > 620:
                coins.remove(coin)

        pygame.draw.rect(screen, (230, 220, 80), (player_x-25, player_y-15, 50, 30))
        font = pygame.font.Font(None, 36)
        screen.blit(font.render(f"分数: {score}", True, (255,255,255)), (10,10))
        pygame.display.flip()
        clock.tick(6
