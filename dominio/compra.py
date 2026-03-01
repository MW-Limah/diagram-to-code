from datetime import date
from .produto import Produto
from .fornecedor import Fornecedor


class Compra:
    """Representa uma compra."""

    def __init__(self, cod_compra: int, nota_fiscal_compra: str, produto: Produto, qtd_compra: int, fornecedor: Fornecedor, data_compra: date) -> None:
        self.cod_compra = cod_compra
        self.nota_fiscal_compra = nota_fiscal_compra
        self.produto = produto
        self.qtd_compra = qtd_compra
        self.fornecedor = fornecedor
        self.data_compra = data_compra