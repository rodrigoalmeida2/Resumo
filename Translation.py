from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-pt")
print(pipe(">>por<< Tom tried to stab me."))

# expected output: O Tom tentou esfaquear-me.
