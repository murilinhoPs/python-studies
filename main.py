def main():
    palavra = "oi"
    # numero = input("digite um número: ")

    # if numero is None or numero == "":
    #     print("Não digitou um número")
    #     return

    # converted_numero = int(numero)
    # print(converted_numero)
    print('Salve mundo', end='!')

    lista1 = []
    other_list = [4, 5, 6]
    lista1.append(3)  # add element at the end of the list
    lista1.append(2)
    lista1.append(1)
    print("")
    print(lista1)  # => [3,2,1]
    lista1.pop()  # removes last element
    print(lista1)  # => [3,2]
    lista1.append(1)
    lista1.append(4)
    # lista1 = [3, 2, 1, 4]
    print(lista1[0], lista1[-1],
          lista1[1])  # => primeiro elemento (index 0), ultimo elemento (4: index -1) e segundo elemento (index 1)
    print(lista1[1:3])  # retornar do index 1 até o 3 (nao inclui o index 3) [2,1]
    print(lista1[2:])  # retornar a lista a partir do 2 index [1, 4]
    print(lista1[:3])  # retorna até o index 3 (nao inclui o index 3) [3,2,1]
    print(lista1[::2])  # retorna de 2 em dois elementos a partir do 0 [3, 1]


if __name__ == '__main__':
    main()
