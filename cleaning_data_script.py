import pandas as pd
from src.cdc_data_frame_cleanup import cleaning_cdc_data
from src.covid_data_frame_cleanup import cleaning_covid_data
from src.census_data_frame_cleanup import cleaning_census_data


#1 Census Data
df = pd.read_csv("data/nst-est2019-alldata.csv")

df_population = cleaning_census_data(df,2020)
df_population.to_csv('data/population_df.csv')


#2 COVID Data
state_api_url = 'https://covidtracking.com/api/v1/states/daily.json'
national_api_url = 'https://covidtracking.com/api/us/daily'

df_covid_state = cleaning_covid_data(state_api_url, 'state')
df_covid_state.to_csv('data/states_covid_pandas_df.csv')

df_covid_natl = cleaning_covid_data(national_api_url)
df_covid_natl.to_csv('data/national_covid_pandas_df.csv')

#3 CDC Data
national_cdc_data = pd.read_csv("data/National_Custom_Data.csv")
state_cdc_data = pd.read_csv("data/State_Custom_Data.csv")


df_national = cleaning_cdc_data(national_cdc_data)
df_states = cleaning_cdc_data(state_cdc_data, 'states')


df_states_official = pd.merge(df_states, df_population,  how='left', 
                                left_on=['State','Calendar_year'], right_on = ['Name','Calendar_year'])
# Drop useless col and add Deaths per hund thou metric
df_states_official = df_states_official.drop('Name', axis = 1)
df_states_official['Deaths_per_hund_thou'] = df_states_official['Total_deaths'] / (df_states_official['Population']/100000)
df_states_official['Percent_p'] = df_states_official['Num_pneumonia_deaths'] / df_states_official['Total_deaths']

df_states_official.to_csv('data/states_cdc_pandas_df.csv')

#Merge National and Population DataFrame to get Population
df_national_official = pd.merge(df_national, df_population,  how='left', 
                                left_on=['Area','Calendar_year'], right_on = ['Name','Calendar_year'])
# Drop useless col and add Deaths per hund thou metric
df_national_official = df_national_official.drop('Name', axis = 1)
df_national_official['Deaths_per_hund_thou'] = df_national_official['Total_deaths'] / (df_national_official['Population']/100000)
df_national_official['Percent_p'] = df_national_official['Num_pneumonia_deaths'] / df_national_official['Total_deaths']
df_national_official.to_csv('data/national_cdc_pandas_df.csv')
