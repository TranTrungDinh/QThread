from PyQt5.QtCore import QThread, pyqtSignal
import cv2

class StreamThread(QThread):
    def __init__(self):
        super().__init__()

    def display_frame(self, frame):
        cv2.imshow('Processed Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.quit()

    def run(self):
        pass  # Luồng này sẽ được kích hoạt bởi signal từ ProcessThread