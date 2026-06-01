# 四个项目小游戏实现
import pygame
import random

def lightcycle_game(screen):
    # 创极速光轮：左右躲避障碍
    clock = pygame.time.Clock()
    x = 380
    speed = 8
    obstacles = []
    timer = 0
    score = 0
    running = True
    font = pygame.font.Font(None, 32)
    while running:
        screen.fill((20,26,30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= speed*1.2
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += speed*1.2
        x = max(300, min(500, x))
        # 生成障碍
        timer += 1
        if timer % 15 == 0:
            obstacles.append([random.randint(300, 500), -50])
        # 障碍下落
        hit = False
        for ob in obstacles:
            ob[1] += speed
            if abs(ob[0]-x) < 30 and ob[1] > 350 and ob[1] < 400:
                hit = True
            pygame.draw.rect(screen, (40,255,255), (ob[0], ob[1], 32, 32))
        if hit:
            break
        pygame.draw.rect(screen, (0,255,0), (x, 380, 32, 50))
        txt = font.render("躲避障碍物！ 方向键←→", True, (240,255,255))
        screen.blit(txt, (320, 60))
        pygame.display.flip()
        if timer > 150:
            score = 30
            break
        clock.tick(40)
    return score

def minecar_game(screen):
    # 七个小矮人矿山车：按节奏按空格
    clock = pygame.time.Clock()
    points = 0
    font = pygame.font.Font(None, 32)
    bar_x = 340
    t = 0
    press_times = []
    targets = [random.randint(20, 240) for _ in range(5)]
    while t < 255:
        screen.fill((232, 210, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                press_times.append(t)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return 0
        pygame.draw.rect(screen, (140,120,40), (bar_x, 350, 220, 6))
        for aim in targets:
            pygame.draw.circle(screen, (250,56,56), (bar_x+aim, 353), 10)
        for pt in press_times:
            pygame.draw.rect(screen, (0,180,0), (bar_x+pt, 345, 6, 16))
        msg = font.render("空格跟节奏打点吧！", True, (60,0,0))
        screen.blit(msg, (bar_x, 300))
        pygame.display.flip()
        t += 5
        clock.tick(45)
    # 评分：按下的点离目标圆近的得分
    for aim in targets:
        nearest = min([abs(pt-aim) for pt in press_times] or [240])
        if nearest < 15:
            points += 7
        elif nearest < 30:
            points += 4
        elif nearest < 45:
            points += 2
    return points

def soar_game(screen):
    # 翱翔·飞越地平线：点击飞鸟
    clock = pygame.time.Clock()
    birds = [[random.randint(200,650), random.randint(200,400)] for _ in range(7)]
    catched = [False]*len(birds)
    font = pygame.font.Font(None, 32)
    timer = 0
    while timer < 350:
        screen.fill((170,210,235))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                for idx, pos in enumerate(birds):
                    if (mx-pos[0])**2+(my-pos[1])**2 < 27**2:
                        catched[idx]=True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return 0
        for idx, pos in enumerate(birds):
            if not catched[idx]:
                pygame.draw.circle(screen, (160,140,90), pos, 24)
        msg = font.render("用鼠标点中飞鸟", True, (40,40,120))
        screen.blit(msg, (340, 500))
        pygame.display.flip()
        timer += 1
        clock.tick(45)
    return sum(catched)*4

def chase_game(screen):
    # 热力追踪：按方向键追球
    clock = pygame.time.Clock()
    player = [600, 400]
    ball = [random.randint(200,600), random.randint(200,500)]
    speed = 7
    font = pygame.font.Font(None, 30)
    caught = False
    t = 0
    while t < 180 and not caught:
        screen.fill((220, 130, 130))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player[0] -= speed
        if keys[pygame.K_RIGHT]: player[0] += speed
        if keys[pygame.K_UP]: player[1] -= speed
        if keys[pygame.K_DOWN]: player[1] += speed
        player[0] = max(100, min(780, player[0]))
        player[1] = max(100, min(580, player[1]))
        # 判重叠
        if abs(player[0] - ball[0]) < 25 and abs(player[1] - ball[1]) < 25:
            caught = True
        pygame.draw.circle(screen, (240,240,240), ball, 22)
        pygame.draw.circle(screen, (50,50,200), player, 22)
        msg = font.render("追上圆球！（方向键）", True, (90,0,0))
        screen.blit(msg, (320, 150))
        pygame.display.flip()
        t += 1
        clock.tick(48)
    return 16 if caught else 2