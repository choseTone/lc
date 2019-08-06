__author__ = 'wangqc'
# https://leetcode.com/problems/unique-word-abbreviation/

import collections

class ValidWordAbbr:

    def __init__(self, dictionary):
        self.dict = collections.defaultdict(set)
        for word in dictionary:
            if word: self.dict[f"{word[0]}{len(word)}{word[-1]}"].add(word)

    def isUnique(self, word):
        return not word or self.dict[f"{word[0]}{len(word)}{word[-1]}"] <= {word}


if __name__ == '__main__':

    obj = ValidWordAbbr(["", "deer","door","cake","card"])
    print(obj.isUnique("dear"))
    print(obj.isUnique("cart"))
    print(obj.isUnique("cane"))
    print(obj.isUnique("make"))
    print(obj.isUnique(""))

