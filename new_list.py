# pseudocode

# Create a function that is responsible for making a new list
def create_new_list(list_1, list_2):
    odd_numbers = [num for num in list_1 if num % 2 != 0]
    even_numbers = [num for num in list_2 if num % 2 == 0]

    result_list = odd_numbers + even_numbers
    return result_list

# Create two lists

# Create a variable that can be used to call the function

# Print the 1st, 2nd and new lists