import pygame as pg
import pytmx
from block import Block
from constants import BLOCK_TYPES

class Renderer(object):

    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.size = tm.width * tm.tilewidth, tm.height * tm.tileheight
        self.tmx_data = tm

    def render(self, surface):

        tw = self.tmx_data.tilewidth
        th = self.tmx_data.tileheight
        gt = self.tmx_data.get_tile_image_by_gid

        if self.tmx_data.background_color:
            surface.fill(self.tmx_data.background_color)

        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = gt(gid)
                    if tile:
                        surface.blit(tile, (x * tw, y * th))

            elif isinstance(layer, pytmx.TiledObjectGroup):
                pass

            elif isinstance(layer, pytmx.TiledImageLayer):
                image = gt(layer.gid)
                if image:
                    surface.blit(image, (0, 0))

    def get_background(self):
        temp_surface = pg.Surface(self.size)
        self.render(temp_surface)
        return temp_surface

    def get_blocks(self):
        blocks = pg.sprite.Group()
        blocks_layer = self.tmx_data.get_layer_by_name('BlocksLayer')
        tw = self.tmx_data.tilewidth
        th = self.tmx_data.tileheight
        gt = self.tmx_data.get_tile_image_by_gid
        gp = self.tmx_data.get_tile_properties_by_gid
        for x, y, gid in blocks_layer:
            tile = gt(gid)
            if tile:
                properties = gp(gid)
                blocks.add(Block(tile, x * tw, y * th, self.block_type(gid)))
        return blocks

    @staticmethod
    def block_type(gid):
        choices = {1: BLOCK_TYPES.BRICK, 2: BLOCK_TYPES.IRON}
        return choices.get(gid, None)
