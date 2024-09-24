velocidade = int (input("Qual a velocidade do carro em Km/h ? "))
print(f'{velocidade}Km/h')

limite = 80
excesso = velocidade - limite
multa = excesso * 20

if velocidade > 80:
    print(f"Multado por excesso de velocidade!\n VALOR DA MULTA: R${multa}")
else:
    print("Velocidade permitida!")