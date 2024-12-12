# YouTube Video Summarizer and Translator

This project is a Python-based application that generates summaries of YouTube videos and translates them into multiple languages. The summarized and translated text can be downloaded as PDF and Word files through a user-friendly Streamlit interface.

## Features

- **Download YouTube Video Audio**: Extract audio from YouTube videos.
- **Audio Transcription**: Convert audio to text using the Whisper model.
- **Summarization**: Generate concise summaries using a Hugging Face summarization pipeline.
- **Translation**: Translate the summaries into different languages using a Hugging Face translation pipeline.
- **File Export**: Save summaries and translations as PDF and Word files.
- **Streamlit Interface**: A simple web-based UI for inputting video URLs and downloading output files.

## Requirements

- Python 3.8+
- Required Python libraries (install via `requirements.txt`):
  - `streamlit`
  - `transformers`
  - `yt-dlp`
  - `whisper`
  - `python-docx`
  - `reportlab`
  - `python-dotenv`

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the root directory with the following content:
   ```env
   ACCESS_TOKEN=your_hugging_face_api_token
   ```

4. **Run the Application**:
   ```bash
   streamlit run main.py
   ```

## Project Structure

```
.
├── main.py                # Main Streamlit interface script
├── video_summarizer.py    # Handles downloading, transcribing, and summarizing
├── save_summaries.py      # Handles exporting summaries as PDF and Word files
├── translator.py          # Handles translation of summaries
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
└── README.md              # Project documentation
```

## Usage

1. Run the Streamlit application using the setup instructions.
2. Enter the URL of a YouTube video in the provided input field.
3. Click the "Process" button to generate the summary.
4. Download the summary and translation as PDF or Word files using the respective buttons.

## Examples

### Generated Summary
Original Summary:
```
Machine learning is fascinating and widely applied across industries.
```

### Translated Summary (Portuguese):
```
O aprendizado de máquina é fascinante e amplamente aplicado em diversas indústrias.
```

## Models Used

1. **Whisper**: For audio transcription.
2. **facebook/bart-large-cnn**: For summarization.
3. **Helsinki-NLP/opus-mt-tc-big-en-pt**: For translation (English to Portuguese).

## Contributing

Feel free to open issues or submit pull requests to contribute to this project. Make sure to follow the standard coding guidelines and document your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for audio transcription.
- [Hugging Face Transformers](https://huggingface.co/transformers/) for summarization and translation pipelines.
- [Streamlit](https://streamlit.io/) for creating the user interface.

