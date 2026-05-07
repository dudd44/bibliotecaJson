# Arquivo principal do sistema
from models.livro import Livro
from services.biblioteca_services import carregar_Livro, salvar_Livros

livros = carregar_Livro()

print("===================================")
print("=======SISTEMA DE BIBLIOTECA=======")
print("===================================")

print("Categoria padrão:", Livro.categoria_padrao())

while True:
    print("\nMENU:")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Alterar livros")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

# cadastrar livro

    if opcao == "1":
        print("\nCadastro de Livro")

        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = input("Ano: ")

        livro = Livro(titulo, autor, ano)
        livros.append(livro)
        salvar_Livros(livros)
        print("Livro cadastrado com sucesso!")


    elif opcao == "2":

        print("\nLista de Livros")
        if len(livros) == 0:
            print("Nenhum livro cadastrado!")
        else:
            for i , livro in enumerate(livros):
                print("\nLivro", i)
                livro.exibir()


    elif opcao == "3":
        for i, Livro in enumerate(livros):
            print(i , ' - ', livro.titulo)
            pos = int(input("Digite o número do livro: "))
            novo = input("Digite o novo título: ")
            livros[pos].titulo = novo
            salvar_Livros(livros)

    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")
