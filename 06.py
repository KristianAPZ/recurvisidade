def bradescoInvestimento(bradesco, dividendo_bradesco, mes=0, valor_acumulado=0, meses_totais=None, taxa=1.05, valor_cem_mil=False, dividendo_total=0):
    if meses_totais is None:
        meses_totais = []
    if mes >= 11:
        mes = 0
        meses_totais.append(1)
    if valor_acumulado >= 100000 and not valor_cem_mil:
        print("\nBBDC4 - BRADESCO")
        print(
            f'\nTempo gasto para atingir o marco inicial de R$ 100.000,00: {sum(meses_totais)} anos e {mes+1} meses')
        valor_cem_mil = True
    if valor_acumulado >= 1000000:
        print(
            f'Tempo gasto para atingir o objetivo final: {sum(meses_totais)} anos e {mes+1} meses')
        print(f"Valor de dividendos recibidos: {dividendo_total:.2f}")
        return
    valor_acumulado = round(valor_acumulado * taxa *
                            dividendo_bradesco + (dinheiro/bradesco[mes]), 2)
    dividendo_total += valor_acumulado * (dividendo_bradesco-1)
    bradescoInvestimento(bradesco, dividendo_bradesco, mes+1,
                         valor_acumulado, meses_totais, taxa, valor_cem_mil, dividendo_total)


def taesaInvestimento(taesa, dividendo_taesa, mes=0, valor_acumulado=0, meses_totais=None, taxa=1.05, valor_cem_mil=False, dividendo_total=0):
    if meses_totais is None:
        meses_totais = []
    if mes >= 11:
        mes = 0
        meses_totais.append(1)
    if valor_acumulado >= 100000 and not valor_cem_mil:
        print("\nTAEE11 - TEASA")
        print(
            f'\nTempo gasto para atingir o marco inicial de R$ 100.000,00: {sum(meses_totais)} anos e {mes+1} meses')
        valor_cem_mil = True
    if valor_acumulado >= 1000000:
        print(
            f'Tempo gasto para atingir o objetivo final: {sum(meses_totais)} anos e {mes+1} meses')
        print(f"Valor de dividendos recibidos: {dividendo_total:.2f}")
        return
    valor_acumulado = round(valor_acumulado * taxa *
                            dividendo_taesa + (dinheiro/taesa[mes]), 2)
    dividendo_total += valor_acumulado * (dividendo_bradesco-1)
    taesaInvestimento(taesa, dividendo_taesa, mes+1,
                      valor_acumulado, meses_totais, taxa, valor_cem_mil, dividendo_total)


def petroRioInvestimento(petroRio, mes=0, valor_acumulado=0, meses_totais=None, taxa=1.05, valor_cem_mil=False):
    if meses_totais is None:
        meses_totais = []
    if mes >= 11:
        mes = 0
        meses_totais.append(1)
    if valor_acumulado >= 100000 and not valor_cem_mil:
        print('\nPRIO3 - Petro Rio')
        print(
            f'\nTempo gasto para atingir o marco inicial de R$ 100.000,00: {sum(meses_totais)} anos e {mes+1} meses')
        valor_cem_mil = True
    if valor_acumulado >= 1000000:
        print(
            f'Tempo gasto para atingir o objetivo final: {sum(meses_totais)} anos e {mes+1} meses')
        print("Não tem dividendos recibidos.\n")
        return
    valor_acumulado = round(valor_acumulado * taxa +
                            (dinheiro/petroRio[mes]), 2)
    petroRioInvestimento(petroRio, mes+1,
                         valor_acumulado, meses_totais, taxa, valor_cem_mil)


bradesco = [15.53, 13, 12.70, 13.14, 12.85, 12,
            11.74, 13.56, 15.10, 15.28, 14.93, 11.30]
petroRio = [45.88, 47, 44.90, 50.10, 46.40, 42.02,
            46.50, 42.46, 43.70, 40.50, 40.04, 41.34]
taesa = [35.25, 34.53, 34, 34.40, 34.12, 32.33,
         33.66, 33.75, 34.78, 34.07, 34.14, 33.88]

dividendo_taesa = 1.0856
dividendo_bradesco = 1.0957
dinheiro = 80.00
bradescoInvestimento(bradesco, dividendo_bradesco, dinheiro)
taesaInvestimento(taesa, dividendo_taesa, dinheiro)
petroRioInvestimento(petroRio, dinheiro)
