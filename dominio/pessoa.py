from typing import List
from .contato import Contato
from .endereco import Endereco
from datetime import date


class Pessoa:
    """Representa uma pessoa do sistema."""

    def __init__( self, codigo: int, nome: str, data_nascimento: date, identidade: str) -> None:
        self.codigo = codigo
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.identidade = identidade

        self.contatos: List[Contato] = []
        self.endereco: Endereco | None = None