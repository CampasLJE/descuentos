# importacion de librerias
import pytest
from calc_descuento import descuento

# caso normal con descuentos bajos
def test_descuentos_correcto():
    assert descuento(100, 20) == 99.9 #cambio realizado se cambio de 80 a 99 para que el descuento no sea el correcto
    assert descuento(250, 10) == 225.0

# casos de limites
def test_descuento_limites():
    # sin descuento
    assert descuento(100, 0) == 100.0
    # descuento completo
    assert descuento(100, 100) == 0.0
    # Precio cero
    assert descuento(0, 50) == 0.0

# Ccasos de error definidos
def test_errores():
    # Porcentaje inválido
    with pytest.raises(ValueError):
        descuento(100, -5)
    with pytest.raises(ValueError):
        descuento(100, 101)
    # Precio negativo
    with pytest.raises(ValueError):
        descuento(-50, 10)
    # Tipos de datos incorrectos
    with pytest.raises(TypeError):
        descuento("cien", 20)