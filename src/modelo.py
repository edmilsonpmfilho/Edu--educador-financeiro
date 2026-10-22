import requests

# ============ CONFIGURAÇÃO DA API OLLAMA ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o Edu, um educador financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funcionam;
- JAMAIS responda a perguntas fora do tema ensino de finanças pessoais. 
  Quando ocorrer, responda lembrando o seu papel de educador financeiro;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 3 parágrafos.
"""

def perguntar(msg, contexto):
    """Envia a pergunta do usuário para o Ollama com o prompt de sistema e contexto."""
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    payload = {
        "model": MODELO, 
        "prompt": prompt, 
        "stream": False
    }
    
    try:
        r = requests.post(OLLAMA_URL, json=payload)
        r.raise_for_status()
        return r.json()['response']
    except requests.exceptions.RequestException as e:
        return f"Erro ao conectar com o assistente financeiro: {e}"
