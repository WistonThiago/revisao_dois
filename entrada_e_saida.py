def saudar_usuario():
    nome = input("Qual é o seu nome? ")
    print("Olá,", nome, "! Seja bem-vindo (a)!")
saudar_usuario()

def soma():
    sumvalue1 = int(input("Digite um número: "))
    sumvalue2 = int(input("Digite outro número: "))
    sumresult = sumvalue1+sumvalue2
    print("A soma desses números é: ",sumresult)
soma()

def multiply():
    multvalue1 = int(input("Digite um número: "))
    multvalue2 = int(input("Digite outro número: "))
    multresult = multvalue1*multvalue2
    print("A multiplicação desses números é: ",multresult)
multiply()

def media():
    mediavalue1 = int(input("Digite um número: "))
    mediaresult = mediavalue1/2
    print("A divisão do número por dois é: ",mediaresult)
media()

def imc():
    altura = float(input("Digite a sua altura: "))
    peso = float(input("Digite o seu peso: "))
    imcresult = round((peso/(altura*altura)), 2)
    print("O seu IMC é de: ",imcresult)
imc()