# -*- coding: utf-8 -*-
# @Time : 2020/10/19 12:04
# @Author : Jclian91
# @File : read_segment_corpus.py
# @Place : Yangpu, Shanghai

train_data = []
test_data = []


# 人民日报语料
with open("./data/199801.txt", "r", encoding="gbk") as f:
    content = [_.strip() for _ in f.readlines() if _.strip()]

# 训练数据
for line in content[:int(len(content)*0.9)]:
    sent_tag = []
    for item in line.split()[1:]:
        word = item.split("/")[0]
        postag = item.split("/")[1]
        for i in range(len(word)):
            if i:
                char_tuple = (word[i], "n", "I-Char")
            else:
                char_tuple = (word[i], "n", "B-Char")

            sent_tag.append(char_tuple)

    train_data.append(sent_tag)

# 测试数据
for line in content[int(len(content)*0.9)+1:]:
    sent_tag = []
    for item in line.split()[1:]:
        word = item.split("/")[0]
        postag = item.split("/")[1]
        for i in range(len(word)):
            if i:
                char_tuple = (word[i], "n", "I-Char")
            else:
                char_tuple = (word[i], "n", "B-Char")

            sent_tag.append(char_tuple)

    test_data.append(sent_tag)


# MSR语料(微软中文分词语料)
with open("./data/msr_training.utf8", "r", encoding="utf-8") as g:
    content = [_.strip() for _ in g.readlines() if _.strip()]

# 训练数据
for line in content[:int(len(content)*0.9)]:
    sent_tag = []
    for item in line.split():
        word = item
        for i in range(len(word)):
            if i:
                char_tuple = (word[i], "n", "I-Char")
            else:
                char_tuple = (word[i], "n", "B-Char")

            sent_tag.append(char_tuple)

    train_data.append(sent_tag)

# 测试数据
for line in content[int(len(content)*0.9)+1:]:
    sent_tag = []
    for item in line.split():
        word = item
        for i in range(len(word)):
            if i:
                char_tuple = (word[i], "n", "I-Char")
            else:
                char_tuple = (word[i], "n", "B-Char")

            sent_tag.append(char_tuple)

    test_data.append(sent_tag)

print(len(train_data))
print(len(test_data))

# 将数据格式整理成CRF++的格式
# 将数据集分为训练集和测试集，比例为9:1
with open("train.txt", "w", encoding="utf-8") as f:
    for line in train_data:
        for word_tuple in line:
            f.write("\t".join(list(word_tuple))+"\n")
        f.write("\n")

with open("predict.txt", "w", encoding="utf-8") as f:
    for line in test_data:
        for word_tuple in line:
            f.write("\t".join(list(word_tuple))+"\n")
        f.write("\n")
