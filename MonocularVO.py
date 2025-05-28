import cv2
import numpy as np

# Create a blank black image (300x300 pixels, 3 color channels)
image = np.zeros((300, 300, 3), dtype=np.uint8)

# Draw a blue rectangle (BGR format)
cv2.rectangle(image, (50, 50), (250, 250), (255, 0, 0), thickness=3)

# Put white text on the image
cv2.putText(image, "Hello OpenCV", (60, 150),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

# Display the image
cv2.imshow("OpenCV Test", image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()