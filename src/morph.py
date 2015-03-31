#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

class Morph:
  def __init__(self, surface, base, pos, pos1):
    self.__surface = surface
    self.__base = base
    self.__pos = pos
    self.__pos1 = pos1
  def surface(self):
    return self.__surface
  def base(self):
    return self.__base
  def pos(self):
    return self.__pos
  def pos1(self):
    return self.__pos1
  def __eq__(self, other):
    return self.__surface == other.__surface and self.__base == other.__base \
       and self.__pos == other.__pos and self.__pos1 == other.__pos1
  def __ne__(self, other):
    return self.__surface != other.__surface or self.__base != other.__base \
       or self.__pos != other.__pos or self.__pos1 != other.__pos1


def create_morphs(text_file):

  morphs = []
  morph_list = []
  for line in open(text_file):
    if "* " in line:
      pass
    elif line.strip() == "EOS":
      morphs.append(morph_list)
      morph_list = []
    else:
      line_item = line.strip().split('\t')
      surface = line_item[0]
      base = line_item[1].split(',')[6]
      pos = line_item[1].split(',')[0]
      pos1 = line_item[1].split(',')[1]
      morph_list.append(Morph(surface, base, pos, pos1))

  return morphs

def main():
  create_morphs(sys.argv[1])

if __name__ == "__main__":
  main()




