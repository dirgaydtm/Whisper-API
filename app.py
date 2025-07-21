from flask import Flask, request, jsonify
from faster_whisper import WhisperModel
import os

model_size = "base"
model = WhisperModel(model_size, device="cpu", compute_type="int8")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Faster Whisper API is running"})

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    if "file" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files["file"]
    temp_path = "temp_audio.mp3"
    audio_file.save(temp_path)

    # Transkripsi audio
    segments, info = model.transcribe(temp_path, beam_size=5)
    text = "".join([segment.text for segment in segments])

    os.remove(temp_path)
    return jsonify({
        "language": info.language,
        "text": text
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
