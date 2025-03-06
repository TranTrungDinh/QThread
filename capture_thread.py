from PyQt5.QtCore import QThread, pyqtSignal
import cv2

class CaptureThread(QThread):
    frame_captured = pyqtSignal(object)

    def __init__(self, video_path, target_fps=15):
        super().__init__()
        self.video_path = video_path
        self.target_fps = target_fps
        self.frame_skip = 0

    def run(self):
        cap = cv2.VideoCapture(self.video_path)
        original_fps = cap.get(cv2.CAP_PROP_FPS)
        self.frame_skip = int(original_fps / self.target_fps)

        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Chỉ đọc một khung hình mỗi frame_skip khung hình
            if frame_count % self.frame_skip == 0:
                self.frame_captured.emit(frame)

            frame_count += 1

        cap.release()