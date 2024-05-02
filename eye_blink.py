#-----Use VideoCapture in OpenCV-----
import cv2
import dlib
import math
from functions import *
from morse_converter import converter
BLINK_RATIO_THRESHOLD = 5.4

#-----livestream from the webcam----- 
cap = cv2.VideoCapture(0)

'''in case of a video
cap = cv2.VideoCapture("__path_of_the_video__")'''

#-----name of the display window in OpenCV-----
cv2.namedWindow('DECODE', cv2.WINDOW_NORMAL)
cv2.resizeWindow('DECODE', 1200, 700)

#-----Training a Model : Face detection with dlib-----
detector = dlib.get_frontal_face_detector()

#-----Detecting Eyes using landmarks in dlib-----
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
#-----these landmarks are based on the standard 68 points -----
left_eye_landmarks  = [36, 37, 38, 39, 40, 41]
right_eye_landmarks = [42, 43, 44, 45, 46, 47]

timer = 0
str = ''
duration = ''

while True:
    #-----capturing frame-----
    frame_read, frame = cap.read()

    #-----exit the application if frame not found-----
    if not frame_read:
        print("Can't receive frame (stream end?). Exiting ...")
        break 

    #-----converting image to grayscale-----
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #-----Face detection with dlib-----
    #detecting faces in the frame 
    faces,_,_ = detector.run(image = frame, upsample_num_times = 0, adjust_threshold = 0.0)

    #-----Detecting Eyes using landmarks in dlib-----
    for face in faces:
        
        landmarks = predictor(frame, face)

        #-----Calculating blink ratio for one eye-----
        left_eye_ratio  = get_blink_ratio(left_eye_landmarks, landmarks)
        right_eye_ratio = get_blink_ratio(right_eye_landmarks, landmarks)
        blink_ratio     = (left_eye_ratio + right_eye_ratio) / 2
        
        if blink_ratio > BLINK_RATIO_THRESHOLD:
            #-----Blink detected!-----
            fl=f'{timer}'
            cv2.putText(frame, fl, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 2,(255,255,255),2,cv2.LINE_AA)
            timer+=1
        else: 
            #-----detect if dot or dash-----
            if timer>20 and timer<=40:    
                str+='.'                
            if timer>40:   
                str+='-' 
            if timer>1 and timer<=20:        
                str+=' '
            timer = 0
        
        cv2.putText(frame,str,(10,100), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
        cv2.putText(frame,converter(str),(10,160), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)

        # print(converter(s))

    cv2.imshow('DECODE', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

#-----releasing the VideoCapture object-----
cap.release()
cv2.destroyAllWindows()