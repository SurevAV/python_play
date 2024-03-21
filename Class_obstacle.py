from Class_names import *
from Class_rect import *
from Class_warestack import *
from Class_blit import *
from Class_shift_item import *

class class_obstacle_make():
    def obstacle(self):
        item = class_obstacle(self.rect.x,self.rect.y, self.stack,
                 self.texture, self.texture_rect_list, self.frame, self.motion, self.direction,
                 self.texture_shift_x, self.texture_shift_y, self.rect.width, self.rect.height)
        y = int(item.rect.y/32.0)
        x = int(item.rect.x/32.0)
        self.list_objects[y][x].object = item
        
    

class class_obstacle(class_stack_1,class_stack_2,class_blit_shift,class_shift_item):
    def __init__(self,x,y, stack,
                 texture, texture_rect_list, frame, motion, direction,
                 texture_shift_x, texture_shift_y, size_x, size_y):
        super().__init__()
        self.name = names.obstacle
        self.is_not_transparent = 0
        self.on_ground = False
        self.armor = 20.0

        distance = size_y - 32.0 
   
        self.rect = class_rect(x, y+distance, size_x, 32.0)

        self.jump = -5.0
        self.direction = direction
        self.motion = motion
        self.frame = frame
        self.texture = texture
        self.texture_rect_list = texture_rect_list
        self.texture_shift_x = texture_shift_x
        self.texture_shift_y = texture_shift_y + distance
        self.stack = stack
        self.list_objects = stack.list_objects

       

  
            
    def update(self,t_shift):

        if self.armor <= 0:
            
            self.position_in_level(None)
            del self

        else:
            self.gravity(t_shift)
 
