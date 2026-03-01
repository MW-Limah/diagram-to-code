from datetime import date

class Pessoa:
    """Representa uma pessoa do sistema."""

    # Atributos
    def __init__(self, codigo: int, nome: str, data_nascimento: date, identidade: str) -> None:
        self.codigo = codigo
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.identidade = identidade

    # Sem métodos