from Class_rect import *

class class_shift_item():
    def shift_item(self,x):

        self.position_in_level(None)
        
        if x < self.rect.x:
            self.rect.select_x(x)
            for item in self.stack.collision_list(self.rect):
                if item != self:
                    self.rect.select_x(item.rect.right)
           
        else:
            self.rect.select_x(x)
            for item in self.stack.collision_list(self.rect):
                if item != self:
                    self.rect.select_x(item.rect.x - self.rect.width)
         
  
        self.position_in_level(self)
