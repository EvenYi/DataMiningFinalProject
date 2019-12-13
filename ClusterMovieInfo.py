import pandas as pd
import collections
import matplotlib as mpl
import matplotlib.pyplot as plt
import heapq
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Pie


def movie_type_pie(movie_type):
    movie_type_labels = []
    movie_type_count = []
    for t in movie_type:
        if not (t in movie_type_labels):
            movie_type_labels.append(t)
    i = 0
    while i < len(movie_type_labels):
        movie_type_count.append(0)
        i += 1
    for t in movie_type:
        index = movie_type_labels.index(t)
        movie_type_count[index] += 1

    print(movie_type_labels)
    print(movie_type_count)
    # max_index = map(movie_type_count.index, heapq.nlargest(10, movie_type_count))
    dict = {'剧情': 'Drama', '动画': 'Animation', '喜剧': 'comedy', '爱情': 'Love', '冒险': 'Adventure', '奇幻': 'Fantasy',
            '犯罪': 'Crime', '动作': 'Action', '传记': 'biography', '科幻': 'Science fiction', '运动': 'Sports', '历史': 'history',
            '战争': 'War', '音乐': 'music', '悬疑': 'Suspense', '家庭': 'Family', '同性': 'Homosexual', '西部': 'Cowboy',
            '儿童': 'child', '惊悚': 'Thriller', '歌舞': 'Cabaret', '武侠': 'Martial arts', '古装': 'ancient costume',
            '黑色电影': 'Film noir', '灾难': 'Disaster film', '情色': 'Erotic', '恐怖': 'Horror film', '舞台艺术': 'Stage art',
            '鬼怪': 'Ghost', '戏曲': 'Tradition drama', '真人秀': 'reality show', '脱口秀': 'Talk Show'}
    movie_type_labels_e = []
    for l in movie_type_labels:
        movie_type_labels_e.append(dict[l])
    print(movie_type_labels)
    print(movie_type_labels_e)
    print(movie_type_count)
    p = int(sum(movie_type_count) * 0.01)
    print(p)

    p_movie_type_count = []
    p_movie_type_labels_e = []
    other = 0
    for each in movie_type_count:
        if each > p:
            p_movie_type_count.append(each)
            i = movie_type_count.index(each)
            p_movie_type_labels_e.append(movie_type_labels_e[i])
        else:
            other += each
    p_movie_type_labels_e.append('other')
    p_movie_type_count.append(other)
    print(p_movie_type_labels_e)
    print(p_movie_type_count)
    plt.axes(aspect=1)
    plt.pie(x=p_movie_type_count, labels=p_movie_type_labels_e, autopct='%0f%%')
    plt.show()


def clean(c_string_list):
    i = 0
    while i < len(c_string_list):
        c_string_list[i] = c_string_list[i].replace(" ", "")
        i += 1
    return c_string_list


def movie_type_country(movie_country):
    movie_country_labels = []
    movie_country_count = []
    for t in movie_country:
        if not (t in movie_country_labels):
            movie_country_labels.append(t)
    i = 0
    while i < len(movie_country_labels):
        movie_country_count.append(0)
        i += 1
    for t in movie_country:
        index = movie_country_labels.index(t)
        movie_country_count[index] += 1
    print(movie_country_labels)
    print(movie_country_count)
    print(sum(movie_country_count)*0.05)


movie_info_data = pd.read_csv(r'D:\python_ml\Datamining\DataMiningFinalProject\Data\movie_info.csv')
movie_info = movie_info_data.values.tolist()
distribution_cluster_data = pd.read_csv(r'D:\python_ml\Datamining\DataMiningFinalProject\Data\f_type_cluster.csv')
distribution_cluster = distribution_cluster_data.values.tolist()
print(len(distribution_cluster))
movie_type = []
movie_country = []
movie_director = []
movie_len = []
print(movie_info[3])
for movie in distribution_cluster:
    for info in movie_info:
        if movie[0] == info[0]:
            movie_len.append(info[5])
            movie_country.extend(clean(info[3].split("/")))
            movie_director.append(info[2])
            movie_type.extend(clean(info[1].split("/")))
print(movie_type)
print(movie_director)
print(movie_country)
print(movie_len)

# movie_type_pie(movie_type)
movie_type_country(movie_country)
