import pygame

class class_image():
    def __init__(self):
        #wall-----------------------------------------------------
        self.list_wall = [self.load_image("images/wall/wall1.png"),
                          self.load_image("images/wall/wall2.png"),
                          self.load_image("images/wall/wall3.png")]
        
        self.list_background_wall = [self.load_image("images/wall/background_wall1.png"),
                                     self.load_image("images/wall/background_wall2.png")]


        self.dict_wall = {"left_up":self.load_image_transparent("images/wall/Wall_01.png"),
                          "up":self.load_image_transparent("images/wall/Wall_02.png"),
                          "up_right":self.load_image_transparent("images/wall/Wall_03.png"),
                          "inside_down_right":self.load_image_transparent("images/wall/Wall_04.png"),
                          "down":self.load_image_transparent("images/wall/Wall_05.png"),
                          "inside_left_down":self.load_image_transparent("images/wall/Wall_06.png"),
                          "left":self.load_image_transparent("images/wall/Wall_11.png"),
                          "empty":self.load_image("images/wall/Wall_12.png"),
                          "right":self.load_image_transparent("images/wall/Wall_14.png"),
                          "left_down":self.load_image_transparent("images/wall/Wall_21.png"),
                          "down_right":self.load_image_transparent("images/wall/Wall_23.png"),
                          "inside_up_right":self.load_image_transparent("images/wall/Wall_24.png"),
                          "inside_left_up":self.load_image_transparent("images/wall/Wall_26.png"),
                          "left_up_right_down":self.load_image_transparent("images/wall/Wall_31.png"),
                          "left_up_down":self.load_image_transparent("images/wall/Wall_32.png"),
                          "up_down":self.load_image_transparent("images/wall/Wall_33.png"),
                          "up_down_right":self.load_image_transparent("images/wall/Wall_34.png"),
                          "empty_2":self.load_image_transparent("images/wall/Wall_35.png"),
                          "left_up_right":self.load_image_transparent("images/wall/Wall_54.png"),
                          "left_right":self.load_image_transparent("images/wall/Wall_55.png"),
                          "left_down_right":self.load_image_transparent("images/wall/Wall_56.png"),
                          "inside_left_up_2":self.load_image_transparent("images/wall/Wall_57.png"),
                          "inside_up_right_2":self.load_image_transparent("images/wall/Wall_58.png")}
        #wall-----------------------------------------------------

        #stakes-----------------------------------------------------
        self.list_stakes = [self.load_image_transparent("images/stakes/stakes.png")]
        #stakes-----------------------------------------------------


        #player-----------------------------------------------------
        self.player = self.load_image_resize("images/player/player2.png")
        self.list_player_textures=[]

        for j in range(0,448,64):
            self.list_motion= [None]
            for i in range(0, 2048, 128):
                self.list_motion.append((i,j,128,64))
            self.list_player_textures.append(self.list_motion)

        self.list_player_textures[0][0] = 9
        self.list_player_textures[1][0] = 9
        self.list_player_textures[2][0] = 8
        self.list_player_textures[3][0] = 7
        self.list_player_textures[4][0] = 9
        self.list_player_textures[5][0] = 5
        self.list_player_textures[6][0] = 6
        #player-----------------------------------------------------

        #treasure_hunter-----------------------------------------------------
        self.treasure_hunter = self.load_image_resize("images/enemys/treasure_hunter.png")
        self.list_treasure_hunter_textures=[]

        for j in range(0,448,64):
            self.list_motion= [None]
            for i in range(0, 2048, 128):
                self.list_motion.append((i,j,128,64))
            self.list_treasure_hunter_textures.append(self.list_motion)

        self.list_treasure_hunter_textures[0][0] = 9
        self.list_treasure_hunter_textures[1][0] = 9
        self.list_treasure_hunter_textures[2][0] = 8
        self.list_treasure_hunter_textures[3][0] = 7
        self.list_treasure_hunter_textures[4][0] = 9
        self.list_treasure_hunter_textures[5][0] = 5
        self.list_treasure_hunter_textures[6][0] = 6
        #treasure_hunter-----------------------------------------------------

        #swordsman-----------------------------------------------------
        self.swordsman = self.load_image_resize("images/enemys/swordsman.png")
        self.list_swordsman_textures=[]

        for j in range(0,448,64):
            self.list_motion= [None]
            for i in range(0, 1152, 64):
                self.list_motion.append((i,j,64,64))
            self.list_swordsman_textures.append(self.list_motion)

        self.list_swordsman_textures[0][0] = 3
        self.list_swordsman_textures[1][0] = 9
        self.list_swordsman_textures[2][0] = 10
        self.list_swordsman_textures[3][0] = 5
        self.list_swordsman_textures[4][0] = 8
        self.list_swordsman_textures[5][0] = 10
        self.list_swordsman_textures[6][0] = 7
        #swordsman-----------------------------------------------------


        #swordsman_2-----------------------------------------------------
        self.swordsman_2 = self.load_image_resize("images/enemys/swordsman_2.png")
        self.list_swordsman_2_textures=[]

        for j in range(0,512,64):
            self.list_motion= [None]
            for i in range(0, 1536, 64):
                self.list_motion.append((i,j,64,64))
            self.list_swordsman_2_textures.append(self.list_motion)

        self.list_swordsman_2_textures[0][0] = 13
        self.list_swordsman_2_textures[1][0] = 9
        self.list_swordsman_2_textures[2][0] = 11
        self.list_swordsman_2_textures[3][0] = 11
        self.list_swordsman_2_textures[4][0] = 11
        self.list_swordsman_2_textures[5][0] = 7
        self.list_swordsman_2_textures[6][0] = 5
        self.list_swordsman_2_textures[7][0] = 8
        #swordsman_2-----------------------------------------------------


        #troll-----------------------------------------------------
        self.troll = self.load_image_resize("images/enemys/troll.png")
        self.list_troll_textures=[]

        for j in range(0,256,64):
            self.list_motion= [None]
            for i in range(0, 1024, 64):
                self.list_motion.append((i,j,64,64))
            self.list_troll_textures.append(self.list_motion)

        self.list_troll_textures[0][0] = 3
        self.list_troll_textures[1][0] = 9
        self.list_troll_textures[2][0] = 7
        self.list_troll_textures[3][0] = 7
        #troll-----------------------------------------------------

        #wood_enemy-----------------------------------------------------
        self.wood_enemy = self.load_image_resize("images/enemys/wood_enemy.png")
        self.list_wood_enemy_textures=[]

        for j in range(0,320 ,64):
            self.list_motion= [None]
            for i in range(0, 1024, 64):
                self.list_motion.append((i,j,64,64))
            self.list_wood_enemy_textures.append(self.list_motion)

        self.list_wood_enemy_textures[0][0] = 3
        self.list_wood_enemy_textures[1][0] = 9
        self.list_wood_enemy_textures[2][0] = 7
        self.list_wood_enemy_textures[3][0] = 6
        self.list_wood_enemy_textures[4][0] = 6
        #wood_enemy-----------------------------------------------------


        #bullet-----------------------------------------------------
        self.list_bullet_textures=[]
        self.bullet = self.load_image("images/bullet/bullet.png")
        self.list_motion= [9]
        for i in range(0, 448, 28):
            self.list_motion.append((i,0,28,2))
        self.list_bullet_textures.append(self.list_motion)
        #bullet-----------------------------------------------------


        #background-----------------------------------------------------
        self.list_background = [self.load_image_resize_with_size("images/background/2.png",800,600),
                                self.load_image_resize_with_size("images/background/3.png",800,600),
                                #self.load_image_resize_with_size("images/background/4.png",800,600),
                                self.load_image_resize_with_size("images/background/5.png",800,600),
                                self.load_image_resize_with_size("images/background/2.png",800,600)]
        #background-----------------------------------------------------


        #stone-----------------------------------------------------
        self.stone = self.load_image_transparent("images/stone/stone.png")
        self.list_stone_textures_rect=[]
        self.list_motion = [9]
        for i in range(0, 1024, 64):
            self.list_motion.append((i,0,64,64))
        self.list_stone_textures_rect.append(self.list_motion)
        #stone-----------------------------------------------------


        #dinosaur-----------------------------------------------------
        self.dinosaur = self.load_image_transparent("images/enemys/2.png")
        self.list_dinosaur_textures=[]

        for j in range(0,280,35):
            self.list_motion= [None]
            for i in range(0, 1200, 75):
                self.list_motion.append((i,j,75,35))
            self.list_dinosaur_textures.append(self.list_motion)

        self.list_dinosaur_textures[0][0] = 9
        self.list_dinosaur_textures[1][0] = 7
        self.list_dinosaur_textures[2][0] = 3
        self.list_dinosaur_textures[3][0] = 8
        self.list_dinosaur_textures[4][0] = 7
        self.list_dinosaur_textures[5][0] = 2
        self.list_dinosaur_textures[6][0] = 9
        self.list_dinosaur_textures[7][0] = 7

        #dinosaur-----------------------------------------------------


        #barrel-----------------------------------------------------
        self.barrel = self.load_image_transparent("images/barrel/barrel.png")
        #barrel-----------------------------------------------------


        #detination-----------------------------------------------------
        self.detonation = self.load_image_transparent("images/detonation/detonation.png")
        #detination-----------------------------------------------------


        #chest-----------------------------------------------------
        self.list_chest_textures=[]
        self.chest = self.load_image_transparent("images/chest/chest.png")
        self.list_motion= [5]
        for i in range(0, 256, 32):
            self.list_motion.append((i,0,32,32))
        self.list_chest_textures.append(self.list_motion)
    
        #chest-----------------------------------------------------

        #trees-----------------------------------------------------
        self.dict_backside = {"tree1":self.load_image("images/backside/tree1.png"),
                              "tree2":self.load_image("images/backside/tree2.png"),
                              "tree3":self.load_image("images/backside/tree3.png"),
                              
                              "willow1":self.load_image("images/backside/willow1.png"),
                              "willow2":self.load_image("images/backside/willow2.png"),
                              "willow3":self.load_image("images/backside/willow3.png"),
                              
                              "ridge1":self.load_image("images/backside/ridge1.png"),
                              "ridge2":self.load_image("images/backside/ridge2.png"),
                              "ridge3":self.load_image("images/backside/ridge3.png"),
                              "ridge4":self.load_image("images/backside/ridge4.png"),
                              "ridge5":self.load_image("images/backside/ridge5.png"),
                              "ridge6":self.load_image("images/backside/ridge6.png"),
                              
                              "grass1":self.load_image("images/backside/grass1.png"),
                              "grass2":self.load_image("images/backside/grass2.png"),
                              "grass3":self.load_image("images/backside/grass3.png"),
                              "grass4":self.load_image("images/backside/grass4.png"),
                              "grass5":self.load_image("images/backside/grass5.png"),
                              "grass6":self.load_image("images/backside/grass6.png"),
                              "grass7":self.load_image("images/backside/grass7.png"),
                              "grass8":self.load_image("images/backside/grass8.png"),
                              "grass9":self.load_image("images/backside/grass9.png"),
                              "grass10":self.load_image("images/backside/grass10.png"),
                              
                              "bush1":self.load_image("images/backside/bush1.png"),
                              "bush2":self.load_image("images/backside/bush2.png"),
                              "bush3":self.load_image("images/backside/bush3.png"),
                              "bush4":self.load_image("images/backside/bush4.png"),
                              "bush5":self.load_image("images/backside/bush5.png"),
                              "bush6":self.load_image("images/backside/bush6.png"),
                              "bush7":self.load_image("images/backside/bush7.png"),
                              "bush8":self.load_image("images/backside/bush8.png"),
                              "bush9":self.load_image("images/backside/bush9.png"),
                              
                              "pointer1":self.load_image("images/backside/pointer1.png"),
                              "pointer2":self.load_image("images/backside/pointer2.png"),
                              "pointer3":self.load_image("images/backside/pointer3.png"),
                              "pointer4":self.load_image("images/backside/pointer4.png"),
                              "pointer5":self.load_image("images/backside/pointer5.png"),
                              "pointer6":self.load_image("images/backside/pointer6.png"),
                              "pointer7":self.load_image("images/backside/pointer7.png"),
                              "pointer8":self.load_image("images/backside/pointer8.png")}
                         
        #trees-----------------------------------------------------

    def load_image_resize_with_size(self, name, size_x, size_y):
        item = pygame.image.load(name)#.convert()
        item = pygame.transform.scale(item, (size_x, size_y))

##        surface = pygame.Surface(item.get_size()).convert_alpha()
##        surface.fill((0, 0, 0, 0.4*255))
##        item.blit(surface, (0, 0))
##        
        
  
        item.set_colorkey((255,255,255))
        return item.convert()
      
   
    def load_image_resize(self, name):
        item = pygame.image.load(name).convert()
        size = item.get_size()
        item = pygame.transform.scale(item, (int(size[0]*2), int(size[1]*2)))
        item.set_colorkey((255,255,255))
        return item.convert()
##    
##    def load_image_resize_flip(self, name):
##        item = pygame.image.load(name).convert()
##        size = item.get_size()
##        item = pygame.transform.scale(item, (int(size[0]*2), int(size[1]*2)))
##        item = pygame.transform.flip(item, True, False)
##        #item.set_colorkey((255,255,255))
##        return item
    
    def load_image(self, name):
        item = pygame.image.load(name).convert()

        
        return item.convert()



    def load_image_transparent(self, name):
        item = pygame.image.load(name).convert()
        item.set_colorkey((255,255,255))
        return item.convert()


    




