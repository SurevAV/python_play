from Class_rect import *
from Class_names import *
from Class_warestack import *
from timeit import default_timer

class class_letter(class_stack_1):
    def __init__(self,x,y,stack,letter):
        self.rect = class_rect(x, y, 32, 32)
        self.name = names.letter
        self.is_not_transparent = 0
        self.armor = 10000

        self.letter =letter.split('-')
        self.stack = stack
        self.in_screen = False
        self.cd = 0
        self.list_objects = stack.list_objects

  
      
        
    def update(self,t_shift):
        if not self.in_screen:
            self.cd = default_timer()
            self.in_screen = True
            self.stack.letter = self
        
        if default_timer() - self.cd > 15.0:
            self.stack.letter = None
            self.position_in_level(None)
            del self

        
     
    def blit_object(self, shift_x, shift_y, screen):
        pass
        

