# Qthread_MiniProject

Dự án nhỏ này sử dụng Yolov8 để nhận diện các xe qua cam hành trình của ô tô

## Thư viện
**PyQt5**
```
pip install PyQt5
```
***opencv-python***
```
pip install opencv-python
```
***ultralytics***
```
pip install ultralytics
```
***numpy***
```
pip install numpy
```

## Cấu trúc
- *main.py*: File chính để khởi chạy ứng dụng.

- *capture_thread.py*: File chứa lớp CaptureThread để đọc frame từ video.

- *process_thread.py*: File chứa lớp ProcessThread để xử lý frame.

- *stream_thread.py*: File chứa lớp StreamThread để hiển thị frame đã xử lý.

## Hướng chạy

- *CaptureThread*: Đọc frame từ video và phát tín hiệu frame_captured khi có frame mới.

- *ProcessThread*: Nhận frame từ CaptureThread, xử lý và phát tín hiệu frame_processed.

- *StreamThread*: Nhận frame đã xử lý từ ProcessThread và hiển thị nó.
  ![image](https://github.com/user-attachments/assets/1b520558-be2b-481a-91a6-8f4f021f4d44)


## Phân tích
Với file *main.py* tạo các signal và slot đã được thiết lập để kết nối giữa các luồng (CaptureThread, ProcessThread, và StreamThread). Đây là cách PyQt5 và QThread hoạt động để giao tiếp giữa các luồng một cách an toàn và hiệu quả.

File *capture_thread.py* sẽ chia video thành các frames. Ở đây để giảm tài nguyên sử dụng và cải thiện năng suất với 60fps ở video gốc, ta chia thành 15fps các frames thừa sẽ được skip.
CaptureThread phát ra signal <ins>frame_captured</ins> khi đọc được frame từ video.

Tiếp đến file *process_thread.py* sử dụng Yolov8 để detect và tracking các xe.
ProcessThread nhận frame thông qua slot process_frame, xử lý frame, và phát ra signal <ins>frame_processed</ins>.

Cuối cùng *stream_thread.py* sẽ nhận kết quả từ *process_thread.py* để hiển thị lên UI.
StreamThread nhận frame đã xử lý thông qua slot display_frame và hiển thị nó.

# Report
https://docs.google.com/document/d/10vtRNH0C2hQlY34z_-Sq-nd98XYPB6SvOJ2noSxmUeI/edit?usp=sharing
