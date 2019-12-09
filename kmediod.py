from pyclustering.cluster.kmedoids import kmedoids
import pandas as pd
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
# Initial medoids for sample 'Simple3'.
initial_medoids = [4358, 10, 13, 456, 536, 3229, 614]

# Create instance of K-Medoids algorithm with prepared centers.
'''
def my_cosine(point1, point2):
    result = 1 - spatial.distance.cosine(point1, point2)
    return result
'''

# metric = distance_metric(type_metric.USER_DEFINED, func=my_cosine)
# metric = distance_metric(type_metric.MANHATTAN, degree=5)
kmedoids_instance = kmedoids(sample, initial_medoids)
# Run cluster analysis.
kmedoids_instance.process()
# Calculate the closest cluster to following two points.
# points = [[0.35, 0.5], [2.5, 2.0]]
# closest_clusters = kmedoids_instance.predict(points)
clusters = kmedoids_instance.get_clusters()
f_type_cluster = []
for item in clusters[0]:  # f type
    # print(data_set[item], end="")
    f_type_cluster.append(data_set[item])

p_type_cluster = []
for item in clusters[1]:  # p type
    # print(data_set[item], item, end="")
    p_type_cluster.append(data_set[item])
for item in clusters[2]:
    # print(data_set[item], item, end="")
    p_type_cluster.append(data_set[item])

v_type_cluster = []
for item in clusters[3]:  # > type
    # print(data_set[item], item, end="")
    v_type_cluster.append(data_set[item])

for item in clusters[5]:
    # print(data_set[item], item, end="")
    v_type_cluster.append(data_set[item])

b_type_cluster = []
for item in clusters[4]:  # b type
    # print(data_set[item], item, end="")
    b_type_cluster.append(data_set[item])


l_type_cluster = []
for item in clusters[6]:  # L type
    # print(data_set[item], item, end="")
    l_type_cluster.append(data_set[item])


f_type = pd.DataFrame(f_type_cluster, columns=['Movie_Name', 'Star_Distribution'])
p_type = pd.DataFrame(p_type_cluster, columns=['Movie_Name', 'Star_Distribution'])
v_type = pd.DataFrame(v_type_cluster, columns=['Movie_Name', 'Star_Distribution'])
b_type = pd.DataFrame(b_type_cluster, columns=['Movie_Name', 'Star_Distribution'])
l_type = pd.DataFrame(l_type_cluster, columns=['Movie_Name', 'Star_Distribution'])

print(f_type.head())
print(p_type.head())
print(v_type.head())
print(b_type.head())
print(l_type.head())
f_type.to_csv(r'D:\python_ml\Datamining\DataMiningFinalProject\Data\f_type_cluster.csv', index=None, header=True)
p_type.to_csv(r'D:\python_ml\Datamining\DataMiningFinalProject\Data\p_type_cluster.csv', index=None, header=True)
v_type.to_csv(r'D:\python_ml\Datamining\DataMiningFinalProject\Data\v_type_cluster.csv', index=None, header=True)
b_type.to_csv(r'D:\python_ml\Datamining\DataMiningFinalProject\Data\b_type_cluster.csv', index=None, header=True)
l_type.to_csv(r'D:\python_ml\Datamining\DataMiningFinalProject\Data\l_type_cluster.csv', index=None, header=True)

# print(closest_clusters)
# visualizer = cluster_visualizer_multidim();
# visualizer.append_clusters(clusters, sample);
# visualizer.show();
