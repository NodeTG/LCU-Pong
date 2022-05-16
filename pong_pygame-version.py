import pygame
import random

pygame.init()

WIDTH = 350
HEIGHT = 200
FPS = 15

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 40
BALL_RADIUS = 10

DOWN_HELD = False
UP_HELD = False

AI_DIFFICULTY = 65  # 0 - 100 | 100 is impossible, 0 means they do literally nothing.

paddle1_x = 0
paddle1_y = 20

paddle2_x = WIDTH - PADDLE_WIDTH
paddle2_y = HEIGHT - PADDLE_HEIGHT - 20

ball_x = 180
ball_y = 100

ball_x_vel = 10
ball_y_vel = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
execute = True
while True:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                exit()
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_DOWN:
                        DOWN_HELD = True
                    case pygame.K_UP:
                        UP_HELD = True
                    case pygame.K_SPACE:
                        execute = True
            case pygame.KEYUP:
                match event.key:
                    case pygame.K_DOWN:
                        DOWN_HELD = False
                    case pygame.K_UP:
                        UP_HELD = False

    if execute:
        # Player Paddle Movement
        if DOWN_HELD:
            paddle1_y += 20
            if paddle1_y + PADDLE_HEIGHT > HEIGHT:
                paddle1_y = HEIGHT - PADDLE_HEIGHT
        if UP_HELD:
            paddle1_y -= 20
            if paddle1_y < 0:
                paddle1_y = 0

        # Ball Collision
        if ball_x + ball_x_vel + BALL_RADIUS >= WIDTH:
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_x_vel *= -1
            ball_y_vel = 10
            print("Player score +1")
        elif ball_x + ball_x_vel < 0:
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_x_vel *= -1
            ball_y_vel = 10
            print("COM score +1")
        else:
            ball_x += ball_x_vel

        if ball_y + ball_y_vel + BALL_RADIUS >= HEIGHT:
            ball_y_vel *= -1
            ball_y = HEIGHT - BALL_RADIUS
        elif ball_y + ball_y_vel <= 0:
            ball_y_vel *= -1
            ball_y = 0 + BALL_RADIUS
        else:
            ball_y += ball_y_vel

        # Paddle Collision
        if ball_y + BALL_RADIUS >= paddle1_y and ball_y <= (paddle1_y + PADDLE_HEIGHT) and ball_x >= paddle1_x and ball_x <= paddle1_x + PADDLE_WIDTH:
            ball_x_vel *= -1
            ball_x = 0 + PADDLE_WIDTH
        elif ball_y + BALL_RADIUS >= paddle2_y and ball_y <= (paddle2_y + PADDLE_HEIGHT) and ball_x + BALL_RADIUS >= paddle2_x and ball_x <= paddle2_x + PADDLE_WIDTH:
            ball_x_vel *= -1
            ball_x = WIDTH - PADDLE_WIDTH - BALL_RADIUS
        
        # Computer Paddle Movement
        if random.randint(0,100) <= AI_DIFFICULTY:
            if ball_y > paddle2_y + PADDLE_HEIGHT - 10:
                paddle2_y += 20
                if paddle2_y + PADDLE_HEIGHT > HEIGHT:
                    paddle2_y = HEIGHT - PADDLE_HEIGHT
            elif ball_y < paddle2_y:
                paddle2_y -= 20
                if paddle2_y < 0:
                    paddle2_y = 0

        # Draw Objects to Screen
        for i in range(PADDLE_WIDTH):
            for j in range(PADDLE_HEIGHT):
                screen.set_at((paddle1_x + i, paddle1_y + j), (255,255,255))

        for i in range(PADDLE_WIDTH):
            for j in range(PADDLE_HEIGHT):
                screen.set_at((paddle2_x + i, paddle2_y + j), (255,255,255))

        for i in range(BALL_RADIUS):
            for j in range(BALL_RADIUS):
                screen.set_at((ball_x + i, ball_y + j), (255,255,255))

        pygame.display.flip()

        clock.tick(FPS)
        #execute = False