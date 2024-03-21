import cv2
import numpy as np

img = cv2.imread('treasure_hunter.png')

img = np.array(img)

for i in range(len(img)):
    for j in range(len(img[i])):
        
        if img[i][j][0] == 58 and img[i][j][1] == 72 and img[i][j][2] == 105:
            

            
            img[i][j][0] =52
            img[i][j][1] =112
            img[i][j][2] =52

        if img[i][j][0] == 81 and img[i][j][1] == 100 and img[i][j][2] == 145:
            

            
            img[i][j][0] =75
            img[i][j][1] =150
            img[i][j][2] =140

        if img[i][j][0] == 100 and img[i][j][1] == 124 and img[i][j][2] == 179:
            

            
            img[i][j][0] =96
            img[i][j][1] =181
            img[i][j][2] =183

            

cv2.imwrite('2.png', img)

