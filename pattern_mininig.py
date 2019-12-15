import pandas as pd
import pickle
import csv
import numpy as np
from decimal import Decimal, ROUND_HALF_UP
import matplotlib.pyplot as plt


def get_information():
    data_origin = pd.read_csv('all_movies_with_id.csv')[['Movie_Name', 'Score', 'Review_People', 'Star_Distribution',
                                                         'Star', 'Comment', 'Comment_Distribution', 'Like']]
    origin_list = data_origin.values.tolist()
    b_data = pd.read_csv('Data/b_type_cluster.csv')
    b_list = b_data.values.tolist()

    f_data = pd.read_csv('Data/f_type_cluster.csv')
    f_list = f_data.values.tolist()

    l_data = pd.read_csv('Data/l_type_cluster.csv')
    l_list = l_data.values.tolist()

    p_data = pd.read_csv('Data/p_type_cluster.csv')
    p_list = p_data.values.tolist()

    v_data = pd.read_csv('Data/v_type_cluster.csv')
    v_list = v_data.values.tolist()

    b_type = []
    f_type = []
    l_type = []
    p_type = []
    v_type = []

    b_names = [each[0] for each in b_list]
    f_names = [each[0] for each in f_list]
    l_names = [each[0] for each in l_list]
    p_names = [each[0] for each in p_list]
    v_names = [each[0] for each in v_list]

    for every_sample in origin_list:
        temp = []
        if every_sample[0] in b_names:
            temp.extend(every_sample[:3])
            temp.append(every_sample[3].split('%')[:-1])
            temp.extend(every_sample[4:6])
            temp.append(every_sample[6].split('%')[:-1])
            temp.append(every_sample[7])
            b_type.append(temp)
        elif every_sample[0] in f_names:
            temp.extend(every_sample[:3])
            temp.append(every_sample[3].split('%')[:-1])
            temp.extend(every_sample[4:6])
            temp.append(every_sample[6].split('%')[:-1])
            temp.append(every_sample[7])
            f_type.append(temp)
        elif every_sample[0] in l_names:
            temp.extend(every_sample[:3])
            temp.append(every_sample[3].split('%')[:-1])
            temp.extend(every_sample[4:6])
            temp.append(every_sample[6].split('%')[:-1])
            temp.append(every_sample[7])
            l_type.append(temp)
        elif every_sample[0] in p_names:
            temp.extend(every_sample[:3])
            temp.append(every_sample[3].split('%')[:-1])
            temp.extend(every_sample[4:6])
            temp.append(every_sample[6].split('%')[:-1])
            temp.append(every_sample[7])
            p_type.append(temp)
        elif every_sample[0] in v_names:
            temp.extend(every_sample[:3])
            temp.append(every_sample[3].split('%')[:-1])
            temp.extend(every_sample[4:6])
            temp.append(every_sample[6].split('%')[:-1])
            temp.append(every_sample[7])
            v_type.append(temp)

    with open('Data/b_type_info.csv', 'w', encoding='utf_8_sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Movie_name', 'Score', 'Review_people', 'Star_Distribution', 'Star', 'Comment',
                         'Comment_Distribution', 'Like'])
        writer.writerows(b_type)

    with open('Data/f_type_info.csv', 'w', encoding='utf_8_sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Movie_name', 'Score', 'Review_people', 'Star_Distribution', 'Star', 'Comment',
                         'Comment_Distribution', 'Like'])
        writer.writerows(f_type)

    with open('Data/l_type_info.csv', 'w', encoding='utf_8_sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Movie_name', 'Score', 'Review_people', 'Star_Distribution', 'Star', 'Comment',
                         'Comment_Distribution', 'Like'])
        writer.writerows(l_type)

    with open('Data/p_type_info.csv', 'w', encoding='utf_8_sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Movie_name', 'Score', 'Review_people', 'Star_Distribution', 'Star', 'Comment',
                         'Comment_Distribution', 'Like'])
        writer.writerows(p_type)

    with open('Data/v_type_info.csv', 'w', encoding='utf_8_sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Movie_name', 'Score', 'Review_people', 'Star_Distribution', 'Star', 'Comment',
                         'Comment_Distribution', 'Like'])
        writer.writerows(v_type)


def types_extract():
    # extract information from each type info file
    b_data = pd.read_csv('Data/b_type_info.csv')[['Movie_name', 'Score', 'Review_people', 'Comment']]
    b_list = b_data.values.tolist()

    f_data = pd.read_csv('Data/f_type_info.csv')[['Movie_name', 'Score', 'Review_people', 'Comment']]
    f_list = f_data.values.tolist()

    l_data = pd.read_csv('Data/l_type_info.csv')[['Movie_name', 'Score', 'Review_people', 'Comment']]
    l_list = l_data.values.tolist()

    p_data = pd.read_csv('Data/p_type_info.csv')[['Movie_name', 'Score', 'Review_people', 'Comment']]
    p_list = p_data.values.tolist()

    v_data = pd.read_csv('Data/v_type_info.csv')[['Movie_name', 'Score', 'Review_people', 'Comment']]
    v_list = v_data.values.tolist()

    # scoreview_dict {movie_name: [scores, number of reviews, number of comments]}
    # comment_length_dict {[comment_length]: count}
    scoreview_dictb = {}
    comment_length_dictb = {}
    for each in b_list:
        if each[0] in scoreview_dictb:
            pass
        else:
            scoreview_dictb[each[0]] = [each[1], each[2], 0]

        if not isinstance(each[3], float):
            scoreview_dictb[each[0]][2] += 1
            if len(each[3]) in comment_length_dictb:
                comment_length_dictb[len(each[3])] += 1
            else:
                comment_length_dictb[len(each[3])] = 1

    scoreview_dictf = {}
    comment_length_dictf = {}
    for each in f_list:
        if each[0] in scoreview_dictf:
            pass
        else:
            scoreview_dictf[each[0]] = [each[1], each[2], 0]

        if not isinstance(each[3], float):
            scoreview_dictf[each[0]][2] += 1
            if len(each[3]) in comment_length_dictf:
                comment_length_dictf[len(each[3])] += 1
            else:
                comment_length_dictf[len(each[3])] = 1

    scoreview_dictl = {}
    comment_length_dictl = {}
    for each in l_list:
        if each[0] in scoreview_dictl:
            pass
        else:
            scoreview_dictl[each[0]] = [each[1], each[2], 0]

        if not isinstance(each[3], float):
            scoreview_dictl[each[0]][2] += 1
            if len(each[3]) in comment_length_dictl:
                comment_length_dictl[len(each[3])] += 1
            else:
                comment_length_dictl[len(each[3])] = 1

    scoreview_dictp = {}
    comment_length_dictp = {}
    for each in p_list:
        if each[0] in scoreview_dictp:
            pass
        else:
            scoreview_dictp[each[0]] = [each[1], each[2], 0]

        if not isinstance(each[3], float):
            scoreview_dictp[each[0]][2] += 1
            if len(each[3]) in comment_length_dictp:
                comment_length_dictp[len(each[3])] += 1
            else:
                comment_length_dictp[len(each[3])] = 1

    scoreview_dictv = {}
    comment_length_dictv = {}
    for each in v_list:
        if each[0] in scoreview_dictv:
            pass
        else:
            scoreview_dictv[each[0]] = [each[1], each[2], 0]

        if not isinstance(each[3], float):
            scoreview_dictv[each[0]][2] += 1
            if len(each[3]) in comment_length_dictv:
                comment_length_dictv[len(each[3])] += 1
            else:
                comment_length_dictv[len(each[3])] = 1

    pickle_file = open('types_statistic.pkl', 'wb')
    pickle.dump([[scoreview_dictb, comment_length_dictb], [scoreview_dictf, comment_length_dictf],
                 [scoreview_dictl, comment_length_dictl], [scoreview_dictp, comment_length_dictp],
                 [scoreview_dictv, comment_length_dictv]], pickle_file)
    pickle_file.close()

    print('b_type: ', scoreview_dictb, comment_length_dictb)
    print('f_type: ', scoreview_dictf, comment_length_dictf)
    print('l_type: ', scoreview_dictl, comment_length_dictl)
    print('p_type: ', scoreview_dictp, comment_length_dictp)
    print('v_type: ', scoreview_dictv, comment_length_dictv)


def compare_scores():
    # get score distribution of different types
    pickle_file = open('types_statistic.pkl', 'rb')
    data = pickle.load(pickle_file)
    pickle_file.close()

    # get scores bar chart
    b_scoreview = data[0][0]
    f_scoreview = data[1][0]
    l_scoreview = data[2][0]
    p_scoreview = data[3][0]
    v_scoreview = data[4][0]

    b_scores = {'2~3': 0, '3~4': 0, '4~5': 0, '5~6': 0, '6~7': 0, '7~8': 0, '8~9': 0, '9~10': 0}
    for each in b_scoreview:
        if 2 <= b_scoreview[each][0] < 3:
            b_scores['2~3'] += 1
        elif 3 <= b_scoreview[each][0] < 4:
            b_scores['3~4'] += 1
        elif 4 <= b_scoreview[each][0] < 5:
            b_scores['4~5'] += 1
        elif 5 <= b_scoreview[each][0] < 6:
            b_scores['5~6'] += 1
        elif 6 <= b_scoreview[each][0] < 7:
            b_scores['6~7'] += 1
        elif 7 <= b_scoreview[each][0] < 8:
            b_scores['7~8'] += 1
        elif 8 <= b_scoreview[each][0] < 9:
            b_scores['8~9'] += 1
        else:
            b_scores['9~10'] += 1

    f_scores = {'2~3': 0, '3~4': 0, '4~5': 0, '5~6': 0, '6~7': 0, '7~8': 0, '8~9': 0, '9~10': 0}
    for each in f_scoreview:
        if 2 <= f_scoreview[each][0] < 3:
            f_scores['2~3'] += 1
        elif 3 <= f_scoreview[each][0] < 4:
            f_scores['3~4'] += 1
        elif 4 <= f_scoreview[each][0] < 5:
            f_scores['4~5'] += 1
        elif 5 <= f_scoreview[each][0] < 6:
            f_scores['5~6'] += 1
        elif 6 <= f_scoreview[each][0] < 7:
            f_scores['6~7'] += 1
        elif 7 <= f_scoreview[each][0] < 8:
            f_scores['7~8'] += 1
        elif 8 <= f_scoreview[each][0] < 9:
            f_scores['8~9'] += 1
        else:
            f_scores['9~10'] += 1

    l_scores = {'2~3': 0, '3~4': 0, '4~5': 0, '5~6': 0, '6~7': 0, '7~8': 0, '8~9': 0, '9~10': 0}
    for each in l_scoreview:
        if 2 <= l_scoreview[each][0] < 3:
            l_scores['2~3'] += 1
        elif 3 <= l_scoreview[each][0] < 4:
            l_scores['3~4'] += 1
        elif 4 <= l_scoreview[each][0] < 5:
            l_scores['4~5'] += 1
        elif 5 <= l_scoreview[each][0] < 6:
            l_scores['5~6'] += 1
        elif 6 <= l_scoreview[each][0] < 7:
            l_scores['6~7'] += 1
        elif 7 <= l_scoreview[each][0] < 8:
            l_scores['7~8'] += 1
        elif 8 <= l_scoreview[each][0] < 9:
            l_scores['8~9'] += 1
        else:
            l_scores['9~10'] += 1

    p_scores = {'2~3': 0, '3~4': 0, '4~5': 0, '5~6': 0, '6~7': 0, '7~8': 0, '8~9': 0, '9~10': 0}
    for each in p_scoreview:
        if 2 <= p_scoreview[each][0] < 3:
            p_scores['2~3'] += 1
        elif 3 <= p_scoreview[each][0] < 4:
            p_scores['3~4'] += 1
        elif 4 <= p_scoreview[each][0] < 5:
            p_scores['4~5'] += 1
        elif 5 <= p_scoreview[each][0] < 6:
            p_scores['5~6'] += 1
        elif 6 <= p_scoreview[each][0] < 7:
            p_scores['6~7'] += 1
        elif 7 <= p_scoreview[each][0] < 8:
            p_scores['7~8'] += 1
        elif 8 <= p_scoreview[each][0] < 9:
            p_scores['8~9'] += 1
        else:
            p_scores['9~10'] += 1

    v_scores = {'2~3': 0, '3~4': 0, '4~5': 0, '5~6': 0, '6~7': 0, '7~8': 0, '8~9': 0, '9~10': 0}
    for each in v_scoreview:
        if 2 <= v_scoreview[each][0] < 3:
            v_scores['2~3'] += 1
        elif 3 <= v_scoreview[each][0] < 4:
            v_scores['3~4'] += 1
        elif 4 <= v_scoreview[each][0] < 5:
            v_scores['4~5'] += 1
        elif 5 <= v_scoreview[each][0] < 6:
            v_scores['5~6'] += 1
        elif 6 <= v_scoreview[each][0] < 7:
            v_scores['6~7'] += 1
        elif 7 <= v_scoreview[each][0] < 8:
            v_scores['7~8'] += 1
        elif 8 <= v_scoreview[each][0] < 9:
            v_scores['8~9'] += 1
        else:
            v_scores['9~10'] += 1

    b_scores_list = []
    for i in list(b_scores.values()):
        number = Decimal(str(i / sum(list(b_scores.values()))))
        b_scores_list.append(number.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP))

    f_scores_list = []
    for i in list(f_scores.values()):
        number = Decimal(str(i / sum(list(f_scores.values()))))
        f_scores_list.append(number.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP))

    l_scores_list = []
    for i in list(l_scores.values()):
        number = Decimal(str(i / sum(list(l_scores.values()))))
        l_scores_list.append(number.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP))

    p_scores_list = []
    for i in list(p_scores.values()):
        number = Decimal(str(i / sum(list(p_scores.values()))))
        p_scores_list.append(number.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP))

    v_scores_list = []
    for i in list(v_scores.values()):
        number = Decimal(str(i / sum(list(v_scores.values()))))
        v_scores_list.append(number.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP))

    print(b_scores_list)
    print(f_scores_list)
    print(l_scores_list)
    print(p_scores_list)
    print(v_scores_list)


def compare_reviews():
    # get reviews distribution of different types
    pickle_file = open('types_statistic.pkl', 'rb')
    data = pickle.load(pickle_file)
    pickle_file.close()

    l_reviews = {'< 1W': 0, '1W ~ 10W': 0, '10W ~ 50W': 0, '50W ~ 100W': 0, '> 100W': 0}
    for each in data[2][0]:
        if data[2][0][each][1] < 10000:
            l_reviews['< 1W'] += 1
        elif 10000 <= data[2][0][each][1] < 100000:
            l_reviews['1W ~ 10W'] += 1
        elif 100000 <= data[2][0][each][1] < 500000:
            l_reviews['10W ~ 50W'] += 1
        elif 500000 <= data[2][0][each][1] < 1000000:
            l_reviews['50W ~ 100W'] += 1
        else:
            l_reviews['> 100W'] += 1

    b_reviews = {'< 1W': 0, '1W ~ 10W': 0, '10W ~ 50W': 0, '50W ~ 100W': 0, '> 100W': 0}
    for each in data[0][0]:
        if data[0][0][each][1] < 10000:
            b_reviews['< 1W'] += 1
        elif 10000 <= data[0][0][each][1] < 100000:
            b_reviews['1W ~ 10W'] += 1
        elif 100000 <= data[0][0][each][1] < 500000:
            b_reviews['10W ~ 50W'] += 1
        elif 500000 <= data[0][0][each][1] < 1000000:
            b_reviews['50W ~ 100W'] += 1
        else:
            b_reviews['> 100W'] += 1

    v_reviews = {'< 1W': 0, '1W ~ 10W': 0, '10W ~ 50W': 0, '50W ~ 100W': 0, '> 100W': 0}
    for each in data[4][0]:
        if data[4][0][each][1] < 10000:
            v_reviews['< 1W'] += 1
        elif 10000 <= data[4][0][each][1] < 100000:
            v_reviews['1W ~ 10W'] += 1
        elif 100000 <= data[4][0][each][1] < 500000:
            v_reviews['10W ~ 50W'] += 1
        elif 500000 <= data[4][0][each][1] < 1000000:
            v_reviews['50W ~ 100W'] += 1
        else:
            v_reviews['> 100W'] += 1

    p_reviews = {'< 1W': 0, '1W ~ 10W': 0, '10W ~ 50W': 0, '50W ~ 100W': 0, '> 100W': 0}
    for each in data[3][0]:
        if data[3][0][each][1] < 10000:
            p_reviews['< 1W'] += 1
        elif 10000 <= data[3][0][each][1] < 100000:
            p_reviews['1W ~ 10W'] += 1
        elif 100000 <= data[3][0][each][1] < 500000:
            p_reviews['10W ~ 50W'] += 1
        elif 500000 <= data[3][0][each][1] < 1000000:
            p_reviews['50W ~ 100W'] += 1
        else:
            p_reviews['> 100W'] += 1

    f_reviews = {'< 1W': 0, '1W ~ 10W': 0, '10W ~ 50W': 0, '50W ~ 100W': 0, '> 100W': 0}
    for each in data[1][0]:
        if data[1][0][each][1] < 10000:
            f_reviews['< 1W'] += 1
        elif 10000 <= data[1][0][each][1] < 100000:
            f_reviews['1W ~ 10W'] += 1
        elif 100000 <= data[1][0][each][1] < 500000:
            f_reviews['10W ~ 50W'] += 1
        elif 500000 <= data[1][0][each][1] < 1000000:
            f_reviews['50W ~ 100W'] += 1
        else:
            f_reviews['> 100W'] += 1

    print('l', l_reviews)
    print('b', b_reviews)
    print('v', v_reviews)
    print('p', p_reviews)
    print('f', f_reviews)

    l_reviews_points = np.array(list(l_reviews.values())) / sum(list(l_reviews.values()))
    b_reviews_points = np.array(list(b_reviews.values())) / sum(list(b_reviews.values()))
    v_reviews_points = np.array(list(v_reviews.values())) / sum(list(v_reviews.values()))
    p_reviews_points = np.array(list(p_reviews.values())) / sum(list(p_reviews.values()))
    f_reviews_points = np.array(list(f_reviews.values())) / sum(list(f_reviews.values()))

    print(l_reviews_points)
    print(b_reviews_points)
    print(v_reviews_points)
    print(p_reviews_points)
    print(f_reviews_points)


def scores_histogram():
    # get score distribution of different types
    pickle_file = open('types_statistic.pkl', 'rb')
    data = pickle.load(pickle_file)
    pickle_file.close()

    l_scores = []
    for each in data[2][0]:
        l_scores.append(data[2][0][each][0])

    b_scores = []
    for each in data[0][0]:
        b_scores.append(data[0][0][each][0])

    v_scores = []
    for each in data[4][0]:
        v_scores.append(data[4][0][each][0])

    p_scores = []
    for each in data[3][0]:
        p_scores.append(data[3][0][each][0])

    f_scores = []
    for each in data[1][0]:
        f_scores.append(data[1][0][each][0])

    plt.figure()

    kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, bins='auto')
    plt.xlabel('scores')
    plt.ylabel('frequency')

    plt.hist(l_scores, **kwargs, label='l-type')
    plt.hist(b_scores, **kwargs, label='b-type')
    plt.hist(v_scores, **kwargs, label='v-type')
    plt.hist(p_scores, **kwargs, label='p-type')
    plt.hist(f_scores, **kwargs, label='f-type')
    plt.legend()
    # plt.hist(l_scores,  color='lightcoral')
    #
    # plt.subplot(152)
    # plt.xlabel('b-type')
    # plt.hist(b_scores, bins='auto', color='bisque')
    #
    # plt.subplot(153)
    # plt.xlabel('v-type')
    # plt.hist(v_scores, bins='auto', color='gold')
    #
    # plt.subplot(154)
    # plt.xlabel('p-type')
    # plt.hist(p_scores, bins='auto', color='lime')
    #
    # plt.subplot(155)
    # plt.xlabel('f-type')
    # plt.hist(f_scores, bins='auto', color='cornflowerblue')

    plt.show()


def reviews_histogram():
    # get score distribution of different types
    pickle_file = open('types_statistic.pkl', 'rb')
    data = pickle.load(pickle_file)
    pickle_file.close()

    l_reviews = []
    for each in data[2][0]:
        l_reviews.append(data[2][0][each][1])

    b_reviews = []
    for each in data[0][0]:
        b_reviews.append(data[0][0][each][1])

    v_reviews = []
    for each in data[4][0]:
        v_reviews.append(data[4][0][each][1])

    p_reviews = []
    for each in data[3][0]:
        p_reviews.append(data[3][0][each][1])

    f_reviews = []
    for each in data[1][0]:
        f_reviews.append(data[1][0][each][1])

    plt.figure()

    # kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, bins='auto')
    # plt.xlabel('number of reviews')
    # plt.ylabel('frequency')
    #
    # plt.hist(l_reviews, **kwargs, label='l-type')
    # plt.hist(b_reviews, **kwargs, label='b-type')
    # plt.hist(v_reviews, **kwargs, label='v-type')
    # plt.hist(p_reviews, **kwargs, label='p-type')
    # plt.hist(f_reviews, **kwargs, label='f-type')
    # plt.legend()
    ax1 = plt.subplot(151)
    plt.xlabel('number of reviews')
    plt.ylabel('number of movies')
    plt.hist(l_reviews, color='lightcoral', label='l-type', bins='auto')
    plt.legend()

    plt.subplot(152)
    plt.xlabel('number of reviews')
    plt.hist(b_reviews, color='bisque', label='b-type', bins='auto')
    plt.legend()

    plt.subplot(153)
    plt.xlabel('number of reviews')
    plt.hist(v_reviews, color='gold', label='v-type', bins='auto')
    plt.legend()

    plt.subplot(154)
    plt.xlabel('number of reviews')
    plt.hist(p_reviews, color='lime', label='p-type', bins='auto')
    plt.legend()

    plt.subplot(155)
    plt.xlabel('number of reviews')
    plt.hist(f_reviews, color='cornflowerblue', label='f-type', bins='auto')
    plt.legend()

    plt.show()


def reviews_box():
    # get score distribution of different types
    pickle_file = open('types_statistic.pkl', 'rb')
    data = pickle.load(pickle_file)
    pickle_file.close()

    l_reviews = []
    for each in data[2][0]:
        l_reviews.append(data[2][0][each][1])

    b_reviews = []
    for each in data[0][0]:
        b_reviews.append(data[0][0][each][1])

    v_reviews = []
    for each in data[4][0]:
        v_reviews.append(data[4][0][each][1])

    p_reviews = []
    for each in data[3][0]:
        p_reviews.append(data[3][0][each][1])

    f_reviews = []
    for each in data[1][0]:
        f_reviews.append(data[1][0][each][1])

    plt.figure()
    plt.subplot()
    points = [l_reviews, b_reviews, v_reviews, p_reviews, f_reviews]
    labels = ['l-type', 'b-type', 'v-type', 'p-type', 'f-type']
    bplot = plt.boxplot(points, patch_artist=True, labels=labels, showfliers=False)
    colors = ['lightcyan', 'bisque', 'gold', 'lime', 'cornflowerblue']
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

    plt.xlabel('Different Types')
    plt.ylabel('number of reviews')
    plt.show()


def ratio_histogram():
    # get comment-review ratio distribution of different types
    pickle_file = open('types_statistic.pkl', 'rb')
    data = pickle.load(pickle_file)
    pickle_file.close()

    l_ratio =[]
    for each in data[2][0]:
        l_ratio.append(data[2][0][each][2] / data[2][0][each][1])

    b_ratio = []
    for each in data[0][0]:
        b_ratio.append(data[0][0][each][2] / data[0][0][each][1])

    v_ratio = []
    for each in data[4][0]:
        v_ratio.append(data[4][0][each][2] / data[4][0][each][1])

    p_ratio = []
    for each in data[3][0]:
        p_ratio.append(data[3][0][each][2] / data[3][0][each][1])

    f_ratio = []
    for each in data[1][0]:
        f_ratio.append(data[1][0][each][2] / data[1][0][each][1])

    plt.figure()

    # kwargs = dict(histtype='stepfilled', alpha=0.4, density=True, bins='auto')
    # plt.xlabel('comments-reviews ratio')
    # plt.ylabel('frequency')
    #
    # plt.hist(l_ratio, **kwargs, label='l-type')
    # plt.hist(b_ratio, **kwargs, label='b-type')
    # plt.hist(v_ratio, **kwargs, label='v-type')
    # plt.hist(p_ratio, **kwargs, label='p-type')
    # plt.hist(f_ratio, **kwargs, label='f-type')
    # plt.legend()
    # plt.show()
    plt.subplot(151)
    plt.xlabel('comments-reviews ratio')
    plt.ylabel('number of movies')
    plt.hist(l_ratio, bins='auto', color='lightcoral', label='l-type')
    plt.legend()

    plt.subplot(152)
    plt.xlabel('comments-reviews ratio')
    plt.hist(b_ratio, bins='auto', color='bisque', label='b-type')
    plt.legend()

    plt.subplot(153)
    plt.xlabel('comments-reviews ratio')
    plt.hist(v_ratio, bins='auto', color='gold', label='v-type')
    plt.legend()

    plt.subplot(154)
    plt.xlabel('comments-reviews ratio')
    plt.hist(p_ratio, bins='auto', color='lime', label='p-type')
    plt.legend()

    plt.subplot(155)
    plt.xlabel('comments-reviews ratio')
    plt.hist(f_ratio, bins='auto', color='cornflowerblue', label='f-type')
    plt.legend()
    plt.show()


def ratio_box():
    # get comment-review ratio distribution of different types
    pickle_file = open('types_statistic.pkl', 'rb')
    data = pickle.load(pickle_file)
    pickle_file.close()

    l_ratio = []
    for each in data[2][0]:
        l_ratio.append(data[2][0][each][2] / data[2][0][each][1])

    b_ratio = []
    for each in data[0][0]:
        b_ratio.append(data[0][0][each][2] / data[0][0][each][1])

    v_ratio = []
    for each in data[4][0]:
        v_ratio.append(data[4][0][each][2] / data[4][0][each][1])

    p_ratio = []
    for each in data[3][0]:
        p_ratio.append(data[3][0][each][2] / data[3][0][each][1])

    f_ratio = []
    for each in data[1][0]:
        f_ratio.append(data[1][0][each][2] / data[1][0][each][1])

    plt.figure()
    plt.subplot()
    points = [l_ratio, b_ratio, v_ratio, p_ratio, f_ratio]
    labels = ['l-type', 'b-type', 'v-type', 'p-type', 'f-type']
    bplot = plt.boxplot(points, patch_artist=True, labels=labels, showfliers=False)
    colors = ['lightcyan', 'bisque', 'gold', 'lime', 'cornflowerblue']
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

    plt.xlabel('Different Types')
    plt.ylabel('comments-reviews ratio')
    plt.show()


def comment_length():
    # get comment length distribution of different types
    pickle_file = open('types_statistic.pkl', 'rb')
    data = pickle.load(pickle_file)
    pickle_file.close()

    l_length = []
    for each in data[2][1]:
        for count in range(data[2][1][each]):
            l_length.append(each)

    b_length = []
    for each in data[0][1]:
        for count in range(data[0][1][each]):
            b_length.append(each)

    v_length = []
    for each in data[4][1]:
        for count in range(data[4][1][each]):
            v_length.append(each)

    p_length = []
    for each in data[3][1]:
        for count in range(data[3][1][each]):
            p_length.append(each)

    f_length = []
    for each in data[1][1]:
        for count in range(data[1][1][each]):
            f_length.append(each)

    plt.figure()

    # kwargs = dict(histtype='stepfilled', alpha=0.4, density=True, bins='auto')
    # plt.xlabel('comment length')
    # plt.ylabel('frequency')
    #
    # plt.hist(l_length, **kwargs, label='l-type')
    # plt.hist(b_length, **kwargs, label='b-type')
    # plt.hist(v_length, **kwargs, label='v-type')
    # plt.hist(p_length, **kwargs, label='p-type')
    # plt.hist(f_length, **kwargs, label='f-type')
    # plt.legend()
    # plt.show()
    plt.subplot(151)
    plt.xlabel('comments-length')
    plt.ylabel('frequency')
    plt.hist(l_length, color='lightcoral', bins='auto', label='l-type', density=True)
    plt.legend()

    # plt.figure()
    plt.subplot(152)
    plt.xlabel('comments-length')
    plt.hist(b_length, color='bisque', bins='auto', label='b-type', density=True)
    plt.legend()

    # plt.figure()
    plt.subplot(153)
    plt.xlabel('comments-length')
    plt.hist(v_length, color='gold', bins='auto', label='v-type', density=True)
    plt.legend()

    # plt.figure()
    plt.subplot(154)
    plt.xlabel('comments-length')
    plt.hist(p_length, color='lime', bins='auto', label='p-type', density=True)
    plt.legend()

    # plt.figure()
    plt.subplot(155)
    plt.xlabel('comments-length')
    plt.hist(f_length, color='cornflowerblue', bins='auto', label='f-type', density=True)
    plt.legend()
    plt.show()


def comment_length_box():
    # get comment length distribution of different types
    pickle_file = open('types_statistic.pkl', 'rb')
    data = pickle.load(pickle_file)
    pickle_file.close()

    l_length = []
    for each in data[2][1]:
        for count in range(data[2][1][each]):
            l_length.append(each)

    b_length = []
    for each in data[0][1]:
        for count in range(data[0][1][each]):
            b_length.append(each)

    v_length = []
    for each in data[4][1]:
        for count in range(data[4][1][each]):
            v_length.append(each)

    p_length = []
    for each in data[3][1]:
        for count in range(data[3][1][each]):
            p_length.append(each)

    f_length = []
    for each in data[1][1]:
        for count in range(data[1][1][each]):
            f_length.append(each)

    plt.figure()
    plt.subplot()
    points = [l_length, b_length, v_length, p_length, f_length]
    labels = ['l-type', 'b-type', 'v-type', 'p-type', 'f-type']
    bplot = plt.boxplot(points, patch_artist=True, labels=labels, showfliers=False)
    colors = ['lightcyan', 'bisque', 'gold', 'lime', 'cornflowerblue']
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

    plt.xlabel('Different Types')
    plt.ylabel('comment-length')
    plt.show()


def clean(c_string_list):
    i = 0
    while i < len(c_string_list):
        c_string_list[i] = c_string_list[i].replace(" ", "")
        i += 1
    return c_string_list


def get_information(movie_name):
    data = pd.read_csv('Data/movie_info.csv')
    data = data.values.tolist()

    # extract information in the form of [type, country]
    info = []
    for each_movie in data:
        if each_movie[0] == movie_name:
            type_info = clean(each_movie[1].split('/'))
            country = clean(each_movie[3].split('/'))
            info = [type_info, country]
    return info


def same_score_pf(one_type, other_type):
    pickle_file = open('types_statistic.pkl', 'rb')
    data = pickle.load(pickle_file)
    pickle_file.close()

    # feed data according to params
    if one_type == 'p':
        one_data = data[3][0]
    elif one_type == 'f':
        one_data = data[1][0]
    elif one_type == 'v':
        one_data = data[4][0]
    elif one_type == 'b':
        one_data = data[0][0]
    elif one_type == 'l':
        one_data = data[2][0]
    else:
        print('one_type should be [p, f, v, b, l]')
        exit(-1)

    if other_type == 'p':
        other_data = data[3][0]
    elif other_type == 'f':
        other_data = data[1][0]
    elif other_type == 'v':
        other_data = data[4][0]
    elif other_type == 'b':
        other_data = data[0][0]
    elif other_type == 'l':
        other_data = data[2][0]
    else:
        print('other_type should be [p, f, v, b, l]')
        exit(-1)

    results = {}
    count = 0
    for p_movie in one_data:
        print(count+1, 'rounds' + 'search for', p_movie, 'in dataset', one_type)
        count += 1
        score = one_data[p_movie][0]

        # get information of p_movie
        p_info = get_information(p_movie)
        if len(p_info) == 0:
            continue

        if score in results:
            results[score][0][p_movie] = p_info
        else:
            results[score] = [{p_movie: p_info}, {}]

    count = 0
    for f_movie in other_data:
        score = other_data[f_movie][0]
        print(count+1, 'rounds search for', f_movie, 'in dataset', other_type)
        count += 1

        # get information of f_movie
        f_info = get_information(f_movie)
        if len(f_info) == 0:
            continue

        # if key [score] has been created
        if score in results:
            results[score][1][f_movie] = f_info

        else:   # indicates no such score in p_movies
            pass

    for each in results:
        if len(results[each][0]) > 0 and len(results[each][1]) > 0:
            print('----------------')
            print(each)
            print(one_type, '-type: ', results[each][0])
            print(other_type, '-type: ', results[each][1])

    file_name = one_type + '-' + other_type + '.pkl'
    pickle_file = open(file_name, 'wb')
    pickle.dump(results, pickle_file)
    pickle_file.close()


def intersection_pie(one_type, other_type):
    file_name = one_type + '-' + other_type + '.pkl'
    pickle_file = open(file_name, 'rb')
    data = pickle.load(pickle_file)
    pickle_file.close()

    one_type_labels = {}
    one_country_labels = {}
    other_type_labels = {}
    other_country_labels = {}

    # get information for drawing p pie and f pie
    for each_score in data:
        one_info = data[each_score][0]
        other_info = data[each_score][1]
        for each_movie in one_info:
            for every_type in one_info[each_movie][0]:
                if every_type in one_type_labels:
                    one_type_labels[every_type] += 1
                else:
                    one_type_labels[every_type] = 1

            for every_country in one_info[each_movie][1]:
                if every_country in one_country_labels:
                    one_country_labels[every_country] += 1
                else:
                    one_country_labels[every_country] = 1

        for each_movie in other_info:
            for every_type in other_info[each_movie][0]:
                if every_type in other_type_labels:
                    other_type_labels[every_type] += 1
                else:
                    other_type_labels[every_type] = 1

            for every_country in other_info[each_movie][1]:
                if every_country in other_country_labels:
                    other_country_labels[every_country] += 1
                else:
                    other_country_labels[every_country] = 1

    # draw pies
    type_dict = {'剧情': 'Drama', '动画': 'Animation', '喜剧': 'comedy', '爱情': 'Love', '冒险': 'Adventure', '奇幻': 'Fantasy',
                 '犯罪': 'Crime', '动作': 'Action', '传记': 'biography', '科幻': 'Science fiction', '运动': 'Sports',
                 '历史': 'history',
                 '战争': 'War', '音乐': 'music', '悬疑': 'Suspense', '家庭': 'Family', '同性': 'Homosexual', '西部': 'Cowboy',
                 '儿童': 'child', '惊悚': 'Thriller', '歌舞': 'Cabaret', '武侠': 'Martial arts', '古装': 'ancient costume',
                 '黑色电影': 'Film noir', '灾难': 'Disaster film', '情色': 'Erotic', '恐怖': 'Horror film', '舞台艺术': 'Stage art',
                 '鬼怪': 'Ghost', '戏曲': 'Tradition drama', '真人秀': 'reality show', '脱口秀': 'Talk Show'}
    country_dict = {'日本': 'Japan', '美国': 'United States', '英国': 'United Kingdom', '台湾': 'Taiwan', '意大利': 'Italy',
                    '法国': 'France', '韩国': 'Korea', '中国大陆': 'China Mainland', '德国': 'Germany', '香港': 'Hong Kong'}

    one_types = []
    one_points = []
    summation = sum(list(one_type_labels.values()))
    other = 0
    for each in one_type_labels:
        if one_type_labels[each] > summation * 0.05:
            one_types.append(type_dict[each])
            one_points.append(one_type_labels[each])
        else:
            other += 1
    one_types.append('other')
    one_points.append(other)

    other_types = []
    other_points = []
    summation = sum(list(other_type_labels.values()))
    other = 0
    for each in other_type_labels:
        if other_type_labels[each] > summation * 0.05:
            other_types.append(type_dict[each])
            other_points.append(other_type_labels[each])
        else:
            other += 1
    other_types.append('other')
    other_points.append(other)

    plt.figure()
    colors = ['salmon', 'sandybrown', 'gold', 'greenyellow', 'turquoise', 'cyan', 'deepskyblue', 'royalblue', 'blueviolet', 'lightpink']
    plt.title('type distribution comparison')
    plt.subplot(121)
    plt.title(one_type + '-type')
    plt.pie(one_points, labels=one_types, autopct='%1.2f%%', colors=colors)

    plt.subplot(122)
    plt.title(other_type + '-type')
    plt.pie(other_points, labels=other_types, autopct='%1.2f%%', colors=colors)

    one_countries = []
    one_points = []
    summation = sum(list(one_country_labels.values()))
    other = 0
    for each in one_country_labels:
        if one_country_labels[each] > summation * 0.05:
            one_countries.append(country_dict[each])
            one_points.append(one_country_labels[each])
        else:
            other += 1
    one_countries.append('other')
    one_points.append(other)

    other_countries = []
    other_points = []
    summation = sum(list(other_country_labels.values()))
    other = 0
    for each in other_country_labels:
        if other_country_labels[each] > summation * 0.05:
            other_countries.append(country_dict[each])
            other_points.append(other_country_labels[each])
        else:
            other += 1
    other_countries.append('other')
    other_points.append(other)

    plt.figure()
    plt.title('country distribution comparison')
    plt.subplot(121)
    plt.title(one_type + '-type')
    plt.pie(one_points, labels=one_countries, autopct='%1.2f%%', colors=colors)

    plt.subplot(122)
    plt.title(other_type + '-type')
    plt.pie(other_points, labels=other_countries, autopct='%1.2f%%', colors=colors)

    plt.show()

# comments_review_ratio()
# reviews_histogram()
# scores_histogram()
# comment_length()
# reviews_box()
# ratio_box()
# comment_length_box()
same_score_pf('l', 'b')
intersection_pie('l', 'b')