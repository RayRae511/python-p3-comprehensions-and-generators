#!/usr/bin/env python3

def return_evens(num_list):
    return [n % 2 == 0 for n in num_list]

num_list = range(0,11)
even_numbers = return_evens(num_list)
print(even_numbers)


def make_exclamation(sentence_list):
    return (sentence + '!' for sentence in sentence_list)


sentence_list = ['Hello', "I'm doing great", 'Python is fun']
exclamained_sentences = make_exclamation(sentence_list)
print(exclamained_sentences)