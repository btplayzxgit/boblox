from __future__ import division

import sys
import math
import random
import time

from collections import deque

from boblox.nointernet.source.noise_gen import NoiseGen


import pyautogui
import turtle
import os
from pyglet import image
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse
from pyglet.gl import *
from numpy import mean as average
from platform import system as operating_sys

global WORDS_IN_CHAT
WORDS_IN_CHAT = ''
username = open('boblox\\account\\username', 'r').read()
keyword = None
UPDATE_TIME = 400
RENDER_DISTANCE = 14
WALKING_SPEED = 3
FLYING_SPEED = 15
CROUCH_SPEED = 2
SPRINT_SPEED = 13
SPRINT_FOV = SPRINT_SPEED / 8
GRAVITY = 20.0
MAX_JUMP_HEIGHT = 1.0
JUMP_SPEED = math.sqrt(2 * GRAVITY * MAX_JUMP_HEIGHT)
TERMINAL_VELOCITY = 50
PLAYER_HEIGHT = 2
PLAYER_FOV = 80.0
TITLE = 'Boblox'
TIME_ZONE = 0
BL_SKY = False


class NotSoMinecraftTerrian:
    seed = 452692 - random.randint(0, 8000)
    map_size = 100
    def complexify_seed(): seed = NotSoMinecraftTerrian.seed; seed = seed - seed * seed + seed / 8 + 785 + seed - 1000
class NotSoMinecraftError(Exception): pass


def test_mode(): NotSoMinecraftTerrian.map_size = 100




def start():
    grp = 20
    pyautogui.alert(title=f'{TITLE}', text='CONTROLS\n\nW - FORWARD\nS - BACKWARDS\nA - LEFT\nD - RIGHT\nC - CROUCH\nSPACE - JUMP\nESC - PAUSE THE GAME\nTAB - FLY\n/ - CHAT\nR - SPRINT\nI - INVENTORY\nSHIFT - CROUCH WITHOUT ZOOM\nE - CRAFT', button='PLAY')


    global creative
    global survival

    creative = False
    survival = False

    gamemode = pyautogui.confirm(title=f'{TITLE}', text='Select gamemode', buttons=['Creative', 'Survival'])
    if gamemode == None: quit()
    if gamemode == 'Creative': creative, survival = True, False
    if gamemode == 'Survival': creative, survival = False, True
    del gamemode


    if sys.version_info[0] >= 3:
        xrange = range

    def cube_vertices(x, y, z, n):
        return [
            x-n,y+n,z-n, x-n,y+n,z+n, x+n,y+n,z+n, x+n,y+n,z-n,
            x-n,y-n,z-n, x+n,y-n,z-n, x+n,y-n,z+n, x-n,y-n,z+n,
            x-n,y-n,z-n, x-n,y-n,z+n, x-n,y+n,z+n, x-n,y+n,z-n,
            x+n,y-n,z+n, x+n,y-n,z-n, x+n,y+n,z-n, x+n,y+n,z+n,
            x-n,y-n,z+n, x+n,y-n,z+n, x+n,y+n,z+n, x-n,y+n,z+n,
            x+n,y-n,z-n, x-n,y-n,z-n, x-n,y+n,z-n, x+n,y+n,z-n,
        ]

    def calculate_biom():
        if NotSoMinecraftTerrian.seed == 12: return 'dessert'
        elif NotSoMinecraftTerrian.seed == 13: return 'dessert'
        elif NotSoMinecraftTerrian.seed == 14: return 'dessert'
        else: return 'grassland'


    def tex_coord(x, y, n=4):
        m = 1.0 / n
        dx = x * m
        dy = y * m
        return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m


    def tex_coords(top, bottom, side):
        top = tex_coord(*top)
        bottom = tex_coord(*bottom)
        side = tex_coord(*side)
        result = []
        result.extend(top)
        result.extend(bottom)
        result.extend(side * 4)
        return result

    TEXTURE_PATH = 'boblox\\nointernet\\source\\normal_texture_pack.png'

    GRASS = tex_coords((1, 0), (0, 1), (0, 0))
    SAND = tex_coords((1, 1), (1, 1), (1, 1))
    BRICK = tex_coords((2, 0), (2, 0), (2, 0))
    STONE = tex_coords((2, 1), (2, 1), (2, 1))
    WOOD = tex_coords((3, 1), (3, 1), (3, 1))
    WOOD2 = tex_coords((1, 2), (1, 2), (1, 2))
    LEAF = tex_coords((3, 0), (3, 0), (3, 0))
    CACTUS = tex_coords((2, 2), (2, 2), (2, 2))
    WATER = tex_coords((0, 2), (0, 2), (0, 2))
    DIRT = tex_coords((0, 1), (0, 1), (0, 1))
    DIAMOND = tex_coords((0, 3), (0, 3), (0, 3))
    BEDROCK = tex_coords((1, 3), (1, 3), (1, 3))
    GOLD = tex_coords((2, 3), (2, 3), (2, 3))
    WOOD_PLANK = tex_coords((3, 3), (3, 3), (3, 3))
    COBBLESTONE = tex_coords((3, 2), (3, 2), (3, 2))
    GLASS = None

    FACES = [
        ( 0, 1, 0),
        ( 0,-1, 0),
        (-1, 0, 0),
        ( 1, 0, 0),
        ( 0, 0, 1),
        ( 0, 0, -1),
    ]


    def normalize(position):
        x, y, z = position
        x, y, z = (int(round(x)), int(round(y)), int(round(z)))
        return (x, y, z)
        


    def sectorize(position):
        x, y, z = normalize(position)
        x, y, z = x // RENDER_DISTANCE, y // RENDER_DISTANCE, z // RENDER_DISTANCE
        return (x, 0, z)


    class Model(object):

        def __init__(self):

            self.batch = pyglet.graphics.Batch()

            self.group = TextureGroup(image.load(TEXTURE_PATH).get_texture())
            self.world = {}
            self.shown = {}

            self._shown = {}

            self.sectors = {}
            self.queue = deque()

            self._initialize()

        def _initialize(self):
            global gen
            gen = NoiseGen(NotSoMinecraftTerrian.seed)

            n = NotSoMinecraftTerrian.map_size
            s = 1
            y = 0
            j = 0
            jh = 0

            biom = calculate_biom()
            
            heightMap = []
            for x in xrange(0, n, s):
                for z in xrange(0, n, s):
                    jh = jh + 1
                    print(f'Generating Height Map Stage 1/2... Parts of stage developed: {jh}')
                    heightMap.append(0)
            jh = 0
            for x in xrange(0, n, s):
                for z in xrange(0, n, s):
                    jh = jh + 1
                    print(f'Generating Height Map Stage 2/2... Parts of stage developed: {jh}')
                    heightMap[z + x * n] = int(gen.getHeight(x, z))
            
            jh = 0
            del jh
            for x in xrange(0, n, s):
                j = j + 1
                for z in xrange(0, n, s):
                    h = heightMap[z + x * n]
                    if (h < 15):
                        self.add_block((x, h, z), SAND, immediate=False)
                        for y in range(h, 15):
                            if biom == 'grassland': self.add_block((x, y, z), WATER, immediate=False)
                            else: self.add_block((x, y, z), SAND, immediate=False)
                        continue
                    if (h < 18):
                        self.add_block((x, h, z), SAND, immediate=False)
                    if biom == 'grassland': self.add_block((x, h, z), GRASS, immediate=False)

                    else: self.add_block((x, h, z), SAND, immediate=False)
                    for y in xrange(h - 1, 0, -1):
                        if y == 9:
                            self.add_block((x, y, z), random.choice([STONE, STONE, STONE, STONE, STONE, STONE, COBBLESTONE, STONE, GOLD, STONE, DIAMOND, STONE, STONE, STONE]), immediate=False)
                        elif y == 10:
                            self.add_block((x, y, z), random.choice([STONE, STONE, STONE, STONE, STONE, STONE, COBBLESTONE, STONE, GOLD, STONE, DIAMOND, STONE, STONE, STONE]), immediate=False)
                        elif y == 11:
                            self.add_block((x, y, z), random.choice([STONE, STONE, STONE, STONE, STONE, STONE, COBBLESTONE, STONE, GOLD, STONE, DIAMOND, STONE, STONE, STONE]), immediate=False)
                        elif y == 1:
                            self.add_block((x, y, z), BEDROCK, immediate=False)
                        
                        
                        

                        else:
                            self.add_block((x, y, z), random.choice([STONE, STONE, STONE, STONE, STONE, COBBLESTONE, STONE, STONE, STONE, STONE, STONE]), immediate=False)
                        
                    if biom != 'dessert':
                        if (h > 20):
                            if random.randrange(0, 1000) > 990:
                                treeHeight = random.randint(5, 7)
                                wood_type = random.choice([WOOD, WOOD2])
                                for y in xrange(h + 1, h + treeHeight):
                                    self.add_block((x, y, z), wood_type, immediate=False)
                                leafh = h + treeHeight
                                for lz in xrange(z + -2, z + 3):
                                    for lx in xrange(x + -2, x + 3): 
                                        for ly in xrange(3):
                                            self.add_block((lx, leafh + ly, lz), LEAF, immediate=False)
                    else:
                        if (h > 20):
                            if random.randrange(0, 1000) > 990:
                                cactusHeight = random.randint(5, 7)
                                for y in xrange(h + 1, h + cactusHeight):
                                    self.add_block((x, y, z), CACTUS, immediate=False)
                print(f'Generating terrian... {j}/{n}%')
            

            j, n, s, y, h, z, x = 0, 0, 0, 0, 0, 0, 0

            del j
            del n
            del s
            del y
            del h
            del z
            del x
        def hit_test(self, position, vector, max_distance=8):
            m = 8
            x, y, z = position
            dx, dy, dz = vector
            previous = None
            for _ in xrange(max_distance * m):
                key = normalize((x, y, z))
                if key != previous and key in self.world:
                    return key, previous
                previous = key
                x, y, z = x + dx / m, y + dy / m, z + dz / m
            return None, None

        def exposed(self, position):
            x, y, z = position
            for dx, dy, dz in FACES:
                if (x + dx, y + dy, z + dz) not in self.world:
                    return True
            return False

        def add_block(self, position, texture, immediate=True):
            if position in self.world:
                self.remove_block(position, immediate)
            self.world[position] = texture
            self.sectors.setdefault(sectorize(position), []).append(position)
            if immediate:
                if self.exposed(position):
                    self.show_block(position)
                self.check_neighbors(position)

        def remove_block(self, position, immediate=True):
            del self.world[position]
            self.sectors[sectorize(position)].remove(position)
            if immediate:
                if position in self.shown:
                    self.hide_block(position)
                self.check_neighbors(position)

        def check_neighbors(self, position):
            x, y, z = position
            for dx, dy, dz in FACES:
                key = (x + dx, y + dy, z + dz)
                if key not in self.world:
                    continue
                if self.exposed(key):
                    if key not in self.shown:
                        self.show_block(key)
                else:
                    if key in self.shown:
                        self.hide_block(key)

        def show_block(self, position, immediate=True):
            texture = self.world[position]
            self.shown[position] = texture
            if immediate:
                self._show_block(position, texture)
            else:
                self._enqueue(self._show_block, position, texture)

        def _show_block(self, position, texture):
            x, y, z = position
            vertex_data = cube_vertices(x, y, z, 0.5)
            texture_data = list(texture)
            self._shown[position] = self.batch.add(24, GL_QUADS, self.group,
                ('v3f/static', vertex_data),
                ('t2f/static', texture_data))

        def hide_block(self, position, immediate=True):
            self.shown.pop(position)
            if immediate:
                self._hide_block(position)
            else:
                self._enqueue(self._hide_block, position)

        def _hide_block(self, position):
            self._shown.pop(position).delete()

        def show_sector(self, sector):
            for position in self.sectors.get(sector, []):
                if position not in self.shown and self.exposed(position):
                    self.show_block(position, False)

        def hide_sector(self, sector):
            for position in self.sectors.get(sector, []):
                if position in self.shown:
                    self.hide_block(position, False)

        def change_sectors(self, before, after):
            before_set = set()
            after_set = set()
            pad = 4
            for dx in xrange(-pad, pad + 1):
                for dy in [0]:
                    for dz in xrange(-pad, pad + 1):
                        if dx ** 2 + dy ** 2 + dz ** 2 > (pad + 1) ** 2:
                            continue
                        if before:
                            x, y, z = before
                            before_set.add((x + dx, y + dy, z + dz))
                        if after:
                            x, y, z = after
                            after_set.add((x + dx, y + dy, z + dz))
            show = after_set - before_set
            hide = before_set - after_set
            for sector in show:
                self.show_sector(sector)
            for sector in hide:
                self.hide_sector(sector)

        def _enqueue(self, func, *args):
            self.queue.append((func, args))

        def _dequeue(self):
            func, args = self.queue.popleft()
            func(*args)

        def process_queue(self):
            start = time.process_time()
            while self.queue and time.process_time() - start < 1.0 / UPDATE_TIME:
                self._dequeue()

        def process_entire_queue(self):
            while self.queue:
                self._dequeue()


    class Window(pyglet.window.Window):

        def __init__(self, *args, **kwargs):
            super(Window, self).__init__(*args, **kwargs)

            self.exclusive = False
            self.flying = False
            self.jumping = False
            self.jumped = False
            self.crouch = False
            self.sprinting = False

            self.fov_offset = 0

            self.collision_types = {"top": False, "bottom": False, "right": False, "left": False}
            self.strafe = [0, 0]
            self.position = (30, 50, 80)
            self.rotation = (0, 0)
            self.sector = None
            self.reticle = None
            self.dy = 0
            self.model = Model()
            self.label = pyglet.text.Label('', font_name='Arial', font_size=18,
                x=10, y=self.height - 10, anchor_x='left', anchor_y='top',
                color=(0, 0, 0, 255))

            pyglet.clock.schedule_interval(self.update, 0.5 / UPDATE_TIME)

        def set_exclusive_mouse(self, exclusive):
            super(Window, self).set_exclusive_mouse(exclusive)
            self.exclusive = exclusive

        def get_sight_vector(self):
            x, y = self.rotation
            m = math.cos(math.radians(y))
            dy = math.sin(math.radians(y))
            dx = math.cos(math.radians(x - 90)) * m
            dz = math.sin(math.radians(x - 90)) * m
            return (dx, dy, dz)

        def get_motion_vector(self):
            if any(self.strafe):
                x, y = self.rotation
                strafe = math.degrees(math.atan2(*self.strafe))
                y_angle = math.radians(y)
                x_angle = math.radians(x + strafe)
                if self.flying:
                    m = math.cos(y_angle)
                    dy = math.sin(y_angle)
                    if self.strafe[1]:
                        dy = 0.0
                        m = 1
                    if self.strafe[0] > 0:
                        dy *= -1
                    dx = math.cos(x_angle) * m
                    dz = math.sin(x_angle) * m
                else:
                    dy = 0.0
                    dx = math.cos(x_angle)
                    dz = math.sin(x_angle)
            else:
                dy = 0.0
                dx = 0.0
                dz = 0.0
            return (dx, dy, dz)

        def update(self, dt):
            self.model.process_queue()
            sector = sectorize(self.position)
            if sector != self.sector:
                self.model.change_sectors(self.sector, sector)
                if self.sector is None:
                    self.model.process_entire_queue()
                self.sector = sector
            m = 8
            dt = min(dt, 0.2)
            for _ in xrange(m):
                self._update(dt / m)

        def _update(self, dt):
            if self.flying:
                speed = FLYING_SPEED
            elif self.sprinting:
                speed = SPRINT_SPEED
            elif self.crouch:
                speed = CROUCH_SPEED
            else:
                speed = WALKING_SPEED

            if self.jumping:
                if self.collision_types["top"]:
                    self.dy = JUMP_SPEED
                    self.jumped = True
            else:
                if self.collision_types["top"]:
                    self.jumped = False
            if self.jumped:
                speed += 0.7

            d = dt * speed
            dx, dy, dz = self.get_motion_vector()
            dx, dy, dz = dx * d, dy * d, dz * d
            if not self.flying:
                self.dy -= dt * GRAVITY
                self.dy = max(self.dy, -TERMINAL_VELOCITY)
                dy += self.dy * dt
            old_pos = self.position
            x, y, z = old_pos
            x, y, z = self.collide((x + dx, y + dy, z + dz), PLAYER_HEIGHT)
            self.position = (x, y, z)
            if old_pos[0]-self.position[0] == 0 and old_pos[2]-self.position[2] == 0:
                disablefov = False
                if self.sprinting:
                    disablefov = True
                self.sprinting = False
                if disablefov:
                    self.fov_offset -= SPRINT_FOV

        def collide(self, position, height):
            pad = 0.25
            p = list(position)
            np = normalize(position)
            self.collision_types = {"top":False,"bottom":False,"right":False,"left":False}
            for face in FACES:
                for i in xrange(3):
                    if not face[i]:
                        continue
                    d = (p[i] - np[i]) * face[i]
                    if d < pad:
                        continue
                    for dy in xrange(height):
                        op = list(np)
                        op[1] -= dy
                        op[i] += face[i]
                        if tuple(op) not in self.model.world:
                            continue
                        p[i] -= (d - pad) * face[i]
                        if face == (0, -1, 0):
                            self.collision_types["top"] = True
                            self.dy = 0
                        if face == (0, 1, 0):
                            self.collision_types["bottom"] = True
                            self.dy = 0
                        break
            return tuple(p)

        def on_mouse_press(self, x, y, button, modifiers):
            if self.exclusive:
                vector = self.get_sight_vector()
                block, previous = self.model.hit_test(self.position, vector)
                if (button == mouse.RIGHT) or \
                        ((button == mouse.LEFT) and (modifiers & key.MOD_CTRL)):

                    if previous:
                        try:
                            self.model.add_block(previous, self.block)
                        except:
                            if survival:
                                print()
                elif button == pyglet.window.mouse.LEFT and block:
                    texture = self.model.world[block]
                    if creative:
                        if texture != WATER:
                            self.model.remove_block(block)
                            if survival:
                                self.block = texture
                                previous = texture
                    if survival:
                        if texture != WATER:
                            if texture != BEDROCK:
                                self.model.remove_block(block)
                                if survival:
                                    self.block = texture
                                    previous = texture     
            else:
                self.set_exclusive_mouse(True)

        def on_mouse_motion(self, x, y, dx, dy):
            if self.exclusive:
                m = 0.15
                x, y = self.rotation
                x, y = x + dx * m, y + dy * m
                y = max(-90, min(90, y))
                self.rotation = (x, y)

        def on_key_press(self, symbol, modifiers):
            if symbol == key.W:
                self.strafe[0] -= 1
            elif symbol == key.S:
                self.strafe[0] += 1
            elif symbol == key.A:
                self.strafe[1] -= 1
            elif symbol == key.D:
                self.strafe[1] += 1
            elif symbol == key.C:
                self.fov_offset -= 60.0
            elif symbol == key.SLASH:
                global keyword
                global WORDS_IN_CHAT
                self.set_exclusive_mouse(False)
                keyword = pyautogui.prompt(title=f'{TITLE}', text=f'CHAT\n\nType something in the chat\n{WORDS_IN_CHAT}')
                if keyword == None:
                    pass
                else:
                    WORDS_IN_CHAT = WORDS_IN_CHAT + f'\n{username}: {keyword}'
                if keyword == '/time set day':
                    global TIME_ZONE
                    WORDS_IN_CHAT = WORDS_IN_CHAT + f'\nTime set to day'
                    TIME_ZONE = 0
                if keyword == '/time set night':
                    WORDS_IN_CHAT = WORDS_IN_CHAT + f'\nTime set to night'
                    TIME_ZONE = 20000
                self.set_exclusive_mouse(True)
                
                
            
                
                
            elif symbol == key.SPACE:
                self.jumping = True
            elif symbol == key.ESCAPE:
                self.set_exclusive_mouse(False)
            elif symbol == key.LSHIFT:
                self.crouch = True
                if self.sprinting:
                    self.fov_offset -= SPRINT_FOV
                    self.sprinting = False
            elif symbol == key.R:
                if not self.crouch:
                    if not self.sprinting:
                        self.fov_offset += SPRINT_FOV
                    self.sprinting = True
            if creative:
                if symbol == key.TAB:
                    self.flying = not self.flying
            if creative:
                if symbol == key.I:
                    item = pyautogui.confirm(title=f'{TITLE}', text='Inventory\n\nSelect item', buttons=['Grass', 'Dirt', 'Stone', 'Bedrock', 'Diamond', 'Gold', 'Wood', 'Birch Wood', 'Leaf', 'Sand', 'Brick', 'Wooden Plank', 'Cobblestone', 'Glass', 'Cactus'])
                    if item == 'Grass': self.block = GRASS
                    if item == 'Dirt': self.block = DIRT
                    if item == 'Stone': self.block = STONE
                    if item == 'Bedrock': self.block = BEDROCK
                    if item == 'Diamond': self.block = DIAMOND
                    if item == 'Gold': self.block = GOLD
                    if item == 'Wood': self.block = WOOD
                    if item == 'Birch Wood': self.block = WOOD2
                    if item == 'Leaf': self.block = LEAF
                    if item == 'Sand': self.block = SAND
                    if item == 'Brick': self.block = BRICK
                    if item == 'Wooden Plank': self.block = WOOD_PLANK
                    if item == 'Cobblestone': self.block = COBBLESTONE
                    if item == 'Glass': self.block = GLASS
                    if item == 'Cactus': self.block = CACTUS
                    del item
            if survival:
                if symbol == key.E:
                    try:
                        craft_item = pyautogui.confirm(title=TITLE, text=f'Do you want to craft this item?', buttons=['Craft', 'Cancel'])
                        if craft_item == 'Cancel': pass
                        elif craft_item == 'Craft':
                            if self.block == WOOD: self.block = WOOD_PLANK
                            elif self.block == WOOD2: self.block = WOOD_PLANK
                            elif self.block == DIRT: self.block = GRASS
                            elif self.block == WOOD_PLANK: self.block = WOOD
                            elif self.block == GRASS: self.block = DIRT
                            elif self.block == SAND: self.block = GLASS
                            elif self.block == GLASS: self.block = DIAMOND
                            elif self.block == STONE: self.block = COBBLESTONE
                            elif self.block == COBBLESTONE: self.block = SAND
                            elif self.block == CACTUS: self.block = WOOD
                            elif self.block == GOLD: self.block = BRICK
                            elif self.block == DIAMOND: self.block = COBBLESTONE
                            elif self.block == BRICK: self.block = COBBLESTONE
                            elif self.block == LEAF: self.block = GRASS
                            else: pyautogui.alert(title=TITLE, text='Failed to craft item', button='Alright')
                        del craft_item
                    except:
                        pyautogui.alert(title=TITLE, text='No item in hand to craft', button='Alright')

        def on_key_release(self, symbol, modifiers):
            if symbol == key.W:
                self.strafe[0] += 1
            elif symbol == key.S:
                self.strafe[0] -= 1
            elif symbol == key.A:
                self.strafe[1] += 1
            elif symbol == key.D:
                self.strafe[1] -= 1
            elif symbol == key.SPACE:
                self.jumping = False
            elif symbol == key.LSHIFT:
                self.crouch = False
            elif symbol == key.C:
                self.fov_offset += 60.0

        def on_resize(self, width, height):
            self.label.y = height - 10
            if self.reticle:
                self.reticle.delete()
            x, y = self.width // 2, self.height // 2
            n = 10
            self.reticle = pyglet.graphics.vertex_list(4,
                ('v2i', (x - n, y, x + n, y, x, y - n, x, y + n))
            )

        def set_2d(self):
            width, height = self.get_size()
            glDisable(GL_DEPTH_TEST)
            viewport = self.get_viewport_size()
            glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(0, max(1, width), 0, max(1, height), -1, 1)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

        def set_3d(self):
            width, height = self.get_size()
            glEnable(GL_DEPTH_TEST)
            viewport = self.get_viewport_size()
            glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(PLAYER_FOV + self.fov_offset, width / float(height), 0.1, 60.0)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            x, y = self.rotation
            glRotatef(x, 0, 1, 0)
            glRotatef(-y, math.cos(math.radians(x)), 0, math.sin(math.radians(x)))
            x, y, z = self.position
            if self.crouch:
                glTranslatef(-x, -y+0.2, -z)
            else:
                glTranslatef(-x, -y, -z)
        def time_system(self):
            global TIME_ZONE
            global BL_SKY
            if TIME_ZONE == 0:
                BL_SKY = False
                sky_r = 12.5 / grp
                sky_g = 12.69 / grp
                sky_b = grp * 897
                sky_trans = 0
                glEnable(GL_FOG)
                glClearColor(sky_r, sky_g, sky_b, sky_trans)
                glDisable(GL_LIGHTING)
                glEnable(GL_LIGHT0)
                glEnable(GL_LIGHT1)
                glEnable(GL_LIGHT2)
                glEnable(GL_LIGHT3)
                glEnable(GL_LIGHT4)
                glEnable(GL_LIGHT5)
                glEnable(GL_LIGHT6)
                glEnable(GL_LIGHT7)
                TIME_ZONE = TIME_ZONE + 1
            else:
                if TIME_ZONE != 20000:
                    if TIME_ZONE != 40000:
                        TIME_ZONE = TIME_ZONE + 1
            if TIME_ZONE == 20000:
                BL_SKY = True
                glDisable(GL_FOG)
                sky_r = 0
                sky_g = 0
                sky_b = 0
                sky_trans = 0
                glClearColor(sky_r, sky_g, sky_b, sky_trans)
                glEnable(GL_LIGHTING)
                glEnable(GL_LIGHT0)
                glDisable(GL_LIGHT1)
                glDisable(GL_LIGHT2)
                glDisable(GL_LIGHT3)
                glDisable(GL_LIGHT4)
                glEnable(GL_LIGHT5)
                glDisable(GL_LIGHT6)
                glDisable(GL_LIGHT7)
                TIME_ZONE = TIME_ZONE + 1
            else:
                if TIME_ZONE != 1:
                    if TIME_ZONE != 20000:
                        if TIME_ZONE != 40000:
                            TIME_ZONE = TIME_ZONE + 1
            if TIME_ZONE == 40000: TIME_ZONE = 0
            if BL_SKY:
                sky_r = 0
                sky_g = 0
                sky_b = 0
                sky_trans = 0
                glClearColor(sky_r, sky_g, sky_b, sky_trans)



        def on_draw(self):
            self.clear()
            self.set_3d()
            glColor3d(1, 1, 1)
            self.model.batch.draw()
            self.draw_focused_block()
            self.set_2d()
            self.draw_label()
            self.draw_reticle()
            self.time_system()

        def draw_focused_block(self):
            vector = self.get_sight_vector()
            block = self.model.hit_test(self.position, vector)[0]
            if block:
                x, y, z = block
                vertex_data = cube_vertices(x, y, z, 0.51)
                glColor3d(0, 0, 0)
                glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
                pyglet.graphics.draw(24, GL_QUADS, ('v3f/static', vertex_data))
                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        def draw_label(self):
            x, y, z = self.position
            if survival:
                if y < 0:
                    self.set_exclusive_mouse(False)
                    try:
                        turtle.title(f'{TITLE}')
                    except:
                        turtle.title(f'{TITLE}')
                    turtle.bgcolor('#8B0000')
                    turtle.speed(0)
                    turtle.write('You Died!', font=('Arial', 32, 'bold'))
                    turtle.hideturtle()
                    turtle.penup()
                    turtle.right(90)
                    turtle.forward(100)
                    turtle.back(50)
                    turtle.write(f'{username} fell out of the map.\nPress F to exit', font=('Arial', 16, 'normal'))
                    turtle.onkey(exit, 'f')
                    turtle.listen()
                    turtle.mainloop()
                    turtle.bye()
            if 400 < y: glClearColor(0, 0, 0, 0)
            if y < 400: glClearColor(float(sky_r), float(sky_g), float(sky_b), float(sky_trans))
            if not BL_SKY: sky_tone = (sky_r + sky_b, sky_g + sky_b, sky_b * 8, sky_trans)
            else: sky_tone = (0, 0, 0, 0)
            global gen
            self.label.text = f'FPS: {int(pyglet.clock.get_fps())} Average FPS: {int(average(int(pyglet.clock.get_fps())))} Position: x={int(x)} y={int(y)} z={int(z)} Sky RGBA: {sky_tone} Terrian Seed: {gen.seed} Time: {TIME_ZONE}'
            self.label.draw()

        def draw_reticle(self):
            glColor3d(0, 0, 0)
            self.reticle.draw(GL_LINES)


    def setup_fog():
        glFogfv(GL_FOG_COLOR, (GLfloat * 4)(0.5, 0.69, 1.0, 1))
        glHint(GL_FOG_HINT, GL_DONT_CARE)
        glFogi(GL_FOG_MODE, GL_LINEAR)
        glFogf(GL_FOG_START, 40.0 - float(grp))
        glFogf(GL_FOG_END, 60.0 + float(grp))
    def setup_high_quality():
        for light_power in range(int(grp) * 2):
            glFogfv(GL_FOG_COLOR, (GLfloat * 4)(2.3, 4.4, 0.0, 241.6))
            glHint(GL_FOG_HINT, GL_DONT_CARE)
            glFogi(GL_FOG_MODE, GL_LINEAR)
            glFogf(GL_FOG_START, 40.0 - float(grp))
            glFogf(GL_FOG_END, 60.0 + float(grp))
            glFogf(GL_FOG_DENSITY, 23.5)
    def setup_double_high_quality():
        for light_power in range(int(grp) * 42):
            glFogfv(GL_FOG_COLOR, (GLfloat * 4)(2.3, 4.4, 0.0, 241.6))
            glHint(GL_FOG_HINT, GL_DONT_CARE)
            glFogi(GL_FOG_MODE, GL_LINEAR)
            glFogf(GL_FOG_START, 40.0 - float(grp))
            glFogf(GL_FOG_END, 60.0 + float(grp))
    def setup():
        global sky_r, sky_g, sky_b, sky_trans
        if BL_SKY == False:
            sky_r = 12.5 / grp
            sky_g = 12.69 / grp
            sky_b = grp * 897
            sky_trans = 0
            glClearColor(sky_r, sky_g, sky_b, sky_trans)
        if TIME_ZONE == 20000:
            sky_r = 0
            sky_g = 0
            sky_b = 0
            sky_trans = 0
            glClearColor(sky_r, sky_g, sky_b, sky_trans)
        glEnable(GL_CULL_FACE)
        global enable_graphics
        def enable_graphics():
            if 0 < grp:
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            if 0 < grp:
                print('Enabling shaders...')
                glEnable(GL_FOG)
                glDisable(GL_LIGHTING)
                glEnable(GL_LIGHT0)
                glEnable(GL_LIGHT1)
                glEnable(GL_LIGHT2)
                glEnable(GL_LIGHT3)
                glEnable(GL_LIGHT4)
                glEnable(GL_LIGHT5)
                glEnable(GL_LIGHT6)
                glEnable(GL_LIGHT7)
                glEnable(GL_BLEND)
                glBlendFunc(GL_ONE, GL_ONE)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
                glBindTexture(GL_TEXTURE_2D, 0)
                glEnable(GL_ALPHA_TEST)
                glShadeModel(GL_SMOOTH)
                glEnable(GL_LINE_SMOOTH)
                glEnable(GL_POLYGON_SMOOTH)
                glEnable(GL_POINT_SMOOTH)
                glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
                glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
                glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
                glClear(GL_COLOR_BUFFER_BIT)
                glEnable(GL_NORMALIZE)
                setup_fog()
                setup_high_quality()
                setup_double_high_quality()
                print('Shaders enabled')
        enable_graphics()
            



    def main():
        icon = pyglet.image.load('boblox\\icon.png')
        window = Window(width=1680, height=740, caption=f'{TITLE}', resizable=True)
        window.set_icon(icon)
        window.set_exclusive_mouse(True)
        setup()
        pyglet.app.run()
    try:
        main()
    except Exception as e:
        raise NotSoMinecraftError(e)

        



def recent_message():
    return keyword
def chat_script():
    return WORDS_IN_CHAT