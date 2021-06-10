import cv2
import imutils
import numpy as np
import argparse


def avwidths(arr):
    if len(arr) == 0:
        return 0
    else:
        return sum(arr) / len(arr)

def detect(frame):
    vio=0
    (bounding_box_cordinates, weights) = HOGCV.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 1.03)    
    bounding_box_cordinates = np.array([[x, y, x + w, y + h] for (x, y, w, h) in bounding_box_cordinates])
       
    person = 1
    centers=[]
    widths=[]

    #w= width
    #h=height
    #c=center

    for (xmax, ymax, xmin, ymin) in bounding_box_cordinates: #rectangle for each person      
        cv2.rectangle(frame, (xmax, ymax), (xmin, ymin), (0, 255, 0), 2)

    for (xmax, ymax, xmin, ymin) in bounding_box_cordinates: #calculating center
        widths.append(xmin-xmax)
        xC=xmax+((xmin-xmax)/2)
        yC=ymax+((ymin-ymax)/2)
        centers.append((xC,yC))        
        person += 1
        
    
    cv2.putText(frame, 'Status : Detecting', (5,25), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0,255,0), 2) #Giving status to screen
    cv2.putText(frame, f'Total Person : {person-1}', (5,55), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0,255,0), 2) #Total person number
    
    violations=[]
    averageWidths = avwidths(widths)
    distance=2*averageWidths 
    for i,person1 in enumerate(centers):
        for k,person2 in enumerate(centers[i+1:]):           
              if abs(person1[1] - person2[1])< distance // 2:                   
                    violations.append((i,k+i+1))
                  
                 
    for (i,k) in violations: #putting red rectangle for violations 
        vio=vio+1 #violations have been committed

        (xmax, ymax, xmin, ymin) = bounding_box_cordinates[i]
        cv2.rectangle(frame, (xmax, ymax), (xmin, ymin), (0, 0, 255), 3)
        (xmax, ymax, xmin, ymin) = bounding_box_cordinates[k]
        cv2.rectangle(frame, (xmax, ymax), (xmin, ymin), (0, 0, 255), 3)
        
    cv2.putText(frame, f'HIGH RISK : {vio}', (5,100), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0,255,0), 2)

    cv2.imshow('output', frame)
    return frame

def detectByPathVideo(path):

    video = cv2.VideoCapture('http://192.168.0.100:8080/video')
    check, frame = video.read()#checking video location
    if check == False: 
        print('Video Not Found. Please Enter a Valid Path (Full path of Video Should be Provided).')
        return

    print('Detecting people...')
    while video.isOpened():
        check, frame =  video.read()

        if check:
            frame = imutils.resize(frame , width=min(1000,frame.shape[1])) #resizing video 
            frame = detect(frame)
            
            key = cv2.waitKey(1)
            if key== ord('q'): #break command
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()


path = "pedestrians.mp4"#video path
HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

detectByPathVideo(path)