#inicializando faturamentos individuais
valor_sp = 67836.43
valor_rj = 36678.66
valor_mg = 29229.88
valor_es = 27165.48
valor_outros = 19849.53

#somando faturamento total
valor_total = valor_sp + valor_rj + valor_mg + valor_es + valor_outros

#imprimindo valores percentuais de faturamento
print(f"\nFaturamentos percentuais:\
    \n\nSP:{(valor_sp * 100)/valor_total:.2f}%\
    \n\nRJ:{(valor_rj * 100)/valor_total:.2f}%\
    \n\nMG:{(valor_mg * 100)/valor_total:.2f}%\
    \n\nES:{(valor_es * 100)/valor_total:.2f}%\
    \n\nOutros:{(valor_outros * 100)/valor_total:.2f}%")


