import cv2 as cv
import numpy as np
import os
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_recognizer.yml')

for person in os.listdir('Faces/val'):
    for img_name in os.listdir(os.path.join('Faces/val', person)):
        img_path = os.path.join('Faces/val', person, img_name)
        img = cv.imread(img_path)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        detect_face = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

        for (x, y, w, h) in detect_face:
            roi = gray[y:y+h, x:x+w]
            label, confidence = face_recognizer.predict(roi)

            # Draw rectangle around the face
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Put label text
            cv.putText(img, f"{people[label]} ({int(confidence)})", (x, y - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Show result
        cv.imshow('Prediction', img)
        cv.waitKey(0)

cv.waitKey(0)