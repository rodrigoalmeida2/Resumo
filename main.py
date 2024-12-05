import os
import streamlit as st
from dotenv import load_dotenv
from Summarization import VideoSummarizer
from Salvar_Resumo import SaveSummaries

# Carrega variáveis de ambiente
load_dotenv()

# Inicializa o estado da aplicação
if 'summaries' not in st.session_state:
    st.session_state['summaries'] = None

if 'pdf_file' not in st.session_state:
    st.session_state['pdf_file'] = None

if 'word_file' not in st.session_state:
    st.session_state['word_file'] = None

# Interface do usuário
st.title("Gerador de Resumo de Vídeos")

# Entrada para URL do vídeo
video_url = st.text_input("Insira o URL do vídeo:")

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

                # Atualiza o estado com os resumos gerados
                st.session_state['summaries'] = summaries

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

                # Atualiza o estado com os nomes dos arquivos
                st.session_state['pdf_file'] = pdf_file
                st.session_state['word_file'] = word_file

            except Exception as e:
                st.error(f"Ocorreu um erro: {str(e)}")
    else:
        st.warning("Por favor, insira uma URL válida.")

# Exibe botões para download dos arquivos, se disponíveis
if st.session_state['pdf_file']:
    with open(st.session_state['pdf_file'], "rb") as pdf:
        st.download_button(
            label="Baixar PDF",
            data=pdf,
            file_name=st.session_state['pdf_file'],
            mime="application/pdf"
        )

if st.session_state['word_file']:
    with open(st.session_state['word_file'], "rb") as docx:
        st.download_button(
            label="Baixar Word",
            data=docx,
            file_name=st.session_state['word_file'],
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

# Limpeza dos arquivos gerados
if st.button("Limpar estado"):
    if st.session_state['pdf_file'] and os.path.exists(st.session_state['pdf_file']):
        os.remove(st.session_state['pdf_file'])
    if st.session_state['word_file'] and os.path.exists(st.session_state['word_file']):
        os.remove(st.session_state['word_file'])

    # Reseta o estado
    st.session_state['summaries'] = None
    st.session_state['pdf_file'] = None
    st.session_state['word_file'] = None

    st.success("Estado limpo com sucesso!")
