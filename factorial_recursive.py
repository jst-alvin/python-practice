def factorial_recursive(n):
    # Base case: 0! and 1! are both 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial_recursive(n - 1)
