import cv2
# from cv2 import xfeatures2d
import numpy as np
import math

lines_coordinates = []

def reading_points(event, x, y, flags, params): #the function that fills the global dictionary of coordinates with coordinate values of the points user marks on the image
    global lines_coordinates
    if event == cv2.EVENT_FLAG_LBUTTON:
        lines_coordinates.append((x,y))
        
def point_reader(img_path):     #primarily the function that invokes the point reading function and stores the ordered points in a local list which is returned to the main function
    org_image = cv2.imread(img_path)
    image = cv2.resize(org_image, (800,800))    #resizing the image to make it confided within the screen
    cv2.imshow('img', image)
    cv2.setMouseCallback('img', reading_points)
    cv2.waitKey(0)

def vanishing_point(img_path):
    global lines_coordinates
    lines = []
    for i in range(0,len(lines_coordinates),2):
        p1 = lines_coordinates[i] #x1-> p1[0] y1->p1[1]
        p2 = lines_coordinates[i+1] #x2->p2[0] y2->p2[1]
        a = p2[1] - p1[1] #y2-y1
        b = p2[0] - p1[0] #x2-x1
        c = b*p1[1] - a*p1[0]
        lines.append((-a,b,c))
    
    vp_list = []
    for i in lines:
        for j in lines:
            if i[0]*j[1] - j[0]*i[1]!= 0:
                x_p = (-i[1]*j[2] + j[1]*i[2])/(i[0]*j[1] - j[0]*i[1])
                y_p = (-i[2]*j[0] + j[2]*i[0])/(i[0]*j[1] - j[0]*i[1])
                vp_list.append((x_p, y_p))
    
    if len(vp_list) == 0:
        print("Vanishing point does not exist")
        return
        
    vanishing_point_x = 0
    vanishing_point_y = 0

    for i in vp_list:
        vanishing_point_x += i[0]
        vanishing_point_y += i[1]

    vanishing_point_x /= len(vp_list)
    vanishing_point_y /= len(vp_list)

    vanishing_point = (vanishing_point_x, vanishing_point_y)

    vp_int = (int(vanishing_point[0]), int(vanishing_point[1]))
    
    print("VP: ", vanishing_point)
    
    org_image = cv2.imread(img_path)
    image = cv2.resize(org_image, (800,800))
    cv2.circle(image,vp_int,radius=5,color = (255,0,255), thickness = -1)
    cv2.imshow('vanishing_pointed_image', image)
    cv2.waitKey(0)

def main():
    path = r"C:\Users\Mohtashim Butt\Documents\Fall-2022\CV\Project\Project_Dataset\predicted_Images\hello.jpg"
    point_reader(path)
    vanishing_point(path)
    
main()
    
    