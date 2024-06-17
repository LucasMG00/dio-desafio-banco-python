#IMPORTANDO BIBLIOTECA datetime PARA INCLUIR A INFORMAÇÃO NO EXTRATO
from datetime import datetime

#VARIÁVEIS E CONSTANTES
saldo = 0
extrato = ""
numero_saques = 0
LIMITE_QTD_SAQUES = 3
LIMITE_VALOR_POR_SAQUE = 500

#MENSAGEM INICIAL AO COMPILAR O PROGRAMA
print("""
*  Seja bem-vindo(a) ao Banco Digital!

** Digite um número de acordo com sua opção para utilizar o banco:""")

#MENU COM INFORMAÇÕES VARIÁVEIS DE ACORDO COM QUANTIDADE DE SAQUES RESTANTE
def menu(const_limite_saques, var_numero_saques):
    qtd_saques_atual = const_limite_saques - var_numero_saques
    status_saque_atual = f'{qtd_saques_atual} {"saques dísponíveis hoje" if qtd_saques_atual != 1 else "saque disponível hoje"}'
    
    return f"""
[1] Depositar   
[2] Sacar       ({status_saque_atual})
[3] Extrato     
[0] Sair        

    => """

#FLUXO DE REPETIÇÃO ATÉ O USUÁRIO DIGITAR O NÚMERO 0
while True:    
    opcao = input(menu(LIMITE_QTD_SAQUES, numero_saques))

    #SELECIONOU DEPOSITAR
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            agora = datetime.now()
            data_hora = agora.strftime("%d/%m/%Y %H:%M")
            extrato += f"Depósito: R$ {valor:.2f} em {data_hora}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    #SELECIONOU SAQUE
    elif opcao == "2":
        excedeu_saques = LIMITE_QTD_SAQUES - numero_saques
        
        if excedeu_saques == 0:
            print("Operação falhou! Número máximo de saques excedido.")
            continue
        
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > LIMITE_VALOR_POR_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite. (Limite para saque é R$ {LIMITE_VALOR_POR_SAQUE:.2f})")

        elif valor > 0:
            saldo -= valor
            agora = datetime.now()
            data_hora = agora.strftime("%d/%m/%Y %H:%M")
            extrato += f"Saque: R$ {valor:.2f} em {data_hora}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    #SELECIONOU EXTRATO
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    #SELECIONOU SAIR
    elif opcao == "0":
        print("\nObrigado por usar o Banco Digital!")
        break

    #SELEÇÃO INVÁLIDA
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
