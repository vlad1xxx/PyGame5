import pygame

screen = pygame.display.set_mode((300, 300))
cursor_image = pygame.image.load("arrow.png").convert_alpha()
pygame.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0, 0, 0))
    if pygame.mouse.get_focused():
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor_image, (x, y))
        pygame.mouse.set_visible(False)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
