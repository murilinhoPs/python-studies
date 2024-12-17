def fat(x: int):
    if x == 1:
        return 1
    return x * fat(x - 1)


print(f"Resultado: {fat(3)}")  # -> 6
