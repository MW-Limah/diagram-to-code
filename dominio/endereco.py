class Endereco:
    """Representa um endereço."""

    def __init__( self, cep: str, estado: str, cidade: str, rua: str, numero: str, complemento: str) -> None:
        self.cep = cep
        self.estado = estado
        self.cidade = cidade
        self.rua = rua
        self.numero = numero
        self.complemento = complemento