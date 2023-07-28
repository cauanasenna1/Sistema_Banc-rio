#Fazer um sistema bancário com as seguintes funções: depósito, saldo e extrato
#depósito só pode inserir numero maior que 0
# o sistema deverá permitir fazer até 3 saques diários com limite máximo de 500 por saque
#caso não tenha saldo, deverá aparecer uma mensagem informando que não há saldo disponível
#saques e depoósitos devem ser armazenados no extrato
menu = ''' [d] Depositar \n [s] Sacar \n [e] Extrato \n [q] Sair \n

=> '''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Insira aqui o valor do seu depósito: "))
        if deposito > 0 :
            saldo += deposito
            extrato += f"Depósito no valor de R${deposito:.2f} \n"
            print(f'''
              Depósito concluído no valor de: R${deposito:.2f}
              Saldo atual: R${saldo:.2f} \n ''')
        else:
            print("O depósito precisa ser maior do que R$0,00")

    if opcao == "s":
        if (numero_saques < LIMITE_SAQUES):
            saque = int(input("Insira aqui o valor do saque: \n"))
            if saque > saldo:
                print(f"Operação negada pois o valor do saque é maior que o saldo \n")
            if saque > 500 :
                print("Você só pode sacar até R$500,00 \n") 
            else :
                numero_saques +=1
                extrato += f"Saque no valor de R${saque:.2f}\n"
                saldo -= saque
                print(f'''
                    Você já realizou {numero_saques} saques hoje.
                    Saque concluído no valor de R${saque:.2f}
                    Saldo atual: R${saldo:.2f} \n''')        
        else:
            print("Você já atingiu o limite de 3 saques diários \n")

    if opcao == "e":
        print(f'''
=====EXTRATO====

{extrato}

Saldo atual no valor de R${saldo:.2f}''')

    if opcao == "q":
        break
