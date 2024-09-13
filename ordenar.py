from typing import *

plays_count = [156, 141, 35, 11, 84, 88, 61, 130]  # ordenar do maior para oo menor
top_artists = ['Radiohead', 'Kishore Kumar', 'The Black Keys', 'Neutral Milk Hotel', 'Beck', 'The Strokes', 'Wilco',
               'My Chemical Romance']
most_played_artists = {}


def create_list():
    for i in range(len(plays_count)):
        artist = top_artists[i]
        count = plays_count[i]
        most_played_artists[artist] = count


create_list()
print(most_played_artists)


# procurar o maior entre eles (passando por todos os elementos)
# adicionar o maior em primeiro numa outra lista
# retornar essa nova lista
# na lógica se trocar o sinal para "<" lista[i] < atual, vai retornar oo menor valor


# if change for lista[i] < atual, it will return the lowest value
def find_higher_value(lista):
    index = 0
    for i in range(1, len(lista)):
        if lista[i] > lista[index]:
            index = i
    return index


# retorna o index_atual quando terminar de passar pela lista toda (len(lista))

# caso base. quando chegar no final da lista retorna o index_maior. return;
# SE não, chamo a função novamente passandoo index_maior e o index_atual + 1 (0 +1; 1+1....)
# MAS se o valor do index_atual (lsta[index_atual]) for maior (>)  que o index_maior (lista[index_maior]), 
# atualizo o valor do index_maior = index_atual (pq quer dizer que o valor do index_atual é maior que o index_maior)
# depois de atualizar o valor, continuo chamando a própria função

def find_higher_value_recursive(lista, index_atual=0, index_maior=0):
    if index_atual == len(lista):
        return index_maior
    if lista[index_atual] > lista[index_maior]:
        index_maior = index_atual
    return find_higher_value_recursive(lista, index_atual + 1, index_maior)


# plays_count.reverse()
print(find_higher_value(plays_count))  # => 0
print(find_higher_value_recursive(plays_count))  # => 0


def sorting_value(lista):
    ordered_list = []

    for i in range(len(lista)):
        higher_index = find_higher_value(lista)
        new_value = lista.pop(higher_index)
        ordered_list.append(new_value)

    return ordered_list


print(sorting_value(plays_count))


def find_higher_in_map(hash_map: Dict):
    actual_k = list(hash_map.keys())[0]
    actual_v = list(hash_map.values())[0]

    for key in hash_map:
        value = hash_map.get(key)
        if value > actual_v:
            actual_k = key
            actual_v = value
    return actual_k, actual_v


# print(find_higher_in_map(most_played_artists))


def sorting(hash_map: Dict):
    ordered_map = {}

    while len(hash_map) > 0:
        higher = find_higher_in_map(hash_map)
        key = higher[0]
        value = higher[1]
        ordered_map[key] = value
        del hash_map[key]

    return ordered_map


print(sorting(most_played_artists))
