import pickle


def le_de_ficheiro(nome_ficheiro):
    """ le os dados de um ficheiro

    :param nome_ficheiro: nome do ficheiro onde estao os dados
    :return: o que leu do ficheiro (depende dos dados guardados)
    """

    with open(nome_ficheiro, "rb") as f:
        return pickle.load(f)


def guarda_em_ficheiro(nome_do_ficheiro, dados):
    """ guarda os dados recebidos num ficheiro

    :param nome_do_ficheiro: nome do ficheiro onde vai guardar os dados
    :param dados: dados a serem guardados
    """

    with open(nome_do_ficheiro, "wb") as f:
        pickle.dump(dados, f)

def carrega_as_listas_dos_ficheiros(nome_ficheiro_lista_de_veiculos,
                                    nome_ficheiro_lista_de_utilizadores,
                                    nome_ficheiro_lista_de_compras):
    """ ... """

    lista_de_veiculos = le_de_ficheiro(nome_ficheiro_lista_de_veiculos)
    lista_de_utilizadores = le_de_ficheiro(nome_ficheiro_lista_de_utilizadores)
    lista_de_compras = le_de_ficheiro(nome_ficheiro_lista_de_compras)
    return lista_de_veiculos, lista_de_utilizadores ,lista_de_compras


def guarda_as_listas_em_ficheiros(lista_de_veiculos,
                                  lista_de_utilizadores,
                                  lista_de_compras,
                                  nome_ficheiro_lista_de_veiculos,
                                  nome_ficheiro_lista_de_utilizadores,
                                  nome_ficheiro_lista_de_compras
                                  ):
    """ .......

    :param _lista_de_utilizadores:
    :param _lista_de_veiculos:
    :return:
    """

    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (S/n)?")
    if op in ['s', 'S']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_veiculos, lista_de_veiculos)
        guarda_em_ficheiro(nome_ficheiro_lista_de_utilizadores, lista_de_utilizadores)
        guarda_em_ficheiro(nome_ficheiro_lista_de_compras, lista_de_compras)

    else:
        print("Cancelada.")
