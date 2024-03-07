import time
import numpy as np
import cv2
import sys
sys.path.append("./RobotGazeFollowing_new")

from gaze_tracker_print_1080p import GAZE_TRACKER
from gaze_estimation.personal import Personal_Module



class ARC():
    def __init__(self):
        self.center = [0, 0]
        self.pitch = []
        self.yaw = []
        self.ear=[]
        self.ear2=[]
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.tracker = GAZE_TRACKER(0)
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
        # self.cap.set(cv2.CAP_PROP_AUTOFOCUS,0)
        self.total_angle = 50
        # self.total_angle = 196.5
        self.a_h = 1.23
        self.a_w=2.16
        self.width = 1920
        self.height = 1080
        # self.width = 3880
        #self.a_h = 1.56
        self.arc_center = []
        self.user_pos = []
        self.u_c_angle = 0
        self.u_c_distance = 0
        self.R = 1.0
        # self.R = 1.4
        self.p_m = Personal_Module()
        self.cali_ready = False
        self.cali_start = 0
        self.cali_start2 = 0
        self.now = 0

    def calibration(self):
        if self.cali_start == 0:
            self.cali_start = time.time()
        rval, frame = self.cap.read()
        re, flag, focusing, attention_vec, face_center = self.tracker.run(frame, [], [], False)
        ear=self.tracker.blink_detector.ear
        if not re:
            return False, False

        if focusing:
            pitch = np.arcsin(-attention_vec[1])
            yaw = np.arcsin(-attention_vec[0] / np.cos(pitch))
            ear=self.tracker.blink_detector.ear
            self.pitch.append(pitch)
            self.yaw.append(yaw)
            self.ear.append(ear)
            self.now = time.time()
            if self.now - self.cali_start > 1:
                self.center[0] = np.average(self.pitch)
                self.center[1] = np.average(self.yaw)
                self.earout=np.average(self.ear)
                self.tracker.blink_detector.thres1=self.earout-0.01
                print("thres1",self.tracker.blink_detector.thres1)
                self.cali_ready = True
                print("self.center",self.center)
                return True, True
            return True, False
        else:
            self.cali_start = time.time()
            self.pitch = []
            self.yaw = []
            self.ear=[]
            return True, False
    def calibration2(self):
        if self.cali_start2 == 0:
            self.cali_start2 = time.time()
        rval, frame = self.cap.read()
        re, flag, focusing, attention_vec, face_center = self.tracker.run(frame, [], [], False)
        ear=self.tracker.blink_detector.ear
        if not re:
            return False, False
        ear=self.tracker.blink_detector.ear
        
        self.ear.append(ear)
        print(time.time()-self.cali_start2)

        if time.time()-self.cali_start2<=3:
            
            ear2=self.tracker.blink_detector.ear
            self.ear2.append(ear2)
            
            return True
        else:
            minear=np.min(self.ear2)
            self.tracker.blink_detector.thres2=minear+0.3*(self.tracker.blink_detector.thres1-minear)
            print("thres2",self.tracker.blink_detector.thres2)
            return False


    def calculate(self):
        rval, frame = self.cap.read()
        re, flag, focusing, attention_vec, face_center = self.tracker.run(frame, [], [], False)
        if not re and flag:
            return int(self.width / 2), int(self.height/2)
        pitch = np.arcsin(-attention_vec[1])
        yaw = np.arcsin(-attention_vec[0] / np.cos(pitch))
        distance = self.height * (np.tan(pitch)-np.tan(self.center[0])) * self.R / self.a_h
        #distance= (np.cos(yaw)*self.R*np.tan(pitch)-np.cos(self.center[1])*self.R*np.tan(self.center[0]))/self.a_h*self.height
        #distance = self.height * np.tan(del_pitch) * self.R / self.a_h  # a.h应该是显示器的高度
        del_yaw = (yaw-self.center[1])*180/np.pi
        scale = del_yaw / self.total_angle
        #x = self.width/2+scale*self.width
        x_distance = self.width*(self.R*np.tan(yaw)-self.R*np.tan(self.center[1]))/self.a_w
        x = self.width / 2 + x_distance
        y = self.height/2 - distance
        if x<=0:
            x=20
        if x>=1920:
            x=1890
        if y<=0:
            y=20
        if y>=1080:
            y=1060
        #print("pitch,yaw",pitch,yaw)
        #print("pos:",x,y)
        return int(x), int(y)


    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    t = ARC()
    t.calibration()
    print(t.calculate())



