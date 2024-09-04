def main():
    palavra = "oi"
    numero = input("digite um número: ")

    if numero is None:
        print("Não digitou um número")

    converted_numero = int(numero)
    print(converted_numero)
    print('Salve mundo', end='!')


if __name__ == '__main__':
    main()
