from pygame.sprite import Sprite


class Tile(Sprite):

    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
