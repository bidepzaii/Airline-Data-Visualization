import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3


## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

## Task 1
sns.boxplot(x='coach_price', data=flight)
plt.title('Coach Price Tickets')
plt.show()
plt.clf()

## Task 2
sns.boxplot(flight['coach_price'][flight['hours'] == 8])
plt.title('8h Coach Price Tickets')
plt.show()
plt.clf()

## Task 3
flight_delay = flight[(flight['delay'] < 200)]

sns.displot(flight_delay['delay'], bins=30)
plt.title('Flight Delay Distribution')
plt.show()
plt.clf()

## Task 4
perc = 0.05
flight_sub = flight.sample(n = int(flight.shape[0]*perc))
sns.scatterplot(flight_sub['coach_price'], flight_sub['firstclass_price'], s=5)
plt.title('Coach and First Class Prices')
plt.show()
plt.clf()

sns.lmplot(x = 'coach_price', y = 'firstclass_price', data = flight_sub, line_kws={'color': 'black'}, lowess=True)
plt.title('Coach and First Class Prices 1')
plt.show()
plt.clf()


## Task 5
sns.boxplot(x='inflight_meal', y='coach_price', data=flight)
plt.title('Coach Price and Meal')
plt.show()
plt.clf()

sns.boxplot(x='inflight_entertainment', y='coach_price', data=flight)
plt.title('Coach Price and Entertainment')
plt.show()
plt.clf()

sns.boxplot(x='inflight_wifi', y='coach_price', data=flight)
plt.title('Coach Price and WiFi')
plt.show()
plt.clf()

## Task 6
sns.scatterplot(flight_sub['passengers'], flight_sub['hours'], s=5)
plt.title('Passenger and Hour')
plt.show()
plt.clf()

sns.lmplot(x='passengers', y='hours', data = flight_sub, x_jitter = .15, y_jitter = .15, fit_reg = False)
plt.title('Passenger and Hour Jitter')
plt.show()
plt.clf()

## Task 7
sns.lmplot(x ='coach_price', y='firstclass_price', hue = 'weekend', palette ='bright', data = flight_sub, fit_reg= False)
plt.title('Coach and First Class Price on Weekdays and Weekends')
plt.show()
plt.clf()

## Task 8
sns.boxplot(x='redeye', y='coach_price', data=flight_sub)
plt.title('Coach Price and RedEye')
plt.show()
plt.clf()

sns.boxplot(x = "day_of_week", y = "coach_price", hue = "redeye", data = flight)
plt.title('Coach Price and Redeye on each day of the Week')
plt.show()
plt.clf()





