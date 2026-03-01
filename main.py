from datetime import date

from dominio import (Cliente, Funcionario, Contato, Endereco, Fornecedor, Produto, Venda, Compra)


def main() -> None:
     
    produto = Produto(
        cod_produto=1,
        nome="Notebook",
        valor=3500.0
    )

     
    contato = Contato(
        tel1="1111-1111",
        tel2=None,
        cel1="99999-9999",
        cel2="88888-8888",
        email="teste@email.com"
    )

     
    endereco = Endereco(
        cep="12345-000",
        estado="SP",
        cidade="São Paulo",
        rua="Rua A",
        numero="123",
        complemento="Apto 1"
    )

     
    cliente = Cliente(
        codigo=1,
        nome="João",
        data_nascimento=date(1990, 1, 1),
        identidade="123456789",
        data_cadastro=date.today(),
        valor_em_aberto=200.0
    )

    cliente.contatos.append(contato)
    cliente.endereco = endereco


     
    fornecedor = Fornecedor(
        cod_fornecedor=10,
        razao="Empresa XYZ LTDA",
        nome_fantasia="XYZ",
        insc_estadual="123456",
        cnpj="00.000.000/0001-00"
    )

    fornecedor.contatos.append(contato)
    fornecedor.endereco = endereco

        
    
    funcionario = Funcionario(
        codigo=2,
        nome="Maria",
        data_nascimento=date(1985, 5, 10),
        identidade="987654321",
        data_admissao=date(2020, 1, 15),
        data_recisao=None
    )

    funcionario.contatos.append(contato)
    funcionario.endereco = endereco


     
    venda = Venda(
        cod_venda=100,
        cliente=cliente,
        produto=produto,
        data_venda=date.today(),
        qtd_venda=2,
        preco_venda=3500.0,
        subtotal_venda=7000.0,
        forma_pagamento="Cartão"
    )

     
    compra = Compra(
        cod_compra=200,
        nota_fiscal_compra="NF123",
        produto=produto,
        qtd_compra=5,
        fornecedor=fornecedor,
        data_compra=date.today()
    )
 
    try:
        cliente.tira_extrato()
    except NotImplementedError as e:
        print("\nMétodo:", e)

if __name__ == "__main__":
    main()