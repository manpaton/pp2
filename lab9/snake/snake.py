import pygame
import time
import random

pygame.init()
#sizes
WIDTH, HEIGHT = 800, 600 
BLOCK_SIZE = 20  
INITIAL_SPEED = 10
SCORE = 0

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)

#creating window for game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

#font
font = pygame.font.SysFont("bahnschrift", 25) 
score_font = pygame.font.SysFont("bahnschrift", 25)

# adding images for game
background = pygame.image.load("snake_fon.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT)) 
apple = pygame.image.load("apple.png")
apple = pygame.transform.scale(apple, (BLOCK_SIZE, BLOCK_SIZE))

# Food types with different weights
food_types = [
    {"image": "apple.png", "points": 1, "time": 5000},  # Обычное яблоко, исчезает через 5 сек
    {"image": "golden_apple.png", "points": 3, "time": 7000},  # Золотое яблоко, исчезает через 7 сек
    {"image": "berry.png", "points": 2, "time": 6000}  # Ягода, исчезает через 6 сек
]

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, RED, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def draw_score(level):
    score_surface = score_font.render(f"Score: {SCORE}  Level: {level}", True, BLACK, WHITE)
    screen.blit(score_surface, (10, 10))

def spawn_food():
    food = random.choice(food_types)  # Выбираем случайный тип еды
    food_x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    food_y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    food_image = pygame.image.load(food["image"])
    food_image = pygame.transform.scale(food_image, (BLOCK_SIZE, BLOCK_SIZE))
    return food_x, food_y, food_image, food["points"], food["time"], pygame.time.get_ticks()

#game loop
def game_loop():
    global SCORE
    game_over = False
    game_close = False
    
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    
    snake_list = []
    length = 1
    speed = INITIAL_SPEED
    level = 1
    
    food_x, food_y, food_image, food_points, food_time, food_spawn_time = spawn_food()
    
    while not game_over:
        while game_close:
            screen.fill(BLACK)
            message = font.render(f"Game Over! Level: {level} Press C to Restart or Q to Quit", True, RED)
            screen.blit(message, [WIDTH / 8, HEIGHT / 3])
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE
        
        x += dx
        y += dy
        
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True
        
        screen.blit(background, (0, 0))
        screen.blit(food_image, (food_x, food_y))
        draw_score(level)
        
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length:
            del snake_list[0]
        
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        
        draw_snake(snake_list)
        pygame.display.update()
        
        # Проверяем, если еда была на поле дольше установленного времени, она исчезает
        if pygame.time.get_ticks() - food_spawn_time > food_time:
            food_x, food_y, food_image, food_points, food_time, food_spawn_time = spawn_food()
        
        if x == food_x and y == food_y:
            food_x, food_y, food_image, food_points, food_time, food_spawn_time = spawn_food()
            length += 1
            SCORE += food_points
            if SCORE % 3 == 0:
                level += 1
                speed += 2
        
        clock.tick(speed)
    
    pygame.quit()
    quit()

game_loop()
