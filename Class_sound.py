import pygame
##
##pygame.init()
pygame.mixer.init(frequency=22050,size=-16,channels=8)

class class_sound():
    def __init__(self):
        self.bullet_list = [self.load_sound('sound/bullet.wav'),
                            self.load_sound('sound/bullet3.wav')]

        self.melee_list = [self.load_sound('sound/melee2.wav'),
                            self.load_sound('sound/melee1.wav')]

        self.list_bullet_in_target = [self.load_sound('sound/bullet_in_target2.wav')]


        self.list_rolling = [self.load_sound('sound/rolling.wav')]
        self.list_destruction = [self.load_sound('sound/destruction1.wav'),
                                 self.load_sound('sound/destruction2.wav'),
                                 self.load_sound('sound/destruction3.wav')]

        self.list_detonation = [self.load_sound('sound/detonation.wav'),
                                self.load_sound('sound/detonation2.wav')]


        pygame.mixer.music.load('music/menu.mp3')
        pygame.mixer.music.set_volume(0.2)
        
    def load_sound(self, name):
        item = pygame.mixer.Sound(name)
        item.set_volume(0.20)
        return item


    




