from calculo import *

def main():
    capital_inicial = 1000
    taxa_juros = 0.05
    periodo = 12

    montante = calcular_juros_compostos(capital_inicial, taxa_juros, periodo)
    print(f"Montante final: R$ {montante}")

    juros_acumulados = calcular_juros_acumulados(capital_inicial, montante)
    print(f"Juros acumulados: R$ {juros_acumulados}")

    taxa_calculada = calcular_taxa_juros(montante, capital_inicial, periodo)
    print(f"Taxa de juros calculada: {taxa_calculada * 100}%")

    periodo_calculado = calcular_periodo(capital_inicial, montante, taxa_juros)
    print(f"Período calculado: {periodo_calculado} períodos")

if __name__ == "__main__":
    main()
