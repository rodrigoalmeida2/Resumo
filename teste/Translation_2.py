from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
  
tokenizer = AutoTokenizer.from_pretrained("unicamp-dl/translation-pt-en-t5")

model = AutoModelForSeq2SeqLM.from_pretrained("unicamp-dl/translation-pt-en-t5")

pten_pipeline = pipeline('text2text-generation', model=model, tokenizer=tokenizer)

print(pten_pipeline("translate Portuguese to English: Eu gosto de comer arroz."))
