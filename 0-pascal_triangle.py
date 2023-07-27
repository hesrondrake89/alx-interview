#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascals triangle of n.

    Args:
      n (int): The number of rows in the triangle.

    Returns:
      A list of lists of integers representing Pascals triangle.
    """

    if n <= 0:
        return []

    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Create a new row for the current iteration
        row = [1]

        # Calculate the elements for the current row based on the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # Add the last element of the row, which is always 1
        row.append(1)

       
        triangle.append(row)

    return triangle

if __name__ == "__main__":
   
    print(pascal_triangle(5))
