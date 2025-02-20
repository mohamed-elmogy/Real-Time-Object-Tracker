import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# creating tracker
tracker = cv2.TrackerCSRT_create()

# Read the first frame
ret, frame = cap.read()

if not ret:
    print("Error: Could not read frame.")
    cap.release()
    exit()

# Let the user select the object to track
bbox = cv2.selectROI("Select Object", frame, False)
cv2.destroyWindow("Select Object")

# Initialize tracker with selected object
success = tracker.init(frame, bbox)

if not success:
    print("Error: Tracker initialization failed!")
    
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Update the tracker
    success, bbox = tracker.update(frame)

    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Tracking Failure", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display the result
    cv2.imshow("Object Tracker", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
