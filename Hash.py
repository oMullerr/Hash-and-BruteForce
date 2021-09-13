import hashlib
from ast import literal_eval
dados = {}

def entrar():
    f = open("senhasgravadas.txt", "r")
    fr = f.read().splitlines()
    for l in fr:
        (key, valor) = l.split(";")
        dados[key] = valor

    try:
        print("=================================")
        usuario = input("Digite seu usuario: ")
        senha = input("Digite sua senha: ")
        senha = hashlib.md5(senha.encode('utf-8')).hexdigest()

    except:
        print("Voce digitou algo errado, tente novamente! ")
        loop = False

    if usuario in dados:
        if dados[usuario] == senha:
            print("----------------------------")
            print("Login realizado com sucesso!")

        else:
            print("Senha incorreta! tente novamente")
            loop = False
    else:
        print("Usuário nao encontrado!")


def cadastrar():
    while True:
        print("=================================")
        nome = input('Insira o nome: ')
        senha = input("Digite uma senha: ")
        if len(senha) > 4 and len(nome) > 4:
            print("Sua senha ou seu nome tem mais de 4 caracteres!")
            break
        senha = hashlib.md5(senha.encode('utf-8')).hexdigest()

        f = open("senhasgravadas.txt", "a+")
        f.write(nome + ";" + senha + "\n")
        f.close()
        print("Conta cadastrada!!")
        break


options = {'1': cadastrar,
           '2': entrar}

# Loop principal, que vai receber o numero digitado e chamar a função corresponde da ação desejada
while True:
    escolhaMenuPrincipal = input("================================= \n"
                                 '1 - Cadastrar uma conta. \n'
                                 '2 - Entrar na conta. \n'
                                 '3 - Sair. \n'
                                 "Escolha uma opção: ")

    if escolhaMenuPrincipal == '3':
        break

    func = options.get(escolhaMenuPrincipal, lambda: 'Opção Inválida!\n')

    if func == entrar:
        func()

    if func == cadastrar:
        func()