import cv2
import os


def display_image(image, title="Image"):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class BaseImageProcessor:
    """
    The foundation of our image processing family!
    Handles core functionality that EVERYONE needs.
    """

    def __init__(self, filename=None, image=None):
        self.image = image.copy() if image is not None else None
        self.original_image = self.image
        self.filename = filename
        print(f"🖼️ Base processor created for {filename}")

    def load(self):
        """Load image from file"""
        self.image = cv2.imread(self.filename)
        if self.image is None:
            raise ValueError(f"Cannot load image from {self.filename}")

        self.original_image = self.image.copy()
        print(f"✅ Image loaded: {self.filename}")
        return self

    def save(self, filepath=None):
        """Save current image"""
        if filepath is None:
            name, ext = os.path.splitext(os.path.basename(self.filename))
            filepath = f"{name}_processed{ext}"

        cv2.imwrite(filepath, self.image)
        print(f"💾 Image saved: {filepath}")
        return self

    def display(self, title=None):
        """Display current image"""
        if title is None:
            title = self.filename if self.filename else "Image"
        display_image(self.image, title)
        return self

    def reset(self):
        """Reset to original image"""
        if self.original_image is not None:
            self.image = self.original_image.copy()
            print("🔄 Image reset to original")
        return self
