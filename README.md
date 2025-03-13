# AI News Chatbot

## Project Overview
This AI-powered news chatbot is designed to provide a seamless and interactive experience with e-newspaper articles. It allows users to upload an image of a news article, extracts the text from the image, summarizes it, and provides a concise and clear report. Users can also ask questions related to the article, and the chatbot responds with informative, human-like audio answers.

## Features
- **Article Image Upload:** Users can upload images of newspaper articles.
- **Text Extraction:** The chatbot uses Optical Character Recognition (OCR) to extract text from the uploaded image.
- **Text Correction:** Automatically corrects spelling and word errors in the extracted text.
- **Article Summarization:** Generates a short, accurate summary of the article.
- **Interactive Q&A:** Users can ask questions based on the article's content.
- **Human-like Audio Response:** Converts answers into natural-sounding speech for an enhanced user experience.

## Technology Stack
- **Front-end:** HTML, CSS (For a sleek and user-friendly interface)
- **Back-end:** Python (Flask Framework)
- **Libraries:**
  - `pytesseract` for OCR
  - `pyttsx3` for text-to-speech conversion
  - `openai` for language processing and response generation

## Folder Structure
```
|-- e-newspaper-chatbot
    |-- index.html         # Front-end interface
    |-- app.py             # Back-end logic and API
    |-- extracted_text/    # Folder for extracted text files
    |-- summaries/        # Folder for summarized text files
```

## Setup and Installation
1. **Clone the Repository:**
```
git clone https://github.com/your-repository/e-newspaper-chatbot.git
cd e-newspaper-chatbot
```
2. **Set up a Virtual Environment (Optional but recommended):**
```
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```
3. **Install Required Libraries:**
```
pip install flask pytesseract pyttsx3 openai
```
4. **Run the Flask App:**
```
python app.py
```
5. **Access the Chatbot:**
Open your browser and go to `http://127.0.0.1:5000/`

## How to Use
1. **Upload an Article Image:** Click on the "Upload" button after selecting your image.
2. **Get the Summary:** The chatbot will extract and summarize the article.
3. **Ask a Question:** Type a question related to the article and click "Ask".
4. **Receive a Voice Response:** The chatbot will provide an audio response with the answer.

## Troubleshooting
- **ModuleNotFoundError:** Ensure all required libraries are installed.
```
pip install -r requirements.txt
```
- **Article Not Found:** Double-check the image quality and text visibility.
- **Audio Not Playing:** Ensure your device's audio output is enabled.

## Future Enhancements
- Implement multi-language support.
- Add more advanced text summarization models.
- Integrate a more natural text-to-speech engine.

## Contributing
Feel free to raise issues or contribute to the project by submitting pull requests.

## License
This project is licensed under the MIT License.
