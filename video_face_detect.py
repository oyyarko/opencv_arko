#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:39:07 2020

@author: arko
"""

import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video.avi', fourcc, 20.0, (640, 480))

haar = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(haar)


while(True):
	ret, frame = cap.read()
	
	if ret==True :
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)'
		
		faces = face_cascade.detectMultiScale(
				frame,
				scaleFactor = 1.1,
				minSize = (30, 40),
				minNeighbors = 3
				)
		
		for (x, y, w, h)  in faces:
			cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 5)
		
		out.write(frame)
		cv2.imshow('video', frame)
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
	
cap.release()
out.release()
cv2.destroyAllWindows()