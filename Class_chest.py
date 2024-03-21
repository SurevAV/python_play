from Class_names import *
from Class_rect import *
from Class_warestack import *
from timeit import default_timer
from Class_bullet import *
from Class_blit import *

class class_chest(class_stack_1,class_stack_2,class_blit_shift):
    def __init__(self,x,y, stack):
        super().__init__()
        self.name = names.chest
        self.is_not_transparent = 0
        self.on_ground = False
        self.no_delete = True
        self.armor = 10.0

        self.rect = class_rect(x, y, 32, 64)
        
        self.direction = 1
        self.motion = 0
        self.frame = 1
        self.texture = stack.list_images.chest
        self.texture_rect_list = stack.list_images.list_chest_textures
        self.texture_shift_x = 0
        self.texture_shift_y = 0

        self.stack = stack
        self.list_objects = stack.list_objects
  


            
    def update(self,t_shift):


        if self.no_delete:
            if abs(self.rect.x - self.stack.player.rect.x)<34 and \
               abs(self.rect.y - self.stack.player.rect.y)<34:
                self.stack.player.armor = 100
                self.stack.player.bullets = 50
                self.armor = -1
                self.no_delete = False
                
            if self.armor <= 0.0:
                self.no_delete = False
        else:
            self.calculate_frame(t_shift)
           
     
            if int(self.frame)==4.0:
                self.position_in_level(None)
                del self
