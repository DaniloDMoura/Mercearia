from datetime import datetime


class Pessoa:


    def __init__(self, nome, telefone, endereco, email):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.email = email

class Fornecedor(Pessoa):


    def __init__(self, cnpj, nome, telefone, endereco, email, categoria):
        super().__init__(nome, telefone, endereco, email)
        self.cnpj = cnpj
        self.categoria = categoria

class Funcionario(Pessoa):


    def __init__(self, clt, nome, telefone, endereco, email):
        super().__init__(nome, telefone, endereco, email)
        self.clt = clt

class Cliente(Pessoa):


    def __init__(self, cpf, nome, telefone, endereco, email):
        super().__init__(nome, telefone, endereco, email)
        self.cpf = cpf

class Categoria:
    

    def __init__(self, codigo, categoria):
        self.codigo = codigo
        self.categoria = categoria

class Produto:


    def __init__(self, codigo, nome, preco, categoria):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:


    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Venda:


    def __init__(self, ccf, vendedor, comprador, item_vendido: Produto, 
                 qte_vendida, total, data = datetime.now()):
        self.ccf = ccf
        self.vendedor = vendedor
        self.comprador = comprador
        self.item_vendido = item_vendido
        self.qte_vendida = qte_vendida
        self.total = total
        self.data = data
