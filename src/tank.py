
import pygame
from pygame.sprite import Sprite

from src.bullet import  Bullet


class Tank(Sprite):

    def __init__(self, bt_game):
        super(Tank, self).__init__()
        self.settings = bt_game.settings
        self.speed = bt_game.settings.player_speed
        self.animation_count = 0
        self.is_moving = False
        self.direction = 'U'
        self.screen = bt_game.screen
        self.screen_rect = bt_game.screen.get_rect()
        self.bullets = pygame.sprite.Group()

        self.move_sprites = [pygame.image.load('../data/images/tanks/gt1.png').convert_alpha(),
                             pygame.image.load('../data/images/tanks/gt2.png').convert_alpha(),
                             pygame.image.load('../data/images/tanks/gt3.png').convert_alpha(),
                             pygame.image.load('../data/images/tanks/gt4.png').convert_alpha(),
                             pygame.image.load('../data/images/tanks/gt5.png').convert_alpha()]

        self.image = self.move_sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = 0

    def move_right(self):
        self.is_moving = True
        self.direction = 'R'

    def move_left(self):
        self.is_moving = True
        self.direction = 'L'

    def move_up(self):
        self.is_moving = True
        self.direction = 'U'

    def move_down(self):
        self.is_moving = True
        self.direction = 'D'

    def stop(self):
        self.is_moving = False

    def fire(self, bt_game):
        new_bullet = Bullet(bt_game, self)
        self.bullets.add(new_bullet)

    def update(self, bt_game):
        pass

    def _can_move(self, bt_game):
        return self._is_in_screen and not self._is_collided(bt_game)

    @property
    def _is_in_screen(self):
        return self.screen_rect.contains(self.rect)

    def _is_collided(self, bt_game):
        bt_game.all_objects.remove(self)
        result = pygame.sprite.spritecollideany(self, bt_game.all_objects)
        bt_game.all_objects.add(self)
        return result

    def _get_animation_idx(self):
        self.animation_count += 1
        if self.animation_count >= 20:
            self.animation_count = 0
        return self.animation_count

    #def draw(self):
        #self.screen.blit(self.image, self.rect)

