import cv2
import numpy as np
# Load the image
img = cv2.imread('C:/Users/nature4.jpg')
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply median blur to reduce noise
gray = cv2.medianBlur(gray, 5)
# Detect edges using adaptive thresholding
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
# Convert the image to color
color = cv2.bilateralFilter(img, 10, 300, 300)
# Combine the color image with the edges mask
cartoon = cv2.bitwise_and(color, color, mask=edges)
# Convert the image from BGR to HSV color space
hsv = cv2.cvtColor(cartoon, cv2.COLOR_BGR2HSV)
# Increase the saturation by a factor of 1.5 to make the colors more vivid
hsv[:,:,1] = np.clip(hsv[:,:,1] * 1.5, 0, 255)
# Finally, convert the image back from HSV to BGR color space
cartoon_enhanced = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
# Display the cartoon image
cv2.imshow("Cartoon", cartoon_enhanced)
cv2.imwrite('C:/Users/cartoon_enhanced_image.png', cartoon_enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows()