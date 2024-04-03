print("""
                Calculadora em Python!
                Digite 1 para somar;
                Digite 2 para subtrair;
                Digite 3 para multiplicar;
                Digite 4 para dividir.
                """)

def calculadora():
    confirm = False
    while (confirm == False):
        try:
            operation = int(input("Escolha uma operação: "))
            print("Processando a sua escolha...")
            if (operation == 1):
                def soma():
                    somatorio = False
                    while (somatorio == False):
                        try:
                            print("Você escolheu a operação de soma!")
                            sumOne = float(input("Digite o primeiro número para somar: "))
                            sumTwo = float(input("Digite o segundo número para somar: "))
                            sumTotal = round((sumOne + sumTwo),2)
                            print("O resultado da sua soma é: ", sumTotal)
                            break
                        except:
                            print("Entrada inválida...")
                soma()
                break
            elif (operation == 2):
                def subtracao():
                    minus = False
                    while (minus == False):
                        try:
                            print("Você escolheu a operação de subtração!")
                            minusOne = float(input("Digite o primeiro número para subtrair: "))
                            minusTwo = float(input("Digite o segundo número para subtrair: "))
                            minusTotal = round((minusOne - minusTwo),2)
                            if(minusOne > minusTwo):
                                print("O resultado da subtração é: ", minusTotal)
                                break
                            elif(minusOne == 0):
                                print("O primeiro é zero.")
                            elif(minusOne < minusTwo):
                                print("O primeiro número é maior que o segundo.")
                        except:
                            print("Entrada inválida...")
                subtracao()
                break
            elif (operation == 3):
                def multiplicacao():
                    multiply = False
                    while (multiply == False):
                        try:
                            print("Você escolheu a operação de multiplicação!")
                            timesOne = float(input("Digite o primeiro número para multiplicar: "))
                            timesTwo = float(input("Digite o segundo número para multiplicar: "))
                            timesTotal = round((timesOne * timesTwo), 2)
                            if (timesOne == 0 or timesTwo == 0):
                                print("Multiplicar por 0 sempre resulta em 0.")
                                break
                            else:
                                print("O resultado da sua multiplicação é: ", timesTotal)
                                break
                        except:
                            print("Entrada inválida...")
                multiplicacao()
                break
            elif (operation == 4):
                def divisao():
                    getBy = False
                    while (getBy == False):
                        try:
                            print("Você escolheu a operação de divisão!")
                            getOne = int(input("Digite o primeiro número para dividir: "))
                            getTwo = int(input("Digite o segundo número para dividir: "))
                            getByTotal = round((getOne/getTwo), 2)
                            if (getOne == 0 or getTwo == 0):
                                print("Impossível dividir por 0 ou dividir 0 por algo, tente novamente.")
                            else:
                                print("O resultado da sua divisão é: ", getByTotal)
                                break
                        except:
                            print("Entrada inválida...")
                divisao()
                break
        except:
            print("""
                Operação desconhecida, insira uma opção válida.
                """)
            print("""
                Calculadora em Python!
                Digite 1 para somar;
                Digite 2 para subtrair;
                Digite 3 para multiplicar;
                Digite 4 para dividir.
                """)
calculadora()