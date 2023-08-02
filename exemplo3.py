# matriz = [[1,2,3], [4,5,6]]

def main():
    mat = []
    nlin = int(input("Digite o numero de linhas: "))
    ncol = int(input("Digite o numero de colunas: "))
    carrega_matriz(mat, nlin, ncol)

    print(f"Soma dos elementos da matriz: {soma_matriz(mat,nlin,ncol)}")

    exibe_matriz(mat,nlin)

def carrega_matriz(mat,nlin,ncol):
    for lin in range(nlin):
        linha = []
        for col in range(ncol):
            linha.append(int(input("Digite um elemento da matriz: ")))
        mat.append(linha)

def soma_matriz(mat,nlin,ncol):
    soma = 0
    for lin in range(nlin):
        for col in range(ncol):
            soma+=mat[lin][col]

    return(soma)

def exibe_matriz(mat,nlin):
    for lin in range(nlin):
        print(mat[lin])

if (__name__ == "__main__" ):
    main()
