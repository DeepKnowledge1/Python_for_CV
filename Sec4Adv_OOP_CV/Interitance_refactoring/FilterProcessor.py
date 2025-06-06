from BasicImageProcessor import BasicImageProcessor
import cv2
import numpy as np


class FilterProcessor(BasicImageProcessor):
    """
    Specialized processor for image filtering operations.
    Inherits basic transformations + adds filtering superpowers!
    """

    def __init__(self, filename=None, image=None):
        super().__init__(filename, image)

    def apply_blur(self, kernel_size=(5, 5), sigma=0):
        """Apply Gaussian blur"""
        self.image = cv2.GaussianBlur(self.image, kernel_size, sigma)
        print(f"🌫️ Applied Gaussian blur with kernel {kernel_size}")
        return self

    def apply_median_blur(self, kernel_size=5):
        """Apply median blur (great for noise reduction)"""
        self.image = cv2.medianBlur(self.image, kernel_size)
        print(f"🎯 Applied median blur with kernel {kernel_size}")
        return self

    def apply_bilateral_filter(self, d=9, sigma_color=75, sigma_space=75):
        """Apply bilateral filter (preserves edges while reducing noise)"""
        self.image = cv2.bilateralFilter(self.image, d, sigma_color, sigma_space)
        print("✨ Applied bilateral filter (edge-preserving)")
        return self

    def sharpen(self):
        """Sharpen the image"""
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        self.image = cv2.filter2D(self.image, -1, kernel)
        print("🔪 Image sharpened")
        return self
