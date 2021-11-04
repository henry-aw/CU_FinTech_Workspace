# -*- coding: utf-8 -*-
"""Loan to Value Filter.

This script filters the bank list by the applicant's maximum home loan
to home value ratio.

"""


def filter_loan_to_value(loan_to_value_ratio, bank_list):

    loan_to_value_approval_list = []

    for bank in bank_list:
        if loan_to_value_ratio <= float(bank[2]):
            loan_to_value_approval_list.append(bank)
    return loan_to_value_approval_list
