#!/usr/bin/python3
"""
This script calculates the minimum number of operations required to obtain
exactly n occurrences of the character 'H' in a file.
"""

def calculate_min_operations(n):
    """
    calculate_min_operations
    Calculates the fewest number of operations needed to result in exactly n 'H' characters.
    Args:
        n (int): The target number of 'H' characters.
    Returns:
        int: The minimum number of operations required.
    """
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
