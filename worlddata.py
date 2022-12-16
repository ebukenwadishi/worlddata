
#imported neccessary libraries 
import numpy as np
import pandas as pd

#function to load the dataset and also using OOP concept to make the dataframe a global 
def ols_reg(filename):
    global df
    df = pd.read_csv(f"{filename}.csv")     #assumption: the directory of both files is same  
    print(df.head())

ols_reg('world data')

"""The dataset extracted from the world data shows 15 unique countries over the period of 10 years with GDP and social rating impact of the countries. """
#To get the top 5 records 
df.head()
#to know the column names 
df.columns
#to remove space in the country 
df['Country'] =df['Country '].str.strip()
#to get some statistical result 
df.describe()
#to check the number of unique countires in the dataset 
df['Country'].nunique()
#to get the unique countires in the dataset 
df['Country'].unique()
#to get the number of unique countires in the dataset 
df['Year'].nunique()
#to get the unique year names in the dataset
df['Year'].unique()
#to check the column names 
df.columns
#to get the GDP value and the total numbers for each
df['GDP'].value_counts()
#to get the rating impact and the total numbers for each
df['ratingimpact'].value_counts()
#to check the relationship between all the features 
df.corr()

"""There are high correlation of years recorded over the impact ratings in the dataset. This shows that the occurence in the countires over the years has a huge effort on the social impact ratings in the countries. """
