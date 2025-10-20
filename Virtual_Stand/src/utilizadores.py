from io_terminal import imprime_lista

nome_ficheiro_lista_de_utilizadores = "lista_de_utilizadores.pk"

def cria_novo_utilizador():
    """ pede os dados de um novo utilizador

    :return: dicionario com o novo utilizador, {"nome": <<nome>>, "email": <<email>>}
    """
    nome = input("Nome:")
    nif = input("Nif:")
    telemovel = input("Telemovel:")
    email = input("Email:")

    return {"Nome: ": nome, "NIF: ": nif, "Email: ": email, "Telemóvel: ": telemovel}

    # todo
    pass


def imprime_lista_de_utilizadores(lista_de_utilizadores):
    """ ..."""

    imprime_lista(cabecalho="Lista de Utilizadores", lista=lista_de_utilizadores)
