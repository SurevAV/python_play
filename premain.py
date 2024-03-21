import csv
from Class_rect import *


class class_cell():
    def __init__(self):
        super().__init__()
        self.object = None
        self.background = None

class class_stack():
    def __init__(self):
        super().__init__()
        
        self.list_objects = []
        self.list_items = []

        self.level_map = list(csv.reader(open('level_1 - level_1.csv', encoding='utf-8') , delimiter=','))
       
        self.size_level_y = float(len(self.level_map)*32)
        self.size_level_x = float(len(self.level_map[0])*32)

##        level_map = []
##        for i in range(200):
##            row = []
##            for j in range(200):
##
##                row.append('w|1')
##
##            level_map.append(row)
##
##
##        level_map[0][0] = "p"
##        level_map[1][0] = " "
##        self.level_map = level_map
        self.letter = None


        self.len_level_y = len(self.level_map)
        self.len_level_x = len(self.level_map[0])

        self.list_sound= None
        self.list_images = None

        self.player = None


        self.key_q = False
        self.key_w = False

        self.key_direction = 0
        self.key_a = False
        self.key_s = False
        self.key_d = False
        self.key_melee = 0

    def range_in_list(self,rect, shift_y1 ,shift_y2, shift_x, shift_x2):
        position_y = int(rect.y/32.0)
        from_y = position_y-shift_y1
        if from_y < 0:
            from_y = 0
        to_y = position_y+shift_y2
        if to_y > self.len_level_y:
            to_y = self.len_level_y

        position_x = int(rect.x/32.0)
        from_x = position_x-shift_x
        if from_x < 0:
            from_x = 0
        to_x = position_x+shift_x2
        if to_x > self.len_level_x:
            to_x = self.len_level_x
        return from_y, to_y, from_x, to_x


    def collision_list(self,rect):
        from_y, to_y, from_x, to_x = self.range_in_list(rect,2,3, 3,3)
     
        list_return = []
        
        for row in self.list_objects[from_y: to_y]:
            for item in row[from_x: to_x]:
            
                if item.object and rect.colliderect(item.object.rect):
                    list_return.append(item.object)
        #print(list_return)
        return list_return









