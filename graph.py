entrada = '3 5, 4 5, 2 6, 3 6, 5 5, 6 1, 5 2, 1 4, 1 1, 4 2, 2 3'
# input("Arestas do grafo (origem destino, origem, destino, ...): ")

initial_lis = entrada.split(',')
max_v = 0
min_v = 1
lista = []
adjacency = []
intersection = []
formatted_lis = []

for ar in initial_lis:
    formatted_lis.append(ar.strip())
    o, d = ar.split()
    o, d = int(o), int(d)
    lista.append((o, d))
    if o > max_v:
        max_v = o
        if d > max_v:
            max_v = d

while min_v <= max_v:
    adjacency += [min_v]
    min_v = min_v + 1

print(formatted_lis)
formatted_set = {(int(val[0]), int(val[2])) for val in formatted_lis}
print(formatted_set)

print()
print('Matriz de Adjacências para Grafo:')
print()
print("V | ", end='')
print(" ".join(map(str, adjacency)), end='')
print(' Grau')

for i in adjacency:
    print('---', end='')

for origin in range(1, max_v + 1):  # não conta o max_v, é ATÉ ele
    intersection = []
    (print(f'\n{origin} | ', end=''))

    for index, destination in enumerate(adjacency):
        # if origin == 5 and value == 2:, força bruta

        # for x in formatted_lis:  # , o problema era o for dentro do outro for
        # -> criar um set para fazer uma busca só nele
        #     int_origin = int(x[0])
        #     int_destination = int(x[2])
        #     if origin == int_origin and destination == int_destination:
        #         intersection.append(1)
        #     else:
        #         intersection.append(0)

        if (origin, destination) in formatted_set or (destination, origin) in formatted_set:
            intersection.append(1)
        else:
            intersection.append(0)
    print(" ".join(map(str, intersection)), end='')
