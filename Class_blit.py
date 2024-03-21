class class_blit_shift():
    def blit_object(self, shift_x, shift_y, screen):
        screen.blit(self.texture, (self.rect.x-shift_x - self.texture_shift_x ,  self.rect.y-shift_y - self.texture_shift_y),
                                    self.texture_rect_list[self.motion][int(self.frame*self.direction)])
class class_blit():
    def blit_object(self, shift_x, shift_y, screen):
        screen.blit(self.texture, (self.rect.x-shift_x ,  self.rect.y-shift_y ))
