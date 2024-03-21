from Class_names import *
from Class_rect import *
from Class_blit import *

class class_backside(class_blit):
    def __init__(self,x,y, stack,item):
        super().__init__()
        self.name = names.backside
      
        self.is_not_transparent = 0
        self.texture = stack.list_images.dict_backside[item]

        

        self.y_size = self.texture.get_size()[1]
        self.x_size = self.texture.get_size()[0]
        self.stack = stack
        

        
        if self.y_size > 32:
            self.rect = class_rect(x, y-(self.y_size - 32), 32, 32)
        elif self.y_size == 32:
            self.rect = class_rect(x, y, 32, 32)
        elif self.y_size < 32:
            self.rect = class_rect(x, y+(32-self.y_size), 32, 32)

        self.is_rendering = False

        

    def round_int(self,x):
        return int(-1 * x // 1 * -1)

    def make(self):
        
        y = int(self.rect.y/32)
        x = int(self.rect.x/32)

        size_x = self.round_int(self.x_size/32)
        size_y = self.round_int(self.y_size/32)

        if size_x > 1:
            self.stack.list_objects[y][x+size_x].background = self
        if size_y > 1:
            self.stack.list_objects[y+size_y][x].background = self
        if size_x >1 and size_y>1:
            self.stack.list_objects[y+size_y][x+size_x].background = self

      
            
        
        

        
       
 


        
