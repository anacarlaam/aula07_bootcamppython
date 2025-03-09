import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    """"
    funcao que le um arquivo csv e retorna um dicionario"
    """
    lista = []
    with open (nome_arquivo_csv,mode='r',encoding='utf-8' ) as arquivo:
        leitor=csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


def filtra_itens_enviado(lista: list) -> list[dict]:
    """"
    Funcao que filtra os itens que ja foram entregues"
    """
    lista_com_produtos_entregues = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_entregues.append(produto)
    return lista_com_produtos_entregues


def somar_valores_produtos_entregues(lista: list) -> int:
    """"
    Funcao que retorna a soma dos valores de todos os produtos entregues"
    """
    valor_total = 0
    for produto in lista:
        valor_total=+ int(produto.get("preco"))
        
    return valor_total



vendas_itens:list[dict]
vendas_itens = ler_csv(path_arquivo)
produtos_entregues: list[dict]
produtos_entregues=filtra_itens_enviado(vendas_itens)
soma_precos: int
soma_precos = somar_valores_produtos_entregues(produtos_entregues)
print("Lista de Produtos:", vendas_itens)
print("Produtos entregues:", produtos_entregues)
print("Valor total dos produtos entregues:", soma_precos)
    