import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculo import calcular_juros_compostos

def test_calculo_juros_compostos_valores_positivos():
    resultado = calcular_juros_compostos(1000, 0.05, 12)
    assert resultado == 1795.86, f"Esperado 1795.86, mas obteve {resultado}"
    
def test_calculo_juros_compostos_valores_negativos():
    resultado = calcular_juros_compostos(-1000, 0.05, 12)
    assert resultado == -1795.86, f"Esperado -1795.86, mas obteve {resultado}"

def test_calculo_juros_compostos_taxa_zero():
    resultado = calcular_juros_compostos(1000, 0, 12)
    assert resultado == 1000.0, f"Esperado 1000.0, mas obteve {resultado}"