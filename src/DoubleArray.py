#!/usr/bin/python
# -*- coding:utf-8 -*-

from collections import defaultdict

class DoubleArray:
    def __init__(self, words):
        self.base, self.check, self.code = \
                                    self._build(words)

    def _build(self, words):
        base = []
        check = []
        code = defaultdict(lambda:0)
        count = 1
        for word in words:
            for ch in word:
                if ch not in code:
                    code[ch] = count
                    count += 1
            if None not in code:
                code[None] = count
                count += 1
        decode_word = []
        decode_words = []
        for word in words:
            for ch in word:
                decode_word.append(code[ch])
            decode_word.append(code[None])
            decode_words.append(decode_word)
            decode_word = []

        base.extend(0 for n in xrange(len(words)*6))
        check.extend(-1 for n in xrange(len(words)*6))
        base_index = 0
        check_index = 0
        for word in decode_words:
            for ch in word:
                check_index = base[base_index] + ch
                if check[check_index] == base_index:
                    base_index = check_index
                    continue
                elif check[check_index] == -1:
                    check[check_index] = base_index
                    if ch == code[None]:
                        base[check_index] = -1
                    else:
                        base[check_index] = len(code.items())
                    base_index = check_index
                else:
                    for i in range(1, 10000):
                        check_index += 1
                        if check[check_index] != -1:
                            continue
                        else:
                            check[check_index] = base_index
                            if ch == code[None]:
                                base[check_index] = -1
                            else:
                                base[check_index] = len(code.items())
                            base[base_index] += i
                            base_index = check_index
                            break
            base_index = 0
        return base, check, code

    def common_prefix_search(self, word):
        prefix = ""
        prefix_list = []
        for ch in word:
            prefix += ch
            if self.search(prefix):
                prefix_list.append(prefix)
        return prefix_list

    def search(self, word):
        base_index = 0
        check_index = 0
        decode_num = []
        for ch in word:
            decode_num.append(self.code[ch])
        decode_num.append(self.code[None])
        for ch in decode_num:
            check_index = self.base[base_index] + int(ch)
            if base_index != self.check[check_index]:
                return None
            base_index = check_index
        if self.base[base_index] == -1:
            return True

if __name__ == "__main__":
    words = ["cat", "center", "cut", "cute", "do", "dog", "fox",  "rat"]
    DA = DoubleArray(words)
    for key, value in sorted(DA.code.items(), key=lambda x:x[1]):
        print key, value
    for i in range(len(DA.base)):
        print i, DA.base[i], DA.check[i]
    print words
    print DA.search("cat")
    print DA.search("cut")
    print DA.common_prefix_search("cats")

