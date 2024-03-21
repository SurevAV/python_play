from Class_names import *
from Class_rect import *
from Class_warestack import *
from timeit import default_timer
from Class_bullet import *
from Class_blit import *

class class_player(class_stack_1,class_stack_2,class_blit_shift):
    def __init__(self,x,y, stack):
        super().__init__()
        self.name = names.player
        self.is_not_transparent = 0
        self.on_ground = False
        self.no_delete = True
        self.armor = 100.0
   
        
        self.rect = class_rect(x, y, 32, 45)
        self.step = 150.0

        self.jump = 0.0
        

        
        self.direction = 1
        self.motion = 0
        self.frame = 1
        self.texture = stack.list_images.player
        self.texture_rect_list = stack.list_images.list_player_textures
        self.texture_shift_x = 48.0
        self.texture_shift_y = 19.0

        self.bullets = 50
        self.cd_bullets = 1.0
       

        self.stack = stack
        self.list_objects = stack.list_objects

        #return----------------
        self.return_time = default_timer()
        self.return_x = self.rect.x
        self.return_y = self.rect.y
  

    def on_item(self, item,t_shift):
        if item.name == names.stakes:
            self.armor = -1
            
    def update(self,t_shift):

        self.calculate_frame(t_shift)

        
        if self.no_delete:
            
            if default_timer()-self.return_time> 120.0 and self.on_ground and abs(self.rect.x - self.return_x)>400.0:
                self.return_x = self.rect.x
                self.return_y = self.rect.y
                self.return_time = default_timer()

     
            if self.stack.key_a:
                self.position_in_level(None)
                self.direction = -1
                if (self.frame > self.texture_rect_list[self.motion][0]) or self.motion  == 0:
                    self.motion = 1
                self.rect.shift_x(-self.step*t_shift)
 
                for item in self.stack.collision_list(self.rect):
                    
                    if item.name == names.barrel or item.name == names.obstacle:
                        #item.shift_item(self.direction*self.step*t_shift)
                        item.shift_item(self.rect.x-item.rect.width-0.1)
                  
                    self.rect.select_x(item.rect.right)
                        
                    
                    
                self.position_in_level(self)
                
            elif self.stack.key_d:
                self.position_in_level(None)
                self.direction = 1
                if (self.frame > self.texture_rect_list[self.motion][0]) or self.motion  == 0:
                    self.motion = 1
            
                self.rect.shift_x(self.step*t_shift)
                
                for item in self.stack.collision_list(self.rect):
                    
                    if item.name == names.barrel or item.name == names.obstacle:
                        #item.shift_item(self.direction*self.step*t_shift)
                        item.shift_item(self.rect.right+0.1)
                   
                    self.rect.select_x(item.rect.x - self.rect.width)
                        
                self.position_in_level(self)
            else:
                if self.motion == 1 and self.on_ground:
                    self.motion = 0
                    
                    
            if self.stack.key_w and self.on_ground:
                if (self.frame > self.texture_rect_list[self.motion][0]) or self.motion  == 0:
                    self.motion = 1
                self.jump = 350

            if self.stack.key_melee > 0 and default_timer() - self.cd_bullets > 0.5:

                self.cd_bullets = default_timer()
                self.frame= 1.0
                self.motion = self.stack.key_melee
                self.stack.list_sound.melee_list[self.stack.key_melee-3].play()
                


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
                        
                    

            if self.stack.key_q:
                if self.bullets > 0 and default_timer() - self.cd_bullets > 0.5:
                    self.cd_bullets = default_timer()
                    self.frame= 1.0
                    self.bullets-=1
                    self.motion = 5
                    
                    if self.direction == 1:
                        self.stack.list_items.append(class_bullet(self.rect.x+self.rect.width+2,
                                                       self.rect.y + 20,self.direction,self.stack))
                    else:
                        self.stack.list_items.append(class_bullet(self.rect.x-28-2,
                                                       self.rect.y + 20,self.direction,self.stack))
       
                        
                        
            self.gravity(t_shift)

            if self.armor <= 0.0:
                self.motion = 6
                self.frame= 1.0
                self.no_delete = False
        else:
            self.gravity(t_shift)
     
            if int(self.frame)==4.0:
                self.position_in_level(None)
                self.rect.select_x(self.return_x)
                self.rect.select_y(self.return_y)
                self.no_delete = True
                self.armor = 100
                self.motion = 0
                self.position_in_level(self)
