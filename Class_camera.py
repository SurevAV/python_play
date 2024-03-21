from Class_rect import *

class class_camera():
    def __init__(self,x,y):
        self.rect = class_rect(x, y, 32, 32)

    def shift(self, x,y):
        shift_x = x-self.rect.x 
        shift_y = y-self.rect.y 
        

        if abs(shift_x) > 20.0:
            self.rect.x += shift_x/35
            
        if abs(shift_y) > 20.0:
            self.rect.y += shift_y/35
