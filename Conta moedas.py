import os
import time

print('Digite a quantidade de moedas separados por um espaço(1, 0.5, 0.25, 0.10, 0.05 respectivamente) e pressione Enter')

m1, m50, m25, m10, m05 = input("Quantidade: ").split()
print("Quantidade Moedas de 1 Real: ", m1)
print("Quantidade Moedas de 0.5: ", m50)
print("Quantidade Moedas de 0.25: ", m25)
print("Quantidade Moedas de 0.10: ", m10)
print("Quantidade Moedas de 0.05: ", m05)
print()

m1 = float(m1)

m50 = float(m50)

m25 = float(m25)

m10 = float (m10)

m05 = float (m05)

print('Seu Total de Moedas é:', int(m1 + m50 + m25 + m10 + m05))

m1 *= 1

m50 *= 0.5

m25 *= 0.25

m10 *= 0.10

m05 *= 0.05

SomaTroco = (m1 + m50 + m25 + m10 + m05)

print('Seu Total Em dinheiro é:', 'R$', SomaTroco)
