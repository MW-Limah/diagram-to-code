class Produto:
    # Atributos
    def __init__(self, cod_produto: str, nome: str, valor: float) -> None:
        self.cod_produto = cod_produto
        self.nome = nome
        self.valor = valor
    
    # Sem métodos