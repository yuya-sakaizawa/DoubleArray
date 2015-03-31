#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import argparse

def get_args():
  """ 
  optional argument setting
  """
  parser = argparse.ArgumentParser()

  parser.add_argument(
      "-i", "--input",
      dest="keyword",
      required=True,
      help="input keyword"
  )
  parser.add_argument(
      "-o", "--output",
      dest="output_file",
      type=argparse.FileType("a+"),
      default=sys.stdout,
      help="output filename as csv"
  )   
  return parser.parse_args()

def entry_keyword():
  print >> args.output_file, "%s,-1,-1,-1000,名詞,固有名詞,一般,*,*,*,*,*,*,登録" \
                                     % (args.keyword)

def main():
  entry_keyword()

if __name__ == "__main__":
  args = get_args()
  main()



