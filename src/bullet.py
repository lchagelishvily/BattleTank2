
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, bt_game, owner):
        super().__init__()
        self.screen = owner.screen
        self.settings = owner.settings
        self.color = self.settings.bullet_color
        self.direction = owner.direction
        self.owner = owner
        self.screen_rect = bt_game.screen.get_rect()
        self.image = pygame.transform.scale2x(pygame.image.load('../images/shots/bullet.png').convert_alpha())
        self.explosion = pygame.transform.scale2x(pygame.image.load('../images/shots/shot.png').convert_alpha())
        self.rect = self.image.get_rect()

        if self.direction == 'U':
            self.rect.midtop = owner.rect.midtop
        elif self.direction == 'D':
            self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
            self.rect.midbottom = owner.rect.midbottom
        elif self.direction == 'L':
            self.rect = pygame.Rect(0, 0, self.settings.bullet_height, self.settings.bullet_width)
            self.rect.midleft = owner.rect.midleft
        elif self.direction == 'R':
            self.rect = pygame.Rect(0, 0, self.settings.bullet_height, self.settings.bullet_width)
            self.rect.midright = owner.rect.midright
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self, bt_game):
        if self.direction == 'U':
            self.y -= self.settings.bullet_speed
        elif self.direction == 'D':
            self.y += self.settings.bullet_speed
        elif self.direction == 'L':
            self.x -= self.settings.bullet_speed
        elif self.direction == 'R':
            self.x += self.settings.bullet_speed

        self.rect.x = self.x
        self.rect.y = self.y

        if not self._is_in_screen:
            self.kill()
        else:
            self._is_collided(bt_game)

    @property
    def _is_in_screen(self):
        return self.screen_rect.contains(self.rect)

    def _is_collided(self, bt_game):
        single_group = pygame.sprite.GroupSingle(self)
        return pygame.sprite.groupcollide(single_group, bt_game.enemies, True, True)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
