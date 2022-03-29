import cv2
import numpy as np
import time
import face_recognition as fr
import os
import csv

path = "D:\Work\Projects\MusicalFace\src"

# imgFenris = 'D:/Work/Projects/MusicalFace/src/Rishabh.jpg'
imgFenris = fr.load_image_file("D:\Work\Projects\MusicalFace\src\Rishabh.jpg")
imgFenris = cv2.cvtColor(imgFenris, cv2.COLOR_BGR2RGB)
faceLoc = fr.face_locations(imgFenris)[0]
encodeFenris = fr.face_encodings(imgFenris)[0]


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while cap.isOpened():
    ret, img = cap.read()
    img = np.flip(img, axis=1)
    faceLocLive = fr.face_locations(img)
    encodeLive = fr.face_encodings(img, faceLocLive)
    for encodeFrame, faceFrame in zip(encodeLive, faceLocLive):
        results = fr.compare_faces([encodeFenris], encodeFrame)
        facedis = fr.face_distance([encodeFenris], encodeFrame)
        cv2.putText(
            img,
            f"{results}, Fenris",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
        ) if results == [True] else cv2.putText(
            img, f"{results}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2
        )
        cv2.imshow("Anonimity is Key !", img)
        k = cv2.waitKey(10)
        if k == 27:
            break
    # break
