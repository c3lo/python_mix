import typing
def horner(x: float, coeffs: typing.List[float])-> float:
    ergebnis: float = coeffs[0]
    for coeff in coeffs[1:]:
        ergebnis *= x
        ergebnis += coeff
    return ergebnis

