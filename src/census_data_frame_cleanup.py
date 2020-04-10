import pandas as pd
import numpy as np

def cleaning_census_data(df, ending_year):

    # Extract only Name, Population and Net Change columns
    pop_years = ['POPESTIMATE' + str(year) for year in list(range(2013,ending_year))]
    pop_change = ['NPOPCHG_' + str(year) for year in list(range(2013,ending_year)) ]
    name_col = ['NAME']

    columns = name_col + pop_years + pop_change
    new_df = df[columns]


    # Calculate and Add 2020 Population Estimate
    new_df['pop_chg_avg'] = new_df[['NPOPCHG_2018', 'NPOPCHG_2019']].mean(axis=1)
    new_df['POPESTIMATE2020'] = (new_df['POPESTIMATE2019'] + new_df['pop_chg_avg']).astype('int')

    # Extract Desired Columns only
    pop_years.append('POPESTIMATE2020')
    columns = name_col + pop_years
    new_df = new_df[columns]


    # Rename Year Columns
    pop_years_clean = [str(year) for year in list(range(2013,ending_year+1))]
    name_col_clean = ['Name']
    column_names = name_col_clean + pop_years_clean
    new_df.columns = column_names

    # Melt Data Frame so there is a row for every Year and Population and rename
    new_df = pd.melt(new_df, id_vars=['Name'], value_vars=pop_years_clean)
    new_df.rename(columns = {'variable' : 'Calendar_year', 'value' : 'Population'}, inplace = True)

    # Changed United States Values to National to match with CDC dataframes
    new_df = new_df.replace('United States', 'National')
    new_df['Calendar_year'] = new_df['Calendar_year'].astype(int)

    return new_df

# df = pd.read_csv("../data/nst-est2019-alldata.csv")
# print(cleaning_census_data(df,2020).head())