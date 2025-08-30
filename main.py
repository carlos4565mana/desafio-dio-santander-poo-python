def menu():
  """Exibe o menu principal do sistema"""
  return """
  ╔══════════════════════════════════════╗
  ║       BANCO  TABAJARA -  POO         ║
  ╠══════════════════════════════════════╣
  ║  [1] Depositar                       ║
  ║  [2] Sacar                           ║
  ║  [3] Extrato                         ║
  ║  [4] Novo cliente                    ║
  ║  [5] Nova conta                      ║
  ║  [6] Listar contas                   ║
  ║  [7] Listar clientes                 ║
  ║  [0] Sair                            ║
  ╚══════════════════════════════════════╝

  => """

def main():
  """Função principal do sistema"""
  clientes = []
  contas = []

  print("🏦 Bem-vindo ao Sistema Bancário POO!")
  while True:
    opcao = input(menu()).strip()
    match opcao:
      case "1":
        depositar(clientes)
      case "2":
        sacar(clientes)

      case "3":
        exibir_extrato(clientes)
      
      case "4":
        criar_cliente(clientes)

      case "5":
        numero_conta = len(contas) + 1
        criar_conta(numero_conta, clientes, contas)

      case "6":
        listar_contas(contas)

      case "7":
        listar_clientes(clientes)

      case "0":
        print("\n👋 Obrigado por usar o Banco TABAJARA!")
        print("🫡 Sistema encerrado com sucesso!")
        break
      
      case _:
        print("\n⚠️ Operação inválida! Tente novamente.")

if __name__ == "__main__":
    main()
