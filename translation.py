from transformers import pipeline

class Translator:
    # Inicializa o pipeline de tradução com o modelo especificado.
    def __init__(self, model_name="Helsinki-NLP/opus-mt-tc-big-en-pt"):
        self.translation_pipeline = pipeline("translation", model=model_name)
    #Traduz uma lista de textos para o idioma especificado.
    def translate(self, text_list, target_language="por"):
        translations = []
        for text in text_list:
            translated_text = self.translation_pipeline(f">>{target_language}<< {text}")
            translations.append(translated_text[0]['translation_text'])
        return translations

# Exemplo de uso
if __name__ == "__main__":
    # Resumos gerados previamente
    summaries = [
        "Tom tried to stab me.",
        "The weather is great today.",
        "Machine learning is fascinating."
    ]

    # Inicializa a classe Translator
    translator = Translator()

    # Traduz os resumos
    translated_summaries = translator.translate(summaries, target_language="por")

    # Exibe os resultados
    print("Resumos Originais:")
    for summary in summaries:
        print(f" - {summary}")

    print("\nResumos Traduzidos:")
    for translated in translated_summaries:
        print(f" - {translated}")
