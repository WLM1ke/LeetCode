# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

import collections


class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        sym = set()
        rez = 0

        counter = collections.defaultdict(int)

        for word in words:
            rev = word[::-1]
            if word != rev:
                if counter[rev] > 0:
                    rez += 2
                    counter[rev] -= 1
                else:
                    counter[word] += 1
            elif counter[word] > 0:
                rez += 2
                counter[word] = 0
                sym.remove(word)
            else:
                counter[word] = 1
                sym.add(word)

        return (rez + (len(sym) > 0)) * 2
