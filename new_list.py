# pseudocode

# Create a function that is responsible for making a new list
def create_new_list(list_1, list_2):
    odd_numbers = [num for num in list_1 if num % 2 != 0]
    even_numbers = [num for num in list_2 if num % 2 == 0]

    result_list = odd_numbers + even_numbers
    return result_list

# Create two lists
list_1 = [10, 20, 25, 30, 35]
list_2 = [40, 45, 60, 75, 90]

# Create a variable that can be used to call the function
new_list = create_new_list(list_1, list_2)

# Print the 1st, 2nd and new lists
print("List 1:", list_1)
print("List 2:", list_2)
print("Result list:", new_list)