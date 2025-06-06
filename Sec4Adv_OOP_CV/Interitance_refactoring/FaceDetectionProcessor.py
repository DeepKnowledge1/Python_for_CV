from BasicImageProcessor import BasicImageProcessor


class FaceDetectionProcessor(
    BasicImageProcessor,
):
    def __init__(self, filename=None, image=None):
        super().__init__(filename, image)

    def detect_faces(self):
        pass
