cedula_2 = [2]
cedula_5 = [5]
cedula_10 = [10]
moeda_25 = [0.25]
moeda_50 = [0.50]
moeda_1 = [1]
cont_2 = 0
cont_5 = 0
cont_10 = 0
cont_25 = 0
cont_50 = 0
cont_1 = 0
valores_aceitos = [0.25, 0.50, 1, 2, 5, 10]
estoque = 0
troco_total = 0

while True:
    print("Olá, digite 1 para consumidor e 2 para administrador")
    acesso = int(input("Digite seu acesso: "))
    # Acesso do consumidor
    if acesso == 1:
        # Variavel de dinheiro inserido pelo usuario
        dinheiro = 0
        print("Bem-vindo a máquina de refrigerante! Valor da bebida: R$5")
        while dinheiro < 5 and estoque > 0:
            # Acumula notas inseridas pelo usuario e também o que falta para o valor total da bebida
            entrada = input("Insira notas de R$2,00, R$5,00 ou R$10,00 ou moedas de R$0,25, R$0,50 ou R$1,00: ")
            if float(entrada) in valores_aceitos:
                dinheiro = dinheiro + float(entrada)
                print("Dinheiro inserido: R$", dinheiro)
                print("Valor faltante: ", 5 - dinheiro)
            else:
                print("Valor inválido! Tente novamente.")
            # Acumula valor unitario de cada moeda/cedula inserida
            if float(entrada) in cedula_2:
                cont_2 = cont_2 + 1
            elif float(entrada) in cedula_5:
                cont_5 = cont_5 + 1
            elif float(entrada) in cedula_10:
                cont_10 = cont_10 + 1
            elif float(entrada) in moeda_25:
                cont_25 = cont_25 + 1
            elif float(entrada) in moeda_50:
                cont_50 = cont_50 + 1
            elif float(entrada) in moeda_1:
                cont_1 = cont_1 + 1
        # Calculo de troco conforme disponibilidade da maquina
        if dinheiro >= 5 and estoque > 0:
            troco = dinheiro - 5
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
    elif acesso == 2:
        # Acesso do administrador
        print("Bem-vindo a área do administrador!")
        print("Opções: repor estoque(1), repor troco(2), consultar quantidade de cédulas e moedas ja inseridas ate o momento(3) ")
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
            print("Quantidade de troco disponivel R$:", troco_total)
        # Imprime o valor unitario das moedas/cedulas inseridas durante o funcionamento do programa
        if reposicao == 3:
            print("Quantidade de cédulas de R$2: ", cont_2)
            print("Quantidade de cédulas de R$5: ", cont_5)
            print("Quantidade de cédulas de R$10: ", cont_10)
            print("Quantidade de moedas de R$0,25: ", cont_25)
            print("Quantidade de moedas de R$0,50: ", cont_50)
            print("Quantidade de moedas de R$1: ", cont_1)
    comando = input("Digite qualquer numero para reiniciar ou 'parar' para finalizar o loop: ")
    if comando == "parar":
        break