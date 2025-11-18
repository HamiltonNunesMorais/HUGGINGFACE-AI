---
title: chat-with-liteLlama
emoji: 🦙
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "3.50.2"
app_file: app.py
pinned: false
---

# Chat com HUGGING FACE

Este é um projeto básico de chatbot que utiliza o modelo **LiteLlama-460M-1T** da Hugging Face para gerar respostas a perguntas.

O app foi criado com **Gradio** e pode ser executado localmente ou hospedado gratuitamente no **Hugging Face Spaces**.

---

## Como funciona

- O usuário digita uma pergunta.
- O modelo LiteLlama gera uma resposta baseada na entrada.
- A interface é simples e interativa, feita com Gradio.

---

## Executar localmente

1. Instale as dependências:

```bash
pip install -r requirements.txt

```
2. Execute o app:
```bash
python app.py

```