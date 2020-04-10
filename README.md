## Using overall United States Mortality to better understand the daily COVID-19 reports
COVID-19 has changed our day-to-day lives significantly and the fall-out effects will be studied for years to come. As of April 6th, 2020, the United States has 41 out of its 50 states with Statewide orders to stay at home  [source](https://www.nytimes.com/interactive/2020/us/coronavirus-stay-at-home-order.html). Additionally, this virus has changed our daily consumption and understanding of death. Most major news outlets in the United States report on daily deaths attributed to COVID-19 despite not normally reporting on mortality totals.  

The following work seeks to add perspective to the daily COVID-19 death totals by comparing them to overall mortality in the United States.  This work's findings provide insight into understanding death data, its pitfalls, and interesting trends, specifically about Influenza & Pneumonia, which may suggest how to view the current COVID-19 totals.

[Accompanying Presentation](https://docs.google.com/presentation/d/1xqk53rEZo9x1Xlf2_WRjyKPh7DWyq3CcHR3l3D6QIRM/edit?usp=sharing)

*by Jaime DyBuncio*

## Table of Contents
- [Goals](#goals)
- [Background](#background)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Hypothesis Tests](#hypothesis-tests)
- [Conclusion](#conclusion)
- [Data Sources](#data-sources])


## Goals
This work seeks to answer the following questions:
<ol>
<li>How do the COVID-19 totals compare to overall United States mortality?</li>
<li>Is the overall United States death rate showing different behavior relative to prior years?</li>
<li>Is the Percentage of Deaths due to Influenza and Pneumonia diverging in 2020 vs. prior years?</li>
</ol>


## Background

<p align="center">
  <img src="images/Weekly_Avg_DR.png" width = 800>
</p>

As the graph shows, the United States averaged over 54,000 deaths per week in 2019. This is useful to use as a barometer to the weekly COVID-19 Death totals we have been ingesting on a day-to-day basis. For example, using 2019's deaths per week as a baseline and comparing it to the most recent COVID-19 data:

* Last week (Mar 29 - Apr 4):
    - The U.S. had 6,300+ deaths classified as COVID-19. This represents ~12%+ of Weekly Avg Deaths in 2019. 
    - New York had 2,800+ COVID-19 deaths last week. NY averaged just over 3k deaths per week last yr.
* This week (Apr 5 - Apr 11):
    - The U.S. is trending towards 11,000 deaths due to COVID-19.  This represents ~20%+ of Weekly Avg Deaths in 2019. 
    - New York is trending towards 4,700 COVID-19 deaths this week.

While I would like to look deeper into if the rise in COVID-19 deaths are closely associated with a rise in overall U.S. mortality, the majority of COVID-19 deaths have occurred in the last two weeks and U.S. mortality data is only reliable from 3 weeks ago.  The mortality data I am using comes from the CDC and utilizes a mortality surveillance system led by The National Center for Health Statistics (NCHS) who receives reporting for all deaths in the U.S. from state vital statistics offices. The data comes from death certificates and the deceased are attributed to their state of residence.  Due to the hand-offs in reporting, there is usually a 2-3 week lag, i.e. the most recent data available data is from 2 weeks ago, but applying the CDC's marker of "% Complete", the most recent data which is 100% complete is from 3 weeks ago.

Despite this, a couple things stick out when looking deeper into U.S. mortality data which will be covered in the next section.  Also, the data pipelines created as part of this project will expedite one's ability to look further into the relationship of overall U.S. mortality and COVID-19 deaths in the subsequent weeks when the CDCs data updates to cover the period into April, 2020.


## Exploratory Data Analysis

<p align="center">
  <img src="images/Annual_DR_Trend.png" width = 800>
</p>

The lines above show the Weekly Death Rate (Total Deaths in the U.S. per 100k in population) by week of the year and across years for the deaths occurring in the United States.  There is clear seasonality in our country's death rate, with it peaking at the beginning and the end of each year.

Something sticks out though when observing the Red-Line which represents 2020's data through March 21st. This only uses data from the CDC marked as 100% Complete.  The Red-Line seems to be following a much lower trajectory than that observed in prior years which would be a surprise.  This would suggest that the U.S. Death Rate this year is actually lower than prior years despite the global pandemic.  It should not be left out though that the deaths due to COVID-19 grew dramatically in the past 3 weeks, which is not included in this dataset, but several States were already in lock-down in the last 2-3 data points shown for 2020.  

Not shown on this graph, but also in the CDC data, suggests that despite the appearingly lower Death Rate, the percent of deaths due to Pneumonia and Influenza started to spike in the U.S. in Weeks 12 and 13.  

Therefore, I seek to answer two core questions via Hypothesis Testing in the next section:

1. Is U.S. Weekly Death Rate (Weely Deaths per 100k)  in 2020 lower compared to that in 2019 and in 2014-19? Data allows me to compare through Week 12 (March 21st).


2. Since I also have Flu & Pneumonia data, is the % of  Deaths due to Influenza & Pneumonia in 2020 higher than that seen in 2019 and 2014-19? Data allows me to compare through Week 13 (March 28th) for certain states.




## Hypothesis Tests


The two Hypothesis Tests I ran to answer the two questions stated above are:
- One-Tailed Mann-Whitney Signed Rank Test to compare to see if 2020's Death Rate is lower than prior year through Week 12.
- Two-Tailed Mann-Whitney Signed Rank Test to compare to see if 2020's % of Deaths due to Influenza & Pneumonia is different than prior years through Week 13

The box plots below show the Interquartile ranges for the two respective sample statistics across the year intervals I am comparing against 2020: Avg Weekly Death Rate (per 100k population) & % of Deaths due to Influenza & Pneumonia.

The two Null Hypothesis Tests I set out to perform are:
1. Weekly Death Rate differences 
    - Null Hypothesis: P(Die in a wk in 2019 > Die in a wk in 2020) = 0.50
    - Alternative Hypothesis: P(Die in a wk in 2019 > Die in a wk in 2020) ≠ 0.50
2. % of Deaths due to Influenza & Pneumonia
    - Null Hypothesis: P(Death due to Influenza & Pneumonia in 2020 > Death due to I&P in 2019) = 0.50
    - Alternative Hypothesis: P(Death due to Influenza & Pneumonia in 2020 > Death due to I&P in 2019)  ≠ 0.50


<p align="center">
  <img src="images/National_thru_wk_12.png" width = 800>
</p>


<p align="center">
  <img src="images/New York_thru_wk_13.png" width = 800>
</p>


Through Weeks 1-12 (through Mar 21), 2014-19 and 2019 had higher death rates than 2020 in the U.S. (𝞪 = 0.01), but this does not hold in the 12 States w/ the highest amount of COVID-19 deaths.

Through Weeks 1-13 (through Mar 28), I failed ot reject the null hypothesis that there is any difference in the % of Deaths due to Influenza & Pneumonia at an alpha of 0.10 for all the top 12 States with the highest amount of COVID-19 deaths aside from Florida (NY is close). But, the totals in the past two weeks are peaking and are highlighted by the two outliers seen in New York's graph.



## Conclusion

[
Issues with daily mortality data explain common headlines popping up.  Daily Death #s & Cause are regularly report on. 
- CDC goes back and publishes Deaths due to Influenza in 2 year lookback.
- CDC only recently added COVID death code.
- CDC marks data as 100% complete but it can still change.
- Issues between discerning b/w Pneumonia, Influenza, & COVID-19
- Russia is classifying all Pneumonia deaths as COVID 

Will re-run analysis to keep watchful eye on how 2020’s overall mortality & pneumonia deaths continue to evolve relative to prior years when thinking about COVID-19 totals.










## Data Sources
Using data from the CDC, The Covid Tracking Project, and the U.S. Census, this repository creates data pipelines for overall U.S. mortality and investigates relationships with it and COVID and Influenza mortality.


*   CDC Influenza & Pneumonia Sources:
    -   [Data Source](https://gis.cdc.gov/grasp/fluview/mortality.html)
    -   [Methods](https://www.cdc.gov/flu/weekly/overview.htm)
    -   [Home Page](https://www.cdc.gov/flu/weekly/index.htm)

*   COVID-19 Sources:
    -   [Data Source: COVID-19 Tracking Project](https://covidtracking.com/data/us-daily)
    -   [Data Source: CDC COVID-19 Death Data](https://www.cdc.gov/nchs/nvss/vsrr/COVID19/index.htm)
    -   [CDC Home Page](https://www.cdc.gov/coronavirus/2019-ncov/covid-data/covidview.html)

*   Census Population Sources:
    -   [Census Data](https://www.census.gov/data/tables/time-series/demo/popest/2010s-state-total.html)

*   Supporting Sources
    -   [Where have all the heart attacks gone?](https://www.nytimes.com/2020/04/06/well/live/coronavirus-doctors-hospitals-emergency-care-heart-attack-stroke.html)
    -   [Increases of deaths at home in NYC](https://gothamist.com/news/surge-number-new-yorkers-dying-home-officials-suspect-undercount-covid-19-related-deaths)
    -   [Issues with undercounting/misreporting](https://www.ibtimes.com/coronavirus-usa-death-toll-nears-10000-experts-say-us-undercounting-2953054)
    -   [Issues with undercounting & CDCs lag](https://www.cnn.com/2020/04/06/health/us-coronavirus-death-count-cdc-explainer/index.html)
