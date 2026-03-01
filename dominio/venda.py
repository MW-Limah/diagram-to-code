from datetime import date
from .cliente import Cliente
from .produto import Produto


class Venda:
    """Representa uma venda."""

    def __init__(self, cod_venda: int, cliente: Cliente, produto: Produto, data_venda: date, qtd_venda: int, preco_venda: float, subtotal_venda: float, forma_pagamento: str) -> None:
        self.cod_venda = cod_venda
        self.cliente = cliente
        self.produto = produto
        self.data_venda = data_venda
        self.qtd_venda = qtd_venda
        self.preco_venda = preco_venda
        self.subtotal_venda = subtotal_venda
        self.forma_pagamento = forma_pagamento