import pandas as pd
import collections
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def clean(c_segment, c_clean_list):
    for c_each in c_clean_list:
        while c_each in c_segment:
            c_segment.remove(c_each)


def words_cloud_generate(cvs, image_name):
    clean_list = ['电影', '一个', '片子', '不错', '不要', '有点', '很多', '一部', '一种', '最后', '剧情', '中国', '故事', '感觉']
    type_cluster_data = pd.read_csv(cvs)
    type_cluster_data = type_cluster_data[['Movie_Name']]
    type_cluster_data = type_cluster_data.values.tolist()
    cluster_words = []
    for f_each in type_cluster_data:
        for segment in movie_segments_data:
            if f_each[0] == segment[0]:
                clean(segment[1], clean_list)
                cluster_words.extend(segment[1])
                break
    words_count = collections.Counter(cluster_words)
    word_loud = WordCloud(font_path='chinese.msyh.ttf',
                          background_color='white',
                          max_words=400,
                          max_font_size=120,
                          width=1000,
                          height=650
                          )
    word_loud = word_loud.generate_from_frequencies(words_count)
    #    image = word_loud.to_image()
    #    image.show()
    word_loud.to_file(image_name)


movie_segments_data = pd.read_csv(r'D:\python_ml\Datamining\DataMiningFinalProject\Data\movie_segments.csv')
movie_segments_data = movie_segments_data.values.tolist()
for each in movie_segments_data:
    each[1] = each[1].split(",")

file_image_list = [[r'D:\python_ml\Datamining\DataMiningFinalProject\Data\f_type_cluster.csv',
                    r'D:\python_ml\Datamining\DataMiningFinalProject\Image\f_type_wordscloud.jpg'],
                   [r'D:\python_ml\Datamining\DataMiningFinalProject\Data\p_type_cluster.csv',
                    r'D:\python_ml\Datamining\DataMiningFinalProject\Image\p_type_wordscloud.jpg'],
                   [r'D:\python_ml\Datamining\DataMiningFinalProject\Data\v_type_cluster.csv',
                    r'D:\python_ml\Datamining\DataMiningFinalProject\Image\v_type_wordscloud.jpg'],
                   [r'D:\python_ml\Datamining\DataMiningFinalProject\Data\b_type_cluster.csv',
                    r'D:\python_ml\Datamining\DataMiningFinalProject\Image\b_type_wordscloud.jpg'],
                   [r'D:\python_ml\Datamining\DataMiningFinalProject\Data\l_type_cluster.csv',
                    r'D:\python_ml\Datamining\DataMiningFinalProject\Image\l_type_wordscloud.jpg']]

words_cloud_generate(r'D:\python_ml\Datamining\DataMiningFinalProject\Data\l_type_cluster.csv',
                     r'D:\python_ml\Datamining\DataMiningFinalProject\Image\l_type_wordscloud.jpg')
