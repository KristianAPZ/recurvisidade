def investimento(dinheiro, dolar, mes=0, valor_acumulado=0, meses_totais=None, valor_cem_mil=False):
    if meses_totais is None:
        meses_totais = []
    if mes >= len(dolar):
        mes = 0
        meses_totais.append(1)
    if (valor_acumulado*dolar[mes]) >= 100000 and not valor_cem_mil:
        print(
            f"Em {sum(meses_totais)} anos e {mes+1} meses com {valor_acumulado} dolares alcanza os cem mil reais")
        valor_cem_mil = True
    if (valor_acumulado*dolar[mes]) >= 1000000:
        print(
            f"Em {sum(meses_totais)} anos e {mes+1} meses com {valor_acumulado} dolares alcanza o milhão de reais")
        return
    taxa = 1.05

    valor_acumulado = round(valor_acumulado*taxa + (dinheiro/dolar[mes]), 2)
    investimento(dinheiro, dolar, mes+1, valor_acumulado,
                 meses_totais, valor_cem_mil)


dinheiro = 500.00
dolar = [4.95, 4.98, 5, 5.17, 5.19, 5.55,
         5.66, 5.65, 5.44, 5.77, 6.05, 6.19]

investimento(dinheiro, dolar)
