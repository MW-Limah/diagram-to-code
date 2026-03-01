[FACULDADE GRAN](https://faculdade.grancursosonline.com.br/)

Este projeto implementa um diagrama de classes utilizando Programação Orientada a Objetos (POO) em Python.

A aplicação simula um pequeno sistema de gestão, contendo entidades como:

- Clientes
- Funcionários
- Fornecedores
- Produtos
- Vendas
- Compras

O foco principal é a estruturação correta das classes, seus relacionamentos e a criação de objetos a partir do modelo proposto.

Conceitos Aplicados

**1. Herança**

- A classe _Pessoa_ serve como base para:
  - Cliente
  - Funcionario
  - Centralizando atributos comuns:

**2. Associação entre objetos**

- Entidades com dados complementares:
  - Contato
  - Endereco

- Relacionamentos principais:
  - Venda → Cliente + Produto
  - Compra → Fornecedor + Produto

**3. Classe Base**

- A classe Base implementa um **repr** customizado para facilitar a visualização dos objetos

Para executar:

- Rode o comando: python main.py

Status do Projeto:

- Estrutura de classes definida
- Relacionamentos implementados
- Criação de Objetos funcional
- Métodos ainda não não implementados
