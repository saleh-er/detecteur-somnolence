import cv2
import dlib
import imutils
from imutils import face_utils
from utils import calculate_ear

# Seuils de détection
EAR_THRESHOLD = 0.25
CONSECUTIVE_FRAMES = 20

# Initialisation
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("../models/shape_predictor_68_face_landmarks.dat")

# Indices des points pour les yeux gauche et droit
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

cap = cv2.VideoCapture(0)
counter = 0

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=600)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    rects = detector(gray, 0)
    
    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        
        ear = (calculate_ear(leftEye) + calculate_ear(rightEye)) / 2.0
        
        # Dessiner les contours des yeux pour le feedback visuel
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        if ear < EAR_THRESHOLD:
            counter += 1
            if counter >= CONSECUTIVE_FRAMES:
                cv2.putText(frame, "ALERTE SOMNOLENCE !", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            counter = 0
            
    cv2.imshow("Détecteur de fatigue", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()