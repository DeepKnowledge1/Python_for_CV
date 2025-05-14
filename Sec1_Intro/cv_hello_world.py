import cv2 as cv


# load imag
img = cv.imread(r"D:\01-DATA\img1.png")


# check if image loadded correctly

if img is None:
    print("Error: Could not load the image")
    exit()

# convert image to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imwrite("output.png", gray)


cv.imshow("Original", img)
cv.imshow("Gray", gray)
cv.waitKey(0)
cv.destroyAllWindows()
