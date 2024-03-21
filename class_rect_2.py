from timeit import default_timer
import csv

##class class_rect():
##    def __init__(self,x,y,width,height):
##        self.x = float(x)
##        self.y = float(y)
##        self.width = float(width)
##        self.height =  float(height)
##        self.center_x = float(width/2)
##        self.center_y = float(height/2)
##
##
##    def colliderect(self,rect):
##        return self.x + self.width > rect.x and \
##               self.x < rect.x +rect.width and \
##               self.y + self.height > rect.y and\
##               self.y < rect.y +rect.height
##
##
##    def right(self):
##        return self.x+self.width
##    def bottom(self):
##        return self.y+self.height
##
##
##list_rect = [class_rect(i,2,32,32) for i in range(20)]
##
##range_1 = range(60)
##start = default_timer()
##
##for i in range_1:
##    for item in list_rect:
##        item.x -= 1
##        item.y -= 1
##        item.x = 1
##        item.y = 1
##        colissions = [rect.colliderect(item) for rect in list_rect]
##        
##print(default_timer()-start)
##
##
##class class_rect_2():
##    def __init__(self,x,y,width,height):
##        self.x = float(x)
##        self.y = float(y)
##        self.width = float(width)
##        self.height =  float(height)
##        self.center_x = float(width/2)
##        self.center_y = float(height/2)
##
##        self.right = self.x+self.width
##        self.bottom = self.y+self.height
##
##
##    def colliderect(self,rect):
##        return self.right > rect.x and \
##               self.x < rect.right and \
##               self.bottom > rect.y and\
##               self.y < rect.bottom
##
##    def shift_x(self,i):
##        self.x += i
##        self.right = self.x+self.width
##
##    def shift_y(self,i):
##        self.y += i
##        self.bottom = self.y+self.height
##
##    def select_x(self,i):
##        self.x = i
##        self.right = self.x+self.width
##
##    def select_y(self,i):
##        self.y = i
##        self.bottom = self.y+self.height
##
##
##   
##
##
##list_rect = [class_rect_2(i,2,32,32) for i in range(20)]
##
##
##range_1 = range(60)
##start = default_timer()
##
##for i in range_1:
##    for item in list_rect:
##        item.shift_x(-1)
##        item.shift_y(-1)
##        item.select_x(1)
##        item.select_y(1)
##        colissions = [rect.colliderect(item) for rect in list_rect]
##     
##print(default_timer()-start)
##
##
##
#-----------------------------------------------------------------------------------------

##list_range = list(range(10000))
##
##start = default_timer()
##for i in list_range:
##    s = i - len(list_range)
##print(default_timer()-start)
##
##len_list = len(list_range)
##start = default_timer()
##for i in list_range:
##    s = i - len_list
##print(default_timer()-start)
#-----------------------------------------------------------------------------------------


##range_1 = range(5000)
##list_range = list(range(10000))
##
##start = default_timer()
##for i in range_1:
##    for item in list_range[1:500]:
##        u = item+1
##
##print(default_timer()-start)
##
##start = default_timer()
##for i in range_1:
##    for i in range(1,500):
##        u = list_range[i]+1
##
##print(default_timer()-start)
##
##
##start = default_timer()
##for i in range_1:
##
##    i =1
##    while i <500:
##        u = list_range[i]+1
##        i+=1
##
##print(default_timer()-start) 
#-----------------------------------------------------------------------------------------

##list_items = [list(range(100)) for i in range(100)]
##
##print(len(list_items),len(list_items[0]))
##
##
##start = default_timer()
##for row in list_items[10: 32]:
##    for item in row[10: 32]:
##        if item:
##            item +=1
##            item +=5
##            
##for row in list_items[10: 32]:
##    for item in row[10: 32]:
##        if item:
##            item +=2
##for row in list_items[10: 32]:
##    
##    for item in row[10: 32]:
##        if item:
##            item +=3
##            item -=5
##print(default_timer()-start)
##
##
##start = default_timer()
##list_objects = []
##for row in list_items[10: 32]:
##    for item in row[10: 32]:
##        if item:
##            item +=1
##            list_objects.append(item)
##for item in list_objects:
##    item +=1
##for item in list_objects:
##    item +=1
##
##print(default_timer()-start)


##x_object = 120
###y_object = 90
##
##x=100
###y=100
##for i in range(10):
##    shift_x = x_object - x
##    
##    if abs(shift_x) > 1.0:
##        x +=shift_x/50
##    print(x)
##
##
##file = open('level_1 - level_1.csv', encoding='utf-8')
##
##rows = list(csv.reader( file, delimiter=','))
##row = [' ']*197
##
##
##file2=open('level_1 - level_2.csv',  'w')
##for i in range(len(rows)):
##    rows[i]+=row
##
##    string = ''
##    for j in rows[i]:
##        string+= j+','
##    file2.write(string+'\n')
##file2.close()


