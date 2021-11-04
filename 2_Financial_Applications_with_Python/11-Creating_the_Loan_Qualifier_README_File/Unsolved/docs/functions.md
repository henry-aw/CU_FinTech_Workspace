# Application Functions

## Calculate_monthly_debt_ratio

Calculates the monthly debt ratio and converts the monthly debt payment and monthly income parameters to int values and divides the monthly debt payment by the monthly income to produce the monthly debt ratio.

```python
def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio
```

## Parameters

* `monthly_debt_payment (float)`: The monthly debt payment.
* `monthly_income (float):` The monthly income.

## Return Values

* `monthly_debt_ratio (int):` The monthly debt ratio.


## Calculate_loan_to_value_ratio

Calculates the loan to value ratio by converting the loan amount and home value parameters to int values and dividing the loan amount by the home value to produce the loan to value ratio.

```python
def calculate_loan_to_value_ratio(loan_amount, home_value):
    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio
```

## Parameters

* `loan_amount (float)`: The loan amount
* `home_value (float)`: The value of the home.

## Returns Values

* `loan_to_value_ratio (int)`: The loan to value ratio.
