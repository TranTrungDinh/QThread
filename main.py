import sys
from PyQt5.QtWidgets import QApplication
from capture_thread import CaptureThread
from process_thread import ProcessThread
from stream_thread import StreamThread

class MainApp:
    def __init__(self):
        self.capture_thread = CaptureThread("D:\\Downloads\\VideoCarTest1.mp4")
        self.process_thread = ProcessThread()
        self.stream_thread = StreamThread()

        # Kết nối các luồng
        self.capture_thread.frame_captured.connect(self.process_thread.process_frame)
        self.process_thread.frame_processed.connect(self.stream_thread.display_frame)

        # Bắt đầu các luồng
        self.capture_thread.start()
        self.process_thread.start()
        self.stream_thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())