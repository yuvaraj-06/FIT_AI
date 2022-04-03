import cv2 
import json
import math
import numpy as np
import cv2
import time
import posemodule as pm

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.detector = pm.poseDetector()
        self.cnt_sq=0
        self.cnt_pu=0
        self.cnt_pu=0
        self.cnt_wt=0
        self.cnt_cr=0
        print("videocap started")

    def __del__(self):
        self.video.release()

    def get_frame(self,ex):
             
            if ex=="squats":
                            #print("assssssssssssssssssssss")
                            pTime = 0
                        
                            self.cnt_sq = 0

                            f=0
                        
                       # while self.cnt_sq < 100000000:
                            ret, img = self.video.read()
                            img = self.detector.findPose(img)
                            lmlist = self.detector.getPosition(img,draw=False)
                            
                            # if u want all dots then put draw= true and comment out the cv2.circle part in the if part below
                            
                            if len(lmlist)!=0:
                                cv2.circle(img,(lmlist[25][1],lmlist[25][2]),10,(0,0,255),cv2.FILLED)
                                cv2.circle(img,(lmlist[23][1],lmlist[23][2]),10,(0,0,255),cv2.FILLED) 
                                #print(lmlist[23])
                                y1 = lmlist[25][2]
                                y2 = lmlist[23][2]
                                
                                length = y2-y1
                                if length>=0 and f==0:
                                    f=1
                                elif length<-50 and f==1:
                                    f=0
                                    self.cnt_sq=self.cnt_sq+1       

                                cTime = time.time()
                                fps = 1/(cTime-pTime)
                                pTime = cTime
                                cv2.putText(img,"Total Number of Squats  "+str(int(self.cnt_sq)),(70,50),cv2.FONT_HERSHEY_DUPLEX,1,
                                (60,100,255),3)
                                cv2.putText(img,"Calories Burnt  "+str(int(self.cnt_sq)*0.32),(70,150),cv2.FONT_HERSHEY_DUPLEX,1,
                                (60,100,255),3)
                               # img = cv2.resize(img, (600,600))                 # Resize image
                                
                                calories = 0.32*self.cnt_sq

                            ret, jpeg = cv2.imencode('.jpg', img)
                            return jpeg.tobytes()
        
            elif ex=="push":
                            self.cnt_sq = 0

                            f=0
                        #time.sleep(5)
                       # while True and self.cnt_sq<10000:
                            ret, img = self.video.read()
                            img = self.detector.findPose(img)
                            lmlist = self.detector.getPosition(img,draw=False)
                            #print(lmlist[3])
                            
                            if len(lmlist)!=0:
                                cv2.circle(img,(lmlist[14][1],lmlist[14][2]),10,(0,0,255),cv2.FILLED)
                                cv2.circle(img,(lmlist[0][1],lmlist[0][2]),10,(0,0,255),cv2.FILLED) 
                                y1 = lmlist[14][2]
                                y2 = lmlist[0][2]
                                
                                length = y2-y1
                                if length>=0 and f==0:
                                    f=1
                                elif length<-50 and f==1:
                                    f=0
                                    self.cnt_sq=self.cnt_sq+1


                                #print(length)

                            
                                cv2.putText(img,"Pushup"+str(int(self.cnt_sq)),(70,250),cv2.FONT_HERSHEY_DUPLEX,2,
                                (60,100,255),2)
                                cv2.putText(img,"Burnt"+str(int(self.cnt_sq)*0.29),(70,350),cv2.FONT_HERSHEY_DUPLEX,2,
                                (60,100,255),2)
                               # img = cv2.resize(img, (620,650))                    # Resize image
                                
                                calories = 0.29*self.cnt_sq
                            ret, jpeg = cv2.imencode('.jpg', img)
                            return jpeg.tobytes()
            elif ex=="pull":
                ret, img = self.video.read()
                img = self.detector.findPose(img)
                lmlist = self.detector.getPosition(img,draw=False)
                f=0
                if len(lmlist)!=0:
                    cv2.circle(img,(lmlist[15][1],lmlist[15][2]),10,(0,0,255),cv2.FILLED)
                    cv2.circle(img,(lmlist[3][1],lmlist[3][2]),10,(0,0,255),cv2.FILLED) 
                    y1 = lmlist[3][2]
                    y2 = lmlist[20][2]
                    
                    length = y2-y1
                    if length>=0 and f==0:
                        f=1
                    elif length<0 and f==1:
                        f=0
                        self.cnt_sq=self.cnt_sq+1

                    cv2.putText(img,"Total Number of Pullups  "+str(int(self.cnt_sq)),(70,250),cv2.FONT_HERSHEY_DUPLEX,3,
                    (60,100,255),3)
                    cv2.putText(img,"Calories Burnt  "+str(int(self.cnt_sq)*1),(70,350),cv2.FONT_HERSHEY_DUPLEX,3,
                    (60,100,255),3)
                                        # Resize image
                ret, jpeg = cv2.imencode('.jpg', img)
                return jpeg.tobytes()
            elif ex=="cru":
                ret, img = self.video.read()
                img = self.detector.findPose(img)
                lmlist = self.detector.getPosition(img,draw=False)
                f=0
                if len(lmlist)!=0:
                                x1 = lmlist[0][1]
                                x2 = lmlist[12][1]
                                
                                length = x1-x2
                                if length>=0 and f==0:
                                    f=1
                                elif length<0 and f==1:
                                    f=0
                                    self.cnt_sq=self.cnt_sq+1

 
                                cv2.putText(img,"Total Number of Crunches  "+str(int(self.cnt_sq)),(70,50),cv2.FONT_HERSHEY_DUPLEX,1,
                                (60,100,255),3)
                                cv2.putText(img,"Calories Burnt  "+str(int(self.cnt_sq)*0.32),(70,150),cv2.FONT_HERSHEY_DUPLEX,1,
                                (60,100,255),3)
                ret, jpeg = cv2.imencode('.jpg', img)
                return jpeg.tobytes()
            elif ex=="weight":
                ret, img = self.video.read()
                img = self.detector.findPose(img)
                lmlist = self.detector.getPosition(img,draw=False)
                f=0
                if len(lmlist)!=0:
                                cv2.circle(img,(lmlist[17][1],lmlist[17][2]),20,(0,0,255),cv2.FILLED)
                                cv2.circle(img,(lmlist[13][1],lmlist[13][2]),20,(0,255,0),cv2.FILLED) 
                                y1 = lmlist[17][2]
                                y2 = lmlist[13][2]
                                
                                length = y2-y1
                                if length>=0 and f==0:
                                    f=1
                                elif length<0 and f==1:
                                    f=0
                                    self.cnt_sq=self.cnt_sq+1

                                cv2.putText(img,"Total Number of bicep curls  "+str(int(self.cnt_sq)),(70,50),cv2.FONT_HERSHEY_DUPLEX,1,
                                (60,100,255),3)
                                cv2.putText(img,"Calories Burnt  "+str(int(self.cnt_sq)*0.32),(70,150),cv2.FONT_HERSHEY_DUPLEX,1,
                                (60,100,255),3)
                ret, jpeg = cv2.imencode('.jpg', img)
                return jpeg.tobytes()




                    