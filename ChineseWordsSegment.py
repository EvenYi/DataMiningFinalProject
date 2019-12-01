import Datapreprocess
import jieba.posseg as pseg
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pkuseg
import jieba

movie_comment_list = Datapreprocess.move_comment()
print(movie_comment_list[5][1])
# seg = pkuseg.pkuseg(model_name='web',postag=True)           # 以默认配置加载模型
# text = seg.cut(movie_comment_list[5][1])  # 进行分词
# print(text)
words_clean_list1 = ['x', 'r', 'w', 't', 'ul', 'uj', 'ug', 'd']
words_clean_list2 = ['是']
seg_list = pseg.cut(movie_comment_list[5][1])
words_list = ['我', '我', '我', '我', '我', '我']
for word, flag in seg_list:
    if flag not in words_clean_list1 and word not in words_clean_list2:
        print(word)
        print(flag)
        words_list.append(word)

with open("txt_save.txt", 'w') as file:
    for i in words_list:
        file.write(str(i) + ' ')
print("文本处理完成")

with open("txt_save.txt") as fp:
    txt = fp.read()
    # print(txt)
    wordcloud = WordCloud(font_path='chinese.msyh.ttf',  # 字体
                          background_color='black',  # 背景色
                          max_words=100,  # 最大显示单词数
                          max_font_size=60  # 频率最大单词字体大小
                          ).generate(txt)
    image = wordcloud.to_image()
    image.show()
