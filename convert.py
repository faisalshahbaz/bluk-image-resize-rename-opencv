import cv2
import glob
import os

# Get images
imgs = glob.glob('/home/lfd/watermark/CVPR17_training_code/TrainData/label/image*.png')


folder = 'resized'
if not os.path.exists(folder):
    os.makedirs(folder)
    
count = 1

for img in imgs:
    pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    #print(img)
    # height = int(width * pic.shape[0] / pic.shape[1])
    pic = cv2.resize(pic, (1015, 653))
    cv2.imwrite(folder + '/image'+str(count)+'.png', pic)
    count += 1
