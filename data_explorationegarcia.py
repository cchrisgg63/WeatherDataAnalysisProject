
# type pip install pandas if you don't have this downloaded already
#and download numpy as well
#importing pandas and numpy for data
import pandas as pd
import numpy as np

text = 'Start of project: ' 
print(text.center(50))

print()

#download the CSV and insert the path with your own information path
#opens the csv files and chnages the values with any * into a NaN
data = pd.read_csv('/Users/admin/reactapp/ECGTech/WeatherDataAnalysisProject/6153237444115dat.csv', na_values = ['*','**','***','****','*****','******'])

# this shows the data if you need to see.  data.info()



#displays the names of the columns in csv
print(data.columns)

#displays the data types for dataset
#print('data dtypes are')
#print(data.dtypes)
print()


print('Mean of TEMP Data is:')
print(round(data['TEMP'].mean(), 2))
print('Standard Deviation of Max Data is :')
print(round(data['MAX'].std(), 2))

USAF_to_city = {
    28450: 'rovaniemi',
    29980: 'kumpula'
}

unique = data['USAF'].unique()

#map them to names
unique_names = [USAF_to_city[code] for code in unique]
print('Unique list is: ', unique_names)
print()


print('Amount of NA or invalid data points in the CSV will appear below:  ')


#selects the desired columns and puts them into a variable
selected = data.loc[:,('USAF', 'YR--MODAHRMN', 'TEMP', 'MAX', 'MIN')]
#Printing the new table with the amount of NaNs that were detected in that csv selection
print(selected.isna().sum())
#creates a new variable with the dropped values from TEMP with NaN
print('Now the NaN values have been removed')
selected = selected.dropna(subset=['TEMP', 'MAX', 'MIN'])
print(selected)



#Creating a new column with the conversion for column TEMP into Celsius with 2 decimal places
#Rounds the number to the closet 0 from the equation 
ConvertedTemp = ((selected['TEMP'] - 32.0) / 1.8)
selected['Celsius'] = round(ConvertedTemp, 2)




#classifies the rows that have 29980 and 28450 as kumpula or rovaniemi into a new column called City
selected['City'] = selected['USAF'].replace({28450: 'Kumpula', 29980: 'Rovaniemi'})
#Now reorganizing the columns to have City in the front and USAF in the back
cols = selected.columns.tolist()
#removing the column and appending it will push it all the way to the back
cols.remove('USAF')
cols.append('USAF')
#this will grab the city column ,remove it, and move it to the first spot
cols.insert(0,cols.pop(cols.index('City')))
#this will reorganize the columns to the new config
selected= selected[cols]


#check the headers of the data a quick snippet basically and we can see all the updated information we did
print('New column added with Celsius Calcualations: ')
print(selected.head())





#creates a new dataframe for kumpula and rovaniemi using the old data that we removed unnessary data and added a Celsius column then separated the 
#two datatables into Kumpula and Rovaniemi


data1 = selected[selected['USAF'] == 28450]
#rovaniemi
data2 = selected[selected['USAF'] == 29980]

print()

print('Median Celsius for Kumpula was: ')
print(data1['Celsius'].median())
print()

text = 'Kumpula May Weather Statistics are:  '
print(text.center(50))
print()
#this variable below will only select the tables dates from a certain date which is listed below...

may_values = data1.loc[
    (data1['YR--MODAHRMN'] >= 201705010000) & 
    (data1['YR--MODAHRMN'] < 201706010000)
]
#round will shorten the calculation and give a easier to read number

KumpCelMeanMay = round(may_values['Celsius'].mean(), 1)
print(f'May Mean is :   {KumpCelMeanMay}')

KumpCelMaxMay = may_values['Celsius'].max()
print(f'May max Celsius is: {KumpCelMaxMay}')

KumpCelMinMay = may_values['Celsius'].min()
print(f'May min is : {KumpCelMinMay}')

print()
text = 'Kumpula June Weather Statistics are:  '
print(text.center(50))
print()

june_values = data1.loc[
    (data1['YR--MODAHRMN'] >= 201705010000) & 
    (data1['YR--MODAHRMN'] < 201706010000)
]

KumpCelMean = round(june_values['Celsius'].mean(), 1)
print(f'May Mean is :   {KumpCelMean}')

KumpCelMax = june_values['Celsius'].max()
print(f'May max Celsius is: {KumpCelMax}')

KumpCelMin = june_values['Celsius'].min()
print(f'May min is : {KumpCelMin}')


#Now to process Rovaniemi's data
print()
print('Median Celsius for Rovaniemi was: ')
print(data2['Celsius'].median())
print()

text = 'Rovaniemi May Weather Statistics are:  '
print(text.center(50))
print()

may_values2 = data2.loc[
    (data2['YR--MODAHRMN'] >= 201705010000) & 
    (data2['YR--MODAHRMN'] < 201706010000)
]

RovCelMeanMay = round(may_values2['Celsius'].mean(), 1)
print(f'May Mean is :   {RovCelMeanMay}')

RovCelMaxMay = may_values2['Celsius'].max()
print(f'May max Celsius is: {RovCelMaxMay}')

RovCelMinMay = may_values2['Celsius'].min()
print(f'May min is : {RovCelMinMay}')


print()

june2_values = data2.loc[
    (data2['YR--MODAHRMN'] >= 201706010000) & 
    (data2['YR--MODAHRMN'] < 201707010000)
]

text = 'Rovaniemi June Weather Statistics are:  '
print(text.center(50))
print()

RovCelMean= round(june2_values['Celsius'].mean(), 1)
print(f'June Mean is :  {RovCelMean}')

RovCelMax = june2_values['Celsius'].max()
print(f'June max Celsius is: {RovCelMax}')

RovCelMin = june2_values['Celsius'].min()
print(f'June min is : {RovCelMin}')

print()