import cv2
import numpy as np
import matplotlib.pyplot as plt


lines_coordinates = []
my_arr = list() #Using this list to save the tuple of co-ordinates i.e., to append (x,y) value as I click on the image
def display_click(event, x, y, flags, params):
    # checking for mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDBLCLK or event == cv2.EVENT_MBUTTONDBLCLK:
        my_arr.append((x,y))
        print(f"({x},{y})")


def point_reader(img):
    #showing the image
    print("BHAAAGOOOOOOOOOOOOo")
    cv2.imshow('image', img)
    print("Khatam karo")

    #reading the image for click
    cv2.setMouseCallback('image', display_click)

    #waiting
    cv2.waitKey(0)
    lines_coordinates = np.ones((2,len(my_arr)))
    for i in range(len(my_arr)):
        lines_coordinates[0][i]=my_arr[i][0]
        lines_coordinates[1][i]=my_arr[i][1]
    return lines_coordinates

img_vis = cv2.imread("Project_Dataset/predicted_Images/hello.jpg")
lines_coordinates = point_reader(img_vis)

print("lines coordinates:",lines_coordinates)
lines = []
for i in range(0,len(lines_coordinates),2):
  p1 = lines_coordinates[i] #x1-> p1[0] y1->p1[1]
  p2 = lines_coordinates[i+1] #x2->p2[0] y2->p2[1]
  a = p2[1] - p1[1] #y2-y1
  b = p2[0] - p1[0] #x2-x1
  c = b*p1[1] - a*p1[0]
  lines.append((-a,b,c))

# print("line:",lines)
vp_list = []
for i in lines:
  for j in lines:
    x_p = (-i[1]*j[2] + j[1]*i[2])/(i[0]*j[1] - j[0]*i[1])
    y_p = (-i[2]*j[0] + j[2]*i[0])/(i[0]*j[1] - j[0]*i[1])
    if i[0]*j[1] - j[0]*i[1]!= 0:
      vp_list.append((x_p, y_p))
# print("Hello:",vp_list)
vanishing_point_x = 0
vanishing_point_y = 0

for i in vp_list:
  vanishing_point_x += i[0]
  vanishing_point_y += i[1]

vanishing_point_x /= len(vp_list)
vanishing_point_y /= len(vp_list)

vanishing_point = (vanishing_point_x, vanishing_point_y)

vp_int = (int(vanishing_point[0]), int(vanishing_point[1]))
cv2.circle(img_vis,vp_int,radius=10,color = (255,0,0), thickness = -1)
plt.imshow(img_vis)
plt.show()

