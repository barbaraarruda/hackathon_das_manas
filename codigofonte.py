# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 09:27:07 2021

@author: barbara
barbarahmiley@gmail.com

"""
import sys

print("Iniciando...")
print("_______________________________________________")
print("GAROTAS COMO EU")
print()
print("Esse programa foi desenvolvido com caráter informacional\ncujo objetivo principal é levar informação sobre assédio\ne como existem medidas de profilaxia e auxílio às potenciais vítimas.\t ")
print("Pode ser utilizado em caráter educacional.\nIndicado para todxs as pessoas que se identificam como mulheres. ")
print()

sexousuario = "F"
leitura = input("Digite a letra correspondente ao sexo que você se identifica,\n'F' para feminino e 'M' para masculino: ")
print()
if (leitura == sexousuario):
    print("Ok, você pode continuar.")
    pass
else:
    print("Sinto muito, você não pode continuar. Encerrando o programa.")
    raise SystemExit()
        
print()
print("_________________________________________________")
print("Vamos começar!")

senha = "859632"
leitura2 =" "
while (leitura2 != senha):
    leitura2 = input("Digite a senha: ")
    if leitura2 == senha :
        print("Acesso liberado")
        pass
    else:
        print("Senha incorreta. Tente novamente.")
      
print()
print("_________________________________________________")
print("\tVamos agora bater um papo sobre consentimento:")
print()
print("Após ler a documentação presente no site e no readme.txt,\nvocê tem ciência de que este programa é utilizado para\nfins educacionais e de pesquisa. Em nenhum momento é solicitado dados pessoais\nPortanto, você é uma participante anônima, e a sua participação não implicará em\nnenhum tipo de penalidade ou que poderá induzir você a tomar uma decisão.")
print("É um ambiente totalmente seguro. Recomenda-se que menores de 18 anos tenham a supervisão de um adulto ou seu responsável para prosseguir.\nNão comercialize esse código sem prévia autorização do Girls Like Me.")
print()

aceite = int(input("Digite '1' caso você concorde e '2' caso você não concorde: "))
if (aceite == 1):
    pass
else:
    print("Sinto muito, você não pode continuar. Encerrando o programa.")
    raise SystemExit()


print()
print("_________________________________________________")
sys.exit(2)
