# -*- coding: utf-8 -*-
# @Time : 2020/10/19 21:23
# @Author : Jclian91
# @File : model_evaluate_crf++.py
# @Place : Yangpu, Shanghai
from seqeval.metrics import f1_score
from seqeval.metrics import precision_score
from seqeval.metrics import accuracy_score
from seqeval.metrics import recall_score
from seqeval.metrics import classification_report

with open("crf_pred.txt", "r", encoding="utf-8") as f:
    content = [_.strip() for _ in f.readlines()]

y_pred = []
y_true = []
for line in content:
    if line:
        y_pred.append(line.split("\t")[-1])
        y_true.append(line.split("\t")[-2])

print("accuary: ", accuracy_score(y_true, y_pred))
print("p: ", precision_score(y_true, y_pred))
print("r: ", recall_score(y_true, y_pred))
print("f1: ", f1_score(y_true, y_pred))
print("classification report: ")
print(classification_report(y_true, y_pred))
