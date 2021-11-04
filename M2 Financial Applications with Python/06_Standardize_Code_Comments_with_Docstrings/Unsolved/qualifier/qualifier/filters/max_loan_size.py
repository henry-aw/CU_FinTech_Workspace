# -*- coding: utf-8 -*-
"""Max Loan Size Filter.

This script filters the bank list by comparing the user's loan value
against the bank's maximum loan size.

"""


def filter_max_loan_size(loan_amount, bank_list):

    loan_size_approval_list = []

    for bank in bank_list:
        if loan_amount <= int(bank[1]):
            loan_size_approval_list.append(bank)
    return loan_size_approval_list
