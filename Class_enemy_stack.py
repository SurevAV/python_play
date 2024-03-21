from Class_names import *
from Class_rect import *
from Class_warestack import *
import random
from Class_blit import *
from Class_obstacle import *
from Class_barrel import *
        
class class_enemy_warestack(class_obstacle_make):

             
    
    def update(self,t_shift):

        
  
        self.calculate_frame(t_shift)

        

        if self.no_delete:

            player_distance_x = self.rect.x - self.stack.player.rect.x
    
##            if self.on_ground and self.stack.player.on_ground:
##                range_y = 50.0
##            else:
##                range_y = 150.0

            if self.on_ground and self.stack.player.on_ground:
                range_y2 = 50.0
                range_y1 = -32.0
            elif not self.on_ground and self.stack.player.on_ground:
                range_y2 = 32.0
                range_y1 = -150.0
            elif self.on_ground and not self.stack.player.on_ground:
                range_y2 = 150.0
                range_y1 = -32.0
            elif not self.on_ground and not self.stack.player.on_ground:
                range_y2 = 150.0
                range_y1 = -150.0


                
            if self.frame < 1.5:
                self.motion = 0
            if abs(player_distance_x) < self.distance_target_1 and range_y1 < self.rect.y - self.stack.player.rect.y < range_y2:
                
                
                if player_distance_x <0.0:
                    self.direction = 1
                else:
                    self.direction = -1


                if 5.0 < abs(player_distance_x) < self.distance_target_2:
         
         
                    if self.direction == -1:
                        self.position_in_level(None)
                        self.motion = 1
                        self.rect.shift_x(-self.step*t_shift)
         
                        for item in self.stack.collision_list(self.rect):
                            self.rect.select_x(item.rect.right)
                            if item.name == names.player:
                               
                                self.motion = self.strike
                                if int(self.frame) == self.strike_frame:
                                    item.armor -= self.reduce_armor*t_shift
                            elif item.name != names.player and self.on_ground:
                                self.jump = 350
                                
                        self.position_in_level(self)
                      
                    elif self.direction == 1:
                        self.position_in_level(None)
                 
                        self.motion = 1
                    
                        self.rect.shift_x(self.step*t_shift)
                        
                        for item in self.stack.collision_list(self.rect):
                            self.rect.select_x(item.rect.x - self.rect.width)
                            if item.name == names.player:
                                
                                self.motion = self.strike
                                if int(self.frame) == self.strike_frame:
                                    item.armor -= self.reduce_armor*t_shift
                            elif item.name != names.player and self.on_ground:
                                self.jump = 350
                        self.position_in_level(self)
                        

               
            if not self.on_ground:
                self.motion = 1
                       
                    
                    
             
            self.gravity(t_shift)

            if self.armor <= 0.0:
                self.motion = self.motion_del
                self.frame= 1.0
                self.no_delete = False
        else:
            self.gravity(t_shift)
     
            if int(self.frame)==self.frame_del:
                self.position_in_level(None)
                
                self.obstacle()

                del self
    



class class_swordsman(class_stack_1,class_stack_2,class_enemy_warestack,class_blit_shift):
    def __init__(self,x,y,stack):
        super().__init__()
        self.name = names.swordsman
        self.is_not_transparent = 0
        self.on_ground = False
        self.no_delete = True
        self.armor = 10.0
   
        
        self.rect = class_rect(x, y, 32, 40)
        self.step = 100.0

        self.jump = 0.0
        

        
        self.direction = 1
        self.motion = 1
        self.frame = 1
        self.texture = stack.list_images.swordsman
        self.texture_rect_list = stack.list_images.list_swordsman_textures
        self.texture_shift_x = 10.0
        self.texture_shift_y = 21.0

        self.distance_target_1 = 320.0
        self.distance_target_2 = 300.0

        self.stack = stack
        self.list_objects = stack.list_objects

        self.strike = random.choice([2,5,6])


        self.motion_del = 4
        self.frame_del = 7

        self.strike_frame = 3
        self.reduce_armor = 100
        
    
        

  
    def on_item(self, item,t_shift):
        if item.name == names.player and self.no_delete:
            self.motion = 3
            item.armor -= 1*t_shift
        elif item.name == names.stakes:
            self.armor = -1



class class_swordsman_2(class_stack_1,class_stack_2,class_enemy_warestack,class_blit_shift):
    def __init__(self,x,y,stack):
        super().__init__()
        self.name = names.swordsman_2
        self.is_not_transparent = 0
        self.on_ground = False
        self.no_delete = True
        self.armor = 10.0
   
        
        self.rect = class_rect(x, y, 32, 40)
        self.step = 100.0

        self.jump = 0.0
        

        
        self.direction = 1
        self.motion = 1
        self.frame = 1
        self.texture = stack.list_images.swordsman_2
        self.texture_rect_list = stack.list_images.list_swordsman_2_textures
        self.texture_shift_x = 10.0
        self.texture_shift_y = 21.0

        self.distance_target_1 = 320.0
        self.distance_target_2 = 300.0

        self.stack = stack
        self.list_objects = stack.list_objects

        self.strike = random.choice([2,3,4])

        self.motion_del = 7
        self.frame_del = 7

        self.strike_frame = 3
        self.reduce_armor = 100
    
        

  
    def on_item(self, item,t_shift):
        if item.name == names.player and self.no_delete:
            self.motion = 5
            item.armor -= 1*t_shift
        elif item.name == names.stakes:
            self.armor = -1
            

class class_wood_enemy(class_stack_1,class_stack_2,class_enemy_warestack,class_blit_shift):
    def __init__(self,x,y,stack):
        super().__init__()
        self.name = names.wood_enemy
        self.is_not_transparent = 0
        self.on_ground = False
        self.no_delete = True
        self.armor = 10.0
   
        
        self.rect = class_rect(x, y, 32, 32)
        self.step = 100.0

        self.jump = 0.0
        

        
        self.direction = 1
        self.motion = 1
        self.frame = 1
        self.texture = stack.list_images.wood_enemy
        self.texture_rect_list = stack.list_images.list_wood_enemy_textures
        self.texture_shift_x = 16.0
        self.texture_shift_y = 32.0

        self.distance_target_1 = 320.0
        self.distance_target_2 = 300.0

        self.stack = stack
        self.list_objects = stack.list_objects

        self.strike = 2

        self.motion_del = 4
        self.frame_del = 5

        self.strike_frame = 5
        self.reduce_armor = 100
        
    def obstacle(self):
        pass
        

  
    def on_item(self, item,t_shift):
        if item.name == names.player and self.no_delete:
            self.motion = 3
            item.armor -= 1*t_shift
        elif item.name == names.stakes:
            self.armor = -1

class class_troll(class_stack_1,class_stack_2,class_enemy_warestack,class_blit_shift):
    def __init__(self,x,y,stack):
        super().__init__()
        self.name = names.troll
        self.is_not_transparent = 0
        self.on_ground = False
        self.no_delete = True
        self.armor = 200.0
   
        
        self.rect = class_rect(x, y, 64, 50)
        self.step = 75.0

        self.jump = 0.0
        

        
        self.direction = 1
        self.motion = 1
        self.frame = 1
        self.texture = stack.list_images.troll
        self.texture_rect_list = stack.list_images.list_troll_textures
        self.texture_shift_x = 0.0
        self.texture_shift_y = 14.0

        self.distance_target_1 = 320.0
        self.distance_target_2 = 300.0

        self.stack = stack
        self.list_objects = stack.list_objects

        self.strike = 2

        self.motion_del = 3
        self.frame_del = 6

        self.strike_frame = 5
        self.reduce_armor = 100

  
    
        

  
    def on_item(self, item,t_shift):
        if item.name == names.player and self.no_delete:
            item.armor -= 1000*t_shift
        elif item.name == names.stakes:
            self.armor = -1
