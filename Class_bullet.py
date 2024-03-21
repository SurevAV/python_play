from Class_names import *
from Class_rect import *
from Class_warestack import *
import random


class class_bullet():
    def __init__(self,x,y, direction,stack):
        super().__init__()
        self.name = names.bullet

        self.armor = 100
      
        
        self.rect = class_rect(x, y, 28, 2)

        self.direction = direction
        self.motion = 0
        self.frame = 1
        self.texture = stack.list_images.bullet
        self.texture_rect_list = stack.list_images.list_bullet_textures
        self.texture_shift_x = 0
        self.texture_shift_y = 0
        self.step = 1000.0


         
        stack.list_sound.bullet_list[random.randint(0, len(stack.list_sound.bullet_list)-1)].play()
        self.stack = stack
        self.list_objects = stack.list_objects
        
        
    def update(self,t_shift):
        self.frame += 5*t_shift
        if self.frame > self.texture_rect_list[self.motion][0]:
            self.frame= 1


       
        self.rect.shift_x(self.step*t_shift*self.direction) 
        for item in self.stack.collision_list(self.rect):
            if abs(self.rect.center_rect_x() - item.rect.center_rect_x())<20:
            
                
                
                self.stack.list_sound.list_bullet_in_target[0].play()
                
                if item.name == names.troll:
                    if self.rect.y - item.rect.y < 20.0:
                        item.armor = -1
                        self.armor = -1
                    else:
                        
                        if random.randint(0, 1)> 0:
                            self.direction *= -1
                            self.rect.shift_x(self.step*t_shift*self.direction)
                        else:
                            item.armor -= 10
                            self.armor = -1
                        
                else:
                    item.armor -= 10
                    self.armor = -1



