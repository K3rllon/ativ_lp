
while True :
    print ('________Calc.py________')
    print ('1- Soma')
    print ('2- Subtração')
    print ('3- Multiplicação')
    print ('4- Divisão')
    print ('5- Elevar ao quadrado')
    print ('0- Sair')
    print ('_______________________')

    p = input('Escolha a operação: ')    

    if p == '0':
        print ('Você saiu')
        break

    if p == '1':
        print ('Você escolheu a opção soma')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print (f'Resultado: {n1+n2}')
        
    else: 
        if p == '2':
            print ('Você escolheu a opção subtração')
            n3 = float(input('Digite o primeiro número: '))
            n4 = float(input('Digite o segundo número: '))
            print (f'Resultado: {n3-n4}')
        else: 
            if p == '3':
                print ('Você escolheu a opção multiplicação')
                n5 = float(input('Digite o primeiro número: '))
                n6 = float(input('Digite o segundo número: '))
                print (f'Resultado: {n5*n6}')
            else:
                if p == '4':
                    print ('Você escolheu a opção divisão')
                    n7= float(input('Digite o primeiro número: '))
                    n8 = float(input('Digite o segundo número: '))
                    print (f'Resultado: {n7/n8}')
                else:
                    if p == '5':
                        print ('Você escolheu a elevar ao quadrado')
                        n9= float(input('Digite um número: '))
                        print (f'Resultado: {n9*n9}')
                    else:
                        print ('Escolha invalida, tente novamente')