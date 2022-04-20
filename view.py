from controller import CategoriaController, ClienteController, EstoqueController
from controller import FornecedorController, FuncionarioController, RelatorioController, VendasController
import datetime as dt
import os


def limpar_tela():
    os.system('cls')

limpar_tela()

while True:
    menu_main = int(input('Mercearia do Tio Caio\n'
                         f"{'1 - Administrativo':<25}"
                         f"{'2 - Financeiro':<25}"
                         f"{'3 - Caixa':<25}"
                          '4 - Desligar\n'
                          'Sua opção: '))
    limpar_tela()

    if menu_main == 1:
        while True:
            menu_adm = int(input('Recursos Administrativos\n'
                                f"{'1 - Categoria':<20}"
                                f"{'2 - Estoque':<20}"
                                 '3 - Fornecedores\n'
                                f"{'4 - Funcionários':<20}"
                                f"{'5 - Clientes':<20}"
                                 '6 - Retornar ao menu anterior\n'
                                 'Sua opção: '))
            limpar_tela()

            if menu_adm == 1:
                while True:
                    menu_cate = int(input('Área de Categorias:\n'
                                         f"{'1 - Cadastrar nova categoria':<40}"
                                         f"{'2 - Visualizar todos os registros':<40}"
                                          '3 - Retornar ao menu anterior\n'
                                          'Sua opção: '))
                    limpar_tela()

                    if menu_cate == 1:
                        print('Forneça os seguintes dados:\n')
                        codigo = input('Código: ')
                        categoria = input('Categoria: ')

                        CategoriaController.cadastrar_cate(codigo, categoria)
                        limpar_tela()

                    elif menu_cate == 2:
                        while True:
                            CategoriaController.leitura_cate()
                            
                            sub_cate = int(input('Você gostaria de:\n'
                                                f"{'1 - Alterar um registro':<30}"
                                                f"{'2 - Remover um registro':<30}"
                                                 '3 - Retornar ao menu anterior\n'
                                                'Sua opção: '))

                            if sub_cate == 1:
                                codigo = input('Forneça o código: ')
                                
                                CategoriaController.alterar_cate(codigo)
                                limpar_tela()
                            
                            elif sub_cate == 2:
                                codigo = input('Forneça o código: ')
                                
                                CategoriaController.remover_cate(codigo)
                                limpar_tela()
                            
                            elif sub_cate == 3:
                                limpar_tela()
                                break
                    
                    elif menu_cate == 3:
                        limpar_tela()
                        break

            elif menu_adm == 2:
                while True:
                    menu_esto = int(input('Área de Estocagem:\n'
                                         f"{'1 - Cadastrar novo produto no estoque':<40}"
                                         f"{'2 - Visualizar todos os registros':<40}"
                                          '3 - Retornar ao menu anterior\n'
                                          'Sua opção: '))
                    limpar_tela()

                    if menu_esto == 1:
                        print('Forneça os seguintes dados:\n')
                        codigo = input('Código: ')
                        nome = input('Nome: ')
                        preco = input('Preco: ')
                        categoria = input('Categoria: ')
                        quantidade = input('Quantidade: ')
                        
                        EstoqueController.cadastrar_esto(codigo, nome, preco, categoria, quantidade)
                        limpar_tela()

                    elif menu_esto == 2:
                        while True:
                            EstoqueController.leitura_esto()
                            
                            sub_esto = int(input('Você gostaria de:\n'
                                                f"{'1 - Alterar um registro':<30}"
                                                f"{'2 - Remover um registro':<30}"
                                                 '3 - Retornar ao menu anterior\n'
                                                 'Sua opção: '))

                            if sub_esto == 1:
                                codigo = input('Forneça o código: ')
                                
                                EstoqueController.alterar_esto(codigo)
                                limpar_tela()
                            
                            elif sub_esto == 2:
                                codigo = input('Forneça o código: ')
                                
                                EstoqueController.remover_esto(codigo)
                                limpar_tela()
                            
                            elif sub_esto == 3:
                                limpar_tela()
                                break
                    
                    elif menu_esto == 3:
                        limpar_tela()
                        break

            elif menu_adm == 3:
                while True:
                    menu_forn = int(input('Área de Fornecedores:\n'
                                         f"{'1 - Cadastrar novo fornecedor':<40}"
                                         f"{'2 - Visualizar todos os registros':<40}"
                                          '3 - Retornar ao menu anterior\n'
                                          'Sua opção: '))
                    limpar_tela()

                    if menu_forn == 1:
                        print('Forneça os seguintes dados:\n')
                        cnpj = input('CNPJ (apenas números): ')
                        nome = input('Nome completo: ')
                        telefone = input('Telefone: ')
                        endereco = input('Endereço: ')
                        email = input('Email: ')
                        categoria = input('Categoria: ')

                        FornecedorController.cadastrar_forn(cnpj, nome, telefone, endereco, email, categoria)
                        limpar_tela()

                    elif menu_forn == 2:
                        while True:
                            FornecedorController.leitura_forn()
                            
                            sub_forn = int(input('Você gostaria de:\n'
                                                f"{'1 - Alterar um registro':<30}"
                                                f"{'2 - Remover um registro':<30}"
                                                 '3 - Retornar ao menu anterior\n'
                                                 'Sua opção: '))

                            if sub_forn == 1:
                                cnpj = input('Forneça o CNPJ (apenas números): ')
                                
                                FornecedorController.alterar_forn(cnpj)
                                limpar_tela()
                            
                            elif sub_forn == 2:
                                cnpj = input('Forneça o CNPJ (apenas números): ')
                                
                                FornecedorController.remover_forn(cnpj)
                                limpar_tela()
                            
                            elif sub_forn == 3:
                                limpar_tela()
                                break
                    
                    elif menu_forn == 3:
                        limpar_tela()
                        break

            elif menu_adm == 4:
                while True:
                    menu_func = int(input('Área de Funcionários:\n'
                                         f"{'1 - Cadastrar novo funcionário':<40}"
                                         f"{'2 - Visualizar todos os registros':<40}"
                                          '3 - Retornar ao menu anterior\n'
                                          'Sua opção: '))
                    limpar_tela()

                    if menu_func == 1:
                        print('Forneça os seguintes dados:\n')
                        clt = input('CLT (apenas números): ')
                        nome = input('Nome completo: ')
                        telefone = input('Telefone: ')
                        endereco = input('Endereço: ')
                        email = input('Email: ')

                        FuncionarioController.cadastrar_func(clt, nome, telefone, endereco, email)
                        limpar_tela()

                    elif menu_func == 2:
                        while True:
                            FuncionarioController.leitura_func()
                            
                            sub_func = int(input('Você gostaria de:\n'
                                                f"{'1 - Alterar um registro':<30}"
                                                f"{'2 - Remover um registro':<30}"
                                                 '3 - Retornar ao menu anterior\n'
                                                 'Sua opção: '))

                            if sub_func == 1:
                                clt = input('Forneça o CLT (apenas números): ')
                                
                                FuncionarioController.alterar_func(clt)
                                limpar_tela()
                            
                            elif sub_func == 2:
                                clt = input('Forneça o CLT (apenas números): ')
                                
                                FuncionarioController.remover_func(clt)
                                limpar_tela()
                            
                            elif sub_func == 3:
                                limpar_tela()
                                break
                    
                    elif menu_func == 3:
                        limpar_tela()
                        break

            elif menu_adm == 5:
                while True:
                    menu_clie = int(input('Área de Clientes:\n'
                                         f"{'1 - Cadastrar novo cliente':<40}"
                                         f"{'2 - Visualizar todos os registros':<40}"
                                          '3 - Retornar ao menu anterior\n'
                                          'Sua opção: '))
                    limpar_tela()

                    if menu_clie == 1:
                        print('Forneça os seguintes dados:\n')
                        cpf = input('CPF (apenas números): ')
                        nome = input('Nome completo: ')
                        telefone = input('Telefone: ')
                        endereco = input('Endereço: ')
                        email = input('Email: ')

                        ClienteController.cadastrar_clie(cpf, nome, telefone, endereco, email)
                        limpar_tela()

                    elif menu_clie == 2:
                        while True:
                            ClienteController.leitura_clie()
                            
                            sub_clie = int(input('Você gostaria de:\n'
                                                f"{'1 - Alterar um registro':<30}"
                                                f"{'2 - Remover um registro':<30}"
                                                 '3 - Retornar ao menu anterior\n'
                                                 'Sua opção: '))

                            if sub_clie == 1:
                                cpf = input('Forneça o CPF (apenas números): ')
                                
                                ClienteController.alterar_clie(cpf)
                                limpar_tela()
                            
                            elif sub_clie == 2:
                                cpf = input('Forneça o CPF (apenas números): ')
                                
                                ClienteController.remover_clie(cpf)
                                limpar_tela()
                            
                            elif sub_clie == 3:
                                limpar_tela()
                                break
                    
                    elif menu_clie == 3:
                        limpar_tela()
                        break

            elif menu_adm == 6:
                limpar_tela()
                break

    elif menu_main == 2:
        while True:
            menu_fin = int(input('Recursos financeiros\n'
                                f"{'1 - Relatório total de vendas':<35}"
                                 '2 - Relatório por período\n'
                                f"{'3 - Produtos mais vendidos':<35}"
                                 '4 - Histórico de clientes\n'
                                 '5 - Retornar ao menu anterior\n'
                                 'Sua opção: '))
            limpar_tela()

            if menu_fin == 1:
                while True:
                    print('Relatório completo de vendas\n')

                    RelatorioController.venda_total()

                    cont = int(input('Deseja retornar?\n'
                                     '1 - Sim\n'
                                     'Sua opção: '))
                    
                    if cont == 1:
                        limpar_tela()
                        break

            elif menu_fin == 2:
                while True:
                    print('Informe as datas no formato ano-mês-dia | Exemplo: 2022-4-16\n')
                    data_ini = input('Data inicial: ')
                    data_fin = input('Data final: ')

                    limpar_tela()

                    RelatorioController.venda_periodo(data_ini, data_fin)

                    novo_rpp = int(input('Deseja verificar outro período?\n'
                                        f"{'1 - Sim':<15}"
                                         '2 - Não\n'
                                         'Sua opção: '))
                    
                    if novo_rpp == 1:
                        limpar_tela()
                        continue

                    elif novo_rpp == 2:
                        limpar_tela()
                        break

            elif menu_fin == 3:
                while True:
                    print('Histórico de produtos vendidos\n')
                    top_prod = int(input('Visualizar quantos produtos: '))

                    limpar_tela()

                    RelatorioController.venda_produto(top_prod)

                    cont_prod = int(input('Deseja visualizar mais produtos?\n'
                                         f"{'1 - Sim':<15}"
                                          '2 - Não\n'
                                          'Sua opção: '))
                    
                    if cont_prod == 1:
                        limpar_tela()
                        continue

                    elif cont_prod == 2:
                        limpar_tela()
                        break

            elif menu_fin == 4:
                while True:
                    print('Histórico de valores gastos\n')

                    RelatorioController.venda_cliente()

                    cont_clie = int(input('Retornar?\n'
                                          '1 - Sim\n'
                                          'Sua opção: '))
                    
                    if cont_clie == 1:
                        limpar_tela()
                        break

            elif menu_fin == 5:
                limpar_tela()
                break
    
    elif menu_main == 3:
        while True:
            ccf = str(round(dt.datetime.now().timestamp()))

            while True:
                vendedor = input('Informe seu ID: ')
                comprador = input('Informe CPF do cliente: ')
                val = VendasController.pdv_validador(vendedor, comprador)

                limpar_tela()

                if val == False:
                    break
                
            while True:
                VendasController.pdv_display(vendedor, comprador)
                print('Registre as compras | Para encerrar o processo digite -999\n')
                codigo = input('Código do produto: ')

                if codigo == '-999':
                    limpar_tela()
                    break

                qte_vendida = int(input('Quantidade: '))
                data = dt.datetime.now()
                VendasController.registrar_venda(ccf, vendedor, comprador, codigo, qte_vendida, data)

                limpar_tela()
                    
            VendasController.leitura_venda(ccf, comprador)

            novo_reg = int(input('Deseja registrar outra compra?\n'
                                f"{'1 - Sim':<15}"
                                 '2 - Não\n'
                                 'Sua opção: '))
                    
            if novo_reg == 1:
                limpar_tela()
                continue

            elif novo_reg == 2:
                limpar_tela()
                break

    elif menu_main == 4:
        break

    