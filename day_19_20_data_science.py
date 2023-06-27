import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('pokemon.csv')
print(data.head())
print(data.info())
print(data.corr())


f,ax=plt.subplots(figsize=(18,18))
sns.heatmap(data.corr(),annot=True, linewidth=0.5,fmt='0.1f',ax=ax)
plt.show()

# will show 10 lines
print(data.head(10))
print(data.columns)
# Line plot

data.Speed.plot(kind='line', color='g',label='Speed',linewidth=1,alpha=0.5,grid=True,linestyle=':')
data.Defense.plot(kind='line', color='g',label='Defense',linewidth=1,alpha=0.5,grid=True,linestyle='-')
plt.legend(loc='upper right')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Line Plot')
plt.show()
aplha Stands for Opacity


# Scatter plot
# x = attack y = defense
data.plot(kind='scatter',x='Attack',y='Defense',alpha=0.5,color='red')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Attack Defense Scatter plot')
plt.show()

# Histogram
# bin is number of bar in figure
data.Speed.plot(kind='hist', bins=50,figsize=(12,12))
plt.show()

data=pd.read_csv('pokemon.csv')
series=data['Defense']
print(type(series))
data_frame=data[['Defense']]
print(type(data_frame))
# <class 'pandas.core.series.Series'>
# <class 'pandas.core.frame.DataFrame'>

# Filtering the data frame
x=data['Defense']>200
print(data[x])

# Filtering Pandas with logical and
print(data['Defense']>200)
print(data['Attack']>100)
# y=data['Defense']>200 & data['Attack']>100
# print(y)
print(data[np.logical_and(data['Defense']>200,data['Attack']>100)])

# Anonymous finction
number_list=[1,2,3]
y=list(map(lambda x:x**2, number_list))
print(y)

# Iterator
name='ronaldo'
it=iter(name)
print(next(it))  # Print next iteration
print(*it)  # Print remaining iteration

# Zip and unzip in Python
list1=[1,2,3,4]
list2=[5,6,7,8]
z=zip(list1,list2)
print(z)
z_list=list(z)
print(z_list)

#How to unzip the data
unzip=zip(*z_list)
un_list1,unlist2=list(unzip)
print(un_list1)
print(unlist2)
print(type(un_list1))


"""
<zip object at 0x000001BA04F30340>
[(1, 5), (2, 6), (3, 7), (4, 8)]
(1, 2, 3, 4)
(5, 6, 7, 8)
<class 'tuple'>

"""

# Data Cleaning 

data=pd.read_csv('pokemon.csv')
print(data.head())
print(data.tail())
print(data.columns)
print(data.shape)
print(data.info())
print(data.describe())
# """
#               #          HP      Attack     Defense     Sp. Atk     Sp. Def       Speed  Generation
# count  800.0000  800.000000  800.000000  800.000000  800.000000  800.000000  800.000000   800.00000
# mean   400.5000   69.258750   79.001250   73.842500   72.820000   71.902500   68.277500     3.32375
# std    231.0844   25.534669   32.457366   31.183501   32.722294   27.828916   29.060474     1.66129
# min      1.0000    1.000000    5.000000    5.000000   10.000000   20.000000    5.000000     1.00000
# 25%    200.7500   50.000000   55.000000   50.000000   49.750000   50.000000   45.000000     2.00000
# 50%    400.5000   65.000000   75.000000   70.000000   65.000000   70.000000   65.000000     3.00000
# 75%    600.2500   80.000000  100.000000   90.000000   95.000000   90.000000   90.000000     5.00000
# max    800.0000  255.000000  190.000000  230.000000  194.000000  230.000000  180.000000     6.00000

# """ 


data.boxplot(column='Attack',by='Legendary')
plt.show()

# Melt and pivot the data
data_new=data.head()
print(data_new)
# """    #           Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
# 0  1      Bulbasaur  Grass  Poison  45      49       49       65       65     45           1      False
# 1  2        Ivysaur  Grass  Poison  60      62       63       80       80     60           1      False
# 2  3       Venusaur  Grass  Poison  80      82       83      100      100     80           1      False
# 3  4  Mega Venusaur  Grass  Poison  80     100      123      122      120     80           1      False
# 4  5     Charmander   Fire     NaN  39      52       43       60       50     65           1      False
#  """

# # Lets melt
# # id_vars # what we do not to melt
# # value_vars # what we want to melt

melted=pd.melt(frame=data_new,id_vars='Name',value_vars=['Attack','Defense'])
print(melted)

"""             Name variable  value
0      Bulbasaur   Attack     49
1        Ivysaur   Attack     62
2       Venusaur   Attack     82
3  Mega Venusaur   Attack    100
4     Charmander   Attack     52
5      Bulbasaur  Defense     49
6        Ivysaur  Defense     63
7       Venusaur  Defense     83
8  Mega Venusaur  Defense    123
9     Charmander  Defense     43 """


# Reverse of melting is called as Pivoting
# In pivoting row data becomes column
print(melted.pivot(index='Name',columns='variable',values='value'))
""" variable       Attack  Defense
Name
Bulbasaur          49       49
Charmander         52       43
Ivysaur            62       63
Mega Venusaur     100      123
Venusaur           82       83 """

# We can concatenate two data frame

data1=data.head()
data2=data.tail()
concatenate_data_row=pd.concat([data1,data2],axis=0,ignore_index=True)
print(concatenate_data_row)


# Now how to add two data along the column use axis=1
data1=data['Attack'].head()
data2=data['Defense'].head()
conc_data_col=pd.concat([data1,data2],axis=1)
print(conc_data_col)
"""    Attack  Defense
0      49       49
1      62       63
2      82       83
3     100      123
4      52       43 """

# Missing the data and testing with assert

""" 
What we can do with missing data
--> leave as it is
--> drop them dropna()
--> fill missing value with fillna()
--> fill missing with test statistics like mean
"""
print(data.info())
# Lets check Type2
print(data['Type 2'].value_counts(dropna=False))
data1=data

# Indexing Pandas Time Series
time_list=["1992-03-08","1994-04-12"]
print(type(time_list[1]))



data=pd.read_csv('pokemon.csv')
data2=data.head()
date_list=["1992-01-10","1992-02-10","1992-03-10","1992-04-10","1993-05-10"]
datetime_object=pd.to_datetime(date_list)
print(datetime_object)
data2["date"]=datetime_object
data2=data2.set_index("date")
print(data2)

"""             #           Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
date
1992-01-10  1      Bulbasaur  Grass  Poison  45      49       49       65       65     45           1      False
1992-02-10  2        Ivysaur  Grass  Poison  60      62       63       80       80     60           1      False
1992-03-10  3       Venusaur  Grass  Poison  80      82       83      100      100     80           1      False
1992-04-10  4  Mega Venusaur  Grass  Poison  80     100      123      122      120     80           1      False
1993-05-10  5     Charmander   Fire     NaN  39      52       43       60       50     65           1      False
 """

# Now we can select any data using location
print(data2.loc["1992-01-10"])
print(data2.loc["1992-01-10":"1992-04-10"])
"""             #           Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
date
1992-01-10  1      Bulbasaur  Grass  Poison  45      49       49       65       65     45           1      False
1992-02-10  2        Ivysaur  Grass  Poison  60      62       63       80       80     60           1      False
1992-03-10  3       Venusaur  Grass  Poison  80      82       83      100      100     80           1      False
1992-04-10  4  Mega Venusaur  Grass  Poison  80     100      123      122      120     80           1      False
 """

# Resample with year
print(data2.resample("A").mean())
"""               #     HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
date
1992-12-31  2.5  66.25   73.25     79.5    91.75    91.25  66.25         1.0        0.0
1993-12-31  5.0  39.00   52.00     43.0    60.00    50.00  65.00         1.0        0.0

"""
# Resample with MONTH
print(data2.resample("M").mean())

"""               #    HP  Attack  Defense  ...  Sp. Def  Speed  Generation  Legenda
ry
date                                    ...

1992-01-31  1.0  45.0    49.0     49.0  ...     65.0   45.0         1.0        0
.0
1992-02-29  2.0  60.0    62.0     63.0  ...     80.0   60.0         1.0        0
.0
1992-03-31  3.0  80.0    82.0     83.0  ...    100.0   80.0         1.0        0
.0
1992-04-30  4.0  80.0   100.0    123.0  ...    120.0   80.0         1.0        0
.0
1992-05-31  NaN   NaN     NaN      NaN  ...      NaN    NaN         NaN        N
aN
1992-06-30  NaN   NaN     NaN      NaN  ...      NaN    NaN         NaN        N
aN
1992-07-31  NaN   NaN     NaN      NaN  ...      NaN    NaN         NaN        N
aN
1992-08-31  NaN   NaN     NaN      NaN  ...      NaN    NaN         NaN        N
aN
1992-09-30  NaN   NaN     NaN      NaN  ...      NaN    NaN         NaN        N
aN
1992-10-31  NaN   NaN     NaN      NaN  ...      NaN    NaN         NaN        N
aN
1992-11-30  NaN   NaN     NaN      NaN  ...      NaN    NaN         NaN        N
aN
1992-12-31  NaN   NaN     NaN      NaN  ...      NaN    NaN         NaN        N
aN
1993-01-31  NaN   NaN     NaN      NaN  ...      NaN    NaN         NaN        N
aN
1993-02-28  NaN   NaN     NaN      NaN  ...      NaN    NaN         NaN        N
aN
1993-03-31  NaN   NaN     NaN      NaN  ...      NaN    NaN         NaN        N
aN
1993-04-30  NaN   NaN     NaN      NaN  ...      NaN    NaN         NaN        N
aN
1993-05-31  5.0  39.0    52.0     43.0  ...     50.0   65.0         1.0        0
.0

[17 rows x 9 columns]
 """

# print(data2.resample("M").first().interpolate("linear"))
# print(data2.resample("M").mean().interpolate("linear"))

# Manipulating dataframes with Pandas

""" 
1.Indexing using square brackets
2. Using column attribute and row
3. loc accessor
4. selecting only some columns
"""

data=pd.read_csv('pokemon.csv')
data=data.set_index("#")
print(data.head())


# Indexing using square bracket
print(data["HP"][1])

# Using column attribute and row labels
print(data.HP[1])

# Using loc accessor
print(data.loc[1,["HP"]])
print(data.loc[1,["HP","Type 2"]])

# Difference between selecting column seris and DataFrame
print(type(data["HP"]))  # Series
print(type(data[["HP"]])) # DataFrame
""" <class 'pandas.core.series.Series'>
<class 'pandas.core.frame.DataFrame'> """


# Slicing and indexing the series 
print(data.loc[1:10,"HP":"Defense"])
"""     HP  Attack  Defense
#
1   45      49       49
2   60      62       63
3   80      82       83
4   80     100      123
5   39      52       43
6   58      64       58
7   78      84       78
8   78     130      111
9   78     104       78
10  44      48       65
 """

# Reverse slicing 
print(data.loc[10:1:-1,"HP":"Defense"])

# Iloc method in pandas-which works in fetching the row data with indexing
print(data.iloc[0])
""" Name          Bulbasaur
Type 1            Grass
Type 2           Poison
HP                   45
Attack               49
Defense              49
Sp. Atk              65
Sp. Def              65
Speed                45
Generation            1
Legendary         False
Name: 1, dtype: object """

# Filtering the dataframe
boolean=data.HP>200
print(data[boolean])
"""         Name  Type 1 Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
#
122  Chansey  Normal    NaN  250       5        5       35      105     50           1      False
262  Blissey  Normal    NaN  255      10       10       75      135     55           2      False
 """

boolean2=data.Attack>5
print(data[boolean & boolean2])
"""         Name  Type 1 Type 2   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
#
262  Blissey  Normal    NaN  255      10       10       75      135     55           2      False """

# Also , we can filter the columns based on other columns

print(data.HP[data.Attack>60])

# How to transform a data
# Plain Python function
# Lambda function
# Defining column using other columns

# def div(n):
#     return n/2

# # Use apply method for applying function
# print(data.HP.apply(div))

# Apply attribite for column
data.HP.apply(lambda n : n/2)

# Defining a column using others column
data["Total Power"]=data.Attack + data.Defense
print(data.head())
"""             Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  Total Power
#
1      Bulbasaur  Grass  Poison  45      49       49       65       65     45           1      False           98
2        Ivysaur  Grass  Poison  60      62       63       80       80     60           1      False          125
3       Venusaur  Grass  Poison  80      82       83      100      100     80           1      False          165
4  Mega Venusaur  Grass  Poison  80     100      123      122      120     80           1      False          223
5     Charmander   Fire     NaN  39      52       43       60       50     65           1      False           95 """


# How to chnage our index name
# Print the current index name
print(data.index.name)  # #

data.index.name="index_name"
print(data.head())
"""                      Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  Total Power
index_name
1               Bulbasaur  Grass  Poison  45      49       49       65       65     45           1      False           98
2                 Ivysaur  Grass  Poison  60      62       63       80       80     60           1      False          125
3                Venusaur  Grass  Poison  80      82       83      100      100     80           1      False          165
4           Mega Venusaur  Grass  Poison  80     100      123      122      120     80           1      False          223
5              Charmander   Fire     NaN  39      52       43       60       50     65           1      False           95
 """

# If we have to change the index value , we have to change all of them.
# Copy the data to new variable
data3=data.copy()
print(data3.head())
data3.index=range(100,900,1)
print(data3.head())

# Hierarchial indexing 
data1=data.set_index(["Type 1","Type 2"])  # Type 1 is outer and Type2 is inner index
print(data1.head())
"""                         Name  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary  Total Power
Type 1 Type 2
Grass  Poison      Bulbasaur  45      49       49       65       65     45           1      False           98
       Poison        Ivysaur  60      62       63       80       80     60           1      False          125
       Poison       Venusaur  80      82       83      100      100     80           1      False          165
       Poison  Mega Venusaur  80     100      123      122      120     80           1      False          223
Fire   NaN        Charmander  39      52       43       60       50     65           1      False           95 """

print(data1.loc["Grass"])
# Pivoting the dataframe
dic={"treatment":["A","A","B","B"],"gender":["F","M","F","M"],"response":[10,45,5,9],"age":[15,4,72,65]}
df=pd.DataFrame(dic)
print(df)

print(df.pivot(index='treatment',columns='gender',values='response'))

""" gender      F   M
treatment
A          10  45
B           5   9
 """
print(df.pivot(index='treatment',columns='gender',values=['response','age']))

""" 
          response     age
gender           F   M   F   M
treatment
A               10  45  15   4
B                5   9  72  65

"""

print("====")
print(df.pivot(index='treatment',columns=['gender','age'],values='response'))
""" 
gender        F     M    F    M
age          15    4    72   65
treatment
A          10.0  45.0  NaN  NaN
B           NaN   NaN  5.0  9.0
"""
# Stacking and Unstacking DataFrame
df1=df.set_index(['treatment','gender'])
print(df1)
"""
                  response  age
treatment gender
A         F             10   15
          M             45    4
B         F              5   72
          M              9   65

"""

print("Unstack level 0",df1.unstack(level=0))

""" 
          response    age
treatment        A  B   A   B
gender
F               10  5  15  72
M               45  9   4  65
"""

print(df1.unstack(level=1))
""" 
          response     age
gender           F   M   F   M
treatment
A               10  45  15   4
B                5   9  72  65

"""
print(df1)
"""
                  response  age
treatment gender
A         F             10   15
          M             45    4
B         F              5   72
          M              9   65

"""

# Swap lebel

df2=df1.swaplevel(0,1)
print(df2)
""" gender treatment response  age
F      A                10   15
M      A                45    4
F      B                 5   72
M      B                 9   65
"""

# melting the DataFrame
print(pd.melt(df, id_vars="treatment",value_vars=["age","response"]))

# Group by 
print(df.groupby("treatment").mean())
 
