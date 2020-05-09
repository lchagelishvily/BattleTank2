import random
import pygame
from tank import Tank


class Enemy(Tank):

    def __init__(self, bt_game):
        
        super(Enemy, self).__init__(bt_game)
        self.speed = bt_game.settings.enemy_speed
        self.is_moving = True
        self.direction = 'D'
        self.change_direction_delay = self.settings.enemy_change_direction_delay

        self.move_sprites = [pygame.image.load('../data/images/tanks/rt1.png').convert_alpha(),
                             pygame.image.load('../data/images/tanks/rt2.png').convert_alpha(),
                             pygame.image.load('../data/images/tanks/rt3.png').convert_alpha(),
                             pygame.image.load('../data/images/tanks/rt4.png').convert_alpha(),
                             pygame.image.load('../data/images/tanks/rt5.png').convert_alpha()]


    def fire(self):
        pass

    def update(self, bt_game):

        if self.change_direction_delay == 0:
            self.direction = random.choice(['U', 'D', 'L', 'R'])
            self.change_direction_delay = self.settings.enemy_change_direction_delay
        else:
            self.change_direction_delay -= 1

        rect = self.rect.copy()
        if self.is_moving:
            if self.direction == 'R':
                self.rect.x += self.speed
                self.image = self.move_sprites[self._get_animation_idx() // 4]
                self.image = pygame.transform.rotate(self.image, -90)
            if self.direction == 'L':
                self.image = self.move_sprites[self._get_animation_idx() // 4]
                self.rect.x -= self.speed
                self.image = pygame.transform.rotate(self.image, 90)
            if self.direction == 'U':
                self.image = self.move_sprites[self._get_animation_idx() // 4]
                self.rect.y -= self.speed
            if self.direction == 'D':
                self.image = self.move_sprites[self._get_animation_idx() // 4]
                self.rect.y += self.speed
                self.image = pygame.transform.rotate(self.image, 180)
            if not self._can_move(bt_game):
                self.rect = rect

    def _can_move(self, bt_game):
        return self._is_in_screen and not self._is_collided(bt_game)


