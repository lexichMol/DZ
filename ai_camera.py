from deepface import DeepFace
import cv2
def take_a_photo():
    a = 0
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        cv2.imshow('Result', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            face_analyze(img)
            break

def face_analyze(img):
    try:
        result_dict = DeepFace.analyze(img_path=img, actions=['emotion'])

        print('[+] emotion:')
        print(result_dict[0].get('dominant_emotion'))

        for k, v in result_dict[0].get('emotion').items():
            print(f'{k} - {round(v, 2)}%')
    except Exception as _ex:
        return _ex
take_a_photo()
