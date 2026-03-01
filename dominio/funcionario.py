from datetime import date
from .pessoa import Pessoa

class Funcionario(Pessoa):
    """Representa um funcionário."""
    def __init__( self, codigo: int, nome: str, data_nascimento: date, identidade: str, data_admissao: date, data_recisao: date | None ) -> None:
        super().__init__(codigo, nome, data_nascimento, identidade)
        self.data_admissao = data_admissao
        self.data_recisao = data_recisao
        
    def cadastrar_cliente(self) -> None:
        raise NotImplementedError("Método ainda não implementado")

    def consulta_cliente(self) -> None:
        raise NotImplementedError("Método ainda não implementado")

    def alterar_cliente(self) -> None:
        raise NotImplementedError("Método ainda não implementado")

    def cadastrar_fornecedor(self) -> None:
        raise NotImplementedError("Método ainda não implementado")

    def consultar_fornecedor(self) -> None:
        raise NotImplementedError("Método ainda não implementado")

    def alterar_fornecedor(self) -> None:
        raise NotImplementedError("Método ainda não implementado")