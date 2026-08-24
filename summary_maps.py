import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#Exercise 1: Median
median_points = reviews.points.median()

#Exercise 2: Data in dataset
countries = reviews.country.unique()

#Exercise 3: Count
reviews_per_country = reviews.country.value_counts()

#Exercise 4: Centered price
centered_price = reviews.price - reviews.price.mean()

#Exercise 5: Highest rated wine
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

#Exercise 6: Counting
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

#Exercise 7: Score by country
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
    
star_ratings = reviews.apply(stars, axis='columns')