from exceptions import SaldoInsuficienteError
from pprint import pprint
from leitor import LeitorDeArquivo

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

cliente = Cliente('Larissa Itimura', '123.456.789-00', 'Desenvolvedora')
print(cliente.nome)
print(cliente.cpf)
print(cliente.profissao)

print(cliente.__dict__)

pprint(cliente.__dict__, width=40)

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.__agencia = 0
        self.saques_nao_permitidos = 0
        self.transferencias_nao_permitidas = 0
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        self.__numero = numero
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    # @agencia.setter
    # def agencia(self, value):
    #     if not isinstance(value, int):
    #         return
    #     if value <= 0:
    #         print("O atributo agência deve ser maior que zero")
    #         return
        
    #     self.__agencia = value

    def __set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo agencia deve ser um inteiro", value)
        if value <= 0:
            raise ValueError("O atributo agencia deve ser maior que zero")
        
        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo numero deve ser um inteiro")
        if value <= 0:
            raise ValueError("O atributo numero deve ser maior que zero")

        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo saldo deve ser um inteiro")

        self.__saldo = value

    def transferir(self, valor, favorecido):
        if valor < 0:
            raise ValueError("O valor a ser sacado não pode ser menor que zero")
        try: 
            self.sacar(valor)
        except SaldoInsuficienteError as E:
            import traceback
            self.transferencias_nao_permitidas += 1
            traceback.print_exc()
            raise E
        favorecido.depositar(valor)

    def sacar(self, valor):
        if valor < 0:
            raise ValueError("O valor a ser sacado não pode ser menor que zero")
        if self.saldo < valor:
            self.saques_nao_permitidos += 1
            raise SaldoInsuficienteError(saldo=self.saldo, valor=valor)
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

# conta_corrente = ContaCorrente(None, 100, 22500)
# print(conta_corrente._ContaCorrente__agencia)

def main():
    import sys

    contas = []
    
    while True:
        try:
            nome = input('Nome do cliente:\n')
            agencia = input('Numero da agencia:\n')
            # breakpoint()
            numero = input('Numero da conta corrente:\n')
            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append(conta_corrente)
        except ValueError as E:
            print(E.args)
            sys.exit()
        except KeyboardInterrupt:
            print(f'\n\n{len(contas)}(s) contas criadas')
            sys.exit()

# if __name__ == '__main__':
#     main()

# conta_corrente = ContaCorrente(None, 400, 1234567)
# conta_corrente.depositar(50)
# conta_corrente.sacar(250)
# print('Saldo: ', conta_corrente.saldo)

# conta_corrente1 = ContaCorrente(None, 400, 1234567)
# conta_corrente2 = ContaCorrente(None, 401, 1234568)
# conta_corrente1.transferir(100, conta_corrente2)
# print('ContaCorrente1 Saldo: ', conta_corrente1.saldo)
# print('ContaCorrente2 Saldo: ', conta_corrente2.saldo)

try:
    leitor = LeitorDeArquivo("arquivo.txt")
    leitor.ler_proxima_linha()
    leitor.ler_proxima_linha()
    leitor.ler_proxima_linha()
except IOError:
    print("Exceção do tipo IOError capturada e tratada.")
finally:
    if 'leitor' in locals():
        leitor.fechar()

# funciona como o de cima por causa do enter e exit do leitor.py
while LeitorDeArquivo("arquivo.txt") as leitor:
    leitor.ler_proxima_linha()

