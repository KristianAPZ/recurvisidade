def inverterString(letra):
    if len(letra) == 0:
        return letra
    else:
        return inverterString(letra[1:]) + letra[0]


print(inverterString("hello"))
