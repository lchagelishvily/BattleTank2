import pygame
from src.bullet import  Bullet
from tank import Tank


class Player(Tank):

    def __init__(self, bt_game):
        super(Player, self).__init__(bt_game)
        self.speed = self.settings.player_speed
        self.direction = 'U'
        self.move_sprites = [pygame.transform.scale2x(pygame.image.load('../images/tanks/gt1.png').convert_alpha()),
                             pygame.transform.scale2x(pygame.image.load('../images/tanks/gt2.png').convert_alpha()),
                             pygame.transform.scale2x(pygame.image.load('../images/tanks/gt3.png').convert_alpha()),
                             pygame.transform.scale2x(pygame.image.load('../images/tanks/gt4.png').convert_alpha()),
                             pygame.transform.scale2x(pygame.image.load('../images/tanks/gt5.png').convert_alpha())]
        self.rect.midbottom = self.screen_rect.midbottom

    def fire(self, bt_game):
        new_bullet = Bullet(bt_game, self)
        self.bullets.add(new_bullet)

    def update(self, bt_game):

        rect = self.rect.copy()
        if self.is_moving:
            if self.direction == 'R':
                self.rect.x += self.speed
                self.image = self.move_sprites[self._get_animation_idx() // 4]
                self.image = pygame.transform.rotate(self.image, -90)
            if self.direction == 'L':
                self.rect.x -= self.speed
                self.image = self.move_sprites[self._get_animation_idx() // 4]
                self.image = pygame.transform.rotate(self.image, 90)
            if self.direction == 'U':
                self.rect.y -= self.speed
                self.image = self.move_sprites[self._get_animation_idx() // 4]
            if self.direction == 'D':
                self.rect.y += self.speed
                self.image = self.move_sprites[self._get_animation_idx() // 4]
                self.image = pygame.transform.rotate(self.image, 180)
            if not self._can_move(bt_game):
                self.rect = rect

    def _can_move(self, bt_game):
        return self._is_in_screen and not self._is_collided(bt_game)

    def _is_collided(self, bt_game):
        return pygame.sprite.spritecollideany(self, bt_game.enemies)



