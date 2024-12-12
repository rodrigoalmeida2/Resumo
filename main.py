import os
import streamlit as st
from dotenv import load_dotenv
from Summarization import VideoSummarizer
from Salvar_Resumo import SaveSummaries
from translation import Translator  # Supondo que você tenha um módulo para tradução

# Carrega variáveis de ambiente
load_dotenv()

# Inicializa o estado da aplicação
if 'summaries' not in st.session_state:
    st.session_state['summaries'] = None

if 'output_format' not in st.session_state:
    st.session_state['output_format'] = "PDF"

if 'translate' not in st.session_state:
    st.session_state['translate'] = False

if 'output_file' not in st.session_state:
    st.session_state['output_file'] = None

# Interface do usuário
st.title("Gerador de Resumo de Vídeos")

# Entrada para URL do vídeo
video_url = st.text_input("Insira o URL do vídeo:")

# Opção para escolher o formato de saída
st.session_state['output_format'] = st.radio(
    "Selecione o formato de saída:",
    options=["PDF", "DOCX", "TXT"],
    index=0
)

# Opção para traduzir o resumo para português
st.session_state['translate'] = st.checkbox("Traduzir resumo para português")

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

                # Tradução opcional
                if st.session_state['translate']:
                    # Inicializa a classe Translator
                    translator = Translator()
                    summaries = translator.translate(summaries, target_language="por")

                # Atualiza o estado com os resumos gerados
                st.session_state['summaries'] = summaries

                # Mostra os resumos na interface
                st.success("Resumo gerado com sucesso!")
                st.write("### Resumos:")
                for idx, summary in enumerate(summaries, start=1):
                    st.write(f"{idx}. {summary}")

                # Salva os resumos no formato escolhido
                output_file = f"resumo_video.{st.session_state['output_format'].lower()}"
                if st.session_state['output_format'] == "PDF":
                    SaveSummaries.save_to_pdf(summaries, output_file)
                elif st.session_state['output_format'] == "DOCX":
                    SaveSummaries.save_to_word(summaries, output_file)
                else:
                    SaveSummaries.save_to_txt(summaries, output_file)

                # Atualiza o estado com o nome do arquivo
                st.session_state['output_file'] = output_file

            except Exception as e:
                st.error(f"Ocorreu um erro: {str(e)}")
    else:
        st.warning("Por favor, insira uma URL válida.")

# Exibe botão para download do arquivo, se disponível
if st.session_state['output_file']:
    with open(st.session_state['output_file'], "rb") as file:
        st.download_button(
            label=f"Baixar {st.session_state['output_format']}",
            data=file,
            file_name=st.session_state['output_file'],
            mime="application/pdf" if st.session_state['output_format'] == "PDF" else "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

# Limpeza dos arquivos gerados
#if st.button("Limpar estado"):
if st.session_state['output_file'] and os.path.exists(st.session_state['output_file']):
    os.remove(st.session_state['output_file'])

# Reseta o estado
st.session_state['summaries'] = None
st.session_state['output_file'] = None
