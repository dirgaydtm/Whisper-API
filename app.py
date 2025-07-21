from flask import Flask, request, jsonify
import whisper
import os

model = whisper.load_model("base")

app = Flask(__name__)

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    if "file" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files["file"]
    temp_path = "temp_audio.mp3"
    audio_file.save(temp_path)

    result = model.transcribe(temp_path)
    os.remove(temp_path)

    return jsonify({"text": result["text"]})

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Whisper API is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
