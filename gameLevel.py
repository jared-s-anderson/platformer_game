import pygame
from pygame import constants
from csvLayout import import_csv_layout, import_graphics
from displaySettings import tile_size
from tileClass import Animation, Tile, FixedTile, Crate, Coins
from enemyClass import Enemies

class gameLevel:
    def __init__(self, data, surface):
        self.display_surface = surface
        self.level_shift = 0

        # Player Setup
        player_design = import_csv_layout(data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.endLevel = pygame.sprite.GroupSingle()
        self.player_setup(player_design)

        # Terrain Setup
        terrain_design = import_csv_layout(data['terrain'])
        self.terrainSprites = self.buildTileGroup(terrain_design, 'terrain')

        # Crate Setup
        crate_design = import_csv_layout(data['crates'])
        self.crateSprites = self.buildTileGroup(crate_design, 'crates')

        # Coins Setup
        coin_design = import_csv_layout(data['coins'])
        self.coinSprites = self.buildTileGroup(coin_design, 'coins')

        # Enemy Setup
        enemy_design = import_csv_layout(data['enemies'])
        self.enemySprites = self.buildTileGroup(enemy_design, 'enemies')

        # Constraint Setup
        constraint_design = import_csv_layout(data['constraints'])
        self.constraintSprites = self.buildTileGroup(constraint_design, 'constraints')
        

    def buildTileGroup(self, layout, type):
        spriteGroup = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrainList = import_graphics('graphics/terrain_tiles.png')
                        tileSurface = terrainList[int(val)]
                        sprite = FixedTile(tile_size, x, y, tileSurface)
                        
                    if type == 'crates':
                        sprite = Crate(tile_size, x, y)

                    if type == 'coins':
                        if val == '0':
                            sprite = Coins(tile_size, x, y, 'graphics/coin_color/gold')
                        if val == '1':
                            sprite = Coins(tile_size, x, y, 'graphics/coin_color/silver')

                    if type == 'enemies':
                        sprite = Enemies(tile_size, x, y)

                    if type == 'constraints':
                        sprite = Tile(tile_size, x, y)
                        
                    spriteGroup.add(sprite)
                
        return spriteGroup

    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '0':
                    print("Player")
                if val == '1':
                    starting_surface = pygame.image.load('graphics/hat.png').convert_alpha()
                    sprite = FixedTile(tile_size, x, y, starting_surface)
                    self.endLevel.add(sprite)


    def reverse_collision(self):
        for enemy in self.enemySprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraintSprites, False):
                enemy.reverse()


    def run(self):
        # Terrain
        self.terrainSprites.draw(self.display_surface)
        self.terrainSprites.update(self.level_shift)

        # Enemies
        self.enemySprites.draw(self.display_surface)
        self.constraintSprites.update(self.level_shift)
        self.reverse_collision()
        self.enemySprites.update(self.level_shift)

        # Crates
        self.crateSprites.draw(self.display_surface)
        self.crateSprites.update(self.level_shift)

        # Coins
        self.coinSprites.draw(self.display_surface)
        self.coinSprites.update(self.level_shift)

        # Player
        self.endLevel.update(self.level_shift)
        self.endLevel.draw(self.display_surface)

        
    