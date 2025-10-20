from veiculos import (cria_novo_veiculo,
                      imprime_lista_de_veiculos,
                      nome_ficheiro_lista_de_veiculos
                      )
from utilizadores import (cria_novo_utilizador,
                          imprime_lista_de_utilizadores,
                          nome_ficheiro_lista_de_utilizadores
                          )
from Compras import (nome_ficheiro_lista_de_compras,
                     imprime_lista_de_compras
                     )

from io_ficheiros import (carrega_as_listas_dos_ficheiros,
                          guarda_as_listas_em_ficheiros
                          )
from io_terminal import pergunta_id
import time


def menu():
    """ main menu da aplicação"""

    lista_de_veiculos = []
    lista_de_utilizadores = []
    lista_de_compras = []

    while True:
        print("""
        *********************************************************************
        |       STAND XOCORRO - OS CLASSICOS DAS 2 RODAS                    |
        *********************************************************************
        |                                                                   |
        | vn - novo veiculo         vl - lista veiculos                     |
        | un - novo utilizador      ul - lista utilizadores                 |
        | cn - nova compra          cl - lista compras                      |
        | ...                                                               |
        | g - guarda tudo           c - carrega tudo                        |
        | x - sair                                                          |
        |                                                                   |
        *********************************************************************
        """)

        op = input("opcao?").lower()

        if op == "x":
            exit()
        elif op == "vn":
            novo_veiculo = cria_novo_veiculo()
            lista_de_veiculos.append(novo_veiculo)
        elif op == "vl":
            imprime_lista_de_veiculos(lista_de_veiculos)
        elif op == "un":
            novo_utilizador = cria_novo_utilizador()
            lista_de_utilizadores.append(novo_utilizador)
        elif op == "ul":
            imprime_lista_de_utilizadores(lista_de_utilizadores)
        elif op == "g":
            guarda_as_listas_em_ficheiros(lista_de_veiculos,
                                          lista_de_utilizadores,
                                          lista_de_compras,
                                          nome_ficheiro_lista_de_veiculos,
                                          nome_ficheiro_lista_de_utilizadores,
                                          nome_ficheiro_lista_de_compras
                                          )
        elif op == "c":
            lista_de_veiculos, lista_de_utilizadores,lista_de_compras = carrega_as_listas_dos_ficheiros(
                nome_ficheiro_lista_de_veiculos=nome_ficheiro_lista_de_veiculos,
                nome_ficheiro_lista_de_utilizadores=nome_ficheiro_lista_de_utilizadores,
                nome_ficheiro_lista_de_compras=nome_ficheiro_lista_de_compras
            )
        elif op == "cn":
            id_comprador = pergunta_id(questao="Qual o id do comprador?", lista=lista_de_utilizadores)
            id_veiculo = pergunta_id(questao="Qual o id do veiculo?", lista=lista_de_veiculos)
            lista_de_compras.append([id_comprador, id_veiculo, time.time()])
        elif op == "cl":
            imprime_lista_de_compras(lista_de_compras)
            #pass
            # todo



if __name__ == "__main__":
    menu()
