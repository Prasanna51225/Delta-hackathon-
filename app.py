import os
import base64
import pyttsx3
from textblob import TextBlob
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Paths to extracted text and summary files
EXTRACTED_TEXT_DIR = r"F:\e-newspaper-chatbot\extracted_text.txt"
SUMMARIZED_TEXT_DIR = r"F:\e-newspaper-chatbot\summarized_text.txt"

# Auto-correct spelling
def correct_text(text):
    blob = TextBlob(text)
    return str(blob.correct())

# Find article by image name
def find_article(image_name):
    text_file = os.path.join(EXTRACTED_TEXT_DIR, f"{image_name}.txt")
    summary_file = os.path.join(SUMMARIZED_TEXT_DIR, f"{image_name}.txt")
    
    if os.path.exists(text_file) and os.path.exists(summary_file):
        with open(text_file, 'r', encoding='utf-8') as f:
            extracted_text = f.read()
        with open(summary_file, 'r', encoding='utf-8') as f:
            summarized_text = f.read()
        return correct_text(extracted_text), summarized_text
    return None, None

# Text-to-speech conversion
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, "output.wav")
    engine.runAndWait()
    with open("output.wav", "rb") as audio_file:
        return base64.b64encode(audio_file.read()).decode("utf-8")

# Upload image and get article summary
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        print("No image in request!")  # Debugging
        return jsonify({'error': 'No file uploaded'}), 400

    image = request.files['image']
    image_name = os.path.splitext(image.filename)[0]
    extracted_text, summary = find_article(image_name)

    if extracted_text and summary:
        response = f"Summary: {summary}"
        audio_base64 = text_to_speech(response)
        return jsonify({'summary': summary, 'audio': audio_base64})

    return jsonify({'error': 'Article not found'}), 404

# Answer questions based on article
@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')
    image_name = data.get('image_name')

    _, summary = find_article(image_name)
    if summary:
        response = f"Based on the article: {summary}"
        audio_base64 = text_to_speech(response)
        return jsonify({'answer': response, 'audio': audio_base64})

    return jsonify({'error': 'Could not find related article'}), 404

if __name__ == '__main__':
    app.run(debug=True)


