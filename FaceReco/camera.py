import cv2
import face_recognition
from index.models import UserProfile
import numpy as np
from index.views import known_face_encodings, known_face_names

known_face_names = []
known_face_encodings = []
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.video.set(3,640)
        self.video.set(4,480)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        rgb_image = image[:, :, ::-1]
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_image, model="cnn")
            face_encodings = face_recognition.face_encodings(rgb_image, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                face_names.append(name)
                for users in UserProfile.objects.all():
                    if users.user.first_name+users.user.last_name == name and users.route[len(users.route)-1] != "first":
                        users.route.append("first")
                        users.save()
                        print("sss")
        process_this_frame = not process_this_frame
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 1
            right *= 1
            bottom *= 1
            left *= 1
            cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
class VideoCamera2(object):
    def __init__(self):
        self.video = cv2.VideoCapture(2)
        self.video.set(3,640)
        self.video.set(4,480)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        rgb_image = image[:, :, ::-1]
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_image, model="cnn")
            face_encodings = face_recognition.face_encodings(rgb_image, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                face_names.append(name)
                for users in UserProfile.objects.all():
                    if users.user.first_name+users.user.last_name == name and users.route[len(users.route)-1] != "second":
                        users.route.append("second")
                        users.save()
        process_this_frame = not process_this_frame
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 1
            right *= 1
            bottom *= 1
            left *= 1
            cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

def gen(camera):
    for name in UserProfile.objects.all():
        known_face_names.append(name.user.first_name + name.user.last_name)
        known_face_encodings.append(np.array(name.face_codes, np.float128))
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
