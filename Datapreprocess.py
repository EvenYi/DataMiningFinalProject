import pandas as pd
import numpy as np
import re


def star_distribution(csv_filename='StarDistribution.csv'):
    data = pd.read_csv(csv_filename)
    data_list = data.values.tolist()
    error_data = []
    for each in data_list:
        if len(each[1].split("%")) == 6:
            each[1] = each[1].split("%")
            if each[1].pop() == "":
                each[1] = [float(i) for i in each[1]]

            else:
                error_data.append(each[0])
        else:
            error_data.append(each[0])
    return data_list


def move_comment(csv_filename='MovieComment.csv'):
    data = pd.read_csv(csv_filename)
    data_list = data.values.tolist()
    return data_list
