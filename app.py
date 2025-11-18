from transformers import pipeline
import gradio as gr

generator = pipeline("text-generation", model="ahxt/LiteLlama-460M-1T")

def responder(pergunta):
    resposta = generator(pergunta, max_length=100, do_sample=True, temperature=0.7)[0]["generated_text"]
    return resposta

gr.Interface(
    fn=responder,
    inputs=gr.Textbox(label="Digite sua pergunta sobre comida: "),
    outputs="text",
    title="Chat com LiteLlama",
    description="Faça perguntas receba respostas geradas pelo modelo LiteLlama-460M-1T."
).launch()
