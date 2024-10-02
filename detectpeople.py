import cv2

# Load the HOG detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Capture video from the camera
cap = cv2.VideoCapture(1) 

while True:
    ret, frame = cap.read()

    # Check if the frame is valid
    if not ret:
        break

    # Detect people in the frame
    rects, _ = hog.detectMultiScale(frame)

    # Draw rectangles around detected people
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('People Detection', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
