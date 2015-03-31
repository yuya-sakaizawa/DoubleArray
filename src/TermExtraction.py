#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from morph import *

class Model:
  def __init__(self):
    pass
  def estimate(self, morphs):
    """
    input	morphs
    output	{B, I, O}
    """
    pass

class RulebaseModel(Model):
  def __init__(self):
    pass
  def estimate(self, morphs):
    """
    input	morphs
    output	{B, I, O}
    """
    tag_list = []
    flag = 0 
    for morph in morphs:
      if morph.pos1() == "固有名詞" and flag == 0:
        tag_list.append((morph.surface(), "B"))
        flag = 1 
      elif morph.pos() == "名詞" and flag == 1:
        tag_list.append((morph.surface(), "I"))
      else:
        tag_list.append((morph.surface(), "O"))
        flag = 0 
    return tag_list

class TermExtractor:
  def __init__(self, model):
    self.model = model
  def extract(self, sentence):
    """
    input	sentence
    output	term
    """
    term = ""
    flag = 0
    term_list = []
    tag_list = self.model.estimate(sentence)
    for surface, tag in tag_list:
      if tag == "B" and flag == 0:
        flag = 1
        term += surface
      elif tag == "I" and flag == 1:
        term += surface
      elif tag == "B" and flag == 1:
        term_list.append(term)
        term = surface
      else:
        if term != "":
          term_list.append(term)
          term = ""
          flag = 0
    return term_list

def term_extraction(sentences):
  model = RulebaseModel()
  TE = TermExtractor(model)
  terms = []
  term_list = []
  for sentence in sentences:
    term_list = TE.extract(sentence)
    terms.append(term_list)
    term_list = []
  for term_list in terms:
    for term in term_list:
      print term

def main():
  sentences = create_morphs(sys.argv[1])
  term_extraction(sentences)

if __name__ == "__main__":
  main()



