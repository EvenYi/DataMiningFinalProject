from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.samples.definitions import SIMPLE_SAMPLES
from pyclustering.utils import read_sample
from pyclustering.cluster import cluster_visualizer_multidim
import math
from pyclustering.utils.metric import distance_metric, type_metric
import numpy as np
from scipy import spatial
import Datapreprocess

# Load list of points for cluster analysis.
data_set = Datapreprocess.star_distribution()
pure_data = []
for each in data_set:
    pure_data.append(each[1])
sample = pure_data
print(sample)
# Initial medoids for sample 'Simple3'.
initial_medoids = [52, 456, 6973, 614]


# Create instance of K-Medoids algorithm with prepared centers.
def my_cosine(point1, point2):
    result = 1 - spatial.distance.cosine(point1, point2)
    return result


metric = distance_metric(type_metric.USER_DEFINED, func=my_cosine)
kmedoids_instance = kmedoids(sample, initial_medoids, metric=metric)
# Run cluster analysis.
kmedoids_instance.process()
# Calculate the closest cluster to following two points.
# points = [[0.35, 0.5], [2.5, 2.0]]
# closest_clusters = kmedoids_instance.predict(points)
clusters = kmedoids_instance.get_clusters()
for each in clusters:
    for item in each:
        print(data_set[item], end="")
    print("----------------------")
# print(closest_clusters)
# visualizer = cluster_visualizer_multidim();
# visualizer.append_clusters(clusters, sample);
# visualizer.show();
