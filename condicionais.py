def verificar_maioridade():
    idade = int(input("Qual é a sua idade? "))
    if (idade >= 18):
        print("Você é maior de idade")
    else:
        print("Você é menor de idade!")
#verificar_maioridade()

def numeroPar():
    par = False
    while (par == False):
      try:
        numero_par = int(input("Digite um número par: "))
        if (numero_par % 2 == 0 and numero_par != 0):
          print("Você digitou um número par, que foi:", numero_par)
          break
        elif (numero_par == 0):
          print("Você digitou zero...")
        else:
          print("Não é par!")
      except:
        print("[404] Entrada inválida...")
#numeroPar()

def resultadoFinal():
   nota = False
   while (nota == False):
      try:
        nota_aluno = float(input("Digite a sua nota: "))
        if(nota_aluno >= 7 and nota_aluno <= 10 and nota_aluno > 0):
            print("Parabéns, você passou! A sua nota foi: ",nota_aluno)
            break
        elif (nota_aluno > 10 or nota_aluno < 0):
            print("Digite uma nota válida")
        else:
            print("Infelizmente você não foi aprovado, você tirou: ",nota_aluno)
            break
      except:
            print("Entrada inválida")
resultadoFinal()