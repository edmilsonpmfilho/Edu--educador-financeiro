# Passo a Passo de Execução

## Setup do Ollama

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull gpt-oss

# 3. Testar se funciona
ollama run gpt-oss "Olá!"
```

## Código Completo

Todo o código-fonte está no arquivo `app.py`.

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 3. Rodar o app, dentro da pasta src
python -m streamlit run app.py
```

## Evidência de Execução


<img width="1920" height="1107" alt="image" src="docs\imagens\01.png"/>
<img width="1920" height="1107" alt="image" src="docs\imagens\02.png" />
