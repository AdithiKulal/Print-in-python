import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Add Custom Event")

# Clock
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Sprite class
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self):
        self.color = random.choice(colors)
        self.image.fill(self.color)

# Create sprites
player = ColorSprite(150, 200, random.choice(colors))
enemy = ColorSprite(450, 200, random.choice(colors))

# Sprite group
all_sprites = pygame.sprite.Group(player, enemy)

# Custom event
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # every 2 seconds

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_COLOR_EVENT:
            player.change_color()
            enemy.change_color()

    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()