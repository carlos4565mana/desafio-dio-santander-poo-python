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
