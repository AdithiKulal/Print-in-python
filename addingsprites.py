import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sprite Playground")

player = pygame.Rect(100, 100, 60, 60)
enemy = pygame.Rect(500, 300, 60, 60)
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= speed
    if keys[pygame.K_RIGHT]: player.x += speed
    if keys[pygame.K_UP]: player.y -= speed
    if keys[pygame.K_DOWN]: player.y += speed

    screen.fill((20, 20, 20))
    pygame.draw.rect(screen, (0, 200, 255), player)
    pygame.draw.rect(screen, (255, 50, 50), enemy)
    pygame.display.flip()

pygame.quit()