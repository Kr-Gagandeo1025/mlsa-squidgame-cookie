import cv2
from cvzone import overlayPNG
import hand_detection_module as HD 
import numpy as np
import os
import time
path = 'frames'
path2 = 'img'
mylist = os.listdir(path)
mylist2 = os.listdir(path2)
graphic = [cv2.imread(f'{path}/{imPath}') for imPath in mylist]
graphic2 = [cv2.imread(f'{path2}/{imPath2}') for imPath2 in mylist2]
intro = graphic[0]
kill = graphic[1]
winner = graphic[2]

cookie = graphic2[1]
mlsa =  graphic2[0]
#INTRO SCREEN WILL STAY UNTIL Q IS PRESSED
while True:
    cv2.imshow('Squid Game', cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
gameOver = False
NotWon =True

#GAME LOGIC
cam = cv2.VideoCapture(0)
cookie_img = cv2.imread('img/sqr(2).png')
size = 200
cookie_img = cv2.resize(cookie_img, (size, size))
  
# Create a mask of logo
img2gray = cv2.cvtColor(cookie_img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
detector = HD.HandDetector()
mnlst=[]
i = 0
while True:
    ret, img = cam.read()
    imgflip = cv2.flip(img,1)
    roi = imgflip[-size-200:-200, -size-200:-200]
    roi[np.where(mask)] = 1
    roi += cookie_img
    img = detector.findHands(imgflip)
    lnList = detector.findPosition(imgflip)

    if(lnList):
        index1=lnList[8]
        # print(index1)
        mX=index1[1]
        mY=index1[2]
        mnlst.append([mX,mY])
        for j in mnlst:
            cv2.circle(imgflip,(j[0],j[1]),4,(255,0,0),-1)
        # mX = np.interp(index1Y, (0,640),(0,1920))
        # mY = np.interp(index1X, (0,480),(0,1080))
    # cv2.imshow("Image",imgflip)
    # alpha = 0.4  # Transparency factor.
    # cookieimg_new = cv2.addWeighted(imgflip[150:250,150:250,:], alpha, roi, 1 - alpha, 0)
    # imgflip[150:250,150:250] = cookieimg_new 
    cv2.imshow('game',cv2.resize(imgflip,(0,0),fx=0.69,fy=0.69))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break