import pytest

from prevod import na_binarni


@pytest.mark.parametrize(
    "cislo,ocekavano",
    [(0, "0"), (1, "1"), (2, "10"), (10, "1010"), (255, "11111111")],
)
def test_prevadi_cisla(cislo, ocekavano):
    assert na_binarni(cislo) == ocekavano


def test_zaporne_cislo_je_chyba():
    with pytest.raises(ValueError):
        na_binarni(-1)
