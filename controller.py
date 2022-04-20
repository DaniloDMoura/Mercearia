from dal import CategoriaDal, ClienteDal, EstoqueDal, FornecedorDal, FuncionarioDal, VendaDal
from model import Categoria, Cliente, Estoque, Fornecedor, Funcionario, Produto, Venda
import datetime as dt

def validador(id, *args):
    val_1 = False
    val_2 = False

    a = len(id)

    if args[0] == 'cliente':
        b = ClienteDal.ler_clie()
        formatado = f'{id[:3]}.{id[3:6]}.{id[6:9]}-{id[9:]}'
        existe = list(filter(lambda x: x.cpf == formatado, b))
    
    elif args[0] == 'fornecedor':
        b = FornecedorDal.ler_forn()
        formatado = f'{id[:2]}.{id[2:5]}.{id[5:8]}/{id[8:12]}-{id[12:]}'
        existe = list(filter(lambda x: x.cnpj == formatado, b))

        if a != 14:
            val_1 = True

    elif args[0] == 'funcionario':
        b = FuncionarioDal.ler_func()
        formatado = f'{id[:3]}.{id[3:8]}.{id[8:10]}-{id[10:]}'
        existe = list(filter(lambda x: x.clt == formatado, b))

    if args[0] == 'cliente' or args[0] == 'funcionario':
        if a != 11:
            val_1 = True

    if args[1] == 'c': 
        if len(existe) != 0:
            val_2 = True
    elif args[1] == 'a' or args[1] == 'r':
        if len(existe) == 0:
            val_2 = True

    return formatado, val_1, val_2

def validador_cod(codigo, id, *args):
    val_cod = False
    
    cod = list(filter(lambda x: x.codigo == codigo, id))

    if args[0] == 'c':
        if len(cod) != 0:
            val_cod = True
    
    elif args[0] == 'a' or args[0] == 'r':
        if len(cod) == 0:
            val_cod = True
    
    return val_cod

def validador_esto(codigo, id, *args):
    val_cod = False
    
    cod = list(filter(lambda x: x.produto.codigo == codigo, id))

    if args[0] == 'c':
        if len(cod) != 0:
            val_cod = True
    
    elif args[0] == 'a' or args[0] == 'r':
        if len(cod) == 0:
            val_cod = True
    
    return val_cod

def validador_cat(categoria, *args):
    val_cat = False

    a = CategoriaDal.ler_cate()

    cat = list(filter(lambda x: x.categoria.lower() == categoria.lower(), a))

    if args[0] == 'categoria':
        if len(cat) != 0:
            val_cat = True

    elif args[0] == 'fornecedor':
        if len(cat) == 0:
            val_cat = True
    
    return val_cat

def mensagens(id, val_1, val_2, *args):
    x = len(id)
    
    if args[0] == 'cliente':
        txt = [args[0].capitalize(), 'CPF', '11']
    
    elif args[0] == 'fornecedor':
        txt = [args[0].capitalize(), 'CNPJ', '14']
    
    elif args[0] == 'funcionário':
        txt = [args[0].capitalize(), 'CLT', '11']

    if args[1] == 'c':
        sub_txt = ['cadastrado', 'já está cadastrado']
    
    elif args[1] == 'a':
        sub_txt = ['alterado', 'não consta no banco de dados']
    
    elif args[1] == 'r':
        sub_txt = ['removido', 'não consta no banco de dados']

    print(f'\nErro - {txt[0]} não {sub_txt[0]}')
    if val_1:
        print(f'{txt[1]} é composto de {txt[2]} números, '
            f'você forneceu apenas {x} números\n')

    elif val_2:
        print(f'{txt[0]} {sub_txt[1]}\n')


class CategoriaController:
    

    @classmethod
    def cadastrar_cate(cls, codigo, categoria):
        a = CategoriaDal.ler_cate()

        val_cat = validador_cat(categoria, 'categoria')
        val_cod = validador_cod(codigo, a, 'c')

        if not val_cod and not val_cat:
            CategoriaDal.salvar_cate(Categoria(codigo, categoria))
            print('\nCategoria cadastrada com sucesso\n')
        
        else:
            print('\nErro - Categoria não cadastrada')
            if val_cod and val_cat:
                print('Código e Categoria já existentes\n')

            elif val_cod:
                print('Código já existente\n')
            
            elif val_cat:
                print('Categoria já existente\n')
            
        input('Pressione ENTER para continuar ')
    
    @classmethod
    def leitura_cate(cls):        
        x = CategoriaDal.ler_cate()

        if len(x) != 0:
            print(f"{'Código':<10} | Categoria")

            for i in x:
                print(f'{i.codigo:<10} | {i.categoria}')
            
            print('\n')
        
        else:
            print('Não há dados a serem lidos\n')
    
    @classmethod
    def alterar_cate(cls, codigo):
        a = CategoriaDal.ler_cate()

        val_cod = validador_cod(codigo, a, 'a')

        if len(a) != 0:
            if not val_cod:
                nova_cat = input('Alterar categoria para: ')

                val_cat = validador_cat(nova_cat, 'categoria')
                
                if not val_cat:
                    CategoriaDal.limpar_cate()

                    for i in a:
                        if i.codigo == codigo:
                            i.categoria = nova_cat
                        
                        CategoriaDal.salvar_cate(Categoria(i.codigo, i.categoria))

                    print('\nCategoria alterada com sucesso\n')
                
                else:
                    print('\nErro - Categoria não alterada\n'
                          'Categoria já existente\n')
            
            else:
                print('\nErro - Categoria não alterada\n'
                      'Código inválido\n')
            
            input('Pressione ENTER para continuar ')
        
        else:
            print('Não há dados a serem lidos\n')
    
    @classmethod
    def remover_cate(cls, codigo):
        a = CategoriaDal.ler_cate()

        val_cod = validador_cod(codigo, a, 'r')

        if len(a) != 0:
            if not val_cod:
                CategoriaDal.limpar_cate()

                for i in a:
                    if i.codigo != codigo:
                        CategoriaDal.salvar_cate(Categoria(i.codigo, i.categoria))
            
                print('\nCategoria removida com sucesso\n')
                
            else:
                print('\nErro - Categoria não removida\n'
                      'Código inválido\n')
            
            input('Pressione ENTER para continuar ')
        
        else:
            print('Não há dados a serem lidos\n')

class FornecedorController:


    @classmethod
    def cadastrar_forn(cls, cnpj, nome, telefone, endereco, email, categoria):
        
        cnpj_formatado, val_cnpj, val_forn = validador(cnpj, 'fornecedor', 'c')
        val_cat = validador_cat(categoria, 'fornecedor')

        if not val_cnpj and not val_cat and not val_forn:
            FornecedorDal.salvar_forn(
                Fornecedor(cnpj_formatado, nome, telefone, endereco, email, categoria))
            
            print('\nFornecedor cadastrado com sucesso\n')
        
        else:          
            if val_cnpj and val_cat:
                print('\nErro - Fornecedor não cadastrado\n')
                print(f'CNPJ com {len(cnpj)}/14 números e Categoria não cadastrada\n')
            
            elif val_cat:
                print('\nErro - Fornecedor não cadastrado\n')
                print('Categoria não consta no banco de dados\n')
            
            else:
                mensagens(cnpj, val_cnpj, val_forn, 'fornecedor', 'c')
        
        input('Pressione ENTER para continuar ')
    
    @classmethod
    def leitura_forn(cls):        
        x = FornecedorDal.ler_forn()

        if len(x) != 0:
            print(f"{'CNPJ':<20} | {'Nome':<35} | {'Telefone':<15} | "
              f"{'Endereço':<30} | {'Email':<35} | Categoria")

            for i in x:
                print(f'{i.cnpj:<20} | {i.nome:<35} | {i.telefone:<15} | '
                    f'{i.endereco:<30} | {i.email:<35} | {i.categoria}')
            
            print('\n')
        
        else:
            print('Não há dados a serem lidos\n')
    
    @classmethod
    def alterar_forn(cls, cnpj):
        a = FornecedorDal.ler_forn()

        cnpj_formatado, val_cnpj, val_forn = validador(cnpj, 'fornecedor', 'a')

        if len(a) != 0:
            if not val_cnpj and not val_forn:
                novo_nom = input('Alterar nome para: ')
                novo_tel = input('Alterar telefone para: ')
                novo_end = input('Alterar endereço para: ')
                novo_ema = input('Alterar email para: ')
                nova_cat = input('Alterar categoria para: ')

                val_cat = validador_cat(nova_cat, 'fornecedor')
                
                if not val_cat:
                    FornecedorDal.limpar_forn()

                    for i in a:
                        if i.cnpj == cnpj_formatado:
                            i.nome = novo_nom
                            i.telefone = novo_tel
                            i.endereco = novo_end
                            i.email = novo_ema
                            i.categoria = nova_cat
                        
                        FornecedorDal.salvar_forn(
                            Fornecedor(
                                i.cnpj, i.nome, i.telefone, i.endereco, i.email, i.categoria))

                    print('\nFornecedor alterado com sucesso\n')
                
                else:
                    print('\nErro - Fornecedor não alterado\n'
                          'Categoria não consta no banco de dados\n')
                    
            else:
                mensagens(cnpj, val_cnpj, val_forn, 'fornecedor', 'a')
        
            input('Pressione ENTER para continuar ')

        else:
            print('Não há dados a serem lidos\n')
    
    @classmethod
    def remover_forn(cls, cnpj):
        a = FornecedorDal.ler_forn()

        cnpj_formatado, val_cnpj, val_forn = validador(cnpj, 'fornecedor', 'r')
        
        if len(a) != 0:
            if not val_cnpj and not val_forn:
                FornecedorDal.limpar_forn()

                for i in a:
                    if i.cnpj != cnpj_formatado:
                        FornecedorDal.salvar_forn(
                            Fornecedor(
                                i.cnpj, i.nome, i.telefone, i.endereco, i.email, i.categoria))
            
                print('\nFornecedor removido com sucesso\n')
 
            else:
                mensagens(cnpj, val_cnpj, val_forn, 'fornecedor', 'r')
            
            input('Pressione ENTER para continuar ')

        else:
            print('Não há dados a serem lidos\n')

class FuncionarioController:
    

    @classmethod
    def cadastrar_func(cls, clt, nome, telefone, endereco, email):

        clt_formatado, val_clt, val_func = validador(clt, 'funcionario', 'c')

        if not val_clt and not val_func:
            FuncionarioDal.salvar_func(
                Funcionario(clt_formatado, nome, telefone, endereco, email))
            
            print('\nFuncionário cadastrado com sucesso\n')
            
        
        else:
            mensagens(clt, val_clt, val_func, 'funcionário', 'c')
        
        input('Pressione ENTER para continuar ')

    @classmethod
    def leitura_func(cls):        
        x = FuncionarioDal.ler_func()

        if len(x) != 0:
            print(f"{'CLT':<20} | {'Nome':<35} | {'Telefone':<15} | "
                f"{'Endereço':<30} | Email")

            for i in x:
                print(f'{i.clt:<20} | {i.nome:<35} | {i.telefone:<15} | '
                    f'{i.endereco:<30} | {i.email}')
            
            print('\n')

        else:
            print('Não há dados a serem lidos\n')
    
    @classmethod
    def alterar_func(cls, clt):
        a = FuncionarioDal.ler_func()

        clt_formatado, val_clt, val_func = validador(clt, 'funcionario', 'a')

        if len(a) != 0:
            if not val_clt and not val_func:
                novo_nom = input('Alterar nome para: ')
                novo_tel = input('Alterar telefone para: ')
                novo_end = input('Alterar endereço para: ')
                novo_ema = input('Alterar email para: ')

                FuncionarioDal.limpar_func()

                for i in a:
                    if i.clt == clt_formatado:
                        i.nome = novo_nom
                        i.telefone = novo_tel
                        i.endereco = novo_end
                        i.email = novo_ema
                        
                    FuncionarioDal.salvar_func(
                        Funcionario(
                            i.clt, i.nome, i.telefone, i.endereco, i.email))

                print('\nFuncionário alterado com sucesso\n')
                
            else:
                mensagens(clt, val_clt, val_func, 'funcionário', 'a')
            
            input('Pressione ENTER para continuar ')

        else:
            print('Não há dados a serem lidos\n')
    
    @classmethod
    def remover_func(cls, clt):
        a = FuncionarioDal.ler_func()

        clt_formatado, val_clt, val_func = validador(clt, 'funcionario', 'r')
        
        if len(a) != 0:
            if not val_clt and not val_func:
                FuncionarioDal.limpar_func()

                for i in a:
                    if i.clt != clt_formatado:
                        FuncionarioDal.salvar_func(
                            Funcionario(
                                i.clt, i.nome, i.telefone, i.endereco, i.email))

                print('\nFuncionário removido com sucesso\n')    
            
            else:
                mensagens(clt, val_clt, val_func, 'funcionário', 'r')
        
            input('Pressione ENTER para continuar ')

        else:
            print('Não há dados a serem lidos\n')

class ClienteController:
    

    @classmethod
    def cadastrar_clie(cls, cpf, nome, telefone, endereco, email):
        
        cpf_formatado, val_cpf, val_clie = validador(cpf, 'cliente', 'c')

        if not val_cpf and not val_clie:
            ClienteDal.salvar_clie(
                Cliente(cpf_formatado, nome, telefone, endereco, email))
            
            print('\nCliente cadastrado com sucesso\n')
        
        else:
            mensagens(cpf, val_cpf, val_clie, 'cliente', 'c')
        
        input('Pressione ENTER para continuar ')

    @classmethod
    def leitura_clie(cls):        
        x = ClienteDal.ler_clie()

        if len(x) != 0:
            print(f"{'CPF':<20} | {'Nome':<35} | {'Telefone':<15} | "
                f"{'Endereço':<40} | Email")

            for i in x:
                print(f'{i.cpf:<20} | {i.nome:<35} | {i.telefone:<15} | '
                    f'{i.endereco:<40} | {i.email}')
            
            print('\n')

        else:
            print('Não há dados a serem lidos\n')
    
    @classmethod
    def alterar_clie(cls, cpf):
        a = ClienteDal.ler_clie()
        
        cpf_formatado, val_cpf, val_clie = validador(cpf, 'cliente', 'a')
        
        if len(a) != 0:
            if not val_cpf and not val_clie:
                novo_nom = input('Alterar nome para: ')
                novo_tel = input('Alterar telefone para: ')
                novo_end = input('Alterar endereço para: ')
                novo_ema = input('Alterar email para: ')

                ClienteDal.limpar_clie()

                for i in a:
                    if i.cpf == cpf_formatado:
                        i.nome = novo_nom
                        i.telefone = novo_tel
                        i.endereco = novo_end
                        i.email = novo_ema
                        
                    ClienteDal.salvar_clie(
                        Cliente(i.cpf, i.nome, i.telefone, i.endereco, i.email))

                print('\nCliente alterado com sucesso\n')   
            
            else:
                mensagens(cpf, val_cpf, val_clie, 'cliente', 'a')

            input('Pressione ENTER para continuar ')

        else:
            print('Não há dados a serem lidos\n')
    
    @classmethod
    def remover_clie(cls, cpf):
        a = ClienteDal.ler_clie()
        
        cpf_formatado, val_cpf, val_clie = validador(cpf, 'cliente', 'r')

        if len(a) != 0:
            if not val_cpf and not val_clie:
                ClienteDal.limpar_clie()

                for i in a:
                    if i.cpf != cpf_formatado:
                        ClienteDal.salvar_clie(
                            Cliente(i.cpf, i.nome, i.telefone, i.endereco, i.email))

                print('\nCliente removido com sucesso\n')  
            
            else:
                mensagens(cpf, val_cpf, val_clie, 'cliente', 'r')

            input('Pressione ENTER para continuar ')

        else:
            print('Não há dados a serem lidos\n')

class EstoqueController:


    @classmethod
    def cadastrar_esto(cls, codigo, nome, preco, categoria, quantidade):
        a = EstoqueDal.ler_esto()

        val_lim = False

        max = 1000

        if int(quantidade) > max:
            val_lim = True

        val_cod = validador_esto(codigo, a, 'c')
        val_cat = validador_cat(categoria, 'fornecedor')

        if not val_cod and not val_cat and not val_lim:
            EstoqueDal.salvar_esto(
                Estoque(Produto(codigo, nome, preco, categoria), quantidade))
            
            print('\nProduto cadastrado com sucesso\n')
        
        else:
            print('\nErro - Produto não cadastrado\n')     
            if val_cod and val_cat:
                print(f'Código já existente e Categoria não cadastrada\n')
            
            elif val_cat:
                print('Categoria não consta no banco de dados\n')
            
            elif val_cod:
                print('Código já existente\n')
            
            elif val_lim:
                print('Quantidade excede limite do estoque')
        
        input('Pressione ENTER para continuar ')
    
    @classmethod
    def leitura_esto(cls):        
        a = EstoqueDal.ler_esto()
        b = FornecedorDal.ler_forn()
        crit_cat = []
        forn_list = []

        max = 1000

        if len(a) != 0:
            print(f"{'Código':<10} | {'Nome':<40} | {'Preço':>15} | "
                f"{'Categoria':<40} | Quantidade")

            for i in a:
                if int(i.quantidade) <= int(0.3*max):
                    print(f'\033[91m{i.produto.codigo:<10} | {i.produto.nome:<40} | '
                          f'{i.produto.preco:>15} | '
                          f'{i.produto.categoria:<40} | {i.quantidade}\033[0m')
                    
                    crit_cat.append(i.produto.categoria)
                
                else:    
                    print(f'{i.produto.codigo:<10} | {i.produto.nome:<40} | '
                        f'{i.produto.preco:>15} | '
                        f'{i.produto.categoria:<40} | {i.quantidade}')
            
            print('\n')

            unic_cat = list(set(crit_cat))
   
            for i in b:
                for j in unic_cat:
                    if j == i.categoria:
                        forn_list.append([i.nome, i.telefone, i.email, i.categoria])

            forn_list.sort(key = lambda x: x[3])

            print('Favor contactar os seguintes fornecedores:\n')
            print(f"{'Fornecedor':<35} | {'Telefone':<15} | " 
                  f"{'Email':<35} | {'Categoria'}")
            
            for i in forn_list:
                print(f'{i[0]:<35} | {i[1]:<15} | {i[2]:<35} | {i[3]}')

            print('\n')

        else:
            print('Não há dados a serem lidos\n')
    
    @classmethod
    def alterar_esto(cls, codigo):
        a = EstoqueDal.ler_esto()

        val_cod = validador_esto(codigo, a, 'a')
        val_lim = False

        max = 1000

        if len(a) != 0:
            if not val_cod:
                novo_nome = input('Alterar nome para: ')
                novo_prec = input('Alterar preço para: ')
                nova_cate = input('Alterar categoria: ')
                nova_quan = input('Alterar quantidade: ')

                val_cat = validador_cat(nova_cate, 'fornecedor', 'a')

                if int(nova_quan) > max:
                    val_lim = True

                if not val_cat and not val_lim:
                    EstoqueDal.limpar_esto()

                    for i in a:
                        if i.produto.codigo == codigo:
                            i.produto.nome = novo_nome
                            i.produto.preco = novo_prec
                            i.produto.categoria = nova_cate
                            i.quantidade = nova_quan
                        
                        EstoqueDal.salvar_esto(
                            Estoque(Produto(
                                i.produto.codigo, i.produto.nome, i.produto.preco, 
                                i.produto.categoria), i.quantidade))

                    print('\nProduto alterado com sucesso\n')
                
                else:
                    print('\nErro - Produto não alterado\n')
                    
                    if val_cat:
                        print('Categoria não consta no banco de dados\n')
                    
                    elif val_lim:
                        print('Quantidade excede limite do estoque\n')

            else:
                print('\nErro - Produto não alterado\n'
                      'Código inválido\n')
            
            input('Pressione ENTER para continuar ')
        
        else:
            print('Não há dados a serem lidos\n')
    
    @classmethod
    def remover_esto(cls, codigo):
        a = EstoqueDal.ler_esto()

        val_cod = validador_esto(codigo, a, 'r')

        if len(a) != 0:
            if not val_cod:
                EstoqueDal.limpar_esto()

                for i in a:
                    if i.produto.codigo != codigo:            
                        EstoqueDal.salvar_esto(
                            Estoque(Produto(
                                i.produto.codigo, i.produto.nome, i.produto.preco, 
                                i.produto.categoria), i.quantidade))
            
                print('\nProduto removido com sucesso\n')
                
            else:
                print('\nErro - Produto não removida\n'
                      'Código inválido\n')
            
            input('Pressione ENTER para continuar ')
        
        else:
            print('Não há dados a serem lidos\n')

class VendasController:


    @classmethod
    def pdv_validador(cls, vendedor, comprador):
        clt_formatado, val_clt, val_func = validador(vendedor, 'funcionario', 'a')
        cpf_formatado, val_cpf, val_clie = validador(comprador, 'cliente', 'a')

        if not val_clt and not val_func and not val_cpf and not val_clie:
            return False

        elif val_clt or val_func:
            print('\nFuncionário não localizado, tente novamente\n')
            input('Pressione ENTER para continuar ')

            return True
        
        elif val_cpf:
            print('\nCPF possui erro, tente novamente\n')
            input('Pressione ENTER para continuar ')
            
            return True
        
        elif val_clie:
            print('\nUsuário não cadastrado')
            input('Pressione ENTER para realizar o cadastro ')

            cpf = input('CPF (somente números): ')
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            endereco = input('Endereço: ')
            email = input('Email: ')

            ClienteController.cadastrar_clie(cpf, nome, telefone, endereco, email)

            return True

    @classmethod
    def pdv_display(cls, vendedor, comprador):
        a = FuncionarioDal.ler_func()
        b = ClienteDal.ler_clie()

        clt_formatado, val_clt, val_func = validador(vendedor, 'funcionario', 'a')
        cpf_formatado, val_cpf, val_clie = validador(comprador, 'cliente', 'a')

        func = list(filter(lambda x: x.clt == clt_formatado, a))
        clie = list(filter(lambda x: x.cpf == cpf_formatado, b))

        print(f'Vendedor(a): {func[0].nome:<50} | Cliente: {clie[0].nome}')

    @classmethod
    def registrar_venda(cls, ccf, vendedor, comprador, codigo, qte_vendida, data):
        a = EstoqueDal.ler_esto()
        b = FuncionarioDal.ler_func()
        c = ClienteDal.ler_clie()

        clt_formatado, val_clt, val_func = validador(vendedor, 'funcionario', 'a')
        cpf_formatado, val_cpf, val_clie = validador(comprador, 'cliente', 'a')
        val_cod = validador_esto(codigo, a, 'a')
 
        func = list(filter(lambda x: x.clt == clt_formatado, b))
        clie = list(filter(lambda x: x.cpf == cpf_formatado, c))

        if len(a) != 0:
            if not val_cod:
                EstoqueDal.limpar_esto()

                for i in a:
                    if i.produto.codigo == codigo:
                        total = float(i.produto.preco) * qte_vendida
                        i.quantidade = int(i.quantidade) - qte_vendida
                        VendaDal.salvar_venda(
                            Venda(ccf, func[0].nome, clie[0].nome, Produto(
                                i.produto.codigo, i.produto.nome, i.produto.preco, 
                                i.produto.categoria), qte_vendida, total, data))
                    
                    EstoqueDal.salvar_esto(
                        Estoque(Produto(
                            i.produto.codigo, i.produto.nome, i.produto.preco, 
                            i.produto.categoria), i.quantidade))
            
            else:
                print('\nCódigo inválido\n')
                input('Pressione ENTER para continuar ')
        else:
            print('Estamos com problemas de estoque aguarde')
    
    @classmethod
    def leitura_venda(cls, ccf, comprador):
        a = VendaDal.ler_venda()
        b = ClienteDal.ler_clie()

        vl_total = 0

        cpf_formatado, val_cpf, val_clie = validador(comprador, 'cliente', 'a')
        
        clie = list(filter(lambda x: x.cpf == cpf_formatado, b))
        
        if len(a) != 0:
            print(f'CCF: {ccf}')

            print(f"{'CNPJ/CPF Consumidor:':<30} {clie[0].cpf}\n"
                  f"{'Nome:':<30} {clie[0].nome}\n"
                  f"{'Endereço:':<30} {clie[0].endereco}\n")
            
            print(f"{'Código':<10} | {'Descrição':<30} | {'Quantidade':>15} | "
                  f"{'VL Unit R$':>20} | {'VL Item R$':>20}")
            
            for i in a:
                if i.ccf == ccf:
                    print(f'{i.item_vendido.codigo:<10} | {i.item_vendido.nome:<30} | {i.qte_vendida:>15} | '
                        f'{i.item_vendido.preco:>20} | {i.total:>20}')
                    vl_total += float(i.total)
            
            print(f"Total R$ {f'{vl_total:.2f}':_>98}\n")
        
        else:
            print('Estamos com problemas de sistema aguarde')

class RelatorioController:


    @classmethod
    def venda_total(cls):
        a = VendaDal.ler_venda()

        acc_tot = 0

        dal_format = "%Y-%m-%d %H:%M:%S.%f"

        if len(a) != 0:
            print(f"{'Data':<10} | {'CCF':<15} | {'Produto':<30} | "
                  f"{'Quantidade Vendida':>20} | {'Total CCF R$':>20}")

            for i in a:
                i.data = dt.datetime.strptime(i.data, dal_format).date()

                print(f'{i.data} | {i.ccf:<15} | {i.item_vendido.nome:<30} | '
                    f'{i.qte_vendida:>20} | {i.total:>20}')
                acc_tot += float(i.total)
            
            print(f"Total R$ {f'{acc_tot:.2f}':_>98}\n")
        
        else:
            print('Estamos com problemas de sistema aguarde')
    
    @classmethod
    def venda_periodo(cls, data_ini, data_fin):      
        a = VendaDal.ler_venda()

        acc_per = 0

        view_format = "%Y-%m-%d"
        dal_format = "%Y-%m-%d %H:%M:%S.%f"

        data_ini = dt.datetime.strptime(data_ini, view_format).date()
        data_fin = dt.datetime.strptime(data_fin, view_format).date()

        if len(a) != 0:
            print(f'Período de análise: {data_ini} à {data_fin}\n')

            print(f"{'Data':<10} | {'CCF':<15} | {'Produto':<30} | "
                  f"{'Quantidade Vendida':>20} | {'Total CCF R$':>20}")

            for i in a:
                i.data = dt.datetime.strptime(i.data, dal_format).date()

                if i.data >= data_ini and i.data <= data_fin:
                    
                    print(f'{i.data} | {i.ccf:<15} | {i.item_vendido.nome:<30} | '
                        f'{i.qte_vendida:>20} | {i.total:>20}')
                    acc_per += float(i.total)
            
            print(f"Total R$ {f'{acc_per:.2f}':_>98}\n")
        
        else:
            print('Estamos com problemas de sistema aguarde')
    
    @classmethod
    def venda_cliente(cls):
        a = VendaDal.ler_venda()

        clie_dict = {}

        if len(a) != 0:
            for i in a:
                chave = i.comprador
                valores = float(i.total)

                if chave in clie_dict:
                    clie_dict[chave] += valores
                else:
                    clie_dict[chave] = valores
            
            clientes = [(k, clie_dict[k]) for k in clie_dict.keys()]
            clientes.sort(key = lambda x: x[1], reverse = True)

            print(f"{'Cliente':<35} | {'Total gasto R$':>20}")

            for i in clientes:
                print(f"{i[0]:<35} | {f'{i[1]:>.2f}':>20}")
            
            print('\n')
        
        else:
            print('Estamos com problemas de sistema aguarde')

    @classmethod
    def venda_produto(cls, top_prod):
        a = VendaDal.ler_venda()
        
        prod_dict = {}

        if len(a) != 0:
            for i in a:
                chave = i.item_vendido.nome
                valores = int(i.qte_vendida)

                if chave in prod_dict:
                    prod_dict[chave] += valores
                else:
                    prod_dict[chave] = valores
            
            produtos = [(k, prod_dict[k]) for k in prod_dict.keys()]
            top_produtos = sorted(produtos, key = lambda x: x[1], reverse = True)[:top_prod]

            print(f'Top {top_prod} produtos mais vendidos\n')
            print(f"{'Produto':<40} | {'Total vendido Un':>20}")

            for i in top_produtos:
                print(f"{i[0]:<40} | {i[1]:>20}")
            
            print('\n')

        else:
            print('Estamos com problemas de sistema aguarde')