import tax_calculator as tax_calculator


def test_tax_calc_s_0():
    assert tax_calculator.calculate_tax(0, "single") == 0


def test_tax_calc_j_0():
    assert tax_calculator.calculate_tax(0, "joint") == 0


def test_tax_calc_s_5k():
    assert tax_calculator.calculate_tax(5000, "single") == 500


def test_tax_calc_j_5k():
    assert tax_calculator.calculate_tax(5000, "joint") == 500


def test_tax_calc_s_9k():
    assert tax_calculator.calculate_tax(9999, "single") == 999


def test_tax_calc_j_19k():
    assert tax_calculator.calculate_tax(19999, "joint") == 1999


def test_tax_calc_s_10k():
    assert tax_calculator.calculate_tax(10009, "single") == 1000


def test_tax_calc_j_20k():
    assert tax_calculator.calculate_tax(20010, "joint") == 2000


def test_tax_calc_s_49k():
    assert tax_calculator.calculate_tax(49999, "single") == 6999


def test_tax_calc_j_99k():
    assert tax_calculator.calculate_tax(99999, "joint") == 13999


def test_tax_calc_s_50k():
    assert tax_calculator.calculate_tax(50006, "single") == 7000


def test_tax_calc_j_100k():
    assert tax_calculator.calculate_tax(100006, "joint") == 14000


def test_tax_calc_s_99k():
    assert tax_calculator.calculate_tax(99999, "single") == 16999


def test_tax_calc_j_199k():
    assert tax_calculator.calculate_tax(199999, "joint") == 33999


def test_tax_calc_s_100k():
    assert tax_calculator.calculate_tax(100005, "single") == 17000


def test_tax_calc_j_200k():
    assert tax_calculator.calculate_tax(200005, "joint") == 34000
