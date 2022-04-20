from model import Categoria, Cliente, Estoque, Fornecedor, Funcionario, Produto, Venda


path_cate = './administrativo/categorias.csv'
path_clie = './administrativo/clientes.csv'
path_esto = './administrativo/estoque.csv'
path_forn = './administrativo/fornecedores.csv'
path_func = './administrativo/funcionarios.csv'
path_vend = './financeiro/vendas.csv'


def ajuste_linha(string):
    string = list(map(lambda x: x.replace('\n', ''), string))
    string = list(map(lambda x: x.split(';'), string))
    
    return string

class FornecedorDal:


    @classmethod
    def salvar_forn(cls, fornecedor: Fornecedor):
        with open(path_forn, 'a') as arq:
            arq.writelines(f'{fornecedor.cnpj};{fornecedor.nome};{fornecedor.telefone};'
                           f'{fornecedor.endereco};{fornecedor.email};{fornecedor.categoria}\n')
        arq.close()
    
    @classmethod
    def ler_forn(cls):
        with open(path_forn, 'r') as arq:
            cls.fornecedores = arq.readlines()
        arq.close()

        cls.fornecedores = ajuste_linha(cls.fornecedores)
        forn = [Fornecedor(i[0], i[1], i[2], i[3], i[4], i[5]) for i in cls.fornecedores]
        
        return forn
    
    @classmethod
    def limpar_forn(cls):
        arq = open(path_forn, 'w')
        arq.close()

class FuncionarioDal:
    

    @classmethod
    def salvar_func(cls, funcionario: Funcionario):
        with open(path_func, 'a') as arq:
            arq.writelines(f'{funcionario.clt};{funcionario.nome};{funcionario.telefone};'
                           f'{funcionario.endereco};{funcionario.email}\n')
        arq.close()
    
    @classmethod
    def ler_func(cls):
        with open(path_func, 'r') as arq:
            cls.funcionarios = arq.readlines()
        arq.close()

        cls.funcionarios = ajuste_linha(cls.funcionarios)
        func = [Funcionario(i[0], i[1], i[2], i[3], i[4]) for i in cls.funcionarios]
        
        return func
    
    @classmethod
    def limpar_func(cls):
        arq = open(path_func, 'w')
        arq.close()

class ClienteDal:
    

    @classmethod
    def salvar_clie(cls, cliente: Cliente):
        with open(path_clie, 'a') as arq:
            arq.writelines(f'{cliente.cpf};{cliente.nome};{cliente.telefone};'
                           f'{cliente.endereco};{cliente.email}\n')
        arq.close()
    
    @classmethod
    def ler_clie(cls):
        with open(path_clie, 'r') as arq:
            cls.clientes = arq.readlines()
        arq.close()

        cls.clientes = ajuste_linha(cls.clientes)
        clie = [Cliente(i[0], i[1], i[2], i[3], i[4]) for i in cls.clientes]
        
        return clie
    
    @classmethod
    def limpar_clie(cls):
        arq = open(path_clie, 'w')
        arq.close()

class CategoriaDal:
    

    @classmethod
    def salvar_cate(cls, categoria: Categoria):
        with open(path_cate, 'a') as arq:
            arq.writelines(f'{categoria.codigo};{categoria.categoria}\n')
        arq.close()
    
    @classmethod
    def ler_cate(cls):
        with open(path_cate, 'r') as arq:
            cls.categorias = arq.readlines()
        arq.close()

        cls.categorias = ajuste_linha(cls.categorias)
        cate = [Categoria(i[0], i[1]) for i in cls.categorias]
        
        return cate
    
    @classmethod
    def limpar_cate(cls):
        arq = open(path_cate, 'w')
        arq.close()

class EstoqueDal:


    @classmethod
    def salvar_esto(cls, estoque: Estoque):
        with open(path_esto, 'a') as arq:
            arq.writelines(f'{estoque.produto.codigo};{estoque.produto.nome};'
                           f'{estoque.produto.preco};{estoque.produto.categoria};'
                           f'{estoque.quantidade}\n')
        arq.close()
    
    @classmethod
    def ler_esto(cls):
        with open(path_esto, 'r') as arq:
            cls.estocagem = arq.readlines()
        arq.close()

        cls.estocagem = ajuste_linha(cls.estocagem)
        esto = [Estoque(Produto(i[0], i[1], i[2], i[3]), i[4]) for i in cls.estocagem]
        
        return esto
    
    @classmethod
    def limpar_esto(cls):
        arq = open(path_esto, 'w')
        arq.close()

class VendaDal:

   
    @classmethod
    def salvar_venda(cls, venda: Venda):
        with open(path_vend, 'a') as arq:
            arq.writelines(f'{venda.ccf};{venda.vendedor};{venda.comprador};'
                           f'{venda.item_vendido.codigo};{venda.item_vendido.nome};'
                           f'{venda.item_vendido.preco};{venda.item_vendido.categoria};'
                           f'{venda.qte_vendida};{venda.total:.2f};{venda.data}\n')
        arq.close()
    
    @classmethod
    def ler_venda(cls):
        with open(path_vend, 'r') as arq:
            cls.vendas = arq.readlines()
        arq.close()

        cls.vendas = ajuste_linha(cls.vendas)
        venda = [Venda(i[0], i[1], i[2], (Produto(i[3], i[4], i[5], i[6])), i[7], i[8], i[9]) for i in cls.vendas]

        return venda
