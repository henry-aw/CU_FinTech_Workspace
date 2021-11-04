# Import pathlib
from pathlib import Path

# Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    # @TODO: Your code here!
