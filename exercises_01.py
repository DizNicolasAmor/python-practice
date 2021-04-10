from decimal import (Decimal, getcontext)

print('\nPYTHON_EXERCISES_01\n')

print('\nFUNCTIONS:\n')

empty_list = []
list_of_int_that_sums_15 = [1, 2, 3, 4, 5]
list_of_float = [1.0, 2.3, 4.5]
list_with_invalid_elements = [1, '2', 3, 'Monday']
list_with_negatives = [1, 3, -10, 4]
list_with_negative_float = [0, 9.4, -4.3, 1.1]
list_with_string_numbers = ["1", "2", "3"]
list_with_string_numbers_and_numbers = ["1", 2, 3.3]
simple_string = 'simple string'
simple_boolean = True
simple_number = 1
simple_tuple = (1, 2)
simple_set = {1, 2}
simple_dictionary = {'a': 1, 'b': 2}


print("\n  1. create a function which accepts a list of numbers and returns it's sum.\n")

def get_sum_from_list(current_list):
    getcontext().prec = 2
    if not isinstance(current_list, list):
        return
    acc = 0
    for element in current_list:
        try:
            acc += Decimal(element)
        except:
            return
    return Decimal(acc)

print("\tTests:\n")

print("\t" + str(get_sum_from_list(empty_list) == 0) + ": should return 0 if list is empty")
print("\t" + str(get_sum_from_list(list_of_int_that_sums_15) == 15) + ": should return the sum  of the int list")
print("\t" + str(get_sum_from_list(list_of_float) == Decimal('7.8')) + ": should return the sum of the float list")
print("\t" + str(get_sum_from_list(list_with_invalid_elements) == None) + ": should return None when list contains invalid data type")
print("\t" + str(get_sum_from_list(list_with_negatives) == -2) + ": should handle list with negative int")
print("\t" + str(get_sum_from_list(list_with_negative_float) == Decimal('6.2')) + ": should handle list with negative float")
print("\t" + str(get_sum_from_list(list_with_string_numbers) == 6) + ": should handle list with numbers as strings")
print("\t" + str(get_sum_from_list(list_with_string_numbers_and_numbers) == Decimal('6.3')) + ": should handle list with numbers and string as numbers")
print("\t" + str(get_sum_from_list(simple_string) == None) + ": should return None when input is a string")
print("\t" + str(get_sum_from_list(simple_boolean) == None) + ": should return None when input is a boolean")
print("\t" + str(get_sum_from_list(simple_number) == None) + ": should return None when input is a number")
print("\t" + str(get_sum_from_list(simple_tuple) == None) + ": should return None when input is a tuple")
print("\t" + str(get_sum_from_list(simple_set) == None) + ": should return None when input is a set")
print("\t" + str(get_sum_from_list(simple_dictionary) == None) + ": should return None when input is a dictionary")


print("\n  2. create a function which accepts a list of numbers and returns it's min/max value (using loops not builtin functions).\n")

def get_min_from_list(current_list):
    if not isinstance(current_list, list):
        return
    if not len(current_list):
        return

    for index, value in enumerate(current_list):
        if not isinstance(value, (int, float)):
            return

        if (index) == 0:
            result = value
        elif value < result:
            result = value

    return result

print("\tTests:\n")

print("\t" + str(get_min_from_list(empty_list) == None) + ": should return None if list is empty")
print("\t" + str(get_min_from_list(list_of_int_that_sums_15) == min(list_of_int_that_sums_15)) + ": should return the min  of the int list")
print("\t" + str(get_min_from_list(list_of_float) == min(list_of_float)) + ": should return the min of the float list")
print("\t" + str(get_min_from_list(list_with_invalid_elements) == None) + ": should return None when list contains invalid data type")
print("\t" + str(get_min_from_list(list_with_negatives) == min(list_with_negatives)) + ": should return min of list with negative ints")
print("\t" + str(get_min_from_list(list_with_negative_float) == min(list_with_negative_float)) + ": should return min in list with negatives and floats")
print("\t" + str(get_min_from_list(list_with_string_numbers) == None) + ": should return None if there are numbers as strings")
print("\t" + str(get_min_from_list(list_with_string_numbers_and_numbers) == None) + ": should return None if there are numbers and numbers as strings")
print("\t" + str(get_min_from_list(simple_string) == None) + ": should return None when input is a string")
print("\t" + str(get_min_from_list(simple_boolean) == None) + ": should return None when input is a boolean")
print("\t" + str(get_min_from_list(simple_number) == None) + ": should return None when input is a number")
print("\t" + str(get_min_from_list(simple_tuple) == None) + ": should return None when input is a tuple")
print("\t" + str(get_min_from_list(simple_set) == None) + ": should return None when input is a set")
print("\t" + str(get_min_from_list(simple_dictionary) == None) + ": should return None when input is a dictionary")

print("\n  3. create a function which accepts a number and a string (as keyworded arguments only) and prints this string several times (defined by the number)")
print("\n  4. create a function which accepts a number which defines if this number could be described as sum of 3's and 5's in any variations (example: f(3) -> True, f(13) -> True, f(4) -> False)")

print('\nGENERATORS:\n')

print("\n  5. create a function which accepts an iterable and yields each element of that iterable (in 2 ways)")
print("\n  6. create a function which yields numbers 1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21... (infinite sequence)")