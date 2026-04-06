# Speech-to-Text API Project (Nhận diện giọng nói)

Đây là một API đơn giản sử dụng **FastAPI** và mô hình **openai/whisper-base** từ Hugging Face để nhận diện giọng nói và chuyển đổi file âm thanh thành văn bản.

## Mục tiêu
Cung cấp dịch vụ cho phép người dùng upload file âm thanh (`.wav`, `.mp3`...) và trả về đoạn văn bản (text) được nói trong file đó.

## Cài đặt

### 1. Yêu cầu hệ thống
- Python 3.8 trở lên.
- Có thể bạn sẽ cần cài đặt phần mềm `ffmpeg` trên hệ điều hành (Windows/Mac/Linux) nếu muốn xử lý các định dạng phức tạp như `.mp3`. Tuy nhiên với file `.wav` thì các thư viện Python có thể tự xử lý được.

### 2. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

## Cách chạy ứng dụng
### 1. Khởi chạy API Server
```bash
uvicorn main:app --reload
```
Server sẽ chạy tại http://127.0.0.1:8000. Lần chạy đầu tiên sẽ tốn vài phút để tải mô hình AI.

### 2. Thử nghiệm trên Swagger UI
Bạn có thể truy cập: http://127.0.0.1:8000/docs
Tại đây, FastAPI sẽ cung cấp giao diện cho phép bạn click để upload trực tiếp một file âm thanh từ máy tính và xem kết quả.

### 3. Kiểm tra bằng Python
Chuẩn bị một file tên sample.wav trong thư mục gốc. Hoặc thay đổi tên file trong test_api.py. Sau đó chạy:

```bash
python test_api.py
```
---

### Một vài lưu ý nhỏ cho bạn:
* Lần chạy đầu tiên, terminal sẽ khựng lại một lúc để tải mô hình Whisper.
* Nếu máy bạn xử lý audio chậm, mô hình `openai/whisper-tiny` sẽ nhanh hơn (nhưng nhận diện kém chính xác hơn một chút). Nếu máy bạn mạnh, bạn có thể đổi thành `openai/whisper-small`.

https://github.com/user-attachments/assets/694a0413-53a6-4203-903d-335ee0c39a4c

