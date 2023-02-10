endereco = "Rua do Cebola, nº 2, Bairro do Limoeiro, Rio de Janeiro, RJ, 23440-120"

import re # Regular Expression (RegEx)

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)