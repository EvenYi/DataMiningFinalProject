# Background
Most research related with movie reviews on public reviewing platforms always classify movies or decide their quality according to the overall rating. However, consider about internet marketers will influence overall rating by giving high or low score deliberately, we use star distribution as feature to cluster movies. Then we analyze movies in different groups, from movie information to comments information. Particularly, we focus on movies in intersections where movies in different groups but have the same overall scores, and analyze the common and the different. 
# Part of results
Visualization of clustering results by K-medoids.
![clusteringresult](https://raw.githubusercontent.com/EvenYi/DataMiningFinalProject/master/Image/cluster_of_star_distribution.png)
## Pattern mining within each cluster
### Comments word cloud
Movies of b-shape star distribution:

![b-type](https://raw.githubusercontent.com/EvenYi/DataMiningFinalProject/master/Image/b_type_wordscloud.jpg)

movies of f-shape star distribution:

![f-type](https://raw.githubusercontent.com/EvenYi/DataMiningFinalProject/master/Image/f_type_wordscloud.jpg)

movies of L-shape star distribution:

![l-type](https://raw.githubusercontent.com/EvenYi/DataMiningFinalProject/master/Image/l_type_wordscloud.jpg)

movies of p-shape star distribution:

![p-type](https://raw.githubusercontent.com/EvenYi/DataMiningFinalProject/master/Image/p_type_wordscloud.jpg)

movies of v-shape star distribution:

![v-type](https://raw.githubusercontent.com/EvenYi/DataMiningFinalProject/master/Image/v_type_wordscloud.jpg)

### Type distribution
b-shape type distribution:
![b-types](Image/b_cluster_movie_type.png)
f-shape type distribution:
![f-type](Image/f_cluster_movie_type.png)
l-shape type distribution:
![l-type](Image/l_cluster_movie_type.png)
p-shape type distribution:
![p-type](Image/p_cluster_movie_type.png)
v-shape type distribution:
![v-type](Image/v_cluster_movie_type.png)

### Country distribution

b-shape country distribution:
![b-type-country](Image/b_cluster_movie_country.png)

f-shape country distribution:
![f-type-country](Image/f_cluster_movie_country.png)

l-shape country distribution:
![l-type-country](Image/l_cluster_movie_country.png)

p-shape country distribution:
![p-type-country](Image/p_cluster_movie_country.png)

v-shape country distribution:
![v-type-country](Image/v_cluster_movie_country.png)

## Pattern mining within interseciton
overall score distribution of movies in different star distribution groups
![score-type](https://raw.githubusercontent.com/EvenYi/DataMiningFinalProject/master/Image/DM-scores-type.png)

### Country distribution and type distribution

#### p-f intersection:
type comparison
![typepf](Image/DM-typepf.png)
country comparison
![countrypf](Image/DM-countrypf.png)

#### v-p intersection:
type comparison
![typevp](Image/DM-typevp.png)
country comparison
![countryvp](Image/DM-countryvp.png)

#### b-v intersection:
type comparison
![typebv]()
country comparison
![countrybv]()