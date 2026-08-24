import pandas as pd
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#Exercise 1: Copy
renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))

#Exercise 2: Index
reindexed = reviews.rename_axis('wines', axis='rows')

#Exercise 3: Dataset
combined_products = pd.concat([gaming_products, movie_products])

#Exercise 4: Powerlifting database
powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))

