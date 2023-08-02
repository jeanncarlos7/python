def carregar_matriz(num_linhas, num_colunas):

    matriz = []
    print("Digite os elementos da matriz:")
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            elemento = float(input(f"Elemento [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def calcular_media(matriz, num_linhas, num_colunas):

    soma = 0
    total_elementos = num_linhas * num_colunas
    for i in range(num_linhas):
        for j in range(num_colunas):
            soma += matriz[i][j]
    media = soma / total_elementos
    return media

def exibir_elementos_impares(matriz, num_linhas, num_colunas):

    print("Elementos ímpares da matriz:")
    for i in range(num_linhas):
        for j in range(num_colunas):
            elemento = matriz[i][j]
            if elemento % 2 != 0:
                print(elemento, end=" ")
        print()

def main():
    num_linhas = int(input("Digite o número de linhas da matriz: "))
    num_colunas = int(input("Digite o número de colunas da matriz: "))

    matriz = carregar_matriz(num_linhas, num_colunas)

    media = calcular_media(matriz, num_linhas, num_colunas)
    print(f"A média dos elementos da matriz é: {media}")

    exibir_elementos_impares(matriz, num_linhas, num_colunas)

if __name__ == "__main__":
    main()
