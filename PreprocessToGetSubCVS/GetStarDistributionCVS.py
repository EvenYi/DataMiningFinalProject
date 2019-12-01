import pandas as pd
import numpy as np

data = pd.read_csv('../all_movies_with_id.csv')

data.head()

data.info()

data_star_distribution = data[['Movie_Name', 'Star_Distribution']]

data_star_distribution.head()

data_star_distribution = data_star_distribution.drop_duplicates()

data_star_distribution.head()

data_star_distribution.describe()

data_star_distribution.isnull().sum()

(data_star_distribution.duplicated(subset=['Movie_Name'])).sum()

data_star_distribution.drop_duplicates(subset=['Movie_Name'], inplace=True)

data_star_distribution.describe()

data_star_distribution.head()

data_star_distribution.to_csv(r'D:\python_ml\Datamining\DataMiningFinalProject\StarDistribution.csv', index=None, header=True)
