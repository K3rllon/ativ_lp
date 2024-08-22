login = ('admin')
senha = ('123')
login2 = input(f'Digite seu login: ')
senha2 = input(f'Digite sua senha: ')
if (login == login2 and senha2 == senha):
    print(f'Olá {login}, seja bem vindo(a) !')
else: 
    print(f"login ou senha incorretos, tente novamente")