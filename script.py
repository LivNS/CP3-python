

# contas a pagar

def cadastrar_conta_pagar():
    fornecedor = input("Nome do fornecedor: ")
    cnpj = input("CNPJ: ")
    descricao = input("Descrição: ")
    num_nf = input("Número da NF: ")
    valor = float(input("Valor: "))
    pago = input("Está pago?  ")
    conta_pagar = {'fornecedor': fornecedor, 'cnpj': cnpj, 'descricao': descricao, 'num_nf': num_nf, 'valor': valor, 'pago': pago}
    contas_pagar.append(conta_pagar)

# cadastrar contas p receber
def cadastrar_conta_receber():
    consumidor = input("Nome do consumidor: ")
    cpf = input("CPF: ")
    descricao = input("Descrição: ")
    num_nf = input("Número da NF: ")
    valor = float(input("Valor: "))

# receber lista
    conta_receber = {'consumidor': consumidor, 'cpf': cpf, 'descricao': descricao, 'num_nf': num_nf, 'valor': valor}
    contas_receber.append(conta_receber)

# valor total das contas a pagar
def calcular_total_pagar():
    total_pagar = sum(conta['valor'] for conta in contas_pagar)
    print("Total a pagar:", total_pagar)

# valor total das contas a receber
def calcular_total_receber():
    total_receber = sum(conta['valor'] for conta in contas_receber)
    print("Total a receber:", total_receber)

# saldo geral
def calcular_saldo_geral():
    total_pagar = sum(conta['valor'] for conta in contas_pagar)
    total_receber = sum(conta['valor'] for conta in contas_receber)
    saldo_geral = total_receber - total_pagar
    print("Saldo Geral:", saldo_geral)

contas_pagar = []
contas_receber = []

# menu
while True:
    print("=== MENU ===")
    print("1. Cadastrar conta a pagar")
    print("2. Cadastrar conta a receber")
    print("3. Calcular total a pagar")
    print("4. Calcular total a receber")
    print("5. Calcular saldo geral")
    print("6. Sair")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            cadastrar_conta_pagar()
        case 2:
            cadastrar_conta_receber()
        case 3:
            calcular_total_pagar()
        case 4:
            calcular_total_receber()
