""" This program is a unique snake game in Python using the pygame library.
The game window will have a gradient background, and the snake and food will have unique colors. """ 

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
FPS = 10
FONT_SIZE = 20
FONT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Unique Snake Game")

# Initialize variables
snake = [(100, 50), (90, 50), (80, 50)]
snake_direction = (1, 0)
food = (random.randint(0, WIDTH // 10 - 1) * 10, random.randint(0, HEIGHT // 10 - 1) * 10)

clock = pygame.time.Clock()

# Display "Designed by Prahlad"
font = pygame.font.Font(None, FONT_SIZE)
design_text = font.render("Designed by Prahlad", True, FONT_COLOR)
design_rect = design_text.get_rect(center=(WIDTH // 2, HEIGHT - FONT_SIZE))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, 1):
        snake_direction = (0, -1)
    elif keys[pygame.K_DOWN] and snake_direction != (0, -1):
        snake_direction = (0, 1)
    elif keys[pygame.K_LEFT] and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
        snake_direction = (1, 0)

    # Move the snake
    x, y = snake[0]
    x += snake_direction[0] * 10
    y += snake_direction[1] * 10

    # Check for collision with walls or itself
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or (x, y) in snake[1:]:
        pygame.quit()
        sys.exit()

    snake.insert(0, (x, y))

    # Check for collision with food
    if (x, y) == food:
        food = (random.randint(0, WIDTH // 10 - 1) * 10, random.randint(0, HEIGHT // 10 - 1) * 10)
    else:
        snake.pop()

    # Draw the background
    screen.fill(BACKGROUND_COLOR)

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0], segment[1], 10, 10))

    # Draw the food
    pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], 10, 10))

    # Draw the "Designed by Prahlad" text
    screen.blit(design_text, design_rect)

    pygame.display.flip()
    clock.tick(FPS)
