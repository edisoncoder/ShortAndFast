def tabuada(inicio,colunas):  # Tabuada 3x3
    for linha in range(2,10):
        for col in range(colunas):
            print(f'  {col+inicio} X {linha} = \033[1m{(col+inicio)*linha:2}\033[0m     ',end='')
        print()
    print()
print('  Tabuada (3x3) \n')
for t in (2,5,8):
    tabuada(t,3)
    print()
