from BaseImageProcessor import BaseImageProcessor
import cv2


class BasicImageProcessor(BaseImageProcessor):
    """
    Handles basic image transformations like resize, rotate, flip, crop.
    Inherits core functionality from BaseImageProcessor.
    """

    def __init__(self, filename=None, image=None):
        super().__init__(filename, image)

    def to_grayscale(self):
        """Convert to grayscale"""
        if len(self.image.shape) == 3:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return self

    def resize(self, width, height, interpolation=cv2.INTER_LINEAR):
        """Resize image"""
        self.image = cv2.resize(
            self.image, (width, height), interpolation=interpolation
        )
        return self

    def rotate(self, angle, center=None, scale=1.0):
        """Rotate image"""
        height, width = self.image.shape[:2]
        if center is None:
            center = (width // 2, height // 2)

        rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
        self.image = cv2.warpAffine(self.image, rotation_matrix, (width, height))
        return self

    def flip(self, flip_code):
        """Flip image (0=vertical, 1=horizontal, -1=both)"""
        self.image = cv2.flip(self.image, flip_code)
        return self

    def crop(self, x, y, width, height):
        """Crop image region"""
        self.image = self.image[y : y + height, x : x + width]
        return self
