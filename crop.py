import cv2
import numpy as np
import dlib
import os
from imutils import face_utils
from imutils.video import VideoStream

#This program is used to make data for training by cropping eyes of user.
dirname = 'data'
model = "shape_predictor_68_face_landmarks.dat"
face_detect = dlib.get_frontal_face_detector()
face_pose = dlib.shape_predictor(model)
vs = VideoStream().start()
j = 1308

while True:
    frame = vs.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_faces = face_detect(gray, 1)
    for i, face_rect in enumerate(detected_faces):
        # Get the the face's pose
        pose_landmarks = face_pose(gray, face_rect)
        pose_landmarks = face_utils.shape_to_np(pose_landmarks)
        LE = gray[pose_landmarks[37][1]-3:pose_landmarks[40][1]+3,pose_landmarks[36][0]-3:pose_landmarks[39][0]+3]
        RE = gray[pose_landmarks[43][1]-3:pose_landmarks[47][1]+3,pose_landmarks[42][0]-3:pose_landmarks[45][0]+3]
        cv2.imwrite(os.path.join(dirname, 'E'+str(j)+'L.jpg'), cv2.equalizeHist(LE))
        cv2.imwrite(os.path.join(dirname, 'E'+str(j)+'R.jpg'), cv2.equalizeHist(RE))
        j = j+1

dlib.hit_enter_to_continue()
