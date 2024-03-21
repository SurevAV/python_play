from Class_names import *
from Class_rect import *
from Class_warestack import *
from Class_blit import *
from Class_obstacle import *

class class_dinosaur(class_stack_1,class_stack_2,class_blit_shift,class_obstacle_make):
    def __init__(self,x,y,stack):
        super().__init__()
        self.name = names.dinosaur
        self.is_not_transparent = 0
      
        self.on_ground = False
        self.no_delete = True
        self.armor = 20.0
   
        
        self.rect = class_rect(x, y, 64, 32)
        self.step = 125.0

        self.jump = 0.0
        

        
        self.direction = 1
        self.motion = 1
        self.frame = 1
        self.texture = stack.list_images.dinosaur
        self.texture_rect_list = stack.list_images.list_dinosaur_textures
        self.texture_shift_x = 2.0
        self.texture_shift_y = 2.0

        self.distance_target_1 = 320.0
        self.distance_target_2 = 300.0

        self.stack = stack
        self.list_objects = stack.list_objects

        
    def obstacle(self):
        self.position_in_level(class_obstacle(self.rect.x,self.rect.y, self.stack,
                 self.texture, self.texture_rect_list, self.frame, self.motion, self.direction,
                 self.texture_shift_x, self.texture_shift_y, self.rect.width, self.rect.height))
            
        
    
  
    def on_item(self, item,t_shift):
        if item.name == names.player and self.no_delete:
            self.motion = 6
            item.armor -= 50*t_shift
        elif item.name == names.stakes:
            self.armor = -1
            
    def update(self,t_shift):

        
  
        self.calculate_frame(t_shift)

        

        if self.no_delete:

            player_distance_x = self.rect.x - self.stack.player.rect.x
    
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



                

            self.motion = 0
            if abs(player_distance_x) < self.distance_target_1 and range_y1 < self.rect.y - self.stack.player.rect.y < range_y2:
                
                self.motion = 2
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
                                self.motion = 3
                                item.armor -= 50.0*t_shift
                            elif item.name != names.player and self.on_ground:
                                self.jump = 350.0
                                
                        self.position_in_level(self)
                      
                    elif self.direction == 1:
                        self.position_in_level(None)
                 
                        self.motion = 1
                    
                        self.rect.shift_x(self.step*t_shift)
                        
                        for item in self.stack.collision_list(self.rect):
                            self.rect.select_x(item.rect.x - self.rect.width)
                            if item.name == names.player:
                                self.motion = 3
                                item.armor -= 50.0*t_shift
                            elif item.name != names.player and self.on_ground:
                                self.jump = 350.0
                        self.position_in_level(self)
                        
            for item in self.stack.list_items:
                if item.name == names.bullet:
                    bullet_distance = self.rect.x - item.rect.x
                    if abs(bullet_distance) < 200.0 \
                       and 0.0 >= self.rect.y - item.rect.y >= -self.rect.height and self.on_ground:

                        self.distance_target_1 = 500.0
                        self.distance_target_2 = 450.0

                        if bullet_distance <0.0:
                            self.direction = 1
                        else:
                            self.direction = -1
                   
                        self.jump = 350.0
               
            if not self.on_ground:
                self.motion = 5
                        #print(item)
                        
                    
                    
             
            self.gravity(t_shift)

            if self.armor <= 0.0:
                self.motion = 7
                self.frame= 1.0
                self.no_delete = False
        else:
            self.gravity(t_shift)
     
            if int(self.frame)==5.0:
                self.position_in_level(None)
                
                self.obstacle()
                
                del self
