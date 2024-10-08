tabuada = int(input('---TABUADA DE 1 A 10, ESCOLHA O NÚMERO:---\n'))
print(f'VOCÊ ESCOLHEU A TABUADA DO NÚMERO: {tabuada}')

for i in range (1, 10+1):
    resultado = tabuada*i
    print(f'{tabuada} x {i} = {resultado}' )
