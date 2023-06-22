import os
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# for dirpath, dirname, filename in os.walk('.'):
#     print(dirpath)
#     print(dirname)
#     print(filename)



df=pd.read_csv('Cities_in_India_with_pincodes.csv',)


print(df.describe())

"""
              State   District Location Pincode
count         94238      94238    94238   94238
unique           28        414    80608   12795
top     Maharashtra  Anantapur   Rampur  852201
freq          10548        902       43      66

"""
# Count the number of unique cities

unique_cities=df['Location'].nunique()
print("Number of unique cities", unique_cities)
# Number of unique cities 80608

# Count the number of Post codes per city
post_code_per_city= df.groupby('Location')['Pincode'].count()

print("Post code per city : \n", post_code_per_city)

# Find the city with highest number of pin codes
city_with_most_postcodes=post_code_per_city.idxmax()
print("city with most postcodes", city_with_most_postcodes)

# Number of post codes
print("Number of post codes",post_code_per_city.max())


# Filter the dataset for a specific city
selected_city = "Arisala"
filtered_df=df[df['Location']==selected_city]
print("Post code for selected city: \n", filtered_df)


# Filter the location with specific pincode
selected_pincode="786160"
filtered_location=df[df["Pincode"]==selected_pincode]
print("Filtered location with Pincode: \n",filtered_location)

# create a dataframe from the dataset

data={
    'State':['Assam']*15,
    'District':['Tinsukia']*15,
    'Location':['Digboi',"DIGBOI CHARALI","GOLAI","MULIABARI","Doomdooma","BORDUBI TE",'Jagun','Kakopathar','Lido Town','Makum','Margherita','Sadiya','Bahbari Gaon','DIHINGIA GAON','HIJIGURI'],
    'Pincode':[786171,786171,786171,786171,786151,786151,786188,786152,786182,786170,786181, 786155,786192,786192, 86192]
}

df1=pd.DataFrame(data)
print(df1)
"""
    State  District        Location  Pincode
0   Assam  Tinsukia          Digboi   786171
1   Assam  Tinsukia  DIGBOI CHARALI   786171
2   Assam  Tinsukia           GOLAI   786171
3   Assam  Tinsukia       MULIABARI   786171
4   Assam  Tinsukia       Doomdooma   786151
5   Assam  Tinsukia      BORDUBI TE   786151
6   Assam  Tinsukia           Jagun   786188
7   Assam  Tinsukia      Kakopathar   786152
8   Assam  Tinsukia       Lido Town   786182
9   Assam  Tinsukia           Makum   786170
10  Assam  Tinsukia      Margherita   786181
11  Assam  Tinsukia          Sadiya   786155
12  Assam  Tinsukia    Bahbari Gaon   786192
13  Assam  Tinsukia   DIHINGIA GAON   786192
14  Assam  Tinsukia        HIJIGURI    86192
"""

# Count the number of locations in each pin code
pincode_counts=df1['Pincode'].value_counts().reset_index()

print(pincode_counts)

"""     index  Pincode
0  786171        1
1  786151        1
2  786188        1
3  786152        1
4  786182        1
5  786170        1
6  786181        1
7  786155        1
8  786192        1
 """

# how to assign different column names
pincode_counts.columns=['Pincode','count']
print(pincode_counts)

# plt.figure(figsize=(10,6))
# sns.barplot(x='Pincode',y='count', data=pincode_counts)
# plt.xlabel('Pincode')
# plt.ylabel('count')
# plt.title("Number of Location in each pincode")
# plt.xticks(rotation=45)
# plt.show()


# # Plot the pie chart for of pincode count

# plt.figure(figsize=(8,8))
# plt.pie(pincode_counts['count'], labels=pincode_counts['Pincode'],autopct="%1.1f%%",startangle=90)
# plt.axis('equal')
# plt.title("Percentage of location in each pin code")
# plt.show()

# Plot the count plot of locations by pincode
# plt.figure(figsize=(12,6))
# sns.countplot(x='Pincode',data=df1)
# plt.xlabel('Pincode')
# plt.ylabel('Location')
# plt.title('Number of locations by Pinocde')
# plt.xticks(rotation=45)
# plt.show()

# Display the first few row of dataset
print(df.head(20))
# count the number of pin codes per district

pincode_counts=df['District'].value_counts(50)
print(pincode_counts)


top_50_district=pincode_counts.head(50)

#create a bar plot 
plt.figure(figsize=(12,6))
pincode_counts.plot(kind='bar')
plt.title('Number of pin codes per District')
plt.xlabel('District')
plt.ylabel('Number of pincodes')
plt.xticks(rotation=90)
plt.show()


#count the number of pincodes per district
pincode_counts=df['District'].value_counts()

# Select the top 20 district

top_20_districts=pincode_counts.head(20)

# create a bar plot
plt.figure(figsize=(12,6))
top_20_districts.plot(kind='bar')
plt.title('Number of pin codes per district(TOP 20)')
plt.xlabel('District')
plt.ylabel('Number of pincodes')
plt.xticks(rotation=45)
plt.show()


# count the number of pin code per district
pincode_counts=df['District'].value_counts()
district_with_most_pin_codes=pincode_counts.idxmax()
max_pin_codes=pincode_counts.max()

print("District with most number of pincodes :", district_with_most_pin_codes)
print("Number of pin codes :", max_pin_codes)

# Count the number of pincodes by province
pincode_counts_by_province=df['State'].value_counts()

# create a bar plot
plt.figure(figsize=(12,6))
pincode_counts_by_province.plot(kind='bar')
plt.title("Number of pin codes by Province")
plt.xlabel("Province")
plt.ylabel("Number of pin codes")
plt.xticks(rotation=90)
plt.show()


# count the number of pin codes by state
pincode_counts_by_state=df['State'].value_counts()
# Filter state with less than 500 pin codes
filtered_state=pincode_counts_by_state[pincode_counts_by_state<500]

# create a bar plot
plt.figure(figsize=(12,6))
filtered_state.plot(kind='bar')
plt.title('Number of pin codes State(State with less than 500 pin codes)')
plt.xlabel('State')
plt.ylabel('NUmber of pin codes')
plt.xticks(rotation=45)
plt.show()

# Determine the state with highest, lowest and middle pin codes
highest_pincode_state=pincode_counts_by_state.idxmax()
lowest_pincode_state=pincode_counts_by_state.idxmin()
middle_pincode_state=pincode_counts_by_state.idxmin()

# Get the pin code counts by selected state
select_states=[highest_pincode_state,lowest_pincode_state,middle_pincode_state]
selected_counts=pincode_counts_by_state[select_states]
print(selected_counts)


# create a bar plot
plt.figure(figsize=(12,6))
selected_counts.plot(kind='bar')
plt.title('Number of pin codes by State')
plt.xlabel('State')
plt.ylabel('Number of pin codes')
plt.xticks(rotation=45)
plt.show()

# Count the number of pin codes by state

pincode_counts_by_state=df['State'].value_counts()
# Sort the states based on pin code counts in descending order
sorted_states=pincode_counts_by_state.sort_values(ascending=False)

# determine the state with highest and second lowest pin code counts
highest_pincode_state=sorted_states.index[0]
second_lowest_pincode_state=sorted_states.index[-2]

# Get the pin code counts for state

selected_states=[highest_pincode_state,second_lowest_pincode_state]
selected_counts=pincode_counts_by_state[selected_states]

# create a bar plot
plt.figure(figsize=(12,6))
selected_counts.plot(kind='bar')
plt.title('Number of pin code by State')
plt.xlabel('State')
plt.ylabel('Number of pin  codes')
plt.xticks(rotation=90)
plt.show()

# Filter the data set for Punjab state
punjab_df=df[df['State']=='Delhi']
# count the number of pincodes per district in Punjab
pincode_counts_by_district=punjab_df['District'].value_counts()
print(pincode_counts_by_district)
# create a pie chart
plt.figure(figsize=(8,8))
plt.pie(pincode_counts_by_district,labels=pincode_counts_by_district.index,autopct="%1.1f%%",startangle=90)
plt.title("Pin codes in Punjab by district")
plt.axis('equal')
plt.show()
