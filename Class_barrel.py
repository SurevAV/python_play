from Class_names import *
from Class_rect import *
from Class_warestack import *
from timeit import default_timer
from Class_blit import *
from Class_shift_item import *

class class_detonation():
    def __init__(self,x,y,stack):
        super().__init__()
        self.name = names.detonation

        self.armor = 100000
      
        
        self.rect = class_rect(x, y, 32, 32)

        self.direction = 1
        self.motion = 0
        self.frame = 0
        self.texture = stack.list_images.detonation
        self.texture_rect_list = [[(0,0,352, 352)]]
        self.texture_shift_x = 160
        self.texture_shift_y = 160
        self.make = default_timer()

        stack.list_sound.list_detonation[1].play()
       

        self.stack = stack
        self.list_objects = stack.list_objects

    def update(self,t_shift):
        if default_timer() - self.make > 0.10:

            position_y = int(self.rect.y/32.0)
            from_y = position_y-5
            if from_y < 0:
                from_y = 0
            to_y = position_y+6
            if to_y > self.stack.len_level_y:
                to_y = self.stack.len_level_y

            position_x = int(self.rect.x/32.0)
            from_x = position_x-5
            if from_x < 0:
                from_x = 0
            to_x = position_x+6
            if to_x > self.stack.len_level_x:
                to_x = self.stack.len_level_x

            
            #from_y, to_y, from_x, to_x = self.stack.range_in_list(self.rect,5,5, 5)
            for row in self.stack.list_objects[from_y: to_y]:
                for item in row[from_x: to_x]:
                    if item.object and ((item.object.rect.x - self.rect.x)**2 + \
                                        (item.object.rect.y - self.rect.y)**2)**0.5<165.0:
         
                        item.object.armor = -1
            self.armor = -1
            
    

class class_barrel(class_stack_1,class_stack_2,class_blit,class_shift_item):
    def __init__(self,x,y,stack):
        super().__init__()
        self.name = names.barrel
        self.is_not_transparent = 0
        self.on_ground = False
        self.armor = 20
        self.rect = class_rect(x, y, 32, 32)
      
        self.jump = 0.0
         
        self.texture = stack.list_images.barrel

        self.stack = stack
        self.list_objects = stack.list_objects

    def on_item(self, item,t_shift):
        if self.jump < -350:
            self.armor = -1.0


    
        

    def update(self,t_shift):
        
        self.gravity(t_shift)

        if self.armor <= 0.0:
            self.stack.list_items.append(class_detonation(self.rect.x,self.rect.y,self.stack))
            self.position_in_level(None)
            del self







