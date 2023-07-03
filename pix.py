valores_aceitos = [0.25, 0.50, 1, 2, 5, 10]
estoque = 0
troco_total = 0
cont_2 = []
cont_5 = []
cont_10 = []
cont_25 = []
cont_50 = []
cont_1 = []
pagamentos_pix = []

# Funcao que calcula o valor do troco
def calcular_troco(dinheiro_inserido, valor_bebida):
    troco = dinheiro_inserido - valor_bebida
    return troco

while True:
    print("Olá, digite 1 para consumidor e 2 para administrador")
    acesso = int(input("Digite seu acesso: "))
    # Acesso do consumidor
    if acesso == 1:
        # Variavel de dinheiro inserido pelo usuario
        dinheiro = 0
        print("Bem-vindo a máquina de refrigerante! Valor da bebida: R$5")
        # Entrada do dinheiro
        metodo_pagamento = int(input("Digite 1 para dinheiro ou 2 para PIX: "))
        if metodo_pagamento == 1:
            while dinheiro < 5 and estoque > 0:
                entrada = input("Insira notas de R$2,00, R$5,00 ou R$10,00 ou moedas de R$0,25, R$0,50 ou R$1,00: ")
                if float(entrada) in valores_aceitos:
                    dinheiro = dinheiro + float(entrada)
                    print("Dinheiro inserido: R$", dinheiro)
                    print("Valor faltante: ", 5 - dinheiro)
                else:
                    print("Valor inválido! Tente novamente.")
                # Acumula valor unitario de cada moeda/cedula inserida
                if float(entrada) == 2:
                    cont_2.append(2)
                elif float(entrada) == 5:
                    cont_5.append(5)
                elif float(entrada) == 10:
                    cont_10.append(10)
                elif float(entrada) == 0.25:
                    cont_25.append(0.25)
                elif float(entrada) == 0.50:
                    cont_50.append(0.50)
                elif float(entrada) == 1:
                    cont_1.append(1)
            # Cálculo de troco conforme disponibilidade da máquina
            if dinheiro >= 5 and estoque > 0:
                troco = calcular_troco(dinheiro, 5)
                if troco <= troco_total:
                    troco_total = troco_total - troco
                    print("Troco: R$", troco)
                    print("Retire sua bebida!")
                    estoque = estoque - 1
                else:
                    print("Não há troco suficiente para esta compra. Compra cancelada.")
            elif estoque == 0:
                print("Não há estoque disponível para esta compra. Tente novamente mais tarde.")
            else:
                print("Compra cancelada.")
        # Método de pagamento pelo pix
        elif metodo_pagamento == 2:
            if estoque > 0:
              # Armazena número de telefone do usuário na lista
                telefone = input("Digite o número do telefone para pagamento via PIX: ")
                pagamentos_pix.append([telefone, 5])
                print("Pagamento via PIX realizado com sucesso!")
            else:
                print("Não há estoque disponível para esta compra. Tente novamente mais tarde.")
        else:
            print("Método de pagamento inválido!")
    # Acesso do administrador        
    elif acesso == 2:
        print("Bem-vindo a área do administrador!")
        print("Opções: \nRepor estoque (1) \nRepor troco (2) \nModificar quantidade de moedas/cédulas (3) \nConsultar saldo atual de estoque (4)")
        print("Consultar saldo atual de troco (5) \nConsultar pagamentos por PIX (6) \nConsultar quantidade de cédulas e moedas já inseridas até o momento (7)")
        reposicao = int(input("Digite qual opção você quer: "))
        # Reposicao do estoque total disponivel
        if reposicao == 1:
            qtd_estoque = int(input("Digite a quantidade para repor: "))
            estoque = estoque + qtd_estoque
            print("Quantidade de estoque total: ", estoque)
        # Reposicao do troco total disponivel
        if reposicao == 2:
            qtd_troco = float(input("Digite a quantidade para repor: "))
            troco_total = troco_total + qtd_troco
            print("Quantidade de troco disponível R$:", troco_total)
        # Altera quantidade de moedas/cédulas
        if reposicao == 3:
            valor_moeda_cedula = float(input("Digite o valor da moeda/cédula a ser modificada: "))
            nova_quantidade = int(input("Digite a nova quantidade: "))
            if valor_moeda_cedula == 2:
                cont_2 = [2] * nova_quantidade
            elif valor_moeda_cedula == 5:
                cont_5 = [5] * nova_quantidade
            elif valor_moeda_cedula == 10:
                cont_10 = [10] * nova_quantidade
            elif valor_moeda_cedula == 0.25:
                cont_25 = [0.25] * nova_quantidade
            elif valor_moeda_cedula == 0.50:
                cont_50 = [0.50] * nova_quantidade
            elif valor_moeda_cedula == 1:
                cont_1 = [1] * nova_quantidade
            else:
                print("Valor inválido!")
        # Mostra estoque atual
        if reposicao == 4:
            print("Estoque atual: ", estoque)
        # Mostra troco atual
        if reposicao == 5:
            print("Troco atual R$:", troco_total)
        # Mostra todos os pagamentos por pix já realizados
        if reposicao == 6:
            for pagamento in pagamentos_pix:
                print(pagamento)
        # Imprime o valor unitario das moedas/cedulas inseridas durante o funcionamento do programa
        if reposicao == 7:
            print("Quantidade de cédulas de R$2: ", len(cont_2))
            print("Quantidade de cédulas de R$5: ", len(cont_5))
            print("Quantidade de cédulas de R$10: ", len(cont_10))
            print("Quantidade de moedas de R$0,25: ", len(cont_25))
            print("Quantidade de moedas de R$0,50: ", len(cont_50))
            print("Quantidade de moedas de R$1: ", len(cont_1))
    
    comando = input("Digite qualquer número para reiniciar ou 'parar' para finalizar o loop: ")
    if comando == "parar":
        break