from pyhanlp import *
import flask
import requests
from flask import request, jsonify

# http://www.hankcs.com/nlp/part-of-speech-tagging.html#h2-8 词性标注

# 格式：[编号:{{实体名: object}, {类型: category}, {起始位置: start_pos}, {结束位置: end_pos}}]
# 格式：{编号: 实体，类型标志，类型，起始位置，结束位置}

resource="resource.txt"
ans="ans.txt"

word_character_dict = {}
with open('word_character.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
for line in lines:
    key = line.split(' ')[0]
    value = line.split(' ')[1].replace('\n', '')
    word_character_dict.update({key: value})

app = flask.Flask('__name__')
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"
@app.route('/ner1', methods=['get', 'post'])
def get_ner():
    # sentence = request.values.get('sentence')
    word_dict = {}
    with open(resource, 'r', encoding='utf8')  as f, open(ans, 'w', encoding='utf8') as f1:
        lines = f.readlines()
        for line in lines:
            cut_words = HanLP.segment(line)
            
            pos = 0
            id = 0
            
            for word in cut_words:
                word_list = []
                object = str(word).split('/')[0]
                category_code = str(word).split('/')[1]
                if word_character_dict.__contains__(category_code):
                    start_pos = pos
                    end_pos = pos + len(object) - 1
                    word_list.append(object)
                    # word_list.append(category_code)
                    category = word_character_dict[category_code]
                    word_list.append(" ")
                    word_list.append(category)
                    # word_list.append(start_pos)
                    # word_list.append(end_pos)
                    word_dict.update({id: word_list})
                    id += 1
                    pos = end_pos + 1
                    for i in word_list:
                        f1.write(str(i))
                    f1.write('\n')
        print("finish")
            


    # return words_list
    return jsonify({"code": 200, "msg": word_dict})

if __name__ == '__main__':
    # get_ner('')
    app.run(debug=True, port=8891, host='127.0.0.1')