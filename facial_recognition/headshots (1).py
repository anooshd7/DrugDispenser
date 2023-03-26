import cv2
import os
from time import sleep


def headshots(name):
    
    #name = str(input("Enter you name here: "))
    newpath = r'/home/pi/Desktop/Hackathon/facial_recognition/dataset/' + name

    if not os.path.exists(newpath):
        os.makedirs(newpath)
    #name = 'Bali' #replace with your name

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("press space to take a photo", 500, 300)

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("press space to take a photo", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        #elif k%256 == 32:
            # SPACE pressed
         #   img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
          #  cv2.imwrite(img_name, frame)
           # print("{} written!".format(img_name))
            #img_counter += 1
        else:
            for i in range(5):
                img_name = "facial_recognition/dataset/" + name + "/image_{}.jpg".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
                i += 1
                sleep(1)
                break

    cam.release()

    cv2.destroyAllWindows()
