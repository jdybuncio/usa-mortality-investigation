import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import scipy.stats as stats

plt.ion()
plt.style.use('ggplot')
font = {'weight': 'bold',
        'size':   12}
plt.rc('font', **font)


def state_sample_statistics(dframe, curr_yr = 2020, starting_yr = 2014, week_end = 12, pct_complete_thresh = 1, state = 'National'):
    
    week_labels = list(dframe['Week'].unique())
    week_labels.sort()
    weeks_lst = week_labels[:week_end]

    years_labels = list(dframe['Calendar_year'].unique())
    years_labels.sort()
    start_index = years_labels.index(starting_yr)
    years_lst = years_labels[start_index:]
    
    dr_curr_yr = []
    dr_last_yr = []
    dr_range = []

    pi_curr_yr = []
    pi_last_yr = []
    pi_range = []
        
    for week in weeks_lst:
        
        for year in years_lst:
            if state == 'National':
                mask = (dframe['Week'] == week) & \
                        (dframe['Calendar_year'] == year) & \
                        (dframe['Percent_complete'] >= pct_complete_thresh)
            else:
                mask = (dframe['Week'] == week) & \
                        (dframe['Calendar_year'] == year) & \
                        (dframe['State'] == state) & \
                        (dframe['Percent_complete'] >= pct_complete_thresh)
            
            df = dframe[mask]
            
            if len(df['Total_deaths']) == 0:
                continue    
            else: 
                if year == curr_yr:
                    dr_curr_yr.append(round(df['Deaths_per_hund_thou'].iloc[0],2))
                    pi_curr_yr.append(round(df['Percent_p_i'].iloc[0],4))
                    
                elif year == curr_yr - 1:
                    
                    dr_last_yr.append(round(df['Deaths_per_hund_thou'].iloc[0],2))
                    pi_last_yr.append(round(df['Percent_p_i'].iloc[0],4))
                    
                    dr_range.append(round(df['Deaths_per_hund_thou'].iloc[0],2))
                    pi_range.append(round(df['Percent_p_i'].iloc[0],4))
                    
                else:
                    dr_range.append(round(df['Deaths_per_hund_thou'].iloc[0],2))
                    pi_range.append(round(df['Percent_p_i'].iloc[0],4))

    return [dr_curr_yr, dr_last_yr, dr_range, pi_curr_yr, pi_last_yr, pi_range]


def box_plots(dframe, curr_yr = 2020, starting_yr = 2014, week_end = 12, pct_complete_thresh = 1, state = 'National'):
    
    dr_curr_yr_lst, dr_prior_yr_lst, dr_range_lst, pi_curr_yr_lst, pi_prior_yr_lst, pi_range_lst = \
        state_sample_statistics(dframe, curr_yr, starting_yr, week_end, pct_complete_thresh, state)
              
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    
    for idx, ax in enumerate(axs.flatten()):
        curr_year_label = str(curr_yr)
        prior_year_label = str(curr_yr-1)
        range_label = str(starting_yr) + '-' + str(curr_yr-1)
        if idx == 0:

            bplot1 = ax.boxplot([dr_range_lst, dr_prior_yr_lst, dr_curr_yr_lst],
                                 vert=True,
                                 patch_artist=True) 
            ax.set_xticks([1,2,3])
            ax.set_xticklabels([f'{range_label} n={len(dr_range_lst)}', 
                                f'{prior_year_label} n={len(dr_prior_yr_lst)}', 
                                f'{curr_year_label} n ={len(dr_curr_yr_lst)}'])

            ax.set_title(f'{state} Box Plot of Avg Weekly Death Rates by Year',fontsize = 12)
            ax.set_ylabel('Avg Wkly Death Rate (Deaths per 100k)', fontsize = 12)
            
            ax.tick_params(axis = 'x', labelsize = 8)
            ax.tick_params(axis = 'y', labelsize = 8)
           
        elif idx == 1:
            
            bplot2 = ax.boxplot([pi_range_lst, pi_prior_yr_lst, pi_curr_yr_lst],
                                 vert=True,
                                 patch_artist=True)
            ax.set_xticks([1,2,3])
            ax.set_xticklabels([f'{range_label} n={len(pi_range_lst)}', 
                                f'{prior_year_label} n={len(pi_prior_yr_lst)}', 
                                f'{curr_year_label} n ={len(pi_curr_yr_lst)}'])
            
            ax.set_title(f'{state} Box Plot of Avg Weekly % of Deaths from Influenza and Pneumonia',fontsize = 10)
            ax.set_ylabel('Avg Wkly % of Deaths Infl&Pneum. ', fontsize = 10)
           
            ax.tick_params(axis = 'x', labelsize = 8)
            ax.tick_params(axis = 'y', labelsize = 8)
            
    # fill with colors
    colors = ['pink', 'lightyellow', 'lightgreen']
    for bplot in (bplot1, bplot2):
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)
    
    # plt.show()
    plt.tight_layout()
    plt.savefig('images/{0}_thru_wk_{1}.png'.format(state,week_end))

def hypothesis_tests(dframe, curr_yr = 2020, starting_yr = 2014, week_end = 12, pct_complete_thresh = 1, state = 'National'):
    
    dr_curr_yr_lst, dr_prior_yr_lst, dr_range_lst, pi_curr_yr_lst, pi_prior_yr_lst, pi_range_lst = \
        state_sample_statistics(dframe, curr_yr, starting_yr, week_end, pct_complete_thresh, state)
    
    ## Death Rate
    
    if len(dr_curr_yr_lst)>5:
        #non param test to see if avg death rate last year is equal to avg death rate this yr
        _, p_val_dr_mw_yr = stats.mannwhitneyu(dr_prior_yr_lst, dr_curr_yr_lst, alternative="greater")
    
        #non param test to see if avg death rate over range is equal to avg death rate this yr
        _, p_val_dr_mw_range = stats.mannwhitneyu(dr_range_lst, dr_curr_yr_lst, alternative="greater")

        #param test to see if avg death rate over range is equal to avg death rate this yr
        _, p_val_dr_t_yr = stats.ttest_ind(dr_prior_yr_lst, dr_curr_yr_lst, equal_var = False)

        #param test to see if avg death rate over range is equal to avg death rate this yr
        _, p_val_dr_t_range = stats.ttest_ind(dr_range_lst, dr_curr_yr_lst, equal_var = False)


        ## Flu & Pneumonia

        _, p_val_pi_mw_yr = stats.mannwhitneyu(pi_curr_yr_lst, pi_prior_yr_lst, alternative="two-sided")

        #non param test to see if avg death rate over range is equal to avg death rate this yr
        _, p_val_pi_mw_range = stats.mannwhitneyu(pi_curr_yr_lst, pi_range_lst, alternative="two-sided")

        #param test to see if avg death rate over range is equal to avg death rate this yr
        _, p_val_pi_t_yr = stats.ttest_ind(pi_prior_yr_lst, pi_curr_yr_lst, equal_var = False)

        #param test to see if avg death rate over range is equal to avg death rate this yr
        _, p_val_pi_t_range = stats.ttest_ind(pi_range_lst, pi_curr_yr_lst, equal_var = False)
    
        d = {}
        d['state'] = state
        d['samp_size_curr_yr'] = len(dr_curr_yr_lst)
        d['pval_dr_MW_yr'] = '{:2.3f}'.format(p_val_dr_mw_yr)
        d['pval_dr_MW_range'] = '{:2.3f}'.format(p_val_dr_mw_range)
        d['pval_dr_T_yr'] = '{:2.3f}'.format(p_val_dr_t_yr)
        d['pval_dr_T_range'] = '{:2.3f}'.format(p_val_dr_t_range)

        d['pval_pi_MW_yr'] = '{:2.3f}'.format(p_val_pi_mw_yr)
        d['pval_pi_MW_range'] = '{:2.3f}'.format(p_val_pi_mw_range)
        d['pval_pi_T_yr'] = '{:2.3f}'.format(p_val_pi_t_yr)
        d['pval_pi_T_range'] = '{:2.3f}'.format(p_val_pi_t_range)

        return d
    else:
        pass