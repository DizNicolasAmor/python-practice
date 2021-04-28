from decimal import (Decimal, localcontext)

print('\nPYTHON_EXERCISES_01\n')

def quick_test_runner(current_function, test_data_list):
    print("\tTests:\n")
    for test in test_data_list:
        print("\t" + str(current_function(test[0]) == test[1]) + ": should return " + str(test[1]) + " when input is " + str(test[0]))

print('\nFUNCTIONS:\n')

print("\n  1. create a function which accepts a list of numbers and returns it's sum.\n")

empty_list = []
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

get_sum_from_list_test_data = (
    (empty_list, 0),
    ([1, 2, 3, 4, 5], 15),
    (list_of_float, Decimal('7.8')),
    (list_with_invalid_elements, None),
    (list_with_negatives, -2),
    (list_with_string_numbers, 6),
    (list_with_string_numbers_and_numbers, Decimal('6.3')),
    (simple_string, None),
    (simple_boolean, None),
    (simple_number, None),
    (simple_tuple, 3),
    (simple_set, 3),
    (simple_dictionary, None),
)

quick_test_runner(get_sum_from_list, get_sum_from_list_test_data)


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

get_min_from_list_test_data = (
    (empty_list, None),
    ([1, 2, 3, 4, 5], min([1, 2, 3, 4, 5])),
    (list_of_float, min(list_of_float)),
    (list_with_invalid_elements, None),
    (list_with_negatives, min(list_with_negatives)),
    (list_with_negative_float, min(list_with_negative_float)),
    (list_with_string_numbers, None),
    (list_with_string_numbers_and_numbers, None),
    (simple_string, None),
    (simple_boolean, None),
    (simple_number, None),
    (simple_tuple, 1),
    (simple_set, 1),
    (simple_dictionary, None)
)

quick_test_runner(get_min_from_list, get_min_from_list_test_data)


print("\n  3. create a function which accepts a number and a string (as keyworded arguments only) and prints this string several times (defined by the number)\n")

def repeat_string(*, num_times, initial_string):
    if not isinstance(num_times, int) or isinstance(num_times, bool):
        return
    if not isinstance(initial_string, str):
        return

    result = initial_string * num_times
    # print(result) # line commented just for the quick tests

    return result

def tests_for_repeat_string(test_data_list):
    print("\tTests:\n")
    for test in test_data_list:
        print("\t" + str(repeat_string(num_times = test[0][0], initial_string = test[0][1]) == test[1]) + ": should return " + str(test[1]) + " when input is " + str(test[0]))

string_input = 'Hello world'

repeat_string_test_data = (
    ((0, string_input), ''),
    ((1, string_input), string_input),
    ((2, string_input), 'Hello worldHello world'),
    ((3, string_input), 'Hello worldHello worldHello world'),
    ((simple_string, string_input), None),
    ((simple_boolean, string_input), None),
    ((2.5, string_input), None),
    ((simple_tuple, string_input), None),
    ((simple_set, string_input), None),
    ((simple_dictionary, string_input), None),
    ((1, 1), None),
    ((1, simple_boolean), None),
    ((1, 2.5), None),
    ((1, simple_tuple), None),
    ((1, simple_set), None),
    ((1, simple_dictionary), None),
)

tests_for_repeat_string(repeat_string_test_data)


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

is_number_a_sum_of_three_and_five_test_data = (
    (0, False),
    (1, False),
    (7, False),
    (11, True),
    (12, True),
    (13, True),
    (30, True),
    (50, True),
    (52, True),
    (-1, False),
    (2.5, False),
    (simple_string, None),
    (simple_boolean, None),
    (simple_tuple, None),
    (simple_set, None),
    (simple_dictionary, None)
)

quick_test_runner(is_number_a_sum_of_three_and_five, is_number_a_sum_of_three_and_five_test_data)


print('\nGENERATORS:\n')

print("\n  5. create a function which accepts an iterable and yields each element of that iterable (in 2 ways)")
print("\n  6. create a function which yields numbers 1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21... (infinite sequence)")