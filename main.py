
#variável para guardar as perguntas
p1 = str("1 - Qual função é usada para exibir algo na tela em Python?")
p2 = str("2 - Qual é a forma correta de criar uma variável?")
p3 = str("3 - Qual tipo de dado armazena texto?")
p4 = str("4 - Qual operador compara igualdade?")
p5 = str("5 - Como iniciamos uma estrutura condicional?")
p6 = str("6 - Qual estrutura é usada para repetição?")
p7 = str("7 - Qual estrutura armazena múltiplos valores ordenados?")
p8 = str("8 - Como definimos uma função?")
p9 = str("9 - Qual valor booleano representa verdadeiro?")
p10 = str("10 - Qual o resultado de: 5 + 2?")

# variável para acumular pontos
pontos = int(0)

# Lista de perguntas
lista_perguntas = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

# Lista de respostas corretas
lista_resposta = ["C","D","C","B","B","B","C","B","C","C"]

# Opções A
lista_opcao_a = ["A) echo()","A) int x = 10","A) int","A) =","A) if (x > 5)","A) repeat","A) dict","A) function minhaFuncao()","A) true","A) 52"]

# Opções B
lista_opcao_b = [
"B) console.log()","B) var x = 10","B) float","B) ==","B) if x > 5:","B) for","B) tuple","B) func minhaFuncao()","B) TRUE","B) 3"]

# Opções C
lista_opcao_c = ["C) print()","C) str","C) str","C) ===","C) if x > 5 then","C) loop","C) list","C) def minhaFuncao():","C) True","C) 7"]

# Opções D
lista_opcao_d = ["D) write()","D) x = 10","D) bool","D) !=","D) if x > 5 {}","D) foreach","D) set","D) create minhaFuncao()","D) 1","D) 10"]

# Opções E
lista_opcao_e = ["E) show()","E) let x = 10","E) char","E) <>","E) if: x > 5","E) iterate","E) str","E) method minhaFuncao()","E) yes","E) Erro"]

print("--- BEM-VINDO AO QUIZ ---")
print("É um quiz sobre o conteudo de Python Básico onde possui 10 perguntas.")
print("\nRegras:\n1 - Você possui 3 tentativas por pergunta.\n2 - Cada acerto vale 10 pontos. \n3 - Se as vidas acabarem, o jogo termina.\n")

#Laço de repetição para apresentar as perguntas e opções de respostas 
#Len para obter a quantidade de perguntas e o range para percorrer a lista, onde i inicia com 0
for i in range(len(lista_perguntas)):

    print(f"{lista_perguntas[i]}\n {lista_opcao_a[i]}\n {lista_opcao_b[i]}\n {lista_opcao_c[i]}\n {lista_opcao_d[i]}\n {lista_opcao_e[i]}")

    tentativas = 0
    #Inicia laço de repetição para validar a tentativa
    while tentativas < 3:
        resposta = input("Informe a opção correta (A / B / C / D / E): ").upper()

        if resposta == lista_resposta[i]:
            pontos += 10
            print(f"\nResposta Correta! Você acumulou {pontos} pontos.\n")
            continuar = str(input("Deseja continuar jogando(S / N):").upper())
            
            match continuar:
                case "S":
                    break  #sai do while e vai para próxima pergunta
                case _:
                    exit() #caso seja diferente de S finaliza o programa
        else:
            tentativas += 1
            print(f"\nResposta errada! Tentativa {tentativas} de 3.")

    #Se tentativas chegar a 3 finaliza o programa
    if tentativas == 3:
        print(f"\nVocê errou 3 vezes.")
        break

print(f"\nFim de jogo!\nPontuação final: {pontos}")
