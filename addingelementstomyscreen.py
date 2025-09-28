import pygame

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic Game Building Concepts")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 102, 204)

# Font setup
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("Welcome to My Game!", True, WHITE)
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 50))

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Black background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, (200, 150, 200, 100))  # x, y, width, height

    # Draw text
    screen.blit(text, text_rect)

    pygame.display.update()

pygame.quit()