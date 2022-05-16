import pygame
from network import Network
import json

pygame.init()

WIDTH = 350
HEIGHT = 200
FPS = 15

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 40
BALL_RADIUS = 10

paddle1_x = 0
paddle1_y = 20

paddle2_x = WIDTH - PADDLE_WIDTH
paddle2_y = 0

ball_x = 180
ball_y = 100

ball_x_vel = 0
ball_y_vel = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

net = Network()
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.K_ESCAPE:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        paddle1_y += 20
        if paddle1_y + PADDLE_HEIGHT > HEIGHT:
            paddle1_y = HEIGHT - PADDLE_HEIGHT
    
    if keys[pygame.K_UP]:
        paddle1_y -= 20
        if paddle1_y < 0:
            paddle1_y = 0
    
    data = {
        "id": net.id,
        "type": "POS_UPDATE",
        "pos": (paddle1_x, paddle1_y),
    }
    data = json.dumps(data)
    reply = net.send(data)

    try:
        d = json.loads(reply)
        if d["type"] == "POS_UPDATE":
            paddle2_x = WIDTH - PADDLE_WIDTH
            paddle2_y = d["pos"][1]
        else:
            print(f"Unknown message received!\n{d}")
    except Exception as e:
        print(e)
        paddle2_x, paddle2_y = 50,0

    
    
    screen.fill((0,0,0))

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