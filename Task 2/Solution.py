def counting_sort(digits):
    # Find the maximum digit in the list
    Max = max(digits)
    
    # Initialize variables for sorting
    arr_in_desc_order = []
    count = [0] * (Max + 1)
    
    # Count the occurrences of each digit
    for i in digits:
        count[i] += 1
    
    # Create a sorted list in descending order
    for i in range(Max, -1, -1):
        arr_in_desc_order.extend([i] * count[i])
    
    # Convert the sorted list to an integer
    return int(''.join(map(str, arr_in_desc_order)))


def solution(l):
    import itertools
    
    # Initialize variables for finding the highest divisible number
    highest_divisible_number = 0
    curr_length = len(l)
    
    # Iterate through different combinations of the input list
    while curr_length > 0:
        combinations = itertools.combinations(l, curr_length)
        
        for i in combinations:
            combined_number = int("".join(map(str, i)))
            
            # Check if the combined number is divisible by 3
            if combined_number % 3 == 0:
                # Sort the digits of the combined number using counting_sort
                combined_number = counting_sort(i)
                
                # Update the highest divisible number
                highest_divisible_number = max(highest_divisible_number, combined_number)
        
        curr_length -= 1
    
    # Convert the digits of the highest divisible number to a sorted integer
    digits = [int(digit) for digit in str(highest_divisible_number)]
    return counting_sort(digits)


# Example usage:
# input_list = [3,1,4,1]
# result = solution(input_list)
# print(result)