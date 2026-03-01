from datetime import date
class Venda:
    # Atributos
    def __init__(self, cod_venda = str, cod_cliente_venda = str, data_venda = date, qtd_venda = int, preco_venda = float, subtotal_venda = float, forma_pagamento = str) -> None:
        self.cod_venda = cod_venda
        self.cod_cliente_venda = cod_cliente_venda
        self.data_venda = data_venda
        self.qtd_venda = qtd_venda
        self.preco_venda = preco_venda
        self.subtotal_venda = subtotal_venda
        self.forma_pagamento = forma_pagamento

    # Sem métodos
