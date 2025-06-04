produtos: [str] = []
precos: [float] = []
estoque: [int] = []
quantidades: [int] = []

def menu():
    print()
    print('\033[0;33m--- Gerenciamento de Estoque e Vendas ---\n')
    print('\033[0;34m[\033[0;33m 1 \033[0;34m] \033[0;34m Incluir Produto')
    print('\033[0;34m[ 2 ] Incluir Venda')
    print('\033[0;34m[ 3 ] Relatório de Estoque')
    print('\033[0;34m[ 4 ] Relatório de Vendas')
    print('\033[0;34m[ 5 ] Produto Mais Vendidos')
    print('\033[0;34m[ 6 ] Média de Vendas')
    print('\033[0;34m[ 7 ] Sair \n')


def incluirproduto():
 while True:
    prod = str(input('Digite o nome do seu produto: '))
    produtos.append(prod.lower())
    preco = float(input('Digite o valor do seu produto: R$'))
    precos.append(preco)
    estoq = int(input('Digite quanto de estoque voce tem desse produto: '))
    estoque.append(estoq)
    quantidades.append(0)
    sim_nao = str(input("Você deseja cadastrar outro produto (sim/não)? "))
    print()
    if sim_nao == "nao":
        break



def estoque_menu():
    print('Relatórios de estoque:\n')
    print(f'{'produtos':<13}', end='')
    print(f'{'preços':^3}', end='')
    print(f'{'estoque':>12}')
    print('________     ______     _______\n')
    for i in range(len(produtos)):
        print(f'{produtos[i]:<13}', end='')
        print(f'{precos[i]:^3}', end='')
        print(f'{estoque[i]:^18}')
    print()

def venda_menu():
    print('Relatórios de vendas:\n')
    print(f'{'produtos':<13}', end='')
    print(f'{'quantidade de vendas':^3}', end='')
    print(f'{'valor':>12}')
    print('________     ____________________      ______\n')
    for i in range(len(produtos)):
        print(f'{produtos[i]:<13}', end='')
        print(f'{quantidades[i]:^3}', end='')
        print(f'{precos[i]:^18}')
    print()


def mais_vendido():
    print('O PRODUO MAIS VENDIDO FOI:\n')
    print(f'{'produtos':<13}', end='')
    print(f'{'quantidade de vendas':^3}', end='')
    print('________     ____________________\n')

    produ_maior = quantidades.index(max(quantidades))
    nome = produtos[produ_maior]

    print(f'{produtos[produ_maior]:<13} ', end='')
    print(f'{max(quantidades):^3}')

    print()




while True:
    while True:
        try:
            menu()
            opcao = int(input('\033[0;0mEscolha a sua opção: '))
            print()
            break
        except:
            print('DIGITE SOMENTE NUMEROS DE 1 A 7')
        break
    if opcao == 7:
        break
    elif opcao == 1:
        incluirproduto()
    elif opcao == 2:
            try:
                escolha = str(input('Selecione o nome do produto que deseja registrar a venda: '))
                escolhasa.append(escolha)
                if escolha.lower() in produtos:
                    indice_produto = produtos.index(escolha.lower())
                    venda = int(input('Digite quantos itens foram vendidos: '))
                    quantidades.insert(indice_produto, venda)
                    venda_calc = estoque[indice_produto] - venda
                    if venda_calc < 0:
                        venda_calc = 0
                        estoque[indice_produto] = venda_calc
                    else:
                        estoque[indice_produto] = venda_calc
                    print(produtos)
                    print(estoque)
                    print(quantidades)
                    print(precos)
            except:
                print('DIGITE PRODUTOS QUE ESTÃO NA LISTA')
    elif opcao == 3:
        estoque_menu()
    elif opcao == 4:
        venda_menu()
    elif opcao == 5:
        mais_vendido()



print('fim')