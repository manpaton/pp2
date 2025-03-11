import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Red Ball")

BALL_RADIUS = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
BALL_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
MOVE_STEP = 20

running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - BALL_RADIUS - MOVE_STEP >= 0:
                ball_y -= MOVE_STEP
            elif event.key == pygame.K_DOWN and ball_y + BALL_RADIUS + MOVE_STEP <= HEIGHT:
                ball_y += MOVE_STEP
            elif event.key == pygame.K_LEFT and ball_x - BALL_RADIUS - MOVE_STEP >= 0:
                ball_x -= MOVE_STEP
            elif event.key == pygame.K_RIGHT and ball_x + BALL_RADIUS + MOVE_STEP <= WIDTH:
                ball_x += MOVE_STEP

pygame.quit()