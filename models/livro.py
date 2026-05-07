# Classe livro
# Esta classe representa um livro dentro do sistema

class Livro:
    def __init__(self, titulo, autor, ano):
        # atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano

# Propriedade (GETTER)
# Permite acessar o título mesmo sendo privado
    @property
    def titulo(self):
        return self.__titulo


# SETTER
# Permite alterar o titulo com validação

    @titulo.setter
    def titulo(self, novo_titulo):
        if len(novo_titulo) < 2:
            print("Título inválido!")
        else:
            self.__titulo = novo_titulo

# Método para mostrar dados

    def exibir(self):
        self.__log()
        print("Título:", self.__titulo)
        print("Autor:", self.__autor)
        print("Ano:", self.__ano)

# Método privado
    def __log(self):
        print("(LOG) Livro Acessado")

# Converter para dicionnario
# necessario para salvar em json

    def to_dict(self):
        return {
            "titulo": self.__titulo,
            "autor": self.__autor,
            "ano": self.__ano
        }

# Metodo estatico
    @staticmethod
    def categoria_padrao():
        return "Literatura"
