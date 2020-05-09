
import itertools
import sys
import pygame
from pygame import event
import pytmx

from enemy import Enemy
from src.player import Player
from src.settings import Settings
from tmx_loader import Renderer


class BattleTank:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Battle Tank")

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()
        self.fps = self.settings.fps
        self.blocks = pygame.sprite.Group()
        self.all_objects = pygame.sprite.Group()
        self.all_tanks = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bg = None
        self.player = None

    def load_game(self):
        renderer = Renderer('../data/maps/level_1.tmx')
        self.bg = renderer.get_background()
        self.all_objects = renderer.get_blocks()

        self.player = Player(self)
        self.player.rect.x = 0
        self.all_objects.add(self.player)

        enemy1 = Enemy(self)
        enemy1.rect.x = 0
        enemy2 = Enemy(self)
        enemy2.rect.x = self.settings.screen_width - enemy2.rect.width
        self.enemies.add(enemy1)
        self.enemies.add(enemy2)

        self.all_objects.add(enemy1)
        self.all_objects.add(enemy2)

    def run_game(self):
        while True:
            self.clock.tick(self.fps)
            self._check_events()
            self.all_objects.update(self)
            self._update_screen()

    def _check_events(self):

        key_event = pygame.event.poll()

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
            self.all_objects.add(self.player.fire(self))

    def _check_keyup_events(self, key_event):
        if key_event.key == pygame.K_RIGHT \
                or key_event.key == pygame.K_LEFT \
                or key_event.key == pygame.K_UP \
                or key_event.key == pygame.K_DOWN:
            self.player.stop()

    def _update_screen(self):
        self.screen.blit(self.bg, self.bg.get_rect())
        self.all_objects.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    bt = BattleTank()
    bt.load_game()
    bt.run_game()
