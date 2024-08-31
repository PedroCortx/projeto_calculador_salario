

AliqINSS = (0.08, 0.09, 0.11, 642.34)
AliqIR = (0.00, 0.075, 0.15, 0.225, 0.275)
DeducaoIR = (0.00, 142.80, 354.80, 636.13, 869.36)

SalBrutos = []
arqsal = open('SALARIO.TXT', 'r', encoding='UTF-8')
leitura = 0

# adicionamos um tratamento de excecoes pois ficamos em dúvida
# se o arquivo de teste 1, que possuia uma primeira linha "Bruto\n",
# poderia ser o caso de um arquivo com inclusao impropria de salarios
while leitura != '':
    leitura = arqsal.readline()
    try:
        SalBrutos.append(float(leitura))
    except ValueError:
        continue

arqsal.close()
SalBrutos.sort()

# Calcula aliquota INSS
def Calculo_INSS(a):
    ValINSS = 0
    if a <= 1751.81:
        ValINSS = (a * AliqINSS[0])
        INSS = AliqINSS[0]
    elif a > 1751.81 and a <= 2919.72:
        ValINSS = (a * AliqINSS[1])
        INSS = AliqINSS[1]
    elif a > 2919.72 and a <= 5839.45:
        ValINSS = (a * AliqINSS[2])
        INSS = AliqINSS[2]
    else:
        ValINSS = AliqINSS[3]
        INSS = 0.00
    return ValINSS, INSS

# Calcula IR
def Calculo_IR(a):
    BaseIR = a - ValINSS
    if BaseIR <= 1903.98:
        ValIR = BaseIR * AliqIR[0] - DeducaoIR[0]
        IR = AliqIR[0]
    elif BaseIR > 1903.98 and BaseIR <= 2826.65:
        ValIR = BaseIR * AliqIR[1] - DeducaoIR[1]
        IR = AliqIR[1]
    elif BaseIR > 2826.65 and BaseIR <= 3751.05:
        ValIR = BaseIR * AliqIR[2] - DeducaoIR[2]
        IR = AliqIR[2]
    elif BaseIR > 3751.05 and BaseIR <= 4664.68:
        ValIR = BaseIR * AliqIR[3] - DeducaoIR[3]
        IR = AliqIR[3]
    else:
        ValIR = BaseIR * AliqIR[4] - DeducaoIR[4]
        IR = AliqIR[4]

    if ValIR < 10.00:
        ValIR = 0

    return ValIR, BaseIR, IR

# cria CALCULOS.TXT e escreve os títulos da tabela
saida = open('CALCULOS.TXT', 'w', encoding= 'Utf-8')
saida.write(f"{('Bruto'):>15} {('AliqINSS'):>15} {('Val.INSS'):>15} "
            f"{('Base I.R.'):>15} {('AliqIR'):>15} {('Val.IR'):>15} {('Liquido'):>15} \n")

# para cada salario, calcula e escreve os valores abaixo dos títulos
for salarios in SalBrutos:
    ValINSS, INSS = Calculo_INSS(salarios)
    ValIR, BaseIR, IR = Calculo_IR(salarios)
    Liquido = BaseIR - ValIR
    saida.write(f'{salarios:>15.2f} {INSS*100:>15} {ValINSS:>15.2f} '
                f'{BaseIR:>15.2f} {IR*100:>15.1f} {ValIR:>15.2f} {Liquido:>15.2f}\n')

# fecha o arquivo e termina o programa
saida.close()
print('\nArquivo CALCULOS.TXT gerado com sucesso.\nFim da execução.')