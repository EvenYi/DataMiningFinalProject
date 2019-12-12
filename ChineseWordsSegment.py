import Datapreprocess
import jieba.posseg as pseg
import pandas as pd
import collections
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

movie_comment_list = Datapreprocess.movie_comment()
words_clean_list1 = ['x', 'r', 'w', 't', 'u', 'ul', 'uj', 'ug', 'd', 'c', 'p']
words_clean_list2 = ['是', '和', '有', '人', '到']
movie_name_flag = movie_comment_list[0][0]
words_list = []
movie_comment_segment = []
final_result = []
i = 0
for each in movie_comment_list:
    if each[0] == movie_name_flag:
        seg_list = pseg.cut(each[1])
        for word, flag in seg_list:
            if flag not in words_clean_list1 and word not in words_clean_list2:
                if len(word) > 1 and flag != 'v':
                    words_list.append(word)
    else:
        movie_comment_segment.append(movie_name_flag)
        movie_comment_segment.append(",".join(words_list))
        print(i)
        i += 1
        final_result.append(movie_comment_segment)
        movie_comment_segment = []
        words_list = []
        movie_name_flag = each[0]
        seg_list = pseg.cut(each[1])
        for word, flag in seg_list:
            if flag not in words_clean_list1 and word not in words_clean_list2:
                if len(word) > 1 and flag != 'v':
                    words_list.append(word)
segment_data = pd.DataFrame(final_result, columns=['Movie_Name', 'Segments'])
segment_data.to_csv(r'D:\python_ml\Datamining\DataMiningFinalProject\Data\movie_segments.csv', index=None, header=True,
                    encoding='utf_8_sig')
'''
data = pd.read_csv(r'D:\python_ml\Datamining\DataMiningFinalProject\Data\movie_segments.csv')
d = data.values.tolist()
i = 0
for each in d:
    if i >= 10:
        break
    print(each)
    i += 1
'''
'''
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

'''
with open("txt_save.txt", 'w') as file:
    for i in words_list:
        file.write(str(i) + ' ')
print("文本处理完成")

with open("txt_save.txt") as fp:
    txt = fp.read()
    # print(txt)
    
'''
