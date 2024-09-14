# EXERCÍCIO 1 – Escreva um programa em Python que permita ao usuário digitar dois números inteiros e exibir o resultado para cada uma das seguintes operações, nesta ordem: soma, subtração, multiplicação, divisão, divisão truncada, resto e exponenciação.
# Confira, no material do curso, os operadores matemáticos.

def calculate_operations():
    print('\n### Digite dois números inteiros ###')
    firstNumber = int (input('Primeiro número: '))
    secondNumber = int (input('Segundo número: '))

    totalSum = firstNumber + secondNumber
    difference = firstNumber - secondNumber
    multiplyNumbers = firstNumber * secondNumber
    divisionResult = firstNumber / secondNumber
    integerDivision = firstNumber // secondNumber
    modulus = firstNumber % secondNumber
    powerResult = firstNumber ** secondNumber

    print('\n### Resultados ###')
    print(f'soma: {totalSum}\nsubtração: {difference}\nmultiplicação: {multiplyNumbers}\ndivisão: {divisionResult}\ndivisão truncada: {integerDivision}\nresto: {modulus}\nexponenciação: {powerResult}')
calculate_operations()


# EXERCÍCIO 2 – Faça um programa em Python que leia dois números inteiros e exiba o quadrado da diferença do primeiro valor pelo segundo.
def square_of_the_difference():
    print('\n### Digite dois números inteiros ###')
    numberOne = int(input('Digite o primeiro número: '))
    numberTwo = int(input('Digite o segundo número: '))

    difference = numberOne - numberTwo
    result = difference ** 2
    print(f'O quadrado da diferença é: {result}')
square_of_the_difference()

 

# EXERCÍCIO 3 – Faça um programa em Python que resolva o seguinte problema: 
# Um concurso possui um prêmio no montante de R$ 780.000,00 para dividir entre três ganhadores da seguinte forma: 
# - o primeiro ganhador receberá 46% do prêmio; 
# - o segundo ganhador receberá 32% do prêmio; 
# - o terceiro ganhador receberá o restante do prêmio. 
# Calcule e mostre o valor do prêmio de cada ganhador, nesta ordem: primeiro colocado, segundo colocado e terceiro colocado.
# Observe que este programa não tem valor de entrada feita pelo usuário.
def winners():
    import locale
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.utf8')
    print('\n### Ganhadores ###')
    cashPrize = float(780000.00)

    firstWinner = locale.currency(cashPrize * 0.46, grouping = True)
    secondWinner = locale.currency(cashPrize * 0.32, grouping = True)
    thirdWinner = locale.currency(cashPrize * 0.22, grouping = True)

    print(f'>> Primeiro ganhador: {firstWinner}\n>> Segundo ganhador: {secondWinner}\n>> Terceiro ganhador: {thirdWinner}')
winners()
