#!/usr/bin/python3
"""
This script calculates the minimum number of operations required to obtain
exactly n occurrences of the character 'H' in a file.
"""


def minOperations(n):
    operation_count = 0
    number = 2
    if type(n) is not int or n <= 1:
        return operation_count
    while n > 1:
        if n % number == 0:
            operation_count += number
            n /= number
        else:
            number += 1
    return(operation_count)
