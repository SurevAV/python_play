from Class_names import *
from Class_rect import *
from Class_warestack import *
import pygame
from Class_blit import *

class class_stone(class_stack_1,class_stack_2,class_blit_shift):
    def __init__(self,x,y, direction,stack):
        self.name = names.stone
        self.is_not_transparent = 0
        self.on_ground = False
        
        self.armor = 10000
        self.rect = class_rect(x, y, 64, 64)
        self.step = 150.0
        self.jump = 0
        

        
        self.direction = direction
        self.motion = 0
        self.frame = 1
        self.texture = stack.list_images.stone
        self.texture_rect_list = stack.list_images.list_stone_textures_rect
        self.texture_shift_x = 0
        self.texture_shift_y = 0


        self.stack = stack
        self.list_objects = stack.list_objects

    def on_item(self, item,t_shift):
        if item.name == names.player:
            item.armor -= 5000*t_shift

        

    def update(self,t_shift):
        self.calculate_frame(t_shift)

        self.position_in_level(None)
        self.rect.shift_x(self.step*t_shift*self.direction)
        
        chanel = pygame.mixer.Channel(0)
        if not chanel.get_busy() and self.on_ground:
            chanel.play(self.stack.list_sound.list_rolling[0])
        
        for item in self.stack.collision_list(self.rect):

            item.armor -= 5000*t_shift
            self.armor -= 5000*t_shift
                
            if self.direction == -1:
                self.rect.select_x(item.rect.right)
            else:
                self.rect.select_x(item.rect.x - self.rect.width)

        self.position_in_level(self)

   
        self.gravity(t_shift)

        if self.armor <= 0:
            self.position_in_level(None)
            del self
