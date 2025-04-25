def sum_list_elements(lst):
    total = 0  # Initialize a variable to store the sum
    
    # Loop through each number in the list
    for num in lst:
        total += num  # Add the current number to the total
    
    return total  # Return the final sum
    # Calling the function with different lists
print(sum_list_elements([1, 2, 3]))       # Output: 6 (1+2+3)
print(sum_list_elements([10, 20, 30]))    # Output: 60 (10+20+30)
print(sum_list_elements([-1, 0, 1]))      # Output: 0 (-1+0+1)

