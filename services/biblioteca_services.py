# Este arquivo contem funções responsáveis por salvar e carregar livros do JSON
import json
from models.livro import Livro


def carregar_Livro():
    livros = []
    try:
        with open("Livros.json", "r") as arquivos:
            dados = json.load(arquivos)
            livro = Livro(
                item["titulo"],
                item["autor"],
                item["ano"]
            )
            livros.append(livro)
    except:
        pass
    return livros

# Salvar livros


def salvar_Livros(lista_livros):
    dados = []

    for livro in lista_livros:
        dados.append(livro.to_dict())
    with open("livros.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
