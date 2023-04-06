import matplotlib.pyplot as plt
import random
import json
import cv2
# from cv2 import xfeatures2d
import numpy as np
import math

lines_coordinates = []

def reading_points(event, x, y, flags, params): #the function that fills the global dictionary of coordinates with coordinate values of the points user marks on the image
    global lines_coordinates
    if event == cv2.EVENT_FLAG_LBUTTON:
        lines_coordinates.append((x,y))
        
def point_reader(org_image):     #primarily the function that invokes the point reading function and stores the ordered points in a local list which is returned to the main function
    # org_image = cv2.imread(img_path)
    global lines_coordinates
    image = cv2.resize(org_image, (800,800))    #resizing the image to make it confided within the screen
    cv2.imshow('img', org_image)
    lines_coordinates = list()
    cv2.setMouseCallback('img', reading_points)
    cv2.waitKey(0)

def main():
    json_gt = [json.loads(line) for line in open("test_label.json")]
    json_pred = [json.loads(line) for line in open('Project_Dataset/test_label.json').readlines()]
    # print("Hello:",json_pred[34])
    pred = json_pred[34]
    x_vals = pred['lanes']
    print(x_vals)

    x_indices = list()
    for i in range(0,len(x_vals)):
        for j in range(0,len(x_vals[i])):
            if(int(x_vals[i][j])!=-2):
                x_indices.append(int(j))
                break
    print("x_indices:",x_indices)

    raw_file = pred['raw_file']
    gt_lanes_vis = list()
    gt = json_gt[34]
    gt_lanes = gt['lanes']
    # print("pred_lans:",pred_lanes)
    # print("gt_lanes:",gt_lanes)
    y_samples = gt['h_samples']
    gt_lanes_vis = [[(x, y) for (x, y) in zip(lane, y_samples) if x >= 0] for lane in gt_lanes]
    pred_lanes_vis = [[(x, y) for (x, y) in zip(lane, y_samples) if x >= 0] for lane in x_vals]
    img_vis = plt.imread("Project_Dataset/"+raw_file)
    x = []
    for q in range(len(gt_lanes_vis)):
        first = random.uniform(0,1)
        while(True):
            second = random.uniform(0,1)
            if second - first > 0.1 or first - second > 0.1:
                break
        while(True):
            third = random.uniform(0,1)
            if third - second > 0.1 or third - first > 0.1 or second - third > 0.1 or first - third > 0.1:
                break
        x.append((first*255,second*255,third*255))

    # for lane in range(0,len(gt_lanes_vis)):
    #     cv2.polylines(img_vis, np.int32([gt_lanes_vis[lane]]), isClosed=False, color=x[lane], thickness=5)
    # print("pred_lanes_vis",pred_lanes_vis)
    # print("gt_lane vid:",gt_lanes_vis)
    for lane in range(0,len(pred_lanes_vis)):
        cv2.polylines(img_vis, np.int32([pred_lanes_vis[lane]]), isClosed=False, color=x[lane], thickness=2)
    cv2.imwrite("Project_Dataset/predicted_Images/top_view.jpg",img_vis)

    # Read source image.
    hello = np.zeros((4,2))
    hello_dst = np.zeros((4,2))
    # for i in range(0,5):
    im_src = cv2.imread(fr"Project_Dataset/predicted_Images/top_view.jpg")
    # Four corners of the book in source image
    
    point_reader(im_src)
    # lines_coordinates.append((x_vals[1][x_indices[1]],y_samples[x_indices[1]]))
    # cv2.circle(im_src,(x_vals[1][x_indices[1]],y_samples[x_indices[1]]),radius=5,color = (255,0,0), thickness = -1)
    # lines_coordinates.append((x_vals[2][x_indices[2]],y_samples[x_indices[2]]))
    # cv2.circle(im_src,(x_vals[2][x_indices[2]],y_samples[x_indices[2]]),radius=5,color = (0,225,0), thickness = -1)
    # lines_coordinates.append((x_vals[1][x_indices[1]+5],y_samples[x_indices[1]+5]))
    # cv2.circle(im_src,(x_vals[1][x_indices[1]+5],y_samples[x_indices[1]+5]),radius=5,color = (0,0,225), thickness = -1)
    # lines_coordinates.append((x_vals[2][x_indices[2]+5],y_samples[x_indices[2]+5]))
    # cv2.circle(im_src,(x_vals[2][x_indices[2]+5],y_samples[x_indices[2]+5]),radius=5,color = (0,225,225), thickness = -1)
    for i in range(0,len(lines_coordinates)):
        for j in range(0,2):
            hello[i][j]=lines_coordinates[i][j]
    print("Hello:",hello)
    # cv2.imshow("Hui",im_src)


    # Read source image.
    im_dst = cv2.imread(fr"Project_Dataset/predicted_Images/top_view.jpg")
    # Four corners of the book in source image
    
    point_reader(im_dst)
    for i in range(0,len(lines_coordinates)):
        for j in range(0,2):
            hello_dst[i][j]=lines_coordinates[i][j]
    print("Type:",type(hello_dst))
    print("Hello:",hello_dst)
    
 

    # hello = hello/5
    # hello_dst = hello_dst/5
    # Calculate Homography
    h, status = cv2.findHomography(hello, hello_dst)
 
    # Warp source image to destination based on homography
    im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))
    im_out = cv2.resize(im_out, (800,800))

    # Display images
    cv2.imshow("Source Image", cv2.resize(im_src, (800,800)))
    cv2.imshow("Destination Image", cv2.resize(im_dst, (800,800)))
    cv2.imshow("Warped Source Image", im_out)
 
    cv2.waitKey(0)
main()
