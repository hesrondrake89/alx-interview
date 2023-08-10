#!/usr/bin/python3
"""
This script calculates the minimum number of operations required to obtain
exactly n occurrences of the character 'H' in a file.
"""

def minOperations(n):
    operation_count = 0
    divisor = 2
    
    if not isinstance(n, int) or n <= 1:
        return operation_count
    
    while n > 1:
        if n % divisor == 0:
            operation_count += divisor
            n /= divisor
        else:
            divisor += 1
            
    return operation_count
