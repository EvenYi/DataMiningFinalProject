import pandas as pd


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


def movie_comment(csv_filename='MovieComment.csv'):
    data = pd.read_csv(csv_filename)
    data_list = data.values.tolist()
    return data_list


if __name__ == '__main__':
    dataset = star_distribution()
    P_candidates = []
    b_candidates = []
    C_candidates = []
    L_candidates = []
    for each in dataset:
        if int(each[1][0]) >= 30 and int(each[1][1]) >= 30:
            P_candidates.append(each)
        elif int(each[1][3]) >= 30 and int(each[1][4]) >= 30:
            b_candidates.append(each)
        elif int(each[1][0]) >= 30 and int(each[1][4]) >= 30:
            C_candidates.append(each)
        elif int(each[1][4]) >= 50:
            L_candidates.append(each)

    print('P_candidates:')
    for each in P_candidates:
        print(each)

    print('----------------------')
    print('b_candidates:')
    for each in b_candidates:
        print(each)

    print('----------------------')
    print('C_candidates:')
    for each in C_candidates:
        print(each)
    print('----------------------')
    print('L_candidates:')
    for each in L_candidates:
        print(each)

