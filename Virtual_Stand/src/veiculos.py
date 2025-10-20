from io_terminal import imprime_lista

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"


def cria_novo_veiculo():
    """ Pede ao utilizador para introduzir um novo veiculo

    :return: dicionario com um veiculo na forma
        {"marca": <<marca>>,"modelo: <<modelo>>,"preço": <<preço>> "matricula": <<matricula>>,"cor": <<cor>>,
        "ano": <<ano>>}
    """
    marca = input("marca? ")
    modelo = input("modelo? ")
    preco = input("preço? ")
    matricula = input("matricula? ").upper()
    ano = input("Ano?")
    cor = input("cor? ")

    return {"marca": marca, "modelo": modelo, "preço": preco, "matricula": matricula, "cor": cor, "Ano": ano}


def imprime_lista_de_veiculos(lista_de_veiculos):
    """ ..."""

    imprime_lista(cabecalho="Lista de Veiculos", lista=lista_de_veiculos)
