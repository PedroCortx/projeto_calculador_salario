import random

saida = open('SALARIO.TXT','w', encoding='utf-8')
for x in range(1000):
    saida.write(f'{random.uniform(1000.00, 20000.00):.2f}\n')

saida.close()
