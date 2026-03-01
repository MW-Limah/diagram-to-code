from datetime import date

class Funcionario:
    
    # Atributos
    def __init__(self, data_admissao = date, data_recisao = date):
        self.data_admissao = data_admissao
        self.data_recisao = data_recisao

    # Métodos necessários = CadastrarCliente(), ConsultaCliente(), AlterarCliente(), CadastrarFornecedor(), ConsultarFornecedor(), AlterarFornecedor()