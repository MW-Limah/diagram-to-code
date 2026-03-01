from datetime import date

class Cliente:

    # Atributos
    def __init__(self, data_cadastro = date, valor_aberto = str) -> None:
        self.data_cadastro = data_cadastro
        self.valor_aberto = valor_aberto

        # Métodos necessários = TiraExtrato(), EfetuarPagamento() 