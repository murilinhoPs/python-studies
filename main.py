def main():
    palavra = "oi"
    # numero = input("digite um número: ")

    # if numero is None or numero == "":
    #     print("Não digitou um número")
    #     return

    # converted_numero = int(numero)
    # print(f"numero convertido: {converted_numero}")
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

    del lista1[2]  # remove the element that is at index 2 => [3,2,4]
    lista1.remove(2)  # remove the element by its value, will remove the value 2 => [3,4]
    print(lista1)
    #  lista1.remove(5) -> throws an error, bc the element doesn't exist
    lista1.insert(0, 1)  # add value 1 at index 0
    print(lista1)
    print(lista1.index(4))  # returns the index of the element (value)
    # print(lista1.index(6)) -> throws an error bc the value 6 is not in the list
    print(1 in lista1)  # returns true if the value 1 exists in the lista
    print(len(lista1))  # tamanho da lista, 3
    print(lista1 + other_list)  # soma as duas listas e retorna uma nova
    lista1.extend(other_list)  # modifica a lista que chamou o método
    print(lista1)  # [1, 3, 4, 4, 5, 6]

    tupla = (1, 2, 3, "murilo")  # like list, but immutable. they have the same methods
    print(tupla[1])
    print(type((1)))  # => int
    print(type((1,)))  # => tuple
    print(len(tupla))  # => 3
    print(tupla + (4, 5, 6))  # => (1, 2, 3, 4, 5, 6)
    print(tupla[:2])  # => (1, 2)
    print(2 in tupla)  # => True

    a, b, c = (1, 2, 3)  # unpack tuples, works with a list
    a, *b, c = (1, 2, 3, 4)  # unpack, but b will have two values a=1, b=[2,3] and c=4
    print(a, b, c)

    empty_dict = {}  # can create by any immutable type, like ints, floats, strings, tuples.
    my_dict = {"name": "Murilo", "age": 25, "hobbies": ["game", "guitar", "rpg"]}
    print(my_dict["name"])
    print(my_dict["hobbies"])  # will throw an error if key doesn't exist
    print(my_dict.get("ddd"))  # if key dont exist, returns None (null)
    my_dict["teste"] = "empty"  # or my_dict.update({"teste": "empty"})
    my_dict.setdefault("five", 5)  # only adds if the value doesn't exist yet on dictionary
    print(my_dict)
    del my_dict["teste"]
    print(my_dict)
    print(list(my_dict.keys()))  # returns all the keys
    print(list(my_dict.values()))  # returns all the values

    empty_set = set()
    my_set = {1, 1, 2, 3, 4, 4}  # list without duplicates
    valid_set = {(1,), 1}  # can't use [1]  bc is not immutable => {[1], 1}
    print(my_set)
    my_set.add(5)  # only adds if element doesn't exist
    print(my_set)  # {1, 1, 2, 3, 4, 4, 5}
    other_set = {3, 4, 5, 8}
    print(my_set & other_set)  # => intersection between values {3,4,5}
    print(my_set | other_set)  # junta os sets, sem repetir os valores => {1, 2, 3, 4, 5, 8}
    print(2 in my_set)  # => True
    print(10 in my_set)  # => False

    idade = 18  # can be any input
    if idade > 18:
        print("você é adulto")
    elif idade < 18:
        print("você é criança")
    else:
        print("você tem 18 anos!")

    animals = ["dog", "cat", "mouse", "chicken"]
    for animal in animals:
        if animal == "mouse":
            break  # don't print if animal == mouse and stop the loop
        print(animal)

    for animal in animals:
        if animal == "chicken":
            continue  # don't print if animal == chicken but continue the loop
        print(f"{animal} is a mammal")

    for i in range(4):  # returns an iterable from 0 to 4 (not counting 4)
        print(f"until4: {i}")

    for n in range(4, 8):  # returns iterable from 4 to 8 (not counting 8)
        print(f"4-8: {n}")

    for n in range(4, 8, 2):  # range(lower, upper, step)", de 2 em 2
        print(f"step2: {n}")

    for index, value in enumerate(animals):  # (for i=0; i < list.length; i++){} => returns an index too
        print(f"index={index} & {value}")

    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]
    for x in adj:  # => print red apple, red banana, red cherry, big apple, big banana...
        for y in fruits:
            print(x, y)
    else:  # código que vai ser executado após a conclusão do loop
        print("Finished for-loop!")

    x = 0
    while x < 6:
        x += 1
        if x == 3:  # will ignore 3 and not print it
            continue
        print(x)
    else:
        print("i não é menor que 6")


if __name__ == '__main__':
    main()
