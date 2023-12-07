import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 4
CARD_SIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Challenge Game")

# Fonts
font = pygame.font.Font(None, 36)

# Colors
card_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)] * 2
random.shuffle(card_colors)

# Game variables
cards_flipped = []
matched_pairs = 0
score = 0

def draw_card(x, y, color, flipped=False):
    if not flipped:
        pygame.draw.rect(screen, WHITE, (x, y, CARD_SIZE, CARD_SIZE))
    else:
        pygame.draw.rect(screen, color, (x, y, CARD_SIZE, CARD_SIZE))

def display_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))



# Game loop
running = True
start_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // CARD_SIZE, x // CARD_SIZE
            index = row * GRID_SIZE + col

            if index < len(card_colors) and index not in cards_flipped and len(cards_flipped) < 2:
                cards_flipped.append(index)

    # Draw the grid of cards
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            index = i * GRID_SIZE + j
            x, y = j * CARD_SIZE, i * CARD_SIZE

            if index < len(card_colors) and (index in cards_flipped or index in range(2)):
                draw_card(x, y, card_colors[index], flipped=(index in cards_flipped))



    # Check for a match
    if len(cards_flipped) == 2:
        pygame.display.flip()
        pygame.time.wait(1000)
        if card_colors[cards_flipped[0]] == card_colors[cards_flipped[1]]:
            matched_pairs += 1
            score += 100
        else:
            score -= 50
        cards_flipped = []

    # Check for game over
    if matched_pairs == GRID_SIZE * GRID_SIZE // 2:
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2)
        print(f"Game Over! Score: {score}, Time: {elapsed_time} seconds")
        running = False

    display_score()
    pygame.display.flip()

pygame.quit()