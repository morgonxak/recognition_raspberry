from threading import Thread

from modul.camera import Camera
from modul.settings import Settings
from modul.database import DataBase
from modul.processing_faceId import processing_faceid
from modul.periphery import Periphery
import cv2
import os

settings = Settings('rc/settings')
settings.load()

door = Periphery()
door.start()

camera = Camera(settings.settings['ID_CARARA'])
dataBase = DataBase(settings.settings['PATH_DATA_BASE'])
face_detector = cv2.CascadeClassifier(os.path.join(settings.settings['PATH_SAVE_MODEL'], 'haarcascade_frontalface_default.xml'))
dedect = processing_faceid(settings.settings['PATH_SAVE_MODEL'])

mode_camera = True
frame = None

def updateFrame():
    global mode_camera, frame

    while mode_camera:
        frame = camera.get_frame()


if __name__ == '__main__':
    camera_thread = Thread(target=updateFrame)
    camera_thread.start()

    while True:
        if frame is None: continue
        if os.path.isfile(os.path.join(settings.settings['PATH_SAVE_MODEL'], 'dataBase_1.pk')):
            print("необходимо обновить классификатор")
            dedect.update_classificator(settings.settings['PATH_SAVE_MODEL'])

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            local_face = frame[y:y + w, x:x + h]
            # cv2.imshow("face", local_face)
            personID = dedect.predict_freme(local_face)
            print(personID)
            if not personID is None:
                print("sadsadasdsadasdsa", personID)
                door.open_door()

        # cv2.imshow("te", frame)
        cv2.waitKey(1)
