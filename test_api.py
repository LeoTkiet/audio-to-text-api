import requests
import json
import os

def test_speech_to_text_api():
    url = "http://127.0.0.1:8000/transcribe"
    
    # change this name to path of the audio file name you have
    audio_file_path = r"audio.mp3"
    
    if not os.path.exists(audio_file_path):
        print(f"Error: File '{audio_file_path}' not found. Please upload an audio file and rename it to match.")
        return

    print(f"Đang gửi request POST tới: {url}")
    print(f"File upload: {audio_file_path}")
    print("Đang đợi AI xử lý...\n")
    
    try:
        # send request as multipart/form-data
        with open(audio_file_path, "rb") as f:
            files = {"file": (audio_file_path, f, "audio/wav")}
            response = requests.post(url, files=files)
        
        if response.status_code == 200:
            print("Thành công! Phản hồi từ API:")
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        else:
            print(f"Thất bại với Mã lỗi: {response.status_code}")
            print(f"Tin nhắn lỗi: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("\nLỗi kết nối: Không thể kết nối với API.")
        print("Hãy đảm bảo bạn đã bật server FastAPI (vd: uvicorn main:app --reload)!")

if __name__ == "__main__":
    test_speech_to_text_api()