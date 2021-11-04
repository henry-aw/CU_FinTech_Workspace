# -*- coding: utf-8 -*-
"""A Collection of Financial Calculators.
This script contains a variety of financial calculator functions needed to
determine loan qualifications.
"""

def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
    """
    Calculates the monthly debt ratio.

    Converts the monthly debt payment and monthly income
    parameters to int values and divides the monthly debt
    payment by the monthly income to produce the monthly
    debt ratio.

    Parameters:
        monthly_debt_payment (float): The monthly debt payment.
        monthly_income (float): The monthly income.

    Returns:
        monthly_debt_ratio (int): The monthly debt ratio.
    """
    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio

def calculate_loan_to_value_ratio(loan_amount, home_value):
    """
    Calculates the loan to value ratio.

    Converts the loan amount and home value parameters to
    int values and divides the loan amount by the home value
    to produce the loan to value ratio.

    Parameters:
        loan_amount (float): The loan amount.
        home_value (float): The value of the home.

    Returns:
        loan_to_value_ratio (int): The loan to value ratio.
    """
    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio
