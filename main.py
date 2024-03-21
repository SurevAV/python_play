from premain import *
from Class_wall import *
from Class_names import *
from Class_bullet import *
from Class_warestack import *
from Class_stone import *
from Class_dinosaur import *
from Class_player import *
from Class_treasure_hunter import *
from Class_barrel import *
from Class_chest import *
from Class_backside import *
from Class_enemy_stack import *
from Class_camera import *
from Class_letter import *
from pygame import *
import pygame
from timeit import default_timer
import random
import time

screen_height = 600
screen_width = 800
half_screen_height = float(screen_height/2)
half_screen_width =  float(screen_width/2)

pygame.init()
#screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN |pygame.DOUBLEBUF| pygame.HWSURFACE, vsync =1)
#screen = pygame.display.set_mode((screen_width, screen_height), pygame.DOUBLEBUF| pygame.HWSURFACE)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")

pygame.font.init() 
my_font = pygame.font.SysFont(None, 35)
clock = pygame.time.Clock()
       
from Class_images import *
from Class_sound import *

stack = class_stack()
stack.list_sound= class_sound()
stack.list_images = class_image()



            
    

class class_main_menu():
    def __init__(self):
        super().__init__()
        self.level_is_make = False
        self.t_shift = 0.01
        self.count = 0
        self.start_play = 0
        self.count_2 = ''
        self.background_color = (56, 58, 90)

        self.screen = screen
        self.point2 = ''

        self.menu_key = True

        self.menu_select = 0
        pygame.mixer.music.play()

        self.item2 = 1/60

        self.camera = class_camera(0,0)

        self.size_screen = False

        self.background_range = range(3)

        self.display_rect = (0,0,800,600)
        

    def run(self):

        

        while 1:
            start = default_timer()
            
            if self.t_shift >0.5:
                self.t_shift = 0.01





            if self.menu_key:
                self.menu()
            else:
                self.play()
         
            pygame.display.flip()
        

            item = self.item2-(default_timer() - start)
            if item > 0.0:
                #time.sleep(item)
                pygame.time.delay(int(item*0.4*1000))
      
       

            self.t_shift = default_timer()-start






    def make_level(self):

        stack.list_objects = []
        stack.list_items = []

        for row in range(len(stack.level_map)):

            items= []
            for column in range(len(stack.level_map[row])):
                cell = class_cell()
                
                if "w|1" in stack.level_map[row][column]:
                    cell.object = class_wall(column*32, row*32,stack)

                if "stakes|1" in stack.level_map[row][column]:
                    cell.object = class_stakes(column*32, row*32,stack)
                    
                if "stone|" in stack.level_map[row][column]:
                    cell.object = class_stone(column*32, row*32,int(stack.level_map[row][column].split('|')[1]),stack)

##                if "enemy|dinosaur" in stack.level_map[row][column]:
##                    cell.object = class_treasure_hunter(column*32, row*32,stack)

                if "enemy|dinosaur" in stack.level_map[row][column]:
                    cell.object = class_dinosaur(column*32, row*32,stack)

                if "enemy|troll" in stack.level_map[row][column]:
                    cell.object = class_troll(column*32, row*32,stack)

                if "enemy|random" in stack.level_map[row][column]:
                    class_enemy = random.choice([class_swordsman,class_swordsman_2,class_wood_enemy,class_treasure_hunter])
                    cell.object = class_enemy(column*32, row*32,stack)
                    

                if "p|1" in stack.level_map[row][column]:
                    stack.player = class_player(column*32, row*32,stack)
                    cell.object = stack.player
                    self.camera.rect.select_x(stack.player.rect.x)
                    self.camera.rect.select_y(stack.player.rect.y)
           
                if "i|1" in stack.level_map[row][column]:
                    cell.object = class_barrel(column*32, row*32,stack)

                if "chest|1" in stack.level_map[row][column]:
                    cell.object = class_chest(column*32, row*32,stack)
                  
                if 'backside' in stack.level_map[row][column]:
                    cell.background = class_backside(column*32, row*32,stack, stack.level_map[row][column].split('|')[1])

                if 'backwall' in stack.level_map[row][column]:
                    cell.background = class_wall(column*32, row*32,stack)
                    cell.background.armor = -1

                if 'letter' in stack.level_map[row][column]:
                    cell.object = class_letter(column*32, row*32,stack, stack.level_map[row][column].split('|')[1])
                    
                items.append(cell)
    
            stack.list_objects.append(items)
        
            

        for i in range(len(stack.list_objects)):
            for j in range(len(stack.list_objects[i])):
                if stack.list_objects[i][j].background: 
                    stack.list_objects[i][j].background.make()
                if stack.list_objects[i][j].object and stack.list_objects[i][j].object.name == names.wall: 
                    stack.list_objects[i][j].object.make()
       




   
                            
        

    def menu(self):
        

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:

                if e.key == pygame.K_ESCAPE and self.level_is_make:
                    self.menu_key = False
                    pygame.mixer.music.stop()

                if e.key == pygame.K_UP:
                    if self.menu_select > 0:
                        self.menu_select -= 1

                if e.key == pygame.K_DOWN:
                    if self.menu_select < 2:
                        self.menu_select += 1

                if e.key == pygame.K_KP_ENTER:
                    if self.menu_select == 2:
                        pygame.quit()
                    elif self.menu_select == 0:
                        self.make_level()
                        self.menu_key = False
                        self.level_is_make = True
                        pygame.mixer.music.stop()
                    elif self.menu_select == 1:
                        if self.size_screen:
                            self.screen = pygame.display.set_mode((screen_width, screen_height))
                            self.size_screen =False
                        else:
                            self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN |pygame.DOUBLEBUF| pygame.HWSURFACE, vsync =1)
                            self.size_screen =True
                

            if e.type == QUIT:
                raise SystemExit
        self.screen.fill((0,0,0),(0,0,800,600))

        if self.level_is_make:
            self.screen.blit(my_font.render("Esc - contine", False, (150, 150, 40)), (340,230))
        
        color = (170, 215, 30)
        if self.menu_select == 0:
            color = (230, 245, 90)
        self.screen.blit(my_font.render("New game", False, color), (340,270))

        color = (170, 215, 30)
        if self.menu_select == 1:
            color = (230, 245, 90)
        self.screen.blit(my_font.render("Size screen", False, color), (340,310))

        color = (170, 215, 30)
        if self.menu_select == 2:
            color = (230, 245, 90)
        self.screen.blit(my_font.render("Exit", False, color), (340,350))
        
        

    def play(self):
        
        


        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key  == pygame.K_w:
                    stack.key_w = True
                if e.key  == pygame.K_q:
                    stack.key_q = True
                if e.key  == pygame.K_e:
                    stack.key_melee = 4
                if e.key  == pygame.K_a:
                    stack.key_a = True
                if e.key  == pygame.K_s:
                    stack.key_s = True
                if e.key  == pygame.K_d:
                    stack.key_d = True
                if e.key  == pygame.K_c:
                    stack.key_melee = 3

                if e.key == pygame.K_ESCAPE:
                    self.menu_key = True
                    pygame.mixer.music.play()


            if e.type == pygame.KEYUP:
                if e.key  == pygame.K_w:
                    stack.key_w = False
                if e.key  == pygame.K_q:
                    stack.key_q = False
                if e.key  == pygame.K_e or e.key  == pygame.K_c:
                    stack.key_melee = 0
                if e.key  == pygame.K_a:
                    stack.key_a = False
                if e.key  == pygame.K_s:
                    stack.key_s = False
                if e.key  == pygame.K_d:
                    stack.key_d = False

            if e.type == QUIT:
                raise SystemExit

       

        list_items_object = []
        list_items_background = []
        list_items_backside= []


        
        from_y, to_y, from_x, to_x = stack.range_in_list(self.camera.rect, 10, 12, 14,15)#10, 12, 14,15
            
         
        for row in stack.list_objects[from_y: to_y]:
            for item in row[from_x: to_x]:
                    
                if item.object:
                    list_items_object.append(item.object)
                    #if item.object.name == names.obstacle:
       
                        #print(1,int(item.object.rect.x/32),int(item.object.rect.y/32),'---')
                if item.background:
                    if item.background.name == names.backside:
                        list_items_backside.append(item.background)
                    else:
                        list_items_background.append(item.background)
                    
        for item in list_items_object:
            
            item.update(self.t_shift)



            
        self.camera.shift(stack.player.rect.x,stack.player.rect.y)

        shift_x = round(self.camera.rect.x - half_screen_width + self.camera.rect.center_x)#float(int())
        shift_y = round(self.camera.rect.y - half_screen_height + self.camera.rect.center_y)#round()

        i = 0 
        while i < len(stack.list_items):
            if stack.list_items[i].armor>1:
                if abs(stack.list_items[i].rect.x - self.camera.rect.x) < 500 and abs(stack.list_items[i].rect.y - self.camera.rect.y) < 400:
                    stack.list_items[i].update(self.t_shift)
                else:
                    del stack.list_items[i] 
            else:
                del stack.list_items[i] 
            i+=1

        
            
            #print(shift_x,shift_y)


        #screen.fill((0,0,0),(0,0,800,600))

            #print(count_not_transparent)
            #if count_not_transparent<560:
        
        for i in self.background_range:
         
            bacground_x = screen_width-( shift_x/abs(i-3)  ) % screen_width#round()
                
            screen.blit(stack.list_images.list_background[i], (bacground_x,  0), (0,0,800-bacground_x,600))
            screen.blit(stack.list_images.list_background[i], (0,  0),(screen_width-bacground_x,0,800,600))
##        bacground_x = round(screen_width-( shift_x/8  ) % screen_width)
##                        
##        self.screen.blit(stack.list_images.list_background[3], (bacground_x,  0), (0,0,800-bacground_x,600))
##        self.screen.blit(stack.list_images.list_background[3], (0,  0),(screen_width-bacground_x,0,800,600))
 
           
        for item in list_items_background:
            self.screen.blit(item.texture, (item.rect.x-shift_x,  item.rect.y-shift_y ))

      
        for item in list_items_backside:
            if item.is_rendering == False:
                self.screen.blit(item.texture, (item.rect.x-shift_x,  item.rect.y-shift_y ))
                item.is_rendering=True
        for item in list_items_backside:
            item.is_rendering=False
         

        for item in list_items_object:
            item.blit_object(shift_x, shift_y, screen)

     
        for item in stack.list_items:
            self.screen.blit(item.texture, (item.rect.x-shift_x - item.texture_shift_x ,  item.rect.y-shift_y - item.texture_shift_y),
                                    item.texture_rect_list[item.motion][int(item.frame*item.direction)])
            

            
        self.count+=1
        self.start_play+=self.t_shift

        if self.start_play > 10:
            self.count_2 = str(round(self.count/self.start_play))
            self.count = 0
            self.start_play = 0
            
        if 1/self.t_shift < 59.0:
            self.count_2 = str(round(1/self.t_shift))+'-'

        self.screen.blit(my_font.render(self.count_2, False, (190, 235, 50)), (0,0))
        self.screen.blit(my_font.render(str(round(stack.player.armor))+' '+str(stack.player.bullets), False, (190, 235, 50)), (0,575))

        if stack.letter:
            row = 500
            for item in stack.letter.letter:
                self.screen.blit(my_font.render(item, False, (174, 170, 115)), (100,row))
                row+=25
            stack.letter.update(self.t_shift)
         
        

 
 
item = class_main_menu()
item.run()


  

                                     
                                     

                            
