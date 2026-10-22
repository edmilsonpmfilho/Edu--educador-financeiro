import json
import pandas as pd

def carregar_dados():
    """Carrega todos os arquivos de dados do cliente e produtos."""
    perfil = json.load(open('../data/perfil_investidor.json'))
    transacoes = pd.read_csv('../data/transacoes.csv')
    historico = pd.read_csv('../data/historico_atendimento.csv')
    produtos = json.load(open('../data/produtos_financeiros.json'))
    
    return perfil, transacoes, historico, produtos

def montar_contexto(perfil, transacoes, historico, produtos):
    """Gera a string de contexto formatada com os dados carregados."""
    contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""
    return contexto
