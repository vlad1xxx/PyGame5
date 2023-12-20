import pygame


class Car(pygame.sprite.Sprite):
    image = pygame.image.load('car2.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.reverse = False
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.x = 0

    def update(self):
        if not self.reverse:
            self.x += 10
        else:
            self.x -= 10
        if self.x > 600 - self.rect.size[0]:
            self.reverse = True
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.x < 0:
            self.reverse = False
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect.x = self.x


def main():
    all_sprites = pygame.sprite.Group()
    _ = Car(all_sprites)
    screen = pygame.display.set_mode((600, 95))
    clock = pygame.time.Clock()
    pygame.init()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()

        screen.fill(pygame.Color("white"))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()