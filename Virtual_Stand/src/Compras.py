"""Faz import da função imprime_lista do io_terminal.py"""

from io_terminal import imprime_lista

nome_ficheiro_lista_de_compras = "lista_de_compra.pk"


def imprime_lista_de_compras(lista_de_compras):
    """Imprime a lista do ficheiro lista_de_compras.pk"""

    imprime_lista(cabecalho="Lista de Compras", lista=lista_de_compras)


