numero1= float(input('digite o primeiro número: '))
numero2= float(input('digite o segundo número: '))
perg = print('Deseja colocar mais algum ')


def soma_a(numero1 ,numero2):
    soma = (numero1+numero2)
    return (soma)
soma_final = soma_a(numero1, numero2)
    
def sub_a(numero1 ,numero2):
    sub= (numero1-numero2)
    return (sub)
sub_final= sub_a(numero1,numero2)

def mult_a(numero1, numero2):
    mult = (numero1 * numero2)
    return (mult)
mult_final = mult_a(numero1, numero2)

def div_a(numero1, numero2):
   div = (numero1 / numero2)
   return (div)
div_final = div_a(numero1, numero2)

print("""
Digite 1 para somar
Digite 2 para subtração
Digite 3 para multiplicação
Digite 4 para divisão
Digite 5 para sair da calculadora""")


opcao = int(input('escolha a opção que desejar: '))

if opcao == 1:
    print('A soma dos numeros é de:', soma_final)
elif opcao == 2:
    print('A subtração dos numeros é de:', sub_final)
elif opcao == 3:
    print('A multiplicação dos numeros é de:', mult_final)
elif opcao == 4:
    print('A divisão dos numeros é de:', div_final)
elif opcao == 5:
    print('Volte sempre!')
else:
    opcao > 5 or opcao < 0
    print("Numero inválido!")



