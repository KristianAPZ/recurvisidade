def investimentoBitcoin(dinheiro, dolar, bitcoin, mes=0, valor_acumulado=0, meses_totais=None, valor_cem_mil=False, valor_um_bitcoin=False):
    if meses_totais is None:
        meses_totais = []
    if mes >= len(dolar):
        mes = 0
        meses_totais.append(1)
    if (valor_acumulado*dolar[mes]) >= 100000 and not valor_cem_mil:
        print(
            f"Em {sum(meses_totais)} anos e {mes+1} meses com {valor_acumulado} dolares alcança os cem mil reais")
        valor_cem_mil = True
    if (valor_acumulado*dolar[mes]) >= bitcoin[mes] and not valor_um_bitcoin:
        print(
            f"Em {sum(meses_totais)} anos e {mes+1} meses com {valor_acumulado} dolares alcança um bitcoin")
        valor_um_bitcoin = True
    if (valor_acumulado*dolar[mes]) >= 1000000:
        print(
            f"Em {sum(meses_totais)} anos e {mes+1} meses com {valor_acumulado} dolares alcança o milhão de reais")
        return
    taxa = 1.05

    valor_acumulado = round(valor_acumulado*taxa + (dinheiro/dolar[mes]), 2)
    investimentoBitcoin(dinheiro, dolar, bitcoin, mes+1, valor_acumulado,
                        meses_totais, valor_cem_mil, valor_um_bitcoin)


dinheiro = 250.00
dolar = [4.95, 4.98, 5, 5.17, 5.19, 5.55,
         5.66, 5.65, 5.44, 5.77, 6.05, 6.19]
bitcoin = [227000, 249625.87, 362034.66, 344548.67, 316822.65,
           357068.67, 356681.9, 336002.66, 322000, 351345.95, 532710.28, 652238.05]

investimentoBitcoin(dinheiro, dolar, bitcoin)
