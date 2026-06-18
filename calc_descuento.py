def descuento(precio: float, porcentaje: float) -> float:

    # validacion y conversion de datos
    if not isinstance(precio, (int, float)) or not isinstance(porcentaje, (int, float)):
        raise TypeError("El precio y el porcentaje deben ser valores numéricos.")
    
    # logica principal para descuento
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    if not (0 <= porcentaje <= 100):
        raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")

    # calculo del descuento
    monto_descuento = precio * (porcentaje / 100)
    return precio - monto_descuento