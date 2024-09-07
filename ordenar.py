from typing import List

plays_count = [156, 141, 35, 11, 84, 88, 61]  # ordenar do maior para oo menor
top_artists = ['Radiohead', 'Kishore Kumar', 'The Black Keys', 'Neutral Milk Hotel', 'Beck', 'The Strokes', 'Wilco']
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

def find_higher_value(lista):
    atual = lista[0]
    index_atual = 0
    for i in range(1, len(lista)):
        if lista[i] > atual:
            atual = lista[i]
            index_atual = i
    return index_atual


# plays_count.reverse()
print(find_higher_value(most_played_artists))


def sorting_value(lista):
    ordered_list = []

    for i in range(len(lista)):
        higher_index = find_higher_value(lista)
        print(lista[higher_index])
        new_value = lista.pop(higher_index)
        ordered_list.append(new_value)

    return ordered_list


print(sorting_value(plays_count))


# def find_higher_in_map(hash_map):
#     values = list(hash_map.values())
#     atual = values[0]
#     index_atual = 0
#     for i in range(1, len(hash_map)):
#         if values[i] > atual:
#             atual = values[i]
#             index_atual = i
#     return index_atual
#
#
# def sorting(hash_map):
#     ordered_list = []
#
#     for i in range(len(hash_map)):
#         higher_index = find_higher_value(hash_map)
#         print(hash_map[higher_index])
#         new_value = hash_map.pop(higher_index)
#         ordered_list.append(new_value)
#
#     return ordered_list
