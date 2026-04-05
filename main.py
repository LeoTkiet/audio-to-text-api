from fastapi import FastAPI, HTTPException, UploadFile, File
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
import torch
import librosa
import io

app = FastAPI()

# global variables for AI
processor = None
model = None

@app.on_event("startup")
async def load_model():
    global processor, model
    try:
        print("Đang tải Processor và Model... (Có thể mất vài phút)")
        # using openai whisper base model
        model_name = "openai/whisper-base"
        
        processor = AutoProcessor.from_pretrained(model_name)
        model = AutoModelForSpeechSeq2Seq.from_pretrained(model_name)
        
        print("Tải model thành công!")
    except Exception as e:
        print(f"Lỗi nghiêm trọng khi khởi động: {e}")

@app.get("/")
async def root():
    return {
        "message": "Speech-to-Text API is ready",
        "model": "openai/whisper-base"
    }

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    if model is None or processor is None:
        raise HTTPException(status_code=503, detail="Model đang tải. Vui lòng thử lại sau.")

    # check file type
    if not file.filename.endswith(('.wav', '.mp3', '.m4a', '.flac')):
        raise HTTPException(status_code=400, detail="Chỉ hỗ trợ file âm thanh (.wav, .mp3, .m4a, .flac)")

    try:
        # read bytes from file
        audio_bytes = await file.read()
        
        # load audio to numpy array with 16kHz sampling rate (standard of Whisper)
        audio_array, sampling_rate = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        
        # process audio and put it into Tensor
        inputs = processor(audio_array, sampling_rate=16000, return_tensors="pt")
        
        # AI generate result (ID of text tokens)
        with torch.no_grad():
            predicted_ids = model.generate(inputs.input_features)
        
        # decode token IDs to readable text
        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
        
        return {
            "filename": file.filename,
            "transcription": transcription.strip()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi trong quá trình nhận diện: {str(e)}")