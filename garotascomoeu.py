# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 09:27:07 2021

@author: barbara
barbarahmiley@gmail.com

"""
import sys
import sklearn
import matplotlib

print("Iniciando...")
print("_______________________________________________")
print("GAROTAS COMO EU")
print()
print("Esse programa foi desenvolvido com caráter informacional\ncujo objetivo principal é levar informação sobre assédio\ne como existem medidas de profilaxia e auxílio às potenciais vítimas.\t ")
print("Pode ser utilizado em caráter educacional.\nIndicado para todxs as pessoas que se identificam como mulheres. ")
       
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
        raise SystemExit()
      
print()
print("_________________________________________________")
print("\tVamos agora bater um papo sobre consentimento:")
print()
print("Após ler a documentação presente no site e no readme.txt,\nvocê tem ciência de que este programa é utilizado para\nfins educacionais e de pesquisa. Em nenhum momento é solicitado dados pessoais\nPortanto, garante-se o anonimato, e a sua participação não implicará em\nnenhum tipo de penalidade ou que poderá induzir você a tomar uma decisão.")
print("É um ambiente totalmente seguro. Recomenda-se que menores de 18 anos tenham a supervisão de um adulto ou seu responsável para prosseguir.\nNão comercialize esse código sem prévia autorização do Girls Like Me.")
print()

aceite = int(input("Digite '1' caso você concorde e '2' caso você não concorde: "))
if (aceite == 1):
    pass
else:
    print("Sinto muito, você não pode continuar. Encerrando o programa.")
    raise SystemExit()


print("_________________________________________________")

def menu():
    print("\tMENU\n\t[1] - Teste de assédio moral;\n\t[2] - Teste de assédio sexual;\n\t[3] - Simulador matemático;\n\t[4] - Contatos úteis;\n\t[5] - Encerrar programa.")
    escolha_menu = int(input("Digite o número da opção escolhida: "))
    return escolha_menu

print()
print()
print("_________________________________________________")

escolha_menu = menu()
print()
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

#inicia-se aqui o simulador matemático. Possui técnicas de Machine Learning integradas. 
if(escolha_menu == 3):
    print()
    print("Inicia-se aqui o Simulador Matemático.")
    print()
    def menu_sim():
        print("\tMENU\n\t[1]-Executar Árvore de Decisão;\n\t[2]-Executar Regressão(Previsão)\n\t[3]-Calculadora do Crime\n\t[4]-Referências")
        escolha_sim = int(input("Digite a opção desejada: "))
        return escolha_sim
    escolha_sim = menu_sim()
    
    if(escolha_sim == 1):
        from sklearn import tree
        print()
        print("Árvore de Decisão")
        X = [[47, 0], [77, 1]]
        Y = [5, 10]
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(X, Y)
        print(clf.predict([[55, 1]]))
        print()
        print("\tRESULTADO:\nDe acordo com a pesquisa realizada entre a Think Eva e o LinkedIn\ndurante março/2019 e março/2020, observou-se um aumento de\n55% das conversas online. De acordo com a árvore de decisão do GCM,ao retornar o valor\n'10', identificou-se que o aumento dessas conversas online pode ter relação direta com o aumento de casos de assédio virtual.")
    
    if(escolha_sim == 2):
        print()
        print("Regressão(Previsão)")
        print()
        print("Esse gráfico demonstra a previsão realizada pelo programa do Garotas Como Eu, com base na pesquisa realizada entre\na Think Eva e o LinkedIn, em como o assédio pode ter sido crescente depois de 30 dias da pesquisa realizada\n,isto é, previsão que em Abril de 2020, houve a crescente demonstrada no gráfico.")
        from sklearn.datasets import make_regression
        x, y = make_regression(n_samples=188, n_features=1, noise=30)
        import matplotlib.pyplot as plt
        plt.scatter(x,y)
        from sklearn.linear_model import LinearRegression
        modelo = LinearRegression()
        modelo.fit(x,y)
        modelo.predict(x)
        plt.scatter(x,y)
        plt.plot(x, modelo.predict(x), color='red', linewidth=3)
        plt.show()
                
    if(escolha_sim == 3):
        print()
        print("Calculadora do Crime")
        print()
        print("\t ATENÇÃO")
        print()
        print("De acordo com o Fórum Brasileiro de Segurança Pública, a cada hora 536 mulheres são agredidas no Brasil.")
        print()
        print("Essa calculadora vai informar, de acordo com a estimativa acima, hipoteticamente quantas mulheres seriam agredidas\nde acordo com a escolha do usuário.\nCálculo apenas informacional e para conscientização do usuário.")
        print()
        print("*****************************")
        print("Se em uma hora existem 536 mulheres sendo agredidas, quantas mulheres podem ser vítimas de agressões no Brasil em um horário X?")
        print("Atenção: digitar um valor entre 1 - 24, correspondente ao tempo desejado")
        print()
        pdr1 = 536
        pdr2 = 1
        temhr = int(input("Digite um valor correspondente ao tempo desejado: "))
        
        rescrime = (pdr1*temhr)/pdr2
        
        print(f"A hora digitada pelo usuário foi {temhr}h. Portanto, a cada {temhr}h,{rescrime} mulheres são agredidas no Brasil.")
        
    if(escolha_sim == 4):
        print()
        print("____________________________________________")
        print("\tREFERÊNCIAS BIBLIOGRÁFICAS E DE DIREITOS AUTORAIS")
        print()
        print("As referências das pesquisas citadas no simulador são:")
        print()
        print("1. O Ciclo do Assédio Sexual no Ambiente de Trabalho.\nParceria de Think Eva e LinkedIn\nDisponível em: https://thinkeva.com.br/pesquisas/assedio-no-contexto-do-mundo-corporativo/")
        print()
        print("2.'Mais de 500 mulheres são agredidas por hora no Brasil, revela pesquisa'\nSite Agência Brasil\nFórum Brasileiro de Segurança Pública\nDisponível em: https://agenciabrasil.ebc.com.br/direitos-humanos/noticia/2019-02/mais-de-500-mulheres-sao-agredidas-por-hora-no-brasil-revela")
        print()
        print("3.'Liberdade Online? Como meninas e jovens mulheres lidam com o assédio nais redes sociais virtuais.'\nONG PLAN INTERNACIONAL\nPesquisa Global.")
        print("--------------------------------------------")
    
#inicia-se aqui os contatos úteis.
if(escolha_menu == 4):
    print()
    print("******************************************************")
    print("\t CONTATOS ÚTEIS")
    print("******************************************************")
    print()
    
    dict_contatos = {"Polícia Rodoviária Estadual": 198, 
                     "Polícia Civil": 197,
                     "Serviço de Atendimento Móvel de Urgência (SAMU)": 192,
                     "Polícia Militar": 190,
                     "Defesa Civil": 199,
                     "Corpo de Bombeiros": 193,
                     "Central de Atendimento à Mulher em Situação de Violência": 180}
    print(dict_contatos)
    print()
    print("Se você está no EXTERIOR ou deseja mais informações, acesse: https://www.gov.br/mdh/pt-br/navegue-por-temas/politicas-para-mulheres/ligue-180")
    
#encerra o programa.
else:
    print("Programa encerrado.")
    exit

    
    
        
       
        
        
        

    




