import pandas as pd
import numpy as np


def clean_csv(df):
    # get rid of Insufficient Data Rows
    mask = df['TOTAL DEATHS'] != 'Insufficient Data'
    new_df = df[mask]

    # get rid of commas
    new_df = new_df.replace(to_replace =',', value = '', regex = True) 

    # rename columns
    column_list = new_df.columns
    new_column_names = []
    for column in column_list:
        new_column_name = column.capitalize().replace(' ','_').replace('&','_')
        new_column_names.append(new_column_name)

    new_df.columns  = new_column_names
    
    return new_df 


def clean_columns(new_df, state = 'National'):
    # new columns
    new_df[['Num_influenza_deaths','Num_pneumonia_deaths','Total_deaths']] = \
    new_df[['Num_influenza_deaths','Num_pneumonia_deaths','Total_deaths']].astype(int)

    new_df['Percent_p_i'] = new_df['Percent_p_i']/100

    new_df['Percent_complete'] = new_df['Percent_complete'].str.replace('> 100%', '100%', regex=False)
    new_df['Percent_complete'] = new_df['Percent_complete'].str.rstrip('%').astype('float') / 100.0
    
    if state == 'National':
        new_df['Threshold'] = new_df['Threshold']/100
        new_df['Baseline'] = new_df['Baseline']/100
    else:
        pass

    return new_df 



def clean_ny(new_df, state = 'National'):
    # Combining New York and New York City data
    if state != 'National':
        mask = (new_df['Sub_area'] == 'New York') | (new_df['Sub_area'] == 'New York City')
        df_ny_combined = new_df[mask].groupby(['Season','Week']).sum()

        df_ny_combined = df_ny_combined.reset_index()
        df_ny_combined = df_ny_combined.drop('Percent_p_i',axis = 1)
        p_i_deaths = df_ny_combined['Num_influenza_deaths'] + df_ny_combined['Num_pneumonia_deaths']
        df_ny_combined['Percent_p_i'] = p_i_deaths/df_ny_combined['Total_deaths']
        df_ny_combined['Percent_complete'] = df_ny_combined['Percent_complete']/2

        df_ny_combined['Area'] = 'State'
        df_ny_combined['Sub_area'] = 'New York Combined'
        df_ny_combined['Age_group'] = 'All'

        list_of_cols = list(new_df.columns)
        df_ny_combined = df_ny_combined[list_of_cols]

        # merging combined NY data w/ original df
        new_df = pd.concat([new_df, df_ny_combined], axis = 0)
        mask = (new_df['Sub_area'] != 'New York City') & (new_df['Sub_area'] != 'New York')
        new_df = new_df[mask]
        new_df = new_df.replace('New York Combined', 'New York')
    else:
        pass

    return new_df

def add_cal_yr(new_df):
    conditions = [
        new_df['Week']<40,
        new_df['Week']>=40    
    ]

    new_df['First_year'] = new_df['Season'].apply(lambda x: int(x[0:4])) 
    new_df['Second_year'] = new_df['Season'].apply(lambda x: int(x[0:4])+1) 
    choices = [new_df['Second_year'],new_df['First_year']]
    new_df['Calendar_year'] = np.select(conditions,choices)
    new_df['Calendar_year'] = new_df['Calendar_year'].astype(int) 

    return new_df

def clean_and_sort(new_df, state = 'National'):
    #drop unused columns
    new_df = new_df.drop('First_year', axis = 1)
    new_df = new_df.drop('Second_year', axis = 1)
    new_df = new_df.drop('Age_group', axis = 1)
 
    if state == 'National':
        new_df = new_df.drop('Sub_area', axis = 1)
    else:
        new_df['State'] = new_df['Sub_area']
        new_df = new_df.drop('Sub_area', axis = 1)
        new_df = new_df.drop('Area', axis = 1)

    #sort values and reset index
    if state == 'National':
        new_df = new_df.sort_values(['Calendar_year','Week']).reset_index()
    else:
        new_df = new_df.sort_values(['State','Calendar_year','Week']).reset_index()

    new_df = new_df.drop('index', axis = 1)
        
    return new_df

def cleaning_cdc_df(df, state = 'National'):
    
    new_df = clean_csv(df)
    new_df = clean_columns(new_df, state)
    new_df = clean_ny(new_df,state)
    new_df = add_cal_yr(new_df)
    new_df = clean_and_sort(new_df, state)
    

    return new_df

df_national = pd.read_csv("../data/National_Custom_Data.csv")
df_states = pd.read_csv("../data/State_Custom_Data.csv")
print(cleaning_cdc_df(df_national).head())
print(cleaning_cdc_df(df_states, 'states').head())