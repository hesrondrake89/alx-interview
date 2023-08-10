#!/usr/bin/python3
"""
This script defines a function for calculating the minimum number of operations required
to obtain exactly n occurrences of the character 'H' in a file.
"""

def calculate_min_operations(n):
    """
    Calculates the minimum number of operations needed to achieve exactly n 'H' characters.
    Args:
        n (int): The target number of 'H' characters.
    Returns:
        int: The minimum number of operations required.
    """
    operations_count = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations_count += divisor
            n //= divisor
        divisor += 1
        
    return operations_count
