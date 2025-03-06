from PyQt5.QtCore import QThread, pyqtSignal
import cv2
import numpy as np
from ultralytics import YOLO  # Nếu sử dụng YOLOv8

class ProcessThread(QThread):
    frame_processed = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        # Tải mô hình YOLO
        self.model = YOLO("yolov8n.pt")  # Sử dụng YOLOv8n, bạn có thể thay đổi thành mô hình khác

    def process_frame(self, frame):
        # Sử dụng YOLO để detect và tracking ô tô
        results = self.model.track(frame, persist=True, classes=[2, 5, 7])  # classes 2: car, 5: bus, 7: truck

        # Vẽ bounding box và ID tracking lên frame
        annotated_frame = results[0].plot()

        # Phát tín hiệu với frame đã được xử lý
        self.frame_processed.emit(annotated_frame)

    def run(self):
        pass  # Luồng này sẽ được kích hoạt bởi signal từ CaptureThread