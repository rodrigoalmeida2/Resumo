import whisper
modelo = whisper.load_model("small")
result = modelo.transcribe("audio.mp3")
print(result["text"])