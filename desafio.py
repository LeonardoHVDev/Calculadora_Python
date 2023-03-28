import math
from pip import main


def main():
    nome = input('Digite seu nome: ')
    
    
    opcao = 0
    while opcao != 2:
        print('''
        [1] historico
        [2] Opcao Matematica
        [3] sair do programa
        ''')
        
        opcao = obter_opcao()   
    
    opcao = 0
    while opcao != 21:
            
        print('''
        [21] soma
        [23] subtracao
        [24] multiplicacao
        [25] divisao
        ''')
        

        opcao = obter_opcao()   
    
    
        numero1 = int(input('Digite algum numero: '))
        numero2 = int(input('Digite outro numero, por favor: '))
        
    
    if opcao == 1:
        historico = numero1 == numero2
        print(''.format(numero1, numero2, historico))
    else:
            print()
           
    if opcao == 2:
        numero1 == numero2
    elif opcao == 21:
        soma = numero1 + numero2
        print('O resultado de {} + {} e {}'.format(numero1, numero2, soma))       
    elif opcao == 22:    
        subtracao = numero1 - numero2
        print('O resultado de {} - {} e {}'.format(numero1, numero2, subtracao))       
    elif opcao == 23:   
        multiplicacao = numero1 * numero2
        print('O resultado de {} * {} e {}'.format(numero1, numero2, multiplicacao))  
    elif opcao == 24:    
        divisao = numero1 / numero2
        print('O resultado de {} / {} e {}'.format(numero1, numero2, divisao))
    else:
        print('Fim do programa! Volte sempre!')  
    
    if opcao == 3:
        ()
        print(''.format())    
    else:
        print('Fim do programa! Volte sempre!')
    
    try:
        print()
    except:
        print('Digitar somente numeros!')
        
        numero1 = int(input(f'Ola {nome}, digite um numero inteiro? '))
        numero2 = int(input(f'Correto {nome}, agora digite mais um numero '))
             
def obter_opcao():
    try:
        return int(input('Qual e a sua opcao?'))
    except:
        print('Opcao nao pode ser vazia e nem contem letras!')
main()
     
    
    


