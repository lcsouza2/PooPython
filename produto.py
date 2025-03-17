class Produto:
    def __init__(self, codigo, nome, descricao, categoria, preco, estoque, perecivel):

        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("Codigo Inválido!")
        
        if not isinstance(nome, str) or len(nome) < 2:
            raise ValueError("Nome Inválido!")
        
        if not isinstance(descricao, str):
            raise ValueError("Descrição Inválida!")
        
        if not isinstance(categoria, str) or categoria not in ["Frutas", "Eletrônicos", "Roupas", "Bebidas"]:
            raise ValueError("Categoria Inválida!")
        
        if not isinstance(preco, float) or preco <= 0:
            raise ValueError("Preço Inválido!")
        
        if not isinstance(estoque, int) or estoque < 0:
            raise ValueError("Estoque Inválido!")

        if not isinstance(perecivel, int) or perecivel not in [0, 1]:
            raise ValueError("Perecível Inválido")

        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque
        self.perecivel = perecivel

    def reajustar_preco(self, percentual):
        if percentual >= 0:
            raise ValueError("Valor Percentual Inválido")            
        self.preco = self.preco * (1 + percentual / 100)