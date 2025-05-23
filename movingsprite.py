import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Rectangle Fun!")

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

rect_width, rect_height = 40, 40
rect_x, rect_y = WIDTH // 2, HEIGHT // 2
rect_speed_x, rect_speed_y = 4, 4
rect_color = random_color()

running = True
while running:
    pygame.time.delay(30)
    screen.fill((0, 0, 0))  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= 5
    if keys[pygame.K_RIGHT]:
        rect_x += 5
    if keys[pygame.K_UP]:
        rect_y -= 5
    if keys[pygame.K_DOWN]:
        rect_y += 5

    rect_x += rect_speed_x
    rect_y += rect_speed_y

    if rect_x <= 0 or rect_x + rect_width >= WIDTH:
        rect_speed_x = -rect_speed_x
        rect_color = random_color()
    if rect_y <= 0 or rect_y + rect_height >= HEIGHT:
        rect_speed_y = -rect_speed_y
        rect_color = random_color()

    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()

pygame.quit()