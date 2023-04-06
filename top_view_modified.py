import matplotlib.pyplot as plt
import random
import json
import cv2
# from cv2 import xfeatures2d
import numpy as np
import math
import glob


def main():
    for p in range(1,12):
        if(p==6):
            continue
        print("p",p)
        json_sample = [json.loads(line) for line in open(fr"C:\Users\Mohtashim Butt\Documents\Fall-2022\CV\Project\curved_path_ki_jasons/sample_{p}.json")]
        # print(json_sample)
        my_lanes=list()
        for i in range(0,len(json_sample[0]['lanes'])):
            my_lanes.append(json_sample[0]['lanes'][i])
        # print("My Lanes:",my_lanes)
        image  = cv2.imread(fr"C:\Users\Mohtashim Butt\Documents\Fall-2022\CV\Project\yolov7\runs\detect\exp9\{p}.jpg")
        # f=50
        # r=20
        #clockwise
        # if(p==1 or p==18):
        pt_1 = my_lanes[0][int(len(my_lanes[1])/2)+50]
        print("pt_1:",pt_1)
        pt_2 = my_lanes[0][int(len(my_lanes[1])/2) + 60]
        print("pt_2:",pt_2)
        # else:
        #     pt_1 = my_lanes[1][int(len(my_lanes[1])/2)+50]
        #     print("pt_1:",pt_1)
        #     pt_2 = my_lanes[1][int(len(my_lanes[1])/2) + 60]
        #     print("pt_2:",pt_2)

        # pt_3 = np.zeros((1,2))
        # pt_4 = np.zeros((1,2))
        pt_3 = list()
        pt_4 = list()

        rec_pt_1 = list()
        rec_pt_2 = list()
        rec_pt_3 = list()
        rec_pt_4 = list()
        counter_1 = 0
        counter_2 = 0
        # print("leng:",len(my_lanes[0]))
        for i in range(0,len(my_lanes[0])):
            # print("JJFIE")
            if(my_lanes[2][i][1]<pt_1[1]+8 and my_lanes[2][i][1]>pt_1[1]-8):
                if(counter_1==0):
                    print("Hello")
                    pt_4.append(my_lanes[2][i][0])
                    pt_4.append(my_lanes[2][i][1])
                    rec_pt_1.append(int((pt_4[0]+pt_1[0])/2+100))
                    rec_pt_1.append(my_lanes[2][i][1])
                    rec_pt_4.append(int((pt_4[0]+pt_1[0])/2-100))
                    rec_pt_4.append(my_lanes[2][i][1])
                    counter_1+=1
                else:
                    continue
            if(my_lanes[2][i][1]<pt_2[1]+8 and my_lanes[2][i][1]>pt_2[1]-8):
                if(counter_2==0):
                    print("Fuck off")
                    pt_3.append(my_lanes[2][i][0])
                    pt_3.append(my_lanes[2][i][1])
                    rec_pt_2.append(rec_pt_1[0])
                    rec_pt_2.append(my_lanes[2][i][1])
                    rec_pt_3.append(rec_pt_4[0])
                    rec_pt_3.append(my_lanes[2][i][1])
                else:
                    continue
        
        

            # f+=70
            # r+=60
        # if(p==1):

        # for i in range(2,3):
        #     for j in range(0,len(my_lanes[i])):
        #         cv2.circle(image,(int(my_lanes[i][j][0]),int(my_lanes[i][j][1])),radius=5,color = (0,0,255), thickness = -1)
        # cv2.circle(image,(int(pt_1[0]),int(pt_1[1])),radius=5,color = (255,0,0), thickness = -1)
        # cv2.circle(image,(int(pt_2[0]),int(pt_2[1])),radius=5,color = (0,255,0), thickness = -1)
        # cv2.circle(image,(int(pt_3[0]),int(pt_3[1])),radius=5,color = (255,255,255), thickness = -1)
        # cv2.circle(image,(int(pt_4[0]),int(pt_4[1])),radius=5,color = (0,0,0), thickness = -1)

        # cv2.circle(image,(int(rec_pt_1[0]),int(rec_pt_1[1])),radius=10,color = (255,0,0), thickness = -1)
        # cv2.circle(image,(int(rec_pt_2[0]),int(rec_pt_2[1])),radius=10,color = (0,255,0), thickness = -1)
        # cv2.circle(image,(int(rec_pt_3[0]),int(rec_pt_3[1])),radius=10,color = (255,255,255), thickness = -1)
        # cv2.circle(image,(int(rec_pt_4[0]),int(rec_pt_4[1])),radius=10,color = (255,255,0), thickness = -1)


        # plt.imshow(image)
        # plt.show()

        pt_1_arr = np.array(pt_1)
        pt_2_arr = np.array(pt_2)
        pt_3_arr = np.array(pt_3)
        pt_4_arr = np.array(pt_4)

        rec_pt_1_arr = np.array(rec_pt_1)
        rec_pt_2_arr = np.array(rec_pt_2)
        rec_pt_3_arr = np.array(rec_pt_3)
        rec_pt_4_arr = np.array(rec_pt_4) 

        src_arr = np.zeros((4,2))
        dst_arr = np.zeros((4,2))

        src_arr[0,:] = pt_1_arr
        src_arr[1,:] = pt_2_arr
        src_arr[2,:] = pt_3_arr
        src_arr[3,:] = pt_4_arr

        dst_arr[0,:] = rec_pt_1_arr
        dst_arr[1,:] = rec_pt_2_arr
        dst_arr[2,:] = rec_pt_3_arr
        dst_arr[3,:] = rec_pt_4_arr

        print("hui",src_arr)
        print("huihui",dst_arr)

        h, status = cv2.findHomography(src_arr, dst_arr)
        im_out = cv2.warpPerspective(image, h, (image.shape[1],image.shape[0]))
        # im_out = cv2.resize(im_out, (800,800))
        # cv2.imshow("Source Image", cv2.resize(image, (800,800)))
        # cv2.imshow("Destination Image", cv2.resize(image, (800,800)))
        # cv2.imshow("Warped Source Image", im_out)
        # cv2.waitKey(0)
        cv2.imwrite(fr"C:\Users\Mohtashim Butt\Documents\Fall-2022\CV\Project\top_view_clips_curved_lane_version\{p}.jpg",im_out)
    
    frameSize = (1280, 720)


    # hehe = cv2.VideoWriter('input_video_lane_change_version.avi',cv2.VideoWriter_fourcc(*'DIVX'), 5, frameSize)

    # for blah in glob.glob(r'C:\Users\Mohtashim Butt\Documents\Fall-2022\CV\Project\Project_Dataset\clips\0530\1492626329051620125_0\*.jpg'):
    #     img = cv2.imread(blah)
    #     hehe.write(img)
    # hehe.release()
    # for M in range(1,40):
    #     img = cv2.imread(fr'C:\Users\Mohtashim Butt\Documents\Fall-2022\CV\Project\Project_Dataset\clips\0601\1494452381594376146\{M}.jpg')
        # img = cv2.imread(blah)
        # cv2.imshow("hehehe",img)
        # cv2.waitKey(0)
    #     hehe.write(img)
    # hehe.release()
    # frameSize = (800, 800)
    # out = cv2.VideoWriter('output_video_lane_change_version.avi',cv2.VideoWriter_fourcc(*'DIVX'), 5, frameSize)

    # for filename in glob.glob(r'C:\Users\Mohtashim Butt\Documents\Fall-2022\CV\Project\top_view_clips\*.jpg'):
    #     img = cv2.imread(filename)
    #     out.write(img)

    # out.release()
    # for M in range(1,40):
    #     img = cv2.imread(fr'C:\Users\Mohtashim Butt\Documents\Fall-2022\CV\Project\top_view_clips_lane_change_version/{M}.jpg')
        # img = cv2.imread(blah)
        # cv2.imshow("hehehe",img)
        # cv2.waitKey(0)
    #     hehe.write(img)
    # hehe.release()


    

main()
