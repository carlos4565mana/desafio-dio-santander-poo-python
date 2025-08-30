import re
from classes import PessoaFisica, ContaCorrente


def validar_cpf(cpf):
  cpf_numeros = re.sub(r'\D', '', cpf)
  if len(cpf_numeros) != 11:
    return False
  if cpf_numeros == cpf_numeros[0] * 11:
    return False
  return True
def formatar_cpf(cpf):
  cpf_limpo = re.sub(r'\D', '', cpf)
  if len(cpf_limpo) == 11:
    return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
  return cpf
def filtrar_cliente(cpf,clientes):
  cpf_limpo = re.sub(r'\D', '', cpf)
  clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf_limpo]
  return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
  if not cliente.contas:
    print("\n⚠️ Cliente não possui conta!")
    return None
    
  # Retorna a primeira conta do cliente (pode ser expandido para escolher)
  return cliente.contas[0]
def obter_dados_cliente():
    nome = input("Informe o nome completo: ").strip()
    
    while True:
        cpf = input("Informe o CPF (somente números): ").strip()
        if validar_cpf(cpf):
            cpf = re.sub(r'\D', '', cpf)  # Remove formatação
            break
        else:
            print("⚠️ CPF inválido! Digite novamente.")
    
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço completo: ").strip()
    
    return {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }

def obter_valor_operacao(operacao):
  while True:
    try:
      valor = float(input(f"Informe o valor do {operacao}: R$ "))
      if valor <= 0:
        print("⚠️ O valor deve ser positivo!")
        continue
      return valor
    except ValueError:
      print("⚠️ Valor inválido! Digite um número.")
def listar_contas(contas):
  if not contas:
    print("\n⚠️ Nenhuma conta cadastrada.")
    return
  print("\n" + "=" * 50)
  print("           CONTAS CADASTRADAS")
  print("=" * 50)
  for conta in contas:
    print(f"""
    Agencia:{conta.agencia}
    Conta:{conta.numero}
    Titular: {conta.cliente.nome}
    CPF: {formatar_cpf(conta.cliente.cpf)}
    Saldo: R$ {conta.saldo:.2f}
    {"-" * 30}""")

