def ler_lista(tamanho):

    print(f"Digite {tamanho} números:")
    lista_numerica = []
    for _ in range(tamanho):
        numero = float(input())
        lista_numerica.append(numero)
    return lista_numerica

def encontrar_max_min(lista_numerica):

    if not lista_numerica:
        return None, None

    maximo = minimo = lista_numerica[0]
    for numero in lista_numerica:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    return maximo, minimo

def buscar_elemento(lista_numerica, alvo):

    if not lista_numerica:
        return -1

    for indice, numero in enumerate(lista_numerica):
        if numero == alvo:
            return indice
    return -1

def main():
    tamanho = int(input("Digite o tamanho da lista: "))
    lista_numerica = ler_lista(tamanho)
    maximo, minimo = encontrar_max_min(lista_numerica)

    if maximo is not None and minimo is not None:
        print(f"Maior elemento: {maximo}")
        print(f"Menor elemento: {minimo}")

    alvo = float(input("Digite o número a ser buscado: "))
    indice = buscar_elemento(lista_numerica, alvo)

    if indice != -1:
        print(f"O número {alvo} foi encontrado na posição {indice}.")
    else:
        print(f"O número {alvo} não foi encontrado na lista.")

if __name__ == "__main__":
    main()
