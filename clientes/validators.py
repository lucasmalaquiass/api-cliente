import re
from validate_docbr import CPF

def cpf_valido(num_cpf):
    cpf = CPF()
    return cpf.validate(num_cpf)
     
def nome_valido(nome):
   return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta
    