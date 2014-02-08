# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odd_list = []
    for number in some_list:
        if number % 2 != 0:
            odd_list.append(number)
    return odd_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    even_list = []
    for number in some_list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    list_of_long_words = []
    for word in word_list:
        if len(word) >= 4:
            list_of_long_words.append(word)
    return list_of_long_words

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    smallest_elem = some_list[0]
    for number in some_list:
        if number < smallest_elem:
            smallest_elem = number
    return smallest_elem

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    largest_elem = some_list[0]
    for number in some_list:
        if number > largest_elem:
            largest_elem = number
    return largest_elem

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    result = []
    for number in some_list:
        result.append(number/2.0)
    return result

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    lengths = []
    for word in word_list:
        lengths.append(len(word))
    return lengths

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    result = ""
    for string in string_list:
        result += string
    return result

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    sum = sum_numbers(numbers)
    average = sum/(len(numbers))
    return average