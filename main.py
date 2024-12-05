import os
import streamlit as st
from dotenv import load_dotenv
from Summarization import VideoSummarizer
from Salvar_Resumo import SaveSummaries

# Carrega variáveis de ambiente
load_dotenv()

# Configura o título da página
st.set_page_config(page_title="YouTube Video Summarizer", layout="centered")

# Interface do Streamlit
st.title("YouTube Video Summarizer")
st.write("Insira a URL de um vídeo do YouTube para transcrever e gerar resumos.")

# Entrada para URL do vídeo
video_url = st.text_input("URL do vídeo:", "")


# Botão para processar o vídeo
if st.button("Processar"):
    if video_url.strip():
        # Token da API Hugging Face
        token = os.getenv('ACCESS_TOKEN')
        
        # Inicializa o summarizer
        summarizer = VideoSummarizer(token)
        
        with st.spinner("Processando o vídeo, por favor aguarde..."):
            try:
                # Processa o vídeo
                summaries = summarizer.process_video(video_url)
                
                # Mostra os resumos na interface
                st.success("Resumo gerado com sucesso!")
                st.write("### Resumos:")
                for idx, summary in enumerate(summaries, start=1):
                    st.write(f"{summary}")
                
                # Salva os resumos em arquivos
                pdf_file = "resumo_video.pdf"
                word_file = "resumo_video.docx"
                SaveSummaries.save_to_pdf(summaries, pdf_file)
                SaveSummaries.save_to_word(summaries, word_file)

                # Botões para baixar os arquivos
                with open(pdf_file, "rb") as pdf:
                    st.download_button(
                        label="Baixar PDF",
                        data=pdf,
                        file_name=pdf_file,
                        mime="application/pdf"
                    )
                
                with open(word_file, "rb") as docx:
                    st.download_button(
                    label="Baixar Word",
                    data=docx,
                    file_name=word_file,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
                
            except Exception as e:
                st.error(f"Ocorreu um erro: {str(e)}")
    else:
        st.warning("Por favor, insira uma URL válida.")
    os.remove("resumo_video.docx")
    os.remove("resumo_video.pdf")




#botao()
#seg("resumo_video.pdf")
#ter("resumo_video.docx") 