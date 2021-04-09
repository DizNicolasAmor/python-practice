from decimal import (Decimal, getcontext)

print('\nPYTHON_EXERCISES_01\n')

print('\nFUNCTIONS:\n')

print("  1. create a function which accepts a list of numbers and returns it's sum.\n")

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

print("\t" + str(get_sum_from_list([]) == 0) + ": should return 0 if list is empty")
listOfIntThatSum15 = [1, 2, 3, 4, 5]
print("\t" + str(get_sum_from_list(listOfIntThatSum15) == 15) + ": should return the sum  of the int list")
listOfFloat = [1.0, 2.3, 4.5]
print("\t" + str(get_sum_from_list(listOfFloat) == Decimal('7.8')) + ": should return the sum of the float list")
listWithInvalidElements = [1, '2', 3, 'Monday']
print("\t" + str(get_sum_from_list(listWithInvalidElements) == None) + ": should return None when list contains invalid data type")
print("\t" + str(get_sum_from_list([1, 3, -10, 4]) == -2) + ": should handle list with negative int")
print("\t" + str(get_sum_from_list([0, 9.4, -4.3, 1.1]) == Decimal('6.2')) + ": should handle list with negative float")
print("\t" + str(get_sum_from_list(["1", "2", "3"]) == 6) + ": should handle list with numbers as strings")
print("\t" + str(get_sum_from_list(["1", 2, 3.3]) == Decimal('6.3')) + ": should handle list with numbers and string as numbers")
print("\t" + str(get_sum_from_list('invalid input') == None) + ": should return None when input is a string")
print("\t" + str(get_sum_from_list(True) == None) + ": should return None when input is a boolean")
print("\t" + str(get_sum_from_list(1) == None) + ": should return None when input is a number")
print("\t" + str(get_sum_from_list((1, 2)) == None) + ": should return None when input is a tuple")
print("\t" + str(get_sum_from_list({1, 2}) == None) + ": should return None when input is a set")
print("\t" + str(get_sum_from_list({'a': 1, 'b': 2}) == None) + ": should return None when input is a dictionary")

print("\n  2. create a function which accepts a list of numbers and returns it's min/max value (using loops not builtin functions)")
print("\n  3. create a function which accepts a number and a string (as keyworded arguments only) and prints this string several times (defined by the number)")
print("\n  4. create a function which accepts a number which defines if this number could be described as sum of 3's and 5's in any variations (example: f(3) -> True, f(13) -> True, f(4) -> False)")

print('\nGENERATORS:\n')

print("\n  5. create a function which accepts an iterable and yields each element of that iterable (in 2 ways)")
print("\n  6. create a function which yields numbers 1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 21... (infinite sequence)")