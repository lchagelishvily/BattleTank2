from enum import Enum

from tile import Tile


class Block(Tile):

    def __init__(self, image, x, y, block_type):
        super().__init__(image, x, y)
        self.block_type = block_type
