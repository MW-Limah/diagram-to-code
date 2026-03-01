from typing import List
from .contato import Contato
from .endereco import Endereco
from .base import Base


class Fornecedor (Base):
    """Representa um fornecedor."""

    def __init__(self, cod_fornecedor: int, razao: str, nome_fantasia: str, insc_estadual: str, cnpj: str) -> None:
        self.cod_fornecedor = cod_fornecedor
        self.razao = razao
        self.nome_fantasia = nome_fantasia
        self.insc_estadual = insc_estadual
        self.cnpj = cnpj
 
        # Relacionamentos
        self.contatos: List[Contato] = []
        self.endereco: Endereco | None = None