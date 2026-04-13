import cv2
import csv
from utils.hand_tracker import get_hand_landmarks

cap = cv2.VideoCapture(0)

label = input("Enter gesture label: ")

file = open('gesture_data.csv', 'a', newline='')
writer = csv.writer(file)

while True:
    success, img = cap.read()

    data, img = get_hand_landmarks(img)

    if data:
        data.append(label)
        writer.writerow(data)

    cv2.imshow("Collect Data", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
file.close()
