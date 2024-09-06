def binary_search(lista, item) -> None:  # apenas em listas ordenadas
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            print(f"index: {meio} - valor: {chute}")
            return item
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1


binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)
binary_search(['Amana', 'Bruno', 'Carlos', 'Duda', 'Edmundo', 'Felipe', 'Guilherme'], 'Edmundo')
