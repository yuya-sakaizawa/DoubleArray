csv=$1
src_dic=$2
dst_dic=$3

/opt/local/libexec/mecab/mecab-dict-index -d $src_dic -u $dst_dic -f utf8 -t utf8 $csv
