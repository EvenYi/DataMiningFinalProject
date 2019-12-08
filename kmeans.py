import math
import Datapreprocess


def getEuclidean(point1, point2):
    dimension = len(point1)
    dist = 0.0
    for i in range(dimension):
        dist += (point1[i] - point2[i]) ** 2
    return math.sqrt(dist)


def centres_initial():
    # initialization: pick k typical sample as the initial centre
    centres = []
    centres.append()
    centres.append()
    centres.append()
    centres.append()

    return centres


def k_means(dataset, k, iteration):
    # dataset is in the form of <movie_name, [coordinates]>
    centres = centres_initial()

    # assign all samples into clusters
    while iteration > 0:
        clusters = []
        for i in range(k):
            clusters.append([])

        # traverse the whole dataset
        for each_point in dataset:
            # find the minimum distance for each point
            minimum_dist = 1e6
            min_index = k+1
            # calculate distances between every point and each current centre
            for i in range(k):
                distance = getEuclidean(each_point[1], centres[i][1])
                if distance < minimum_dist:
                    minimum_dist = distance
                    min_index = i
            # add items into corresponding clusters
            clusters[min_index].append(each_point)

        # re-calculate centres for each cluster
        dimension = len(dataset[0][1])
        sum_list = []
        for i in range(dimension):
            sum_list.append(0)

        for i in range(k):  # for each cluster
            for item in clusters[i]:
                for index in range(dimension):
                    sum_list[index] += item[1][index]

            number = len(clusters[i])
            for dimen in range(dimension):
                centres[i] = []
                centres[i].append(sum_list[dimen] / number)

        iteration -= 1


def show_clusters(clusters):
    for each in clusters:
        print(each)


def main():
    data = Datapreprocess.star_distribution()
    k_means(data, 4, 10)