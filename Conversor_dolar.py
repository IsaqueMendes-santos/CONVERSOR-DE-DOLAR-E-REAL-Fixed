# Valor da cotação do dólar
dolar = 5.50


# Função: converte dólar para real
def converter_para_real(valor_em_dolar):
    return valor_em_dolar * dolar


# Função: converte real para dólar
def converter_para_dolar(valor_em_real):
    return valor_em_real / dolar


# Laço principal do programa
while True:
    print("\n===== CONVERSOR DE MOEDAS =====")
    print("1 - Dólar para Real")
    print("2 - Real para Dólar")
    print("3 - Encerrar")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        valor = float(input("Informe o valor em dólar: US$ "))
        resultado = converter_para_real(valor)
        print(f"Valor convertido: R$ {resultado:.2f}")

    elif escolha == 2:
        valor = float(input("Informe o valor em real: R$ "))
        resultado = converter_para_dolar(valor)
        print(f"Valor convertido: US$ {resultado:.2f}")

    elif escolha == 3:
        print("Programa finalizado.")
        break

    else:
        print("Opção inválida. Tente novamente.")