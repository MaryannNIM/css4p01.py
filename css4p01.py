# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:59:58 2024

@author: User
"""

import pandas as pd
import statistics
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv("movie_dataset.csv")

print(df)
print(df.info())

print(df.describe())


#To get the highest rated movie
highest_rated_movie = df['Rating'].max()
Movie_name = df.query(f'Rating=={highest_rated_movie}')
print(Movie_name['Title'])



#To get the average revenue.
average_revenue = df['Revenue (Millions)'].mean()
print(average_revenue)



#To get the average revenue from 2015-2017.
Average = df.query('Year>=2015 and Year<=2016')
average_revenue = Average['Revenue (Millions)'].mean()
print(average_revenue)



#How many movies were released in year 2016?
Released_year = len(df.query('Year==2016'))
print(Released_year)



#How many movies in the dataset have a rating of at least 8.0?
Movie_Rating = len(df.query('Rating>=8.0'))
print(Movie_Rating)




#How many movies were directed by Christopher Nolan
Director_name = len(df.query('Director=="Christopher Nolan"'))
print(Director_name)



#What is the median rating of movies directed by Christopher Nolan?

ratings = df.query('Director=="Christopher Nolan"')['Rating']
statistics.median(ratings)
print(statistics.median(ratings))


#What is the percentage increase in number of mumber of movies made between 2006 and 2016
Released_year_2016 = len(df.query('Year==2016'))
Released_year_2006 = len(df.query('Year==2006'))
Percentage_increase = 100*(Released_year_2016 - Released_year_2006)/Released_year_2016
print(Percentage_increase)



#Year with the highest average rating
highest_rated_movie = df['Rating'].max()
Movie_Year = df.query(f'Rating=={highest_rated_movie}')
print(Movie_Year['Year'])




#Find the most common actor in all the movies

Actor_split = pd.DataFrame(df['Actors'].str.split(',',).tolist(),index=df['Rank']).stack()

n = Actor_split.nunique('0')

print(n)





#How many genre are there in the dataset
Genre_split = pd.DataFrame(df['Genre'].str.split(',',).tolist(),index=df['Rank']).stack()

n = Genre_split.nunique('0')

print(n)



#Correlation of Yearly Revenue

x = df['Year']
y = df['Revenue (Millions)']
plt.title("Yearly Revenue")
plt.xlabel("Year")
plt.ylabel("Revenue (Millions)")
plt.bar(x, y)
plt.show()












