import pygame

pygame.init()

WIDTH = 350
HEIGHT = 200
FPS = 30

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 40
BALL_RADIUS = 10

DOWN_HELD = False
UP_HELD = False

paddle1_x = 0
paddle1_y = 20

paddle2_x = WIDTH - PADDLE_WIDTH
paddle2_y = HEIGHT - PADDLE_HEIGHT - 20

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

ball_x_vel = 4
ball_y_vel = 4

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

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
            case pygame.KEYUP:
                match event.key:
                    case pygame.K_DOWN:
                        DOWN_HELD = False
                    case pygame.K_UP:
                        UP_HELD = False

    # Player Paddle Movement
    if DOWN_HELD:
        paddle1_y += 4
    if UP_HELD:
        paddle1_y -= 4

    # Ball Collision
    if ball_x + ball_x_vel + BALL_RADIUS >= WIDTH:
        ball_x_vel *= -1
        ball_x = WIDTH - BALL_RADIUS
        print("Player score +1")
    elif ball_x + ball_x_vel <= 0:
        ball_x_vel *= -1
        ball_x = 0 + BALL_RADIUS
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
    
    # Computer Paddle Movement
    if ball_y > paddle2_y:
        paddle2_y += 4
    elif ball_y < paddle2_y:
        paddle2_y -= 4

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