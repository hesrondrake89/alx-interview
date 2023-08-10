#!/usr/bin/python3
"""
This module provides a function to calculate the minimum number of operations required
to achieve exactly n occurrences of the character 'H'.
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
    # It takes at least 2 operations to produce any output: (min, Copy All => Paste)
    if n < 2:
        return 0
    
    operations_count, divisor = 0, 2
    
    while divisor <= n:
        if n % divisor == 0:
            operations_count += divisor
            n /= divisor
            divisor -= 1
        divisor += 1
    
    return operations_count

