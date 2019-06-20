#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Kashfar"

# YOUR HELPER FUNCTION GOES HERE


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = raw_input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()
    regex_word = test_word.replace(' ', '\\w')
    result = [
        word for word in words if len(test_word) == len(word) and re.match(regex_word, word)
    ]
    # for word in words:
    #     if len(test_word) == len(word):
    #         regex_word = test_word.replace(' ', '\\w')

    #         match_object = re.match(regex_word, word)
    #         if match_object:
    #             result.append(word)
    print(result)


if __name__ == '__main__':
    main()