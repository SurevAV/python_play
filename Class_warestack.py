
class class_stack_2():
    def calculate_frame(self,t_shift):
       
        self.frame += 8.0*t_shift
        if self.frame > self.texture_rect_list[self.motion][0]:
            self.frame= 1.0
            self.motion = 0
    
class class_stack_1():
    def position_in_level(self, item):
        y = int(self.rect.y/32.0)
        x = int(self.rect.x/32.0)

        if x < 0 or y < 0 or y >= self.stack.len_level_y or x >= self.stack.len_level_x:
            del self
        else:
            self.list_objects[y][x].object = item

    def on_item(self, item,t_shift):
        pass

    
    def gravity(self,t_shift):

        self.position_in_level(None)
        self.jump -= 500.0*t_shift
        
        if self.jump < - 750.0:
            self.jump = -750.0
        
    
        self.rect.shift_y(-self.jump*t_shift)
        self.on_ground = False
      

        

        from_y, to_y, from_x, to_x = self.stack.range_in_list(self.rect,2,3, 3,3)
        for row in self.list_objects[from_y: to_y]:
            for item in row[from_x: to_x]:
                if item.object and self.rect.colliderect(item.object.rect) and item.object != self:

                    if self.jump <=0.0:
                        self.rect.select_y(item.object.rect.y-self.rect.height)
                        self.on_ground = True
                        self.on_item( item.object,t_shift)
                        self.jump = 0.0
                    else:
                        self.rect.select_y(item.object.rect.bottom)
                        self.jump = 0.0
                    break

        self.position_in_level(self)
