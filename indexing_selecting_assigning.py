import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

#Exercise 1: Select columns 
desc = reviews.description

#Exercise 2: Select columns
first_description = reviews.description.iloc[0]

#Exercise 3: Select rows
first_row = reviews.iloc[0]

#Exercise 4: Select and assign
first_descriptions = reviews.description.iloc[:10]

#Exercise 5: Select with indexing
indices = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[indices]

#Exercise 6: Select with indexing
cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]

#Exercise 7: Select with range
cols = ['country', 'variety']
df = reviews.loc[:99, cols]

#Exercise 8: Select with filtering
italian_wines = reviews[reviews.country == 'Italy']

#Exercise 9: Select with filtering
italian_wines = reviews[reviews.country == 'Italy']
top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand']))
    & (reviews.points >= 95)
]