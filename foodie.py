#-*- coding : utf-8 -*-
# coding: utf-8

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
txt = open("foodie.txt", "r").read()

ex = {'我们', '可以','具体','信息','以便','不能','反馈','什么','怎么','评论','756131624','删除','现在','之后','出来','该条','不好','484626750','官方','加入','带来','不便','请谅解','QQ','提供','这个', '问题','问题', '开发者', '为什么', '已经','没有', '不了', '版本', '解决', '回复'}

ls = []
words = jieba.lcut(txt)
counts = {}
for word in words:
    ls.append(word)
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

for word in ex:
    del (counts[word])

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{:<10}{:>5}".format(word, count))

wz = open('ms.txt', 'w+')
wz.write(str(ls))

# print(ls)

wzhz = WordCloud(background_color="white",width=1200, height=1000,min_font_size=6, margin=2).generate(" ".join(ls))

plt.imshow(wzhz)
plt.axis("off")
plt.show()