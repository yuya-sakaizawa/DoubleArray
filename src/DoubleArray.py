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
        words = [word+"#" for word in words]
        for word in words:
            for ch in word:
                if ch not in code:
                    code[ch] = count
                    count += 1

        base.extend(0 for n in xrange(count*5))
        check.extend(-1 for n in xrange(count*5))
        base_index = 0
        check_index = 0
        for word in words:
            for ch in word:
                check_index = base[base_index] + code[ch]
                if check[check_index] == -1 or check[check_index] == base_index:
                    check[check_index] = base_index
                    if ch == "#":
                        base[check_index] = -1
                    else:
                        base[check_index] = len(code.items())
                    base_index = check_index
                else:
                    for i in range(1, 100):
                        check_index += 1
                        if check[check_index] != -1:
                            continue
                        else:
                            check[check_index] = base_index
                            if ch == "#":
                                base[check_index] = -1
                            else:
                                base[check_index] = len(code.items())
                            base[base_index] += i
                            base_index = check_index
                            break
                print ch
                print base
                print check
            base_index = 0
        return base, check, code

    def common_prefix_search(self, word):
        prefix = ""
        prefix_list = []
        for ch in word:
            prefix += ch
            print prefix
            if self.search(prefix):
                prefix_list.append(prefix)
        return prefix_list
            

    def search(self, word):
        base_index = 0
        check_index = 0
        word = word+"#"
        for ch in word:
            check_index = self.base[base_index] + self.code[ch]
            if base_index != self.check[check_index]:
                #print base_index
                #print check_index
                #print self.check[check_index]
                return None
            base_index = check_index
        if self.base[base_index] == -1:
            return True

if __name__ == "__main__":
    words = ["ca", "cat", "do", "dog", "fox", "rat"]
    DA = DoubleArray(words)
    for key, value in sorted(DA.code.items(), key=lambda x:x[1]):
        print key, value
    print DA.base
    print DA.check
    print DA.search("ca")
    print DA.search("cat")
    print DA.search("do")
    print DA.search("dog")
    print DA.search("fox")
    print DA.search("rat")
    print DA.common_prefix_search("cats")

