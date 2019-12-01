import Datapreprocess
import jieba.posseg as pseg
import collections
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pkuseg
import jieba

movie_comment_list = Datapreprocess.movie_comment()
# seg = pkuseg.pkuseg(model_name='web',postag=True)           # 以默认配置加载模型
# text = seg.cut(movie_comment_list[5][1])  # 进行分词
# print(text)
words_clean_list1 = ['x', 'r', 'w', 't', 'u', 'ul', 'uj', 'ug', 'd', 'c', 'p']
words_clean_list2 = ['是', '和', '有', '人', '到']
movie_name_flag = movie_comment_list[0][0]
words_list = []
for each in movie_comment_list:
    if each[0] == movie_name_flag:
        seg_list = pseg.cut(each[1])
        for word, flag in seg_list:
            if flag not in words_clean_list1 and word not in words_clean_list2:
                if len(word) > 1 and flag != 'v':
                    words_list.append(word)
    else:
        words_count = collections.Counter(words_list)
        word_loud = WordCloud(font_path='chinese.msyh.ttf',  # 字体
                              background_color='black',  # 背景色
                              max_words=200,  # 最大显示单词数
                              max_font_size=80  # 频率最大单词字体大小
                              )
        word_loud = word_loud.generate_from_frequencies(words_count)
        image = word_loud.to_image()
        image.show()
        break

'''
with open("txt_save.txt", 'w') as file:
    for i in words_list:
        file.write(str(i) + ' ')
print("文本处理完成")

with open("txt_save.txt") as fp:
    txt = fp.read()
    # print(txt)
    
'''
