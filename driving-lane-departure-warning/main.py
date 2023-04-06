"""Departure Warning System with a Monocular Camera"""

__author__ = "Junsheng Fu"
__email__ = "junsheng.fu@yahoo.com"
__date__ = "March 2017"


from lane import *
import glob
from moviepy.editor import VideoFileClip


if __name__ == "__main__":

    demo = 1 # 1: image, 2 video

    if demo == 2:
        for blah in glob.glob(r'C:\Users\Mohtashim Butt\Documents\Fall-2022\CV\Project\yolov7\runs\detect\exp8\*.jpg'):
            # imagepath = fr'C:\Users\Mohtashim Butt\Documents\Fall-2022\CV\Project\yolov7\runs\detect\exp\{1}.jpg'
            img = cv2.imread(blah)
            cv2.imshow("Raw",img)
            cv2.waitKey(0)
            img_aug = process_frame(img)

            f, (ax1, ax2) = plt.subplots(1, 2, figsize=(25, 9))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            ax1.imshow(img)
            ax1.set_title('Original Image', fontsize=30)
            img_aug = cv2.cvtColor(img_aug, cv2.COLOR_BGR2RGB)
            ax2.imshow(img_aug)
            ax2.set_title('Augmented Image', fontsize=30)
            print("AJEEEEEEEEB")
            plt.show()
            cv2.imshow("ajeeeeb_yaar",img)
            cv2.imshow("FML_More",img_aug)
            cv2.waitKey(0)

    else:
        video_output = r'C:\Users\Mohtashim Butt\Documents\Fall-2022\CV\Project\driving-lane-departure-warning\examples\project_video_curved_lane_version.mp4'
        clip1 = VideoFileClip(r"C:\Users\Mohtashim Butt\Documents\Fall-2022\CV\Project\Object_detedted_Front_view_curved_lane_version.avi")
        print("FUck")
        clip = clip1.fl_image(process_frame) #NOTE: it should be in BGR format
        clip.write_videofile(video_output, audio=False)

