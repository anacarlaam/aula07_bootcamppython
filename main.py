from etl import ler_csv,filtra_itens_enviado,somar_valores_produtos_entregues

path_arquivo = "vendas.csv"

vendas_itens:list[dict]
vendas_itens = ler_csv(path_arquivo)
produtos_entregues: list[dict]
produtos_entregues=filtra_itens_enviado(vendas_itens)
soma_precos: int
soma_precos = somar_valores_produtos_entregues(produtos_entregues)
print("Lista de Produtos:", vendas_itens)
print("Produtos entregues:", produtos_entregues)
print("Valor total dos produtos entregues:", soma_precos)