import itertools
import sys

import pygame
from pygame import event
from enemy import Enemy
from src.player import Player
from src.settings import Settings


class BattleTank:

    clock = pygame.time.Clock()

    def __init__(self):

        # Инициализация экрана
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((640, 480))
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        self.bg = pygame.transform.scale2x(pygame.image.load('../images/tiles/bg.png').convert())
        pygame.display.set_caption("Battle Tank")

        # Генерация поля
        # Todo Вынести в отдельный метод
        self.all_tanks = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        new_enemy = Enemy(self)
        self.enemies.add(new_enemy)
        self.all_tanks.add(new_enemy)
        self.player = Player(self)

        self.all_tanks.add(self.player)

    def run_game(self):
        while True:

            self.clock.tick(30)
            self._check_events()
            self.player.update(self)
            self.player.bullets.update(self)
            self.enemies.update(self)
            self._update_screen()

    def _check_events(self):

        key_event = pygame.event.poll()

        #for key_event in pygame.event.get():
        if key_event.type == pygame.QUIT:
            sys.exit()
        elif key_event.type == pygame.KEYDOWN:
            self._check_keydown_events(key_event)
        elif key_event.type == pygame.KEYUP:
            self._check_keyup_events(key_event)

    def _check_keydown_events(self, key_event):
        if key_event.key == pygame.K_q:
            sys.exit()
        elif key_event.key == pygame.K_RIGHT:
            self.player.move_right()
        elif key_event.key == pygame.K_LEFT:
            self.player.move_left()
        elif key_event.key == pygame.K_UP:
            self.player.move_up()
        elif key_event.key == pygame.K_DOWN:
            self.player.move_down()
        elif key_event.key == pygame.K_SPACE:
            self.player.fire(self)

    def _check_keyup_events(self, key_event):
        if key_event.key == pygame.K_RIGHT \
                or key_event.key == pygame.K_LEFT \
                or key_event.key == pygame.K_UP \
                or key_event.key == pygame.K_DOWN:
            self.player.stop()

    def _update_screen(self):
        self.setup_background()
        self.all_tanks.draw(self.screen)

        for bullet in self.player.bullets.sprites():
            bullet.draw()
        pygame.display.flip()

    def setup_background(self):

        background = pygame.transform.scale2x(pygame.image.load('../images/tiles/bg.png'))
        brick_width, brick_height = background.get_width(), background.get_height()
        for x, y in itertools.product(range(0, self.settings.screen_width, brick_width),
                                      range(0, self.settings.screen_height, brick_height)):
            self.screen.blit(background, (x, y))


if __name__ == '__main__':
    bt = BattleTank()
    bt.run_game()
