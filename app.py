from transformers import pipeline
import gradio as gr

# Cria o pipeline de sumarização
pipe = pipeline("summarization", model="facebook/bart-large-cnn")

# Função que será chamada pela interface
def resumir_texto(texto):
    resultado = pipe(texto, max_length=130, min_length=30, do_sample=False)
    return resultado[0]['summary_text']

# Interface Gradio
gr.Interface(
    fn=resumir_texto,
    inputs=gr.Textbox(lines=10, label="Digite o texto para resumir"),
    outputs=gr.Textbox(label="Resumo gerado"),
    title="Resumo de Texto com BART",
    description="Insira um texto e receba um resumo gerado pelo modelo BART da Hugging Face.",
    theme="default"
).launch()
