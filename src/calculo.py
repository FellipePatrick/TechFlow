def calcular_juros_compostos(capital_inicial, taxa_juros, periodo):
    montante = capital_inicial * (1 + taxa_juros) ** periodo
    return round(montante, 2)

def calcular_juros_acumulados(capital_inicial, montante):
    juros_acumulados = montante - capital_inicial
    return round(juros_acumulados, 2)

def calcular_taxa_juros(montante, capital_inicial, periodo):
    taxa_juros = (montante / capital_inicial) ** (1 / periodo) - 1
    return round(taxa_juros, 5)

def calcular_periodo(capital_inicial, montante, taxa_juros):
    periodo = (montante / capital_inicial) ** (1 / (1 + taxa_juros))
    return round(periodo, 2)
