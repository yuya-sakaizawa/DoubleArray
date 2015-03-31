#!/usr/bin/python
# -*- coding:utf-8 -*-

import MeCab

def keyword_extraction(text):
  """
  input:text
  output:keywords
  """
  tagger = MeCab.Tagger("-d /opt/local/lib/mecab/dic/unidic-utf8 -u user.dic")
  node = tagger.parseToNode(text.encode('utf-8'))
  keywords = []
  while node:
    if node.feature.split(",")[0] == "名詞":
      keywords.append(node.surface)
    node = node.next
  return keywords


if __name__ == "__main__":
  text = u"""人工知能は、コンピュータに人間と同様の知能を実現させようという試み、あるいはそのための一連の基礎技術をさす。人工知能という名前は1956年にダートマス会議でジョン・マッカーシーにより命名された。現在では、機械学習、自然言語処理、パターン認識などの研究分野がある。"""
  keywords = keyword_extraction(text)
  for word in keywords:
    print word,



