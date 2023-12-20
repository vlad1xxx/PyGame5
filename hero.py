import pygame

screen = pygame.display.set_mode((300, 300))
cursor_image = pygame.image.load("creature.png").convert_alpha()
x, y = 0, 0
pygame.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 10
            elif event.key == pygame.K_DOWN:
                y += 10
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_LEFT:
                x -= 10
    screen.fill((255, 255, 255))
    screen.blit(cursor_image, (x, y))
    pygame.display.flip()
    pygame.time.Clock().tick(60)