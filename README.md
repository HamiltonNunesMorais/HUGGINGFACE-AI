---
title: chat-with-AI
emoji: 🦙
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "3.50.2"
app_file: app.py
pinned: false
---
# Resumo de Texto com BART - Hugging Face + Gradio

Este projeto é uma aplicação simples de **resumo automático de texto** usando o modelo [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn) da Hugging Face, com interface interativa criada com **Gradio**.

## Funcionalidades

- Interface web para inserir qualquer texto.
- Geração de resumo automático com o modelo BART.
- Publicação fácil no Hugging Face Spaces.

![alt text](test.gif)

## Deploy no Hugging Face Spaces
- Crie um novo Space em huggingface.co/spaces.
- Escolha o tipo Gradio.
- Faça upload dos arquivos app.py, requirements.txt e README.md
- o arquivo `README.md` deve conter **apenas os metadados** no formato YAML entre `---`. Esses metadados são usados pelo Hugging Face para configurar o Space. Não inclua instruções, textos explicativos ou exemplos fora desse bloco, pode haver conflitos.

Exemplo de `README.md` válido para Spaces:

```markdown
---
title: chat-with-AI
emoji: 🦙
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "3.50.2"
app_file: app.py
pinned: false
---
```
## Acesse o projeto online

Você pode testar a aplicação diretamente no Hugging Face Spaces:

[Clique aqui para acessar o Space](https://huggingface.co/spaces/HNDMORA/chat-with-AI)


## Executar localmente

1. Clone o repositorio.

2. Instale as dependências:

```bash
pip install -r requirements.txt

```
3. Execute o app:
```bash
python app.py

```
