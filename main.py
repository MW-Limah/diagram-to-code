from datetime import date

from dominio import (Cliente, Funcionario, Contato, Endereco, Fornecedor, Produto, Venda, Compra)


def main() -> None:
     
    # produto = Produto(
    #     cod_produto=1,
    #     nome="Notebook",
    #     valor=3500.0
    # )
    # 
    # print(produto)

    # contato = Contato(
    #     tel1="1248-2479",
    #     tel2="5681-1687",
    #     cel1="95451-9956",
    #     cel2="92314-9654",
    #     email="email@gmail.com"
    # )
    # print(contato)


    # endereco = Endereco(
    #     cep="12345-000",
    #     estado="SP",
    #     cidade="São Paulo",
    #     rua="Rua A",
    #     numero="123",
    #     complemento="Apto 1"
    # )
    # print(endereco)


    # cliente = Cliente(
    #     codigo=1,
    #     nome="João",
    #     data_nascimento=date(1990, 1, 1),
    #     identidade="123456789",
    #     data_cadastro=date.today(),
    #     valor_em_aberto=200.0
    # )
    # cliente.contatos.append(contato)
    # cliente.endereco = endereco
    # print(cliente)

    # fornecedor = Fornecedor(
    #     cod_fornecedor=10,
    #     razao="Empresa XYZ LTDA",
    #     nome_fantasia="XYZ",
    #     insc_estadual="123456",
    #     cnpj="00.000.000/0001-00"
    # )
    # fornecedor.contatos.append(contato)
    # fornecedor.endereco = endereco
    # print(fornecedor)

    # funcionario = Funcionario(
    #     codigo=2,
    #     nome="Maria",
    #     data_nascimento=date(1985, 5, 10),
    #     identidade="987654321",
    #     data_admissao=date(2020, 1, 15),
    #     data_recisao=None
    # )
    # funcionario.contatos.append(contato)
    # funcionario.endereco = endereco
    # print(fornecedor)
     
    # venda = Venda(
    #     cod_venda=100,
    #     cliente=cliente,
    #     produto=produto,
    #     data_venda=date.today(),
    #     qtd_venda=2,
    #     preco_venda=3500.0,
    #     subtotal_venda=7000.0,
    #     forma_pagamento="Cartão"
    # )
    # print(venda)

    # compra = Compra(
    #     cod_compra=200,
    #     nota_fiscal_compra="NF123",
    #     produto=produto,
    #     qtd_compra=5,
    #     fornecedor=fornecedor,
    #     data_compra=date.today()
    # )
    # print(compra)

    # try:
    #     cliente.tira_extrato()
    # except NotImplementedError as e:
    #     print("\nMétodo:", e)

if __name__ == "__main__":
    main()