import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import scipy.stats as stats
from src.stats_tests_functions import state_sample_statistics, box_plots, hypothesis_tests, weekly_comparison
import os

plt.ion()
plt.style.use('ggplot')
font = {'weight': 'bold',
        'size':   12}
plt.rc('font', **font)


if __name__ == "__main__":
    # os.chmod('src/cleaning_data_script.py', 777)

    # os.system('cleaning_data_script.py')

    exec(open('src/cleaning_data_script.py').read())
    # execfile()

    # use cleaning files to get clean DataFrames
    df_national_official = pd.read_csv('data/national_cdc_pandas_df.csv', index_col=0)
    df_states_official = pd.read_csv('data/states_cdc_pandas_df.csv', index_col=0)
    df_covid_states = pd.read_csv('data/states_covid_pandas_df.csv', index_col=0)
    df_covid_national = pd.read_csv('data/national_covid_pandas_df.csv', index_col = 0)

    # list of 12 states with most highest COVID Cases
    df = df_covid_states.groupby('State').sum()[['Deathincrease','Positiveincrease']].sort_values(by = 'Positiveincrease', ascending = False)
    df.iloc[0:12]
    list_of_states = df.index[0:12]
    lst_of_states = list(list_of_states)
    lst_of_states.append('National') # add national

    # Aggregate Stats Testing into CSV File
    p_value_dict = []
    for state in lst_of_states:
        if state == 'National':
            p_value_dict.append(hypothesis_tests(df_national_official, 2020, 2014, 14, 1))
        else:
            p_value_dict.append(hypothesis_tests(df_states_official, 2020, 2014, 15, 1, state = state))
    list_of_dicts = []
    for elem in p_value_dict:
        if elem == None:
            continue
        else:
            list_of_dicts.append(elem)
    stats_dict = pd.DataFrame(list_of_dicts)
    stats_dict.to_csv('images/stats_testing_results_through_wk12.csv')

    # obtain desired images
    for state in list_of_states:
        box_plots(df_states_official, 2020, 2014, 15, 1, state = state)


    weekly_comparison(df_national_official, df_covid_national)