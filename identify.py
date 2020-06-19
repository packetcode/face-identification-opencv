import cv2

# Initialize the classifier
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read the image
img = cv2.imread("images/portrait-2.jpg")

while True:
    # Get the gray version of our image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Get the coordinates of the location of the face in the picture
    faces = faceCascade.detectMultiScale(gray_img,
                                         scaleFactor=1.2,
                                         minNeighbors=5,
                                         minSize=(50, 50))

    # Draw a rectangle at the location of the coordinates
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the image
    cv2.imshow("Identified Face", img)

    # Wait for the user to press q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all Windows
cv2.destroyAllWindows()
