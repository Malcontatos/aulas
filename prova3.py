contador = 0
soma = 0

while True:
    numero = int (input('Digite um número: \nAperte 0 para SAIR\n'))
    
    if numero == 0:
        break

    soma += numero
    contador += 1

media = soma / contador
print(f'A média entre os números {soma} e {contador} é: {media}\nQuantidade de números digitados: {contador}')

