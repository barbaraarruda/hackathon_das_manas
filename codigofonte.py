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

def menu():
    print("\tMENU\n\t[1] - Teste de assédio moral;\n\t[2] - Teste de assédio sexual;\n\t[3] - Simulador matemático;\n\t[4] - Contatos úteis;\n\t[5] - Encerrar programa.")
    escolha_menu = int(input("Digite o número da opção escolhida: "))
    return escolha_menu

print()
print()
print("_________________________________________________")

escolha_menu = menu()

#inicia-se o teste de assédio moral aqui, de acordo com as formas mais comuns observadas sobre assédio.
if (escolha_menu == 1):
    print()
    print("\tInicia-se aqui o teste de assédio moral")
    print()
    print("Instruções:\nDigite '1' para SIM e '2' para NÃO.")
    qupam = int(input("1.A pessoa pega algo pertencente a você sem a sua autorização? ")) #não é assédio moral, é outra prática criminosa
    qusam = int(input("2.A pessoa realiza agressões verbais e/ou te xinga no trabalho? "))
    qutam = int(input("3.Seu/sua superior lhe aplica punições absurdas ou sem motivo aparente? "))
    quqam = int(input("4.Você já recebeu uma carta anônima com duplo sentido? ")) #não é assédio moral, é stalking
    qunam = int(input("5.Você já sofreu ameaças e caso tomasse providências legais, seria demitida ou punida? "))
    quxam = int(input("6.Alguém já colocou em dúvida/desmereceu a sua prática profissional/suas conquistas (com tom de ofensa)? "))
    
    print()
    print("\t RESULTADO:")
    print()
    print("As questões 1 e 4 não são consideradas assédio moral, apesar de serem condutas ilegais.")
    print()
    if (qusam == 1):
        print("Você marcou SIM na questão 2. Agredir verbalmente, xingar, denegrir a sua imagem é assédio moral e é crime previsto no Código Penal Brasileiro.")
    print()
    if (qutam == 1):
        print("Você marcou SIM na questão 3. Aplicar punições severas ou aplicar punições sem nenhum motivo aparente é assédio moral e é crime previsto no Código Penal Brasileiro.")
    print()
    if (qunam == 1):
        print("Você marcou SIM na questão 5. Sofrer ameaças e ser impedida de buscar ajuda legal, com chantagem, seja ela emocional ou financeira é assédio moral e é crime previsto no Código Penal Brasileiro.")
    print()
    if (quxam == 1):
        print("Você marcou SIM na questão 6. Desmerecer, diminuir, duvidar, de forma ofensiva, práticas profissionais ou conquistas pessoais de uma mulher por ela ser mulher, é assédio moral e é crime previsto no Código Penal Brasileiro.")   


#inicia-se o teste de assédio sexual aqui, de acordo com as formas mais comuns observadas sobre assédio
if (escolha_menu == 2):
    print()
    print("\tInicia-se aqui o teste de assédio sexual")
    print()
    print("Instruções:\nDigite '1' para SIM e '2' para NÃO.")
    qupas = int(input("1.Já te pediram favores sexuais em troca de produtos ou promoções de cargo, vaga de emprego ")) 
    qusas = int(input("2.A pessoa se aproxima mas nem tanto - mantendo uma distância de você - a cada olhar que você a dirige? ")) #não é assédio sexual.
    qutas = int(input("3.Alguém já fez piadinhas ou comentários obscenos com você/ou direcionados a você? "))
    quqas = int(input("4.Já fizeram imposições de trabalhos impossíveis ou abusivos para você? ")) #não é assédio sexual, é assédio moral.
    qunas = int(input("5.Já te tocaram de forma indesejada, que lhe causou constrangimento ou desconforto? "))
    quxas = int(input("6.Ao chegar em um local, as pessoas já fizeram comentários sobre as suas roupas e o seu corpo, em caráter obsceno? "))
    
    print()
    print("\t RESULTADO:")
    print()
    print("As questões 2 e 4 não são consideradas assédio sexual mas podem ser condutas ilegais.")
    print()
    if (qupas == 1):
        print("Você marcou SIM na questão 1. Pedir favores sexuais em troca de benefícios é assédio sexual e é crime previsto no Código Penal Brasileiro.")
    print()
    if (qutas == 1):
        print("Você marcou SIM na questão 3. Fazer piadinhas ou comentários obscenos direcionados a uma mulher é assédio sexual e é crime previsto no Código Penal Brasileiro.")
    print()
    if (qunas == 1):
        print("Você marcou SIM na questão 5. Tocar de forma indesejada o corpo feminino é assédio sexual e é crime previsto no Código Penal Brasileiro.")
    print()
    if (quxas == 1):
        print("Você marcou SIM na questão 6. Fazer comentários sobre roupas e aspectos corporais de uma mulher, de forma obscena, é assédio moral e é crime previsto no Código Penal Brasileiro.")       

sys.exit(2)
