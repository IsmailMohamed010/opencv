import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

DIR = r'Faces/train'
haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
features = []
labels = [] 
def create_train():
    for person in people:
        for img in os.listdir(os.path.join(DIR, person)):
            image = cv.imread(os.path.join(DIR, person, img))
            image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in faces_rect:
                faces_roi = image[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(people.index(person))

create_train()

print(len(features))
print(len(labels))  

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

np.save('features.npy', features)
np.save('labels.npy', labels)

face_recognizer.save('face_recognizer.yml')