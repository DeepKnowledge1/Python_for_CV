from FilterProcessor import FilterProcessor
from EdgeDetectionProcessor import EdgeDetectionProcessor
import cv2


class AdvancedProcessor(FilterProcessor, EdgeDetectionProcessor):
    """
    The SUPERHERO processor that combines ALL capabilities!
    Uses multiple inheritance to get powers from BOTH parents!
    """

    def enhance_contrast(self, alpha=1.5, beta=0):
        """Enhance image contrast"""
        self.image = cv2.convertScaleAbs(self.image, alpha=alpha, beta=beta)
        print(f"🌟 Contrast enhanced (alpha={alpha}, beta={beta})")
        return self

    def histogram_equalization(self):
        """Apply histogram equalization for better contrast"""
        if len(self.image.shape) == 3:
            yuv = cv2.cvtColor(self.image, cv2.COLOR_BGR2YUV)
            yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
            self.image = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
        else:
            self.image = cv2.equalizeHist(self.image)
        print("📊 Histogram equalization applied")
        return self

    def adaptive_threshold(
        self,
        max_value=255,
        adaptive_method=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        threshold_type=cv2.THRESH_BINARY,
        block_size=11,
        C=2,
    ):
        """Apply adaptive thresholding"""
        if len(self.image.shape) == 3:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        else:
            gray = self.image

        self.image = cv2.adaptiveThreshold(
            gray, max_value, adaptive_method, threshold_type, block_size, C
        )
        print("🎯 Adaptive thresholding applied")
        return self
