import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import csv
import matplotlib.pyplot as plt
import numpy as np

"""
df = pd.read_csv('C:\\Users\FitzL\Desktop\olympics.csv')
#print(df.head())
print("")

df = pd.read_csv('C:\\Users\FitzL\Desktop\olympics.csv', index_col = 0, skiprows=1)
#print(df.head())
print("")

#print(df.columns)
print("")

for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col:"Gold"+col[4:]}, inplace = True)
    if col[:2] == '02':
        df.rename(columns={col:"Silver"+col[4:]}, inplace = True)
    if col[:2] == '03':
        df.rename(columns={col:"Bronze"+col[4:]}, inplace = True)
    if col[:2] == '#':
        df.rename(columns={col:"#"+col[4:]}, inplace = True)
#print(df.head())
print("")

#print(df["Gold"] > 0)

only_gold = df.where(df["Gold"]>0)
print(only_gold.head())

df['country'] = df.index
df = df.set_index("Gold")
print(df.head())
print("------------------------")
df = df.reset_index()
print(df.head())
"""
a = 1
b = 2
c = 3
d = 4
e = 5

sales = [a,b,c,d,e]
df = pd.DataFrame(sales)
print(df)
df = df.rename(index={0: 'a'})
df = df.rename(index={1: 'b'})
df = df.rename(index={2: 'c'})
df = df.rename(index={3: 'd'})
df = df.rename(index={4: 'e'})
print(df)

try_ = pd.Series(
    [1,2,3,4,5],
    index=["A","B","C","D","E"]
)
#ax = df[[0]].plot(kind='bar', title ="Percentage", figsize=(15, 10), legend=True, fontsize=12)
plt.xlabel("The variable")
plt.ylabel("The value")
plt.ylim([0, 10])
plt.yticks(np.arange(0, 11, 1.0))

my_colors = 'rgbkymc'  #red, green, blue, black, yellow, purple, cyan etc.

try_.plot(
    kind='bar',
    color=my_colors,
)

plt.show()






s = pd.Series(
    [5, 4, 4, 1, 12],
    index = ["AK", "AX", "GA", "SQ", "WN"],
)

#Set descriptions:
plt.title("Total Delay Incident Caused by Carrier")
plt.ylabel('Delay Incident')
plt.xlabel('Carrier')
plt.xticks(rotation = 45)
#Set tick colors:
ax = plt.gca()
#ax.tick_params(axis='x', colors='blue', rotation = 90)
ax.tick_params(axis='y', colors='red', rotation = 45)

#Plot the data:
my_colors = 'rgbkymc'  #red, green, blue, black, yellow, purple, cyan etc.

s.plot(
    kind='bar',
    color=my_colors,
)

plt.show()



from scipy.stats import mstats


Col_1 = [1,2,3]
Col_2 = [1000,20000,1000]
Col_3 = [100,203,109]
Col_4 = [1,3,5]

print("Kruskal Wallis H-test test:")

H, pval = mstats.kruskalwallis(Col_1, Col_2, Col_3, Col_4)

print("H-statistic:", H)
print("P-Value:", pval)

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")