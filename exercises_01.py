from decimal import (Decimal, localcontext)

print('\nPYTHON_EXERCISES_01\n')

print('\nFUNCTIONS:\n')

print("\n  1. create a function which accepts a list of numbers and returns it's sum.\n")

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

def get_sum_from_list(current_list):
    with localcontext() as ctx:
        ctx.prec  = 2
        if not isinstance(current_list, (list, tuple, set)):
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
print("\t" + str(get_sum_from_list(simple_tuple) == 3) + ": should return correct value when input is a tuple")
print("\t" + str(get_sum_from_list(simple_set) == 3) + ": should return correct value when input is a set")
print("\t" + str(get_sum_from_list(simple_dictionary) == None) + ": should return None when input is a dictionary")


print("\n  2. create a function which accepts a list of numbers and returns it's min/max value (using loops not builtin functions).\n")

def get_min_from_list(current_list):
    if not isinstance(current_list, (list, tuple, set)):
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
print("\t" + str(get_min_from_list(simple_tuple) == 1) + ": should return correct value when input is a tuple")
print("\t" + str(get_min_from_list(simple_set) == 1) + ": should return correct value when input is a set")
print("\t" + str(get_min_from_list(simple_dictionary) == None) + ": should return None when input is a dictionary")


print("\n  3. create a function which accepts a number and a string (as keyworded arguments only) and prints this string several times (defined by the number)\n")

def repeat_string(*, num_times, initial_string):
    if not isinstance(num_times, int) or isinstance(num_times, bool):
        return
    if type(initial_string) is not str:
        return

    result = initial_string * num_times
    # print(result) # line commented just for the quick tests

    return result

string_test = 'Hello world'
string_test_repeated_two_times = 'Hello worldHello world'
string_test_repeated_three_times = 'Hello worldHello worldHello world'

print("\tTests:\n")

print("\t" + str(repeat_string(num_times = 0, initial_string = string_test) == '') + ": should return empty string when num_times is 0")
print("\t" + str(repeat_string(num_times = 1, initial_string = string_test) == string_test) + ": should return same string as param when num_tiems is 1")
print("\t" + str(repeat_string(num_times = 2, initial_string = string_test) == string_test_repeated_two_times) + ": should return initial_string twice when num_tiems is 2")
print("\t" + str(repeat_string(num_times = 3, initial_string = string_test) == string_test_repeated_three_times) + ": should return initial_string three times when num_tiems is 3")
print("\t" + str(repeat_string(num_times = simple_string, initial_string = string_test) == None) + ": should return None when num_times is a string")
print("\t" + str(repeat_string(num_times = simple_boolean, initial_string = string_test) == None) + ": should return None when num_times is a boolean")
print("\t" + str(repeat_string(num_times = 2.5, initial_string = string_test) == None) + ": should return None when num_times is a float")
print("\t" + str(repeat_string(num_times = simple_tuple, initial_string = string_test) == None) + ": should return None when num_times is a tuple")
print("\t" + str(repeat_string(num_times = simple_set, initial_string = string_test) == None) + ": should return None when num_times is a set")
print("\t" + str(repeat_string(num_times = simple_dictionary, initial_string = string_test) == None) + ": should return None when num_times is a dictionary")
print("\t" + str(repeat_string(num_times = 1, initial_string = 1) == None) + ": should return None when initial_string is a number")
print("\t" + str(repeat_string(num_times = 1, initial_string = simple_boolean) == None) + ": should return None when initial_string is a boolean")
print("\t" + str(repeat_string(num_times = 1, initial_string = 2.5) == None) + ": should return None when initial_string is a float")
print("\t" + str(repeat_string(num_times = 1, initial_string = simple_tuple) == None) + ": should return None when initial_string is a tuple")
print("\t" + str(repeat_string(num_times = 1, initial_string = simple_set) == None) + ": should return None when initial_string is a set")
print("\t" + str(repeat_string(num_times = 1, initial_string = simple_dictionary) == None) + ": should return None when initial_string is a dictionary")


print("\n  4. create a function which accepts a number which defines if this number could be described as sum of 3's and 5's in any variations (example: f(3) -> True, f(13) -> True, f(4) -> False)\n")

def is_number_a_sum_of_three_and_five(current_number):
    if type(current_number) is float:
        return False
    if type(current_number) is not int:
        return

    aux = 0

    while aux*5 < current_number:
        if (current_number - (aux * 3)) % 5 == 0:
            return True
        if (current_number - (aux * 5)) % 3 == 0:
            return True
        aux += 1

    return False

print("\tTests:\n")

print("\t" + str(is_number_a_sum_of_three_and_five(0) == False) + ": should return False when param is 0")
print("\t" + str(is_number_a_sum_of_three_and_five(1) == False) + ": should return False when param is 1")
print("\t" + str(is_number_a_sum_of_three_and_five(7) == False) + ": should return False when param is 7")
print("\t" + str(is_number_a_sum_of_three_and_five(11) == True) + ": should return True when param is 11")
print("\t" + str(is_number_a_sum_of_three_and_five(12) == True) + ": should return True when param is 12")
print("\t" + str(is_number_a_sum_of_three_and_five(13) == True) + ": should return True when param is 13")
print("\t" + str(is_number_a_sum_of_three_and_five(30) == True) + ": should return True when param is 30")
print("\t" + str(is_number_a_sum_of_three_and_five(50) == True) + ": should return True when param is 50")
print("\t" + str(is_number_a_sum_of_three_and_five(52) == True) + ": should return True when param is 52")
print("\t" + str(is_number_a_sum_of_three_and_five(-1) == False) + ": should return False when param is a negative int")
print("\t" + str(is_number_a_sum_of_three_and_five(2.5) == False) + ": should return False when param is a Float")
print("\t" + str(is_number_a_sum_of_three_and_five(simple_string) == None) + ": should return None when param is a string")
print("\t" + str(is_number_a_sum_of_three_and_five(simple_boolean) == None) + ": should return None when param is a boolean")
print("\t" + str(is_number_a_sum_of_three_and_five(simple_tuple) == None) + ": should return None when param is a tuple")
print("\t" + str(is_number_a_sum_of_three_and_five(simple_set) == None) + ": should return None when param is a set")
print("\t" + str(is_number_a_sum_of_three_and_five(simple_dictionary) == None) + ": should return None when param is a dictionary")

print('\nGENERATORS:\n')

print("\n  5. create a function which accepts an iterable and yields each element of that iterable (in 2 ways)")
print("\n  6. create a function which yields numbers 1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21... (infinite sequence)")