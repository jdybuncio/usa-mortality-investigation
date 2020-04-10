import requests
import json
import pandas as pd
import numpy as np
import datetime as dt


def get_data_from_api(api_url):
    r = requests.get(api_url)
    
    if r.status_code != 200:
        return 'api error'

    covid_list = json.loads(r.content)

    list_of_dicts = []
    for i in range(len(covid_list)):
        list_of_dicts.append(covid_list[i])

    df = pd.DataFrame(list_of_dicts)

    return df

def add_date_columns(df):

    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d', errors='ignore')

    start_date = min(df.date)
    end_date = max(df.date)
    date_series = pd.date_range(start_date, end_date, freq='D').to_series()
    df_date = pd.DataFrame(date_series)
    df_date = df_date.reset_index()
    df_date.columns = ['Date', 'Date2']
    df_date = df_date.drop('Date2', axis = 1)

    df_date['Week'] = df_date['Date'].apply(lambda x: (x + dt.timedelta(days=1)).weekofyear)
    df_date['Calendar_year'] = df_date['Date'].dt.year

    new_df = pd.merge(df, df_date,  how='left', 
                                    left_on=['date'], right_on = ['Date'])
    
    return new_df

def clean_df(new_df, state = 'National'):
    if state == 'National':
        columns = ['Date', 'Week', 'Calendar_year', 'deathIncrease',
            'hospitalizedIncrease', 'negativeIncrease', 'positiveIncrease',
            'totalTestResultsIncrease']
    else:
        columns = ['state', 'Date', 'Week', 'Calendar_year', 'deathIncrease',
            'hospitalizedIncrease', 'negativeIncrease', 'positiveIncrease',
            'totalTestResultsIncrease']

    new_df = new_df[columns]

    column_list = new_df.columns
    new_column_names = []
    for column in column_list:
        new_column_name = column.capitalize().replace(' ','_').replace('&','_')
        new_column_names.append(new_column_name)
    new_df.columns = new_column_names

    if state == 'National':
        new_df = new_df.sort_values('Date') 
    else:
        new_df = new_df.sort_values(['State','Date']) 

    
    new_df = new_df.reset_index()
    new_df = new_df.drop('index', axis = 1)

    new_df = new_df.dropna()

    return new_df

def clean_state_names(new_df):
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
    }

    state_map = {v: k for k, v in us_state_abbrev.items()}
    new_df['State'] = new_df['State'].apply(lambda x: state_map[x])
    return new_df

def cleaning_covid_data(api_url, state = 'National'):
    df = get_data_from_api(api_url)
    new_df = add_date_columns(df)
    new_df = clean_df(new_df,state)
    if state == 'National':
        return new_df
    else:
        new_df = clean_state_names(new_df)
        return new_df


# state_api_url = 'https://covidtracking.com/api/v1/states/daily.json'
# national_api_url = 'https://covidtracking.com/api/us/daily'
# print(cleaning_covid_data(state_api_url, 'state').head())
# print(cleaning_covid_data(national_api_url).head())