# -*- coding: utf-8 -*-
# @Time : 2020/10/19 18:11
# @Author : Jclian91
# @File : predict_crf++.py
# @Place : Yangpu, Shanghai
import os
text = "上海野生动物园群熊伤人事件救援画面曝光"
# text = "浙江正筹划疫苗接种工作，当地相关部门：仍仅限于紧急接种小部分人群"
# text = "亚阿停火4分钟又开炮？在法亚美尼亚人抗议 阿塞拜疆使馆前举旗"
# text = "土耳其被曝秘密试射俄制S400防空导弹 美方高层放出狠话"
# text = "国家税务总局稽查局副局长林枫接受纪律审查和监察调查"
# text = "科技助力产业兴 澜沧旧貌换新颜"
# text = "羊毛党不过是流量"
# text = "广西龙胜金秋梯田美如画"
# text = "早在上映第四天，《姜子牙》累计票房就已经高达10.36亿，后来单日票房一路下跌，最低时跌至500万左右，是同档期对手《我和我的家乡》的五分之一，甚至还不及小成本电影《一点就到家》，位列国庆档新片倒数第二。用“断崖式下跌”来形容这部国漫新作的单日票房走向毫不为过。"
# text = "15日，莘庄工业区新时代文明实践的“大本营”——坐落于颛盛路745号的莘庄工业区新时代文明实践分中心正式落成。"

# 生成待预测的文本
with open("predict.data", "w", encoding="utf-8") as g:
    for char in text:
        g.write("%s\tn\tB-Char\n" % char)

# 利用CRF模型，调用命令行进行预测
os.system("crf_test -m model predict.data > predict_new.txt")

# 处理预测后的进行，并将其加工成中文分词后的结果
with open("predict_new.txt", "r", encoding="utf-8") as f:
    content = [_.strip() for _ in f.readlines()]

predict_tags = []
for line in content:
    predict_tags.append(line.split("\t")[-1])

words = []
for i in range(len(predict_tags)):
    word = ""
    if predict_tags[i] == "B-Char":
        word += text[i]
        j = i + 1
        while j < len(text) and predict_tags[j] == "I-Char":
            word += text[j]
            j += 1

    if word:
        words.append(word)

print("原句:%s" % text)
print("分词结果:%s" % ("/".join(words)))
