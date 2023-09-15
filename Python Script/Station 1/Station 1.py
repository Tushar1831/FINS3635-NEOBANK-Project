#import pandas as pd
import pandas as pd

#importing numpy as np
import numpy as np

#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# import seaborn as sns
import seaborn as sns

#Import data
weather = pd.read_csv(r'C:\Users\tusha\OneDrive\Desktop\FINS3635 NEOBANK Project\Data\Weather (2).csv', encoding = 'latin1', delimiter = ',')  # Weather file

    # Client Cash Accounts

filename = r'C:\Users\tusha\OneDrive\Desktop\FINS3635 NEOBANK Project\Data\Client_Cash_Accounts (2).xlsx'

cash_account = pd.ExcelFile(filename)


    ## Corn Price History

filename_1 = r'C:\Users\tusha\OneDrive\Desktop\FINS3635 NEOBANK Project\Data\CORN_PriceHistory (4).xlsx'

corn_price_history = pd.ExcelFile(filename_1)

    ### Wheat Price History

filename_2 = r'C:\Users\tusha\OneDrive\Desktop\FINS3635 NEOBANK Project\Data\WHEAT_PriceHistory (2).xlsx'

wheat_price_history = pd.ExcelFile(filename_2)

# Converting excel files to Dataframes

cash_account_dict = pd.read_excel(cash_account, na_values = 'Missing', sheet_name = None) # Dictionary of DataFrames

corn_price_history_df = pd.read_excel(corn_price_history, na_values = 'Missing', sheet_name = 'Price History') 

wheat_price_history_df = pd.read_excel(wheat_price_history, na_values = 'Missing', sheet_name = 'Price History') 


# Cleansing and transforming weather to prepare for Station 2

    #Checking missing values
weather.isnull()

    # Using interpolate() to fill in missing values in DataFrame using linear method

weather = weather.interpolate(method = 'linear', limit_direction = 'forward') # Direction of maximum wind gust has null value

    


    # Dealing with outliers 
    
weather_numeric_col = ['Minimum temperature (°C)','Maximum temperature (°C)', 'Rainfall (mm)', 
                       'Speed of maximum wind gust (km/h)', '9am Temperature (°C)', '9am relative humidity (%)', 
                       '3pm Temperature (°C)', '3pm relative humidity (%)']

weather.boxplot(weather_numeric_col, rot = 90) # Visualising outliers

    ##Removing outliers and replacing them with null values
        ## Rainfall 

for x in ['Rainfall (mm)']:
    q75,q25 = np.percentile(weather.loc[:,x],[75,25])
    intr_qr = q75 - q25
    
    max = q75 + (1.5*intr_qr)
    min = q25 - (1.5*intr_qr)
    
    weather.loc[weather[x] < min,x] = np.nan
    weather.loc[weather[x] > max,x] = np.nan

        ## Minimum temperature (°C)
for x in ['Minimum temperature (°C)']:
    q75,q25 = np.percentile(weather.loc[:,x],[75,25])
    intr_qr = q75 - q25
    
    max = q75 + (1.5*intr_qr)
    min = q25 - (1.5*intr_qr)
    
    weather.loc[weather[x] < min,x] = np.nan
    weather.loc[weather[x] > max,x] = np.nan
    

        ## Maximum temperature (°C)
    
for x in ['Maximum temperature (°C)']:
    q75,q25 = np.percentile(weather.loc[:,x],[75,25])
    intr_qr = q75 - q25
    
    max = q75 + (1.5*intr_qr)
    min = q25 - (1.5*intr_qr)
    
    weather.loc[weather[x] < min,x] = np.nan
    weather.loc[weather[x] > max,x] = np.nan

for x in ['Speed of maximum wind gust (km/h)']:
    q75,q25 = np.percentile(weather.loc[:,x],[75,25])
    intr_qr = q75 - q25
    
    max = q75 + (1.5*intr_qr)
    min = q25 - (1.5*intr_qr)
    
    weather.loc[weather[x] < min,x] = np.nan
    weather.loc[weather[x] > max,x] = np.nan
    

for x in ['9am Temperature (°C)']:
    q75,q25 = np.percentile(weather.loc[:,x],[75,25])
    intr_qr = q75 - q25
    
    max = q75 + (1.5*intr_qr)
    min = q25 - (1.5*intr_qr)
    
    weather.loc[weather[x] < min,x] = np.nan
    weather.loc[weather[x] > max,x] = np.nan
    

for x in ['9am relative humidity (%)']:
    q75,q25 = np.percentile(weather.loc[:,x],[75,25])
    intr_qr = q75 - q25
    
    max = q75 + (1.5*intr_qr)
    min = q25 - (1.5*intr_qr)
    
    weather.loc[weather[x] < min,x] = np.nan
    weather.loc[weather[x] > max,x] = np.nan
    

for x in ['3pm Temperature (°C)']:
    q75,q25 = np.percentile(weather.loc[:,x],[75,25])
    intr_qr = q75 - q25
    
    max = q75 + (1.5*intr_qr)
    min = q25 - (1.5*intr_qr)
    
    weather.loc[weather[x] < min,x] = np.nan
    weather.loc[weather[x] > max,x] = np.nan
    
for x in ['3pm relative humidity (%)']:
    q75,q25 = np.percentile(weather.loc[:,x],[75,25])
    intr_qr = q75 - q25
    
    max = q75 + (1.5*intr_qr)
    min = q25 - (1.5*intr_qr)
    
    weather.loc[weather[x] < min,x] = np.nan
    weather.loc[weather[x] > max,x] = np.nan
    
    
    
    ## Removing null values from weather dataset
weather = weather.dropna(axis = 0)

    # Convert 'Date' to a Date-time dtype
import datetime as dt
weather['Date'] = pd.to_datetime(weather['Date']).dt.date

    #Check for duplicates

weather_duplicates = weather.duplicated(subset = ['Date'], keep = False)

        #Sorting
duplicated_weather_entries = weather[weather_duplicates].sort_values('Date')

        #Print relevant columns
print(duplicated_weather_entries['Date']) ## no duplicate entries found

    #Replace white space from '9am wind direction' with 'nan' then drop null values                   
weather['9am wind direction'] = weather['9am wind direction'].replace('',np.nan, regex = True)
weather = weather.dropna(axis = 0)


# Cleansing Corn Price DataFrame to prepare for Station 2
    # Removing rows 0-13 & columns 12-14  as they are irrelevant to dataset
corn_price_history_df.drop([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], axis = 0, inplace = True)
corn_price_history_df.head() # Rows dropped

corn_price_history_df.drop(['Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14'], axis = 1, inplace = True)
corn_price_history_df.head() # Columns dropped

    #Reset index
corn_price_history_df = corn_price_history_df.reset_index(drop = True)

    #Replace column names with header

new_header = corn_price_history_df.iloc[0]
corn_price_history_df = corn_price_history_df[1:]
corn_price_history_df.columns = new_header

corn_price_history_df = corn_price_history_df.fillna(0) #Fillned null value with as this was the first data entry required

corn_price_history_df.boxplot(rot = 90) # Visualising outliers

# Replacing outliers with null values

for x in ['Open Interest']:
    q75,q25 = np.percentile(corn_price_history_df.loc[:,x], [75,25])
    intr_qr = q75 - q25
    
    max = q75 + (1.5*intr_qr)
    min = q25 - (1.5*intr_qr)
    
    corn_price_history_df.loc[corn_price_history_df[x] < min,x] = np.nan
    corn_price_history_df.loc[corn_price_history_df[x] > max,x] = np.nan
    
for x in ['Cvol']:
    q75,q25 = np.percentile(corn_price_history_df.loc[:,x], [75,25])
    intr_qr = q75 - q25
    
    max = q75 + (1.5*intr_qr)
    min = q25 - (1.5*intr_qr)
    
    corn_price_history_df.loc[corn_price_history_df[x] < min,x] = np.nan
    corn_price_history_df.loc[corn_price_history_df[x] > max,x] = np.nan
 


# Cleansing Wheat Prices to prepare for Station 2 




# Cleansing and transforming cash_account_df to prepare for Station 2

    #Merging DataFrames within cash_account_df for each client
    


        



