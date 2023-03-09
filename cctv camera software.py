import cv2
import time     # cctv requires the current time
import os

def minimizeWindow():
    import win32gui,win32con
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window,win32con.SW_MINIMIZE)

def cctv():
    video = cv2.VideoCapture(0)     #parameter = primary camera
    video.set(3, 640)   # defined resolution, parameters = width, height
    video.set(4,480)
    width = video.get(3)
    height = video.get(4)
    print("Video resolution is set to {} x {}".format(width, height))
    print("Help-- \n1. Press z to exit.\n2. Press m to minimize.")

    fgbg = cv2.createBackgroundSubtractorMOG2()
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # get current date and time of vid recording
    date_time = time.strftime("rec %d-%m-%y %H-%M-%S")

    name = ("C://Users//Aimee//Documents//C - 2nd Year Uni//PERSONAL CODING PROJECTS//Python Projects//Project 1 - CCTV Camera Software//footages//"+date_time+".mp4v")   # created folder to save the footages
    out = cv2.VideoWriter(name,fourcc,20,(640,480),False)

    while video.isOpened():
        check, frame = video.read()
        if check == True:
            frame = cv2.flip(frame,1)

            t = time.ctime()
            cv2.rectangle(frame,(5,5,100,20),(255,255,255),cv2.FILLED)

            # writing stuff on the video screen like 'Camera 1' and the time.
            cv2.putText(frame,"Camera 1",(20,20),cv2.FONT_HERSHEY_DUPLEX,0.5,(5,5,5),1)
            cv2.putText(frame,t,(420,460),cv2.FONT_HERSHEY_DUPLEX,0.5,(5,5,5),1)

            #frame showing.
            cv2.imshow("CCTV camera",frame)

            # makes the video
            out.write(frame)

            #saves video in folder
            if cv2.waitKey(1) == ord("z"):    # if user presses esc key...
                print("Video footage saved in current directory")
                break
            elif cv2.waitKey(1) == ord("m"):    # if user presses m then...
                minimizeWindow()
        else:
            print("Can't open camera, check configuration.")
            break
    video.release()
    out.release()
    cv2.destroyAllWindows()

print("*"*80+ "\n" + " " *30+"Welcome to cctv software\n"+"*"*80)
ask = int(input("Do you want to open the cctv?\n1. yes\n2. no\n>>>"))

if ask == 1:
    cctv()
elif ask == 2:
    print("Bye bye!")
    exit()
