import cv2
import os


# 1. `__init__`: Initialize the class with an optional image
# 2. `load`: Load an image from a file
# 3. `save`: Save the current image to a file
# 4. `display`: Display the current image
# 5. `reset`: Reset to the original image
# 6. `to_grayscale`: Convert the image to grayscale
# 7. `resize`: Resize the image to specified dimensions
# 8. `rotate`: Rotate the image by a specified angle
# 9. `flip`: Flip the image horizontally, vertically, or both
# 10. `crop`: Crop a region of interest from the image
# 11. `apply_blur`: Apply Gaussian blur to the image
# 12. `detect_edges`: Detect edges in the image using the Canny edge detector


def display_image(image, title="Image"):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class ImageProcossor:

    def __init__(self, filename, image=None):
        self.image = image.copy() if image is not None else None
        self.orignial_image = self.image
        self.file = filename

    def load(self):
        self.image = cv2.imread(self.file)

        if self.image is None:
            raise ValueError(f"The image path {self.file} is not valid")

        self.orignial_image = self.image.copy()

        return self

    def save(self, filepath):
        if filepath is None:
            name, ext = os.path.splitext(os.path.basename(self.file))
            filepath = f"{name}_procssed.{ext}"

        cv2.imwrite(filepath, self.image)

        return self

    def display(self, title=None):
        if title is None:
            title = self.file if self.file else "Image"
        display_image(self.image, title)
        return self

    def reset(self):
        self.image = self.orignial_image.copy()
        return self

    def to_grayscale(self):
        # Only convert if it's a color image (3 channels)
        if len(self.image.shape) == 3:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return self

    def resize(self, width, height, interpolation=cv2.INTER_LINEAR):
        self.image = cv2.resize(
            self.image, (width, height), interpolation=interpolation
        )
        return self

    def rotate(self, angle, center=None, scale=1.0):
        height, width = self.image.shape[:2]
        if center is None:
            center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
        self.image = cv2.warpAffine(self.image, rotation_matrix, (width, height))
        return self

    def flip(self, flip_code):
        self.image = cv2.flip(self.image, flip_code)
        return self

    def crop(self, x, y, width, height):
        self.image = self.image[y : y + height, x : x + width]
        return self

    def apply_blur(self, kernel_size=(5, 5), sigma=0):
        self.image = cv2.GaussianBlur(self.image, kernel_size, sigma)
        return self

    def detect_edges(
        self, threshold1=100, threshold2=200, aperture_size=3, L2gradient=False
    ):
        # Convert to grayscale if needed
        if len(self.image.shape) == 3:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        else:
            gray = self.image
        self.image = cv2.Canny(
            gray,
            threshold1,
            threshold2,
            apertureSize=aperture_size,
            L2gradient=L2gradient,
        )
        return self
