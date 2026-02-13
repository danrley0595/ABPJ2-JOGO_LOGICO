# Declaração variaveis perguntas
p1 = str("Pergunta 1")
p2 = str("Pergunta 2")
p3 = str("Pergunta 3")
p4 = str("Pergunta 4")
p5 = str("Pergunta 5")
p6 = str("Pergunta 6")
p7 = str("Pergunta 7")
p8 = str("Pergunta 8")
p9 = str("Pergunta 9")
p10 = str("Pergunta 10")

# variavel para acumular pontos
pontos = int(0)

# Criação da lista de perguntas e respostas
lista_perguntas = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
lista_resposta = ["A","B","C","D","E","A","B","C","D","E"]
lista_opçao_a = ["A","A","A","A","A","A","A","A","A","A"]
lista_opçao_b = ["B","B","B","B","B","B","B","B","B","B"]
lista_opçao_c = ["C","C","C","C","C","C","C","C","C","C"]
lista_opçao_d = ["D","D","D","D","D","D","D","D","D","D"]
lista_opçao_e = ["E","E","E","E","E","E","E","E","E","F"]

# Laço de repetição para apresentar as perguntas e opções de respostas 
i = 0
for p in lista_perguntas:

    print(f"{p}\n {lista_opçao_a[i]}\n {lista_opçao_b[i]}\n {lista_opçao_c[i]}\n {lista_opçao_d[i]}\n {lista_opçao_e[i]}")
    resposta = str(input("Informe a opção CORRETA(informe a letra maiúsculo):"))
    if resposta == lista_resposta[i]:
        pontos += 10
        print(f"\nResposta Correta!Você acumulou {pontos}.")
        resp_cont = str(input("Deseja continuar(s/n)?"))
        if resp_cont == "n":
            break;
        else:
            i += 1
            
    else:
        print("\nQue pena você errou :( , pontos acumulados: {pontos} ")
        resp_tentar = str(input("Deseja tentar novamente(s/n)?"))
        if resp_tentar == "n":
            break;
