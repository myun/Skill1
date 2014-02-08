import Skills1

numbers = [1,2,3,4,4,5,6,7,8,9,10]
print "All odd numbers: ", Skills1.all_odd(numbers)
print "All even numbers: ", Skills1.all_even(numbers)

words = ["hello", "Shakespeare", "Othello", "Mermaid", "coconuts", "hi", "bell"]

print "All words with length greater than or equal to 4 characters: ", Skills1.long_words(words)
print "The smallest number is: ", Skills1.smallest(numbers)
print "The greatest number is: ", Skills1.largest(numbers)
print "Here is a list of all the numbers divided by two. ", Skills1.halvesies(numbers)
print "Here is a list of all the word lengths. ", Skills1.word_lengths(words)
print "Here is a sum of all the numbers. ", Skills1.sum_numbers(numbers)
print "Here is the result of multiplying all the numbers. ", Skills1.mult_numbers(numbers)

print "Here are all of the words joined together. ", Skills1.join_strings(words)
print "This is the average of all the numbers. ", Skills1.average(numbers)