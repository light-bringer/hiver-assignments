'''
An anagram is defined as a word, phrase, or sentence formed from another by rearranging its
letters. For example spar and rasp are anagrams.
Given a list of strings, identify the largest anagram group and return it. For example consider the
following list:
["abc", "abfr", "gkn", "cab", "frba", "qgf", "gqf", "bac"]
The above list has 4 anagram groups:
["abc", "cab", "bac"],
["abfr", "frba"],
["gkn"],
["qgf", "gqf"]
The largest anagram group is ["abc", "cab", "bac"] containing the maximum elements (three), so it
will be the answer.
Note:
1. There will be always just 1 largest anagram group.
2. The order the strings in the result should be the order as they appear in input.

import operator

'''

from __future__ import print_function
from collections import defaultdict

strings = ["abc", "abfr", "gkn", "cab", "frba", "qgf", "gqf", "bac", "arbf", "fbra", "afrb"]

def anagram_group(strings):
    agram_dict = defaultdict(list)
    
    for string in strings: 
        agram_dict["".join(sorted(string))].append(string)
    print(agram_dict)
    max_key = max(agram_dict, key=lambda key: len(agram_dict[key]))
    return agram_dict[max_key]

    
def test():
    testcases = (["abc", "abfr", "gkn", "cab", "frba", "qgf", "gqf", "bac", "arbf", "fbra", "afrb"], ["abc", "abfr", "gkn", "cab", "frba", "qgf", "gqf", "bac"])
    for testcase in testcases:
        print(anagram_group(testcase))

def main():
    strings = input("enter strings separated by a space").split()
    print(anagram_group(strings))


if __name__ == "__main__":
    test()
    main()