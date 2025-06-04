import random
class Produto:
    def __init__(self, codigo, nome, categoria, preco, quantidadeEstoque):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidadeEstoque = quantidadeEstoque

    def get_codigo(self):
        print("Código do produto:", produto1.get_codigo())
        return self.codigo

    def get_nome(self):
        print("Nome do produto:", produto1.get_nome())
        return self.nome

    def get_categoria(self):
        print("Categoria do produto:", produto1.get_categoria())
        return self.categoria

    def get_preco(self):
        print("Preço do produto:", produto1.get_preco())
        return self.preco

    def get_quantidade_estoque(self):
        print("Quantidade em estoque:", produto1.get_quantidade_estoque())
        return self.quantidadeEstoque

    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.preco = novo_preco
            print(f'O novo preco é {novo_preco}')
        else:
            print("Erro: O preço deve ser um valor não negativo.")

    def vender(self, quantidade_vendida):
        if quantidade_vendida <= self.quantidadeEstoque and quantidade_vendida > 0:
            self.quantidadeEstoque -= quantidade_vendida
            total_venda = quantidade_vendida * self.preco
            print(f'Venda realizada:')
            print(f'Nome: {self.nome}')
            print(f'Categoria: {self.categoria}')
            print(f'Quantidade vendida: {quantidade_vendida}')
            print(f'Preço unitário: {self.preco:.2f}')
            print(f'Total da venda: {total_venda:.2f}')
            print("Quantidade em estoque após a venda:", produto1.get_quantidade_estoque())
        elif quantidade_vendida <= 0:
            print("Erro: A quantidade vendida deve ser maior que zero.")
        else:
            print("Erro: Quantidade em estoque insuficiente para realizar a venda.")

    def comprar(self, quantidade_comprada):
        if quantidade_comprada > 0:
            self.quantidadeEstoque += quantidade_comprada
            print(f'Compra realizada: {quantidade_comprada} unidades adicionadas ao estoque.')
        else:
            print("Erro: A quantidade comprada deve ser maior que zero.")

produto1 = Produto(1, "Camisa", "Vestuário", 79.90, 75)
produto1.set_preco(85.50)
produto1.vender(20)
produto1.vender(60)
produto1.comprar(50)