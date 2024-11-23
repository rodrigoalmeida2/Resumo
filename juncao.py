import whisper
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


def transcricao():
    modelo = whisper.load_model("small")
    result = modelo.transcribe("audio.mp3")
    return result["text"]


def PT_to_EN(text):
    tokenizer = AutoTokenizer.from_pretrained("unicamp-dl/translation-pt-en-t5")

    model = AutoModelForSeq2SeqLM.from_pretrained("unicamp-dl/translation-pt-en-t5")

    pten_pipeline = pipeline('text2text-generation', model=model, tokenizer=tokenizer)

    print(pten_pipeline(f"translate Portuguese to English: {text}"))


def Summa(pt_to_en):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    ARTICLE = pt_to_en

    print(summarizer(ARTICLE, max_length=200, min_length=50, do_sample=False))


def EN_to_PT(resumo):
    pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-pt")
    print(pipe(f">>por<< {resumo}"))


def main():
    trans = transcricao()
    print(trans)
    #PT_to_EN(trans)

main()