#!/bin/sh

echo "抽出したい語を入力してください"
read INPUT

python entry_keyword.py -i $INPUT -o ../data/user.csv
bash create_user_dic.sh ../data/user.csv ~/Downloads/unidic-mecab-2.1.2_src/ user.dic
python extraction_none.py

