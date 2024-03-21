from Class_names import *
from Class_rect import *

from Class_blit import *


class class_wall(class_blit):
    def __init__(self,x,y,stack):
        super().__init__()
        self.name = names.wall
      
        self.is_not_transparent = 1
     
        
        self.armor = 200.0
        
     
        self.rect = class_rect(x, y, 32, 32)

     
        self.y = int(self.rect.y/32)
        self.x = int(self.rect.x/32)
        
    
##        if self.y >0 and stack.list_objects[self.y-1][self.x ].object and \
##           stack.list_objects[self.y-1][self.x].object.name == names.wall:
##            self.number_texture = 1
##        else:
##            self.number_texture = 0
        self.texture = stack.list_images.list_wall[1]

        self.stack = stack
        self.list_objects = stack.list_objects

        
    def update(self,t_shift):
      
    
        if self.armor <= 0.0:
            self.texture = self.stack.list_images.list_background_wall[1]

            self.list_objects[self.y][self.x].object = None
            self.list_objects[self.y][self.x].background = self
            #self.stack.list_sound.list_destruction[1].play()
##
##
##            if self.y <len(self.list_objects)-1 and self.list_objects[self.y+1][self.x].object and \
##               self.list_objects[self.y+1][self.x].object.name == names.wall:
##                self.list_objects[self.y+1][self.x].object.texture = self.stack.list_images.list_wall[2]

    def check(self,x,y):
        return self.list_objects[y][x].object and self.list_objects[y][x].object.name == names.wall
            
        
    def make(self):
        if self.armor <= 0:
          
            self.texture = self.stack.list_images.list_background_wall[1]

    
            if self.y <len(self.list_objects)-1 and self.list_objects[self.y+1][self.x].object and \
               self.list_objects[self.y+1][self.x].object.name == names.wall:
                self.list_objects[self.y+1][self.x].object.texture = self.stack.list_images.list_wall[2]

      
        elif self.x > 1 and self.x < len(self.list_objects[0])-1 and \
             self.y > 1 and self.y < len(self.list_objects)-1 and self.armor >= 0:
            
            

            x = self.x
            y = self.y
          

            if  not self.check(x-1, y) and  not self.check(x, y-1) and  self.check(x+1, y) and  self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['left_up']
            elif self.check(x-1, y) and  not self.check(x, y-1) and  self.check(x+1, y) and  self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['up']

            elif self.check(x-1, y) and  not self.check(x, y-1) and  not self.check(x+1, y) and  self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['up_right']

            elif self.check(x-1, y) and  self.check(x, y-1) and  self.check(x+1, y) and not self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['down']

            elif not self.check(x-1, y) and  self.check(x, y-1) and  self.check(x+1, y) and  self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['left']

            elif  self.check(x-1, y) and   self.check(x, y-1) and  not self.check(x+1, y) and  self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['right']

            elif not self.check(x-1, y) and  self.check(x, y-1) and  self.check(x+1, y) and  not self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['left_down']

            elif  self.check(x-1, y) and   self.check(x, y-1) and not self.check(x+1, y) and not self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['down_right']

            elif not self.check(x-1, y) and  not self.check(x, y-1) and not self.check(x+1, y) and not self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['left_up_right_down']

            elif not self.check(x-1, y) and  not self.check(x, y-1) and  self.check(x+1, y) and not self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['left_up_down']

            elif  self.check(x-1, y) and  not self.check(x, y-1) and  self.check(x+1, y) and not self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['up_down']

            elif self.check(x-1, y) and  not self.check(x, y-1) and not self.check(x+1, y) and not self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['up_down_right']

            elif not self.check(x-1, y) and  not self.check(x, y-1) and not self.check(x+1, y) and self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['left_up_right']

            elif not self.check(x-1, y) and  self.check(x, y-1) and not self.check(x+1, y) and self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['left_right']

            elif not self.check(x-1, y) and  self.check(x, y-1) and not self.check(x+1, y) and not self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['left_down_right']

            elif  self.check(x-1, y) and   self.check(x, y-1) and  self.check(x+1, y) and  self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['empty']
              
            if not self.check(x+1, y+1) and self.check(x-1, y) and self.check(x, y-1) and self.check(x+1, y) and self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['inside_down_right']
            elif not self.check(x-1, y+1) and self.check(x-1, y) and self.check(x, y-1) and self.check(x+1, y) and self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['inside_left_down']
            elif not self.check(x+1, y-1) and self.check(x-1, y) and self.check(x, y-1) and self.check(x+1, y) and self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['inside_up_right']
            elif not self.check(x-1, y-1) and self.check(x-1, y) and self.check(x, y-1) and self.check(x+1, y) and self.check(x, y+1):
                self.texture = self.stack.list_images.dict_wall['inside_left_up']
                
 

            

class class_stakes(class_blit):
    def __init__(self,x,y,stack):
        super().__init__()
        self.name = names.stakes
        self.is_not_transparent = 0
    
        self.armor = 200.0
        self.rect = class_rect(x, y, 32, 32)
        self.texture = stack.list_images.list_stakes[0]

        self.y = int(self.rect.y/32)
        self.x = int(self.rect.x/32)

        self.stack = stack
        self.list_objects = stack.list_objects

    def update(self,t_shift):
        if self.armor < 0.0:
            self.list_objects[self.y][self.x].object = None
            del self

   


                
            

  
