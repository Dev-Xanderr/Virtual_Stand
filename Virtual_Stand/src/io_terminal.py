from pprint import pprint


def imprime_lista(cabecalho, lista):
    """ imprime a lista

    :param cabecalho: cabecalho para a listagem
    :param lista: lista a ser impressa
    """

    cabecalho = f":::::::::::::::::: {cabecalho} ::::::::::::::::::"
    comprimento_cabecalho = len(cabecalho)

    print(cabecalho)
    for id, item in enumerate(lista):
        pprint(f"[{id}]: {item}")
    print(comprimento_cabecalho * ":")


def pergunta_id(questao, lista):
    """ ... ????

    :param questao:
    :param lista:
    :return:
    """

    while True:
        id = int(input(questao))
        if 0 <= id < len(lista):
            return id
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")
