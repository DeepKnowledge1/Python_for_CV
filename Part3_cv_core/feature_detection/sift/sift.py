import cv2
import numpy as np

# === SINGLE IMAGE SIFT ===
# Load image
img = cv2.imread(r"C:\Users\abdulgader\Downloads\av.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and descriptors
keypoints, descriptors = sift.detectAndCompute(gray, None)

# Draw keypoints
img_with_keypoints = cv2.drawKeypoints(img, keypoints, None)

# Show results
cv2.imshow("SIFT Features", img_with_keypoints)
cv2.waitKey(0)

print(f"Found {len(keypoints)} keypoints")

# === COMPARE TWO IMAGES ===
# Load two images
img1 = cv2.imread(r"C:\Users\abdulgader\Downloads\av.png")
img2 = cv2.imread(r"C:\Users\abdulgader\Downloads\av1.png")
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Find keypoints and descriptors
kp1, desc1 = sift.detectAndCompute(gray1, None)
kp2, desc2 = sift.detectAndCompute(gray2, None)

# Match features
bf = cv2.BFMatcher()
matches = bf.knnMatch(desc1, desc2, k=2)

# Filter good matches
good = []
for m, n in matches:
    dis = m.distance < 0.7 * n.distance
    if dis:
        good.append([m])

# Draw matches
img_matches = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)

# Show matches
cv2.imshow("Matches", img_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Found {len(good)} good matches")
