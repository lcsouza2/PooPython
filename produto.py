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

        self.set_codigo(codigo)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.set_categoria(categoria)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_perecivel(perecivel)

    def reajustar_preco(self, percentual):
        if percentual >= 0:
            raise ValueError("Valor Percentual Inválido")            
        self.__preco = self.__preco * (1 + percentual / 100)


    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self, codigo):
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("Codigo Inválido!")
        self.__codigo = codigo

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if not isinstance(nome, str) or len(nome) < 2:
            raise ValueError("Nome Inválido!")
        self.__nome = nome

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        if not isinstance(descricao, str):
            raise ValueError("Descrição Inválida!")
        self.__descricao = descricao

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        if not isinstance(categoria, str) or categoria not in ["Frutas", "Eletrônicos", "Roupas", "Bebidas"]:
            raise ValueError("Categoria Inválida!")
        self.__categoria = categoria

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if not isinstance(preco, float) or preco <= 0:
            raise ValueError("Preço Inválido!")
        self.__preco = preco

    def get_estoque(self):
        return self.__estoque

    def set_estoque(self, estoque):
        if not isinstance(estoque, int) or estoque < 0:
            raise ValueError("Estoque Inválido!")
        self.__estoque = estoque

    def get_perecivel(self):
        return self.__perecivel

    def set_perecivel(self, perecivel):
        if not isinstance(perecivel, int) or perecivel not in [0, 1]:
            raise ValueError("Perecível Inválido")
        self.__perecivel = perecivel
