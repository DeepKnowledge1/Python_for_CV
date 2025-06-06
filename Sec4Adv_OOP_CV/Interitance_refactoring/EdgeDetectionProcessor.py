from BasicImageProcessor import BasicImageProcessor
import cv2

import numpy as np


class EdgeDetectionProcessor(BasicImageProcessor):
    """
    Specialized processor for edge detection operations.
    Inherits basic transformations + adds edge detection expertise!
    """

    def detect_edges_canny(self, threshold1=100, threshold2=200, aperture_size=3):
        """Detect edges using Canny detector"""
        if len(self.image.shape) == 3:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        else:
            gray = self.image

        self.image = cv2.Canny(gray, threshold1, threshold2, apertureSize=aperture_size)
        print(
            f"🔍 Canny edge detection applied (thresholds: {threshold1}, {threshold2})"
        )
        return self

    def detect_edges_sobel(self, dx=1, dy=1, ksize=3):
        """Detect edges using Sobel operator"""
        if len(self.image.shape) == 3:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        else:
            gray = self.image

        sobel_x = cv2.Sobel(gray, cv2.CV_64F, dx, 0, ksize=ksize)
        sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, dy, ksize=ksize)
        self.image = np.sqrt(sobel_x**2 + sobel_y**2).astype(np.uint8)
        print(f"📐 Sobel edge detection applied (dx={dx}, dy={dy})")
        return self

    def detect_edges_laplacian(self, ksize=3):
        """Detect edges using Laplacian operator"""
        if len(self.image.shape) == 3:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        else:
            gray = self.image

        self.image = cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)
        self.image = np.absolute(self.image).astype(np.uint8)
        print(f"🌊 Laplacian edge detection applied (kernel size: {ksize})")
        return self
