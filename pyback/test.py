import numpy as np
import cv2 as cv
import json

cap = cv.VideoCapture('../../web/video/Game_Of_Hunting_EP1_new.mp4')

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'MPEG')
out = cv.VideoWriter('../../web/video/output.avi', fourcc, 24.0, (1920, 1080))

data = json.load(open('data.json'))

frame_idx = 0

while cap.isOpened():
    ret, frame = cap.read()

    if ret:

        f = [f for f in data if f['frame_idx'] == frame_idx][0]

        vis = frame.copy()
        key_points = f['key_points']
        for kp in key_points:
            cv.rectangle(vis, (kp['pt'][0]-2,kp['pt'][1]-2),(kp['pt'][0]+2,kp['pt'][1]+2),kp['color'],-1)

        cv.imshow('frame', vis)
            # write the frame
        out.write(vis)
        frame_idx += 1

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()
