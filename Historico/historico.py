from datetime import datetime
from cadastro import consultar_ponto, consultar_linha
import json

__all__ = [
    "registrar_modificacao",
    "salvar_dados",
]

listaTipos = ["criação", "alteração", "deleção"]

historico_pontos = []

historico_linhas = []

def carregar_dados():
    global historico_pontos
    global historico_linhas
    try:
        with open("historico.json", "r") as file:
            data = json.load(file)
            historico_pontos = data.get("pontos", [])
            historico_linhas = data.get("linhas", [])
    except:
        historico_pontos = []
        historico_linhas = []

def salvar_dados():
    global historico_pontos
    global historico_linhas
    with open("historico.json", "w") as file:
        json.dump({"pontos": historico_pontos, "linhas": historico_linhas}, file, indent=4)

def registrar_modificacao(tipo_modificacao, objeto_alterado, id_objeto):
    if tipo_modificacao not in [0,1,2]:
        return  "Erro: Tipo de modificação inválido.", 3
    
    if objeto_alterado == "ponto":
        msg, codigo = consultar_ponto(id_objeto)

        if codigo == 1:
            historico_pontos.append({'tipo' : tipo_modificacao, "objeto" : objeto_alterado, 'id' : id_objeto, "data": datetime.now().strftime("%Y-%m-%d %H:%M")})
            return "Modificação registrada com sucesso!", 1
        else:
            return msg, codigo
    elif objeto_alterado == "linha":
        msg, codigo = consultar_linha(id_objeto)

        if codigo == 1:
            historico_linhas.append({'tipo' : tipo_modificacao, "objeto" : objeto_alterado, 'id' : id_objeto, "data": datetime.now().strftime("%Y-%m-%d %H:%M")})
            return "Modificação registrada com sucesso!", 1
        else:
            return msg, 2
    else:
        return "Erro: Tipo de objeto inválido.", 4
    
def consultar_historico_ponto(id_ponto):
    resultado = []

    for item in historico_pontos:
        if item.get("id") == id_ponto:
            resultado.append(item) 
    if resultado == []:
        return "Ponto não encontrado no histórico", 2
    else:
        return resultado, 1
    
def consultar_historico_linha(id_linha):
    resultado = []

    for item in historico_linhas:
        if item.get("id") == id_linha:
            resultado.append(item) 
    if resultado == []:
        return "Linha não encontrada no histórico", 2
    else:
        return resultado, 1

carregar_dados()