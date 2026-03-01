from datetime import date
from pessoa import Pessoa


class Cliente(Pessoa):
    """Representa um cliente."""

    def __init__(self, codigo: int, nome: str, data_nascimento: date, identidade: str, data_cadastro: date, valor_em_aberto: float) -> None:
        super().__init__(codigo, nome, data_nascimento, identidade)
        self.data_cadastro = data_cadastro
        self.valor_em_aberto = valor_em_aberto

    def tira_extrato(self) -> None:
        raise NotImplementedError("Método ainda não implementado")

    def efetuar_pagamento(self) -> None:
        raise NotImplementedError("Método ainda não implementado")