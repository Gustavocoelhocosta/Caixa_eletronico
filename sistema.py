# uma classe chamada Caixa_eletronico, que contém um dicionário onde as chaves são os valores das notas e o valores as quantidades de cada nota
class Caixa_eletronico:
    def __init__(self):
        self.__notas_armazenadas = {100:0, 50:0, 20:0, 10:0}

    def notas_armazenadas(self):
        return self.__notas_armazenadas

    # Registra o abastecimento, tem como parâmetros o Valor da Nota(inteiro), e a quantidade de notas(inteiro)
    def registrar_abastecimento(self, nota:int, quantidade:int):
        if nota in self.notas_armazenadas() and isinstance(quantidade, int): #verifica se o valor da nota é um valor previamente cadastrado, e se a quantidade de notas é um inteiro
            self.notas_armazenadas()[nota] += quantidade
        else:
            print("parâmetros não aprovados")

    # mostra a quantidade de cada nota, e o saldo total do caixa.
    def mostrar_saldo(self):
        saldo = 0
        for valor_nota in self.notas_armazenadas():
            saldo += valor_nota * self.notas_armazenadas()[valor_nota]
            print(f"notas de R${valor_nota} - {self.notas_armazenadas()[valor_nota]}")
        print(f"saldo total igual a {saldo}")

    # Aprova ou rejeita o saque, tem como parâmetro o valor solicitado do saque, caso aprova retorna o boleano True, juntamente com um dicionário com as notas(chave do dicionário) e as quantidades de cada nota (valores do dicionário), caso o saque seja rejeitado, retorna o boleano False e None.
    def aprovar_saque(self, valor_saque_solicitado:int):
        valor_saque_inicial = valor_saque_solicitado
        notas_saque = {}
        if isinstance(valor_saque_solicitado, int) and valor_saque_solicitado > 0: #verifica se o valor do saque é maior que zero e do tipo inteiro.
            valor_saque_subtotal = valor_saque_inicial
            for valor_nota in self.notas_armazenadas():
                notas_solicitadas =  int(valor_saque_subtotal / valor_nota)
                if notas_solicitadas <= self.notas_armazenadas()[valor_nota]:
                    notas_aprovadas = notas_solicitadas
                else:
                    notas_aprovadas = self.notas_armazenadas()[valor_nota]
                valor_saque_subtotal -= notas_aprovadas * valor_nota
                notas_saque[valor_nota] = notas_aprovadas

            if valor_saque_subtotal == 0:
                for valor_nota in notas_saque:
                    self.notas_armazenadas()[valor_nota] -= notas_saque[valor_nota]
                return True, notas_saque

        else:
            return False, None
