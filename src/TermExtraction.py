#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from morph import *

class Rulebase:
  def __init__(self):
    pass
  def _estimate(self, morphs):
    tag_list = []
    flag = 0 
    for morph in morphs:
      if morph.pos1() == "固有名詞" and flag == 0:
        tag_list.append((morph.surface(), "B"))
        flag = 1 
      elif (morph.pos() == "名詞" or morph.surface() == "・") and flag == 1:
        tag_list.append((morph.surface(), "I"))
      else:
        tag_list.append((morph.surface(), "O"))
        flag = 0 
    return tag_list

class Model(Rulebase):
  def __init__(self):
    pass

class TermExtractor(Model):
  def __inti__(self):
    pass
  def extract(self, sentence):
    tag_list = self._estimate(sentence)
    for surface, tag in tag_list:
      print surface, tag

def term_extraction(sentences):
  TE = TermExtractor()
  for sentence in sentences:
    TE.extract(sentence)

def main():
  sentences = create_morphs(sys.argv[1])
  term_extraction(sentences)

if __name__ == "__main__":
  main()



