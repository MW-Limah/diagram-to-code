from datetime import date

class Compra:
    # Atributos
    def __init__(self, cod_compra: str, nota_fiscal_compra: str, cod_pro_compra: str, qtd_compra: int, cod_for_compra: str, data_compra: date) -> None:
        self.cod_compra = cod_compra
        self.nota_fiscal_compra = nota_fiscal_compra
        self.cod_pro_compra = cod_pro_compra
        self.qtd_compra = qtd_compra
        self.cod_for_compra = cod_for_compra
        self.data_compra = data_compra
    
    # Sem métodos