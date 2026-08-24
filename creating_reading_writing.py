import pandas as pd
pd.set_option('display.max_rows', 5)

#Exercise 1: Dataframe
fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])

#Exercise 2: Dataframe
fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])

#Exercise 3: Series
ingredients = pd.Series(
    ['4 cups', '1 cup', '2 large', '1 can'],
    index=['Flour', 'Milk', 'Eggs', 'Spam'],
    name='Dinner'
)

#Exercise 4: Read CSV
reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)

#Exercise 5: Save dataframe
animals.to_csv("cows_and_goats.csv")
