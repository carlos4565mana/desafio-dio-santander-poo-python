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
  print("🏦 Bem-vindo ao Sistema Bancário POO!")
  while True:
    opcao = input(menu()).strip()


if __name__ == "__main__":
    main()
