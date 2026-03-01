from .base import Base

class Produto(Base):
    """Representa um produto."""

    def __init__(self, cod_produto: int, nome: str, valor: float) -> None:
        self.cod_produto = cod_produto
        self.nome = nome
        self.valor = valor