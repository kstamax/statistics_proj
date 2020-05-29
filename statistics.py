import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


class Interval:
    def __init__(self, a, b):
        self.values = []
        self.interval_min = a
        self.interval_max = b

def krok(a, b, items):
    part = (b-a)/items
    return part

def my_sigma(mu, my_list):
    summa = 0
    for item in my_list:
        summa+=(item - mu)**2
    summa = (summa/98)**1/2
    return summa

def gaussian(x, mu, sigma):
    return math.exp(-0.5*((x-mu)/sigma)**2) / sigma / math.sqrt(2*math.pi)

def ksisquare(empirical_frequences, expected_frequences):
    summa = 0
    for x in  range(len(empirical_frequences)):
        summa += (((empirical_frequences[x]-expected_frequences[x])**2)/expected_frequences[x])
    return summa

df = pd.read_excel(r'Variant19.xlsx', sheet_name=0)
my_list = list(df['Data'])
my_list.remove(53.24715)


h = krok(min(my_list), max(my_list), 7)
a = min(my_list)
b = min(my_list) + h
interval1 = Interval(a, b)
a = b
b+=h
interval2 = Interval(a,b)
a = b
b+=h
interval3 = Interval(a,b)
a = b
b+=h
interval4 = Interval(a,b)
a = b
b+=h
interval5 = Interval(a,b)
a = b
b+=h
interval6 = Interval(a,b)
a = b
b+=h
interval7 = Interval(a,b)

mu = np.mean(my_list)
sigma = my_sigma(mu, my_list)
list_intervalov = [interval1, interval2, interval3, interval4, interval5, interval6, interval7]
for interval in list_intervalov:
    for value in my_list:
        if value >= interval.interval_min and value<interval.interval_max:
            interval.values.append(value)

empirical_frequences = []
bins = []
for interval in list_intervalov:
    empirical_frequences.append(len(interval.values))
    bins.append(interval.interval_min) 
    bins.append(interval.interval_max)


expected_frequences = [abs(99*(gaussian(interval.interval_max, mu, sigma)-gaussian(interval.interval_min, mu, sigma))) for interval in list_intervalov]

ksi = ksisquare(empirical_frequences,expected_frequences)
ksikrit = 14.067
print(sigma)
print(empirical_frequences)
print(expected_frequences)
print(ksi)
fig, ax1 = plt.subplots()
ax1.boxplot(empirical_frequences)
fig, ax2 = plt.subplots()
ax2.hist(my_list, bins, histtype='bar', rwidth=0.8)

if ksi > ksikrit:
    print(ksi, '>', ksikrit)
    print("Гіпотизу відхиляємо")
else:
    print(ksi, '<', ksikrit)
    print("Гіпотизу приймаємо")
plt.show()