# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiplicação(x, y):
    return x * y

def divisão(x, y):
    return x / y

print("\n SELECIONE A OPÇÃO DESEJADA")
print("1. SOMA")
print("2. SUBTRAÇÃO")
print("3. MULTIPLICAÇÃO")
print("4. DIVISÃO")

digite_opcao = input("\n SELECIONE A OPÇÃO ")
num1 = int(input("\n DIGITE PRIMEIRO NUMERO "))
num2 = int(input("\n DIGITE SEGUNDO NUMERO "))

if digite_opcao == '1':
   print("\n")
   print(num1, '+', num2, '= ', soma(num1, num2))
   print("\n")

elif digite_opcao == '2':
    print("\n")
    print(num1, '-', num2, '= ', sub(num1, num2))
    print("\n") 

elif digite_opcao == '3':
    print("\n")
    print(num1, '*', num2, '= ', multiplicação(num1, num2))
    print("\n")

else:
    print("\n")
    print(num1, '/', num2, '= ', divisão(num1, num2))
    print("\n")

