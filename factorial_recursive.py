def factorial_recursive(n):
    # Base case: 0! and 1! are both 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial_recursive(n - 1)
        # Calling the function with different numbers
print(factorial_recursive(4))     # Output: 24 (4*3*2*1)
print(factorial_recursive(1))     # Output: 1 (base case)
print(factorial_recursive(6))     # Output: 720 (6*5*4*3*2*1)

