import cv2
from utils.hand_tracker import get_hand_landmarks
from utils.predictor import predict_gesture
from utils.alert import play_alert, show_alert
from config.labels import GESTURE_LABELS

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    data, img = get_hand_landmarks(img)

    if data:
        gesture = predict_gesture(data)
        message = GESTURE_LABELS.get(gesture, "Unknown")

        cv2.putText(img, message, (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 3)

        if message == "EMERGENCY":
            play_alert()
            show_alert(message)

    cv2.imshow("Patient Alert System", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
