from Class_names import *
from Class_rect import *
from Class_warestack import *
from timeit import default_timer
from Class_bullet import *
from Class_blit import *
from Class_obstacle import *


class class_treasure_hunter(class_stack_1,class_stack_2,class_blit_shift,class_obstacle_make):
    def __init__(self,x,y, stack):
        super().__init__()
        self.name = names.treasure_hunter
        self.is_not_transparent = 0
        self.on_ground = False
        self.no_delete = True
        self.armor = 20.0
   
        
        self.rect = class_rect(x, y, 32, 45)
        self.step = 125.0

        self.jump = 0.0
        

        
        self.direction = 1
        self.motion = 0
        self.frame = 1
        self.texture = stack.list_images.treasure_hunter
        self.texture_rect_list = stack.list_images.list_treasure_hunter_textures
        self.texture_shift_x = 48.0
        self.texture_shift_y = 19.0

       
        self.cd_bullets = 1
      

        self.stack = stack
        self.list_objects = stack.list_objects

        self.key_a = False
        self.key_w = False
        self.key_s = False
        self.key_d = False
        self.key_q = False
        self.key_melee = 0 # 3 4

    def obstacle(self):
        self.position_in_level(class_obstacle(self.rect.x,self.rect.y, self.stack,
                 self.texture, self.texture_rect_list, self.frame, self.motion, self.direction,
                 self.texture_shift_x, self.texture_shift_y, self.rect.width, self.rect.height))
            
        
    
  

    def on_item(self, item,t_shift):
        if item.name == names.stakes:
            self.armor = -1


    def move(self,t_shift):
        if self.key_a:
            self.position_in_level(None)
            self.direction = -1
            if (self.frame > self.texture_rect_list[self.motion][0]) or self.motion  == 0:
                self.motion = 1
            self.rect.shift_x(-self.step*t_shift)
 
            for item in self.stack.collision_list(self.rect):
                if item.name != names.player and self.on_ground:
                    self.jump = 350

                self.rect.select_x(item.rect.right)
                
            self.position_in_level(self)
                
        elif self.key_d:
            self.position_in_level(None)
            self.direction = 1
            if (self.frame > self.texture_rect_list[self.motion][0]) or self.motion  == 0:
                self.motion = 1
            
            self.rect.shift_x(self.step*t_shift)
                
            for item in self.stack.collision_list(self.rect):
                if item.name != names.player and self.on_ground:
                    self.jump = 350
        
                self.rect.select_x(item.rect.x - self.rect.width)
                        
            self.position_in_level(self)
        else:
            if self.motion == 1 and self.on_ground:
                self.motion = 0
                    
                    
        if self.key_w and self.on_ground:
            if (self.frame > self.texture_rect_list[self.motion][0]) or self.motion  == 0:
                self.motion = 1
            self.jump = 350

        if self.key_melee > 0 and default_timer() - self.cd_bullets > 0.5:

            self.cd_bullets = default_timer()
            self.frame= 1.0
            self.motion = self.key_melee
            self.stack.list_sound.melee_list[self.key_melee-3].play()
                
        if int(self.frame) == 3  and (self.motion == 3 or self.motion == 4):

            if self.motion == 4:
                widht = 52
                height = 25
            elif self.motion == 3:
                widht = 40
                height = 55
                    
            if self.direction == 1:
                rect = class_rect(self.rect.right+1, self.rect.y-5, widht, height)
            else:
                rect = class_rect(self.rect.x-widht-1, self.rect.y-5, widht, height)
                    
            for item in self.stack.collision_list(rect):
          
                if self.motion==3 and item.name == names.dinosaur:
                    pass
                else:
                    item.armor -= 100*t_shift
                        
        if self.key_q:
            if default_timer() - self.cd_bullets > 0.5:
                self.cd_bullets = default_timer()
                self.frame= 1.0
            
                self.motion = 5
                    
                if self.direction == 1:
                    self.stack.list_items.append(class_bullet(self.rect.x+self.rect.width+2,
                                                       self.rect.y + 20,self.direction,self.stack))
                else:
                    self.stack.list_items.append(class_bullet(self.rect.x-28-2,
                                                       self.rect.y + 20,self.direction,self.stack))
       
                        
                        
        
        
            
    def update(self,t_shift):

        self.calculate_frame(t_shift)

        
        if self.no_delete:

            self.key_a = False
            self.key_w = False
            self.key_s = False
            self.key_d = False
            self.key_q = False
            self.key_melee = 0 # 3 4

            for item in self.stack.list_items:
                if item.name == names.bullet:
                    bullet_distance = self.rect.x - item.rect.x
                    if abs(bullet_distance) < 200.0 \
                       and 0.0 >= self.rect.y - item.rect.y >= -self.rect.height and self.on_ground:

                     

                        if bullet_distance <0.0:
                            self.direction = 1
                            if item.direction == -1:
                                self.key_w  = True
                                
                            
                        else:
                            self.direction = -1
                            if item.direction == 1:
                                self.key_w  = True
                   
                        

            
            player_distance_x = self.rect.x - self.stack.player.rect.x
            player_distance_y = self.rect.y - self.stack.player.rect.y

            if abs(player_distance_x) < 45.0 and abs(player_distance_y) < 50.0:
                if player_distance_x < 0.0:
                    self.direction = 1
                else:
                    self.direction = -1

                self.key_melee= 4

            if abs(player_distance_x) < 400.0 and abs(player_distance_y) < 10.0:
                if player_distance_x < 0.0:
                    self.direction = 1
                else:
                    self.direction = -1

                self.key_q= True

            if abs(player_distance_x) < 400.0 and player_distance_y > 20.0:
                self.key_w= True

            if abs(player_distance_x) < 400.0 and abs(player_distance_y) < 200.0:
                if abs(player_distance_x) > 250.0:
                    if player_distance_x < 0:
                        self.direction = 1
                        self.key_d= True
                    else:
                        self.direction = -1
                        self.key_a= True
                    
                
            

            
            
            self.move(t_shift)
            
            self.gravity(t_shift)

            if self.armor <= 0.0:
                self.motion = 6
                self.frame= 1.0
                self.no_delete = False
        else:
            self.gravity(t_shift)
     
            if int(self.frame)==4.0:
                self.position_in_level(None)
                
                self.obstacle()
                
                del self
             
