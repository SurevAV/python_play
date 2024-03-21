
class class_rect():
    def __init__(self,x,y,width,height):
        self.x = float(x)
        self.y = float(y)
        self.width = float(width)
        self.height =  float(height)
        self.center_x = float(width/2)
        self.center_y = float(height/2)

        self.right = self.x+self.width
        self.bottom = self.y+self.height


    def colliderect(self,rect):
        return self.right > rect.x and \
               self.x < rect.right and \
               self.bottom > rect.y and\
               self.y < rect.bottom

    def shift_x(self,i):
        self.x += i
        self.right = self.x+self.width

    def shift_y(self,i):
        self.y += i
        self.bottom = self.y+self.height

    def select_x(self,i):
        self.x = i
        self.right = self.x+self.width

    def select_y(self,i):
        self.y = i
        self.bottom = self.y+self.height

    def center_rect_x(self):
        return self.x+self.center_x

    def center_rect_y(self):
        return self.y+self.center_y

