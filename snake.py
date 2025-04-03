import pygame
import random
import sys


pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRID_SIZE = 20

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

snake = [(100, 100), (80, 100), (60, 100)] 
snake_dir = (GRID_SIZE, 0)  

# Food initial position
food = (random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
        random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)


score = 0
level = 1
speed = 10  


font = pygame.font.SysFont("Arial", 20)


def generate_food():
    while True:
        new_food = (random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                    random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
        if new_food not in snake:
            return new_food


clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                snake_dir = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                snake_dir = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                snake_dir = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                snake_dir = (GRID_SIZE, 0)

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    if new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
        
        pygame.quit()
        sys.exit()
    
    if new_head in snake:
        pygame.quit()
        sys.exit()
    
    snake.insert(0, new_head)
    
    if new_head == food:
        score += 1
        food = generate_food()
        
        if score % 3 == 0:
            level += 1
            speed += 2  
    else:
        snake.pop()  
    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))
    
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], GRID_SIZE, GRID_SIZE))
    
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))
    
    pygame.display.update()
    clock.tick(speed)