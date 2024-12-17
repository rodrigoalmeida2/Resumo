# YouTube Video Summarizer and Translator

This project is a Python-based application that generates summaries of YouTube videos and translates them into other languages if needed, using Hugging Face as its main source of pretrained models. The summarized and translated text can be downloaded as PDF, WORD or TXT files through an Streamlit interface.

## Features

- **Download YouTube Video Audio**: Extract audio from YouTube videos.
- **Audio Transcription**: Convert audio to text using the Whisper model.
- **Summarization**: Generate concise summaries using a Hugging Face summarization pipeline.
- **Translation**: Translate the summaries into different languages using a Hugging Face translation pipeline.
- **File Export**: Save summaries and translations as PDF, WORD or TXT files.
- **Streamlit Interface**: A simple web-based UI for inputting video URLs and downloading output files.

## Requirements

- Python 3.8+
- Required Python libraries (install via `requirements.txt`):
  - `streamlit`
  - `transformers`
  - `yt-dlp`
  - `whisper`
  - `python-docx`
  - `fpdf`
  - `python-dotenv`

## FFmpeg
- Yout gotta have FFmpeg already installed in your machine
- FFmpeg is the leading multimedia framework, able to decode, encode, transcode, mux, demux, stream, filter and play pretty much anything that humans and machines have created.
- Go to https://www.ffmpeg.org/

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rodrigoalmeida2/Resumo.git
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

## Usage

1. Run the Streamlit application using the setup instructions.
2. Enter the URL of a YouTube video in the provided input field.
3. Click the "Process" button to generate the summary.
4. Download the summary and translation as files using the respective buttons.

## Models Used

1. **Whisper**: For audio transcription.
2. **facebook/bart-large-cnn**: For summarization.
3. **Helsinki-NLP/opus-mt-tc-big-en-pt**: For translation (English to Portuguese).

## Contributing

Feel free to open issues or submit pull requests to contribute to this project.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for audio transcription.
- [Hugging Face Transformers](https://huggingface.co/transformers/) for summarization and translation pipelines.
- [Streamlit](https://streamlit.io/) for creating the user interface.

