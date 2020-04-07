# United States Mortality Investigation
As of April 6, 2020, the United States has 41 states with Statewide orders to stay at home to prevent the further spread of COVID-19 [source](https://www.nytimes.com/interactive/2020/us/coronavirus-stay-at-home-order.html). This was done in the context of the growing threat of COVID-19 and related death estimates in the hundreds-of-thousands [source](https://www.nytimes.com/aponline/2020/03/29/us/politics/ap-us-virus-outbreak-washington.html?searchResultPosition=3).  The following work seeks to look at how the worldwide pandemic and drastic changes to daily lives may have impacted overall United States mortality at both the national and state levels.  


## Goals
<ol>
<li>Is overall United States mortality showing different behavior relative to prior years?</li>
<li>Is there any relationship between COVID-19 cases and overall mortality seen in U.S. States?</li>
<li>How can prior flu-season data frame the current projections of COVID-19's impact relative to overall mortality?</li>
</ol>


## TL/DR
<ol>
<li>Look into overall Mortality in the context of a pandemic. Adds something to compare daily numbers and reports to since we are not used to seeing deaths reported daily</li>
<li>Adds insight into potential ramifications of statewide shutdowns and corresponding changes in behavior<li>
<li>Provides color into issues with reporting on deaths and COVID-19 (& pneumonia)  which helps to explain social discourse and confusion<li>
<li>Looks into prior Flu Seasons to put COVID-19 projections against them - both the projections with and without social distancing<li> 
</ol>


##  Working Plan

*   Monday:
    -   Finalize research question
    -   Create GitHub Repo
    -   Add Data Source 1 
    -   Initial Clean of Data
*   Tuesday:
    -   Add Data Source 2
    -   Initial Clean of Data 2
    -   Join Data Together
    -   Initial EDA
*   Wednesday
    -   Define Hypthesis Tests
    -   Work on Visualizatons
    -   Build out intro on Causes of Death vs. Trump Tweet
*   Thursday
    -   Continue finalizing EDA
    -   Start Powerpoint Presentation
*   Friday
    -   Finalize GitHub Repo
    -   Finalize Powerpoint Presentation    

## Slide Deck

*   Slide Deck - Slide 1:
    -   Context: Stay-at-home order Map
    -   Context: Growing Corona Cases and Deaths reported everyday which we aren't used to
    -   How about overall mortality? Visual
    -   Looking into overall mortality can give us: Perspective to current #s, Insight into impact of Behavioral Changes, & shine light on confusion in reporting on COVID-19 and Deaths in general
*   Slide Deck - Slide 2:
    -   Overall Mortality different in behavior than prior years - natiowide & state levels?
    -   Reasons of Death in USA in 2017
    -   Add in reasons why we could be seeing less: More Deaths at Home, Less Cardiac patients at hospital, and Change in Behaviors
    -   Data Reporting Issues: Call into question data methodology. Why there can be increased lag this year in relation to prior.   
*   Slide Deck - Slide 3:
    -   Any relationship between COVID-19 cases and overall mortality observed? 
    -   We report daily on rise in COVID cases, but similarly, what is change in overall Deaths and would it follow intuition that overall is rising as well (i.e. somewhere like NYC seeing more overal deaths this year?)
    -   Data Issues: Add in rise in pneumonia and lack of COVID-19 deaths tracked on CDC. Mention sources which speak to underreporting of COVID-19.  
*   Slide Deck - Slide 4:
    -   Current COVID-19 death projections has been another major discourse. What are projections with and without social distancing in relation to overall mortality?
    -   Trump Tweet
    -   Interesting Flu related data relative to overall mortality. Difference in Influenza, Pneumonia, & COVID-19
*   Slide Deck - Slide 5:
    -   Summary
    -   Perspective: Overall Mortality in these times where we're seeing one type of death reported every day
    -   Impact of Change in Behaviors: connected to above topic
    -   Data Issues: Confusion and various discourses are seen in unreliable data and changing behaviors
    -   COVID vs. Prior Flu Seasons 

## Data Sources
Using data from the CDC and The Covid Tracking Project, this repository creates data pipelines for overall U.S. mortality and investigates relationships with it and COVID and Influenza mortality.


*   CDC Influenza&Pneumonia Sources:
    -   [Data Source](https://gis.cdc.gov/grasp/fluview/mortality.html)
    -   [Methods](https://www.cdc.gov/flu/weekly/overview.htm)
    -   [Home Page](https://www.cdc.gov/flu/weekly/index.htm)

*   COVID-19 Sources:
    -   [Data Source: COVID-19 Tracking Project](https://covidtracking.com/data/us-daily)
    -   [Data Source: CDC COVID-19 Death Data](https://www.cdc.gov/nchs/nvss/vsrr/COVID19/index.htm)
    -   [CDC Home Page](https://www.cdc.gov/coronavirus/2019-ncov/covid-data/covidview.html)

*   Cause of Death Sources:
    -   [Data Source: CDC 2017 Cause of US Deaths](https://www.cdc.gov/nchs/fastats/leading-causes-of-death.htm)
    -   [Causes of Death in 2017 by State](//www.cdc.gov/nchs/data/dvs/LCWK9_2015.pdf)

*   Supporting Sources
    -   [Where have all the heart attacks gone?](https://www.nytimes.com/2020/04/06/well/live/coronavirus-doctors-hospitals-emergency-care-heart-attack-stroke.html)
    -   [Increases of deaths at home in NYC - could explain lower mortality and also definitely explaines lower COVID-19 counts](https://gothamist.com/news/surge-number-new-yorkers-dying-home-officials-suspect-undercount-covid-19-related-deaths)
    -   [Issues with undercounting/misreporting](https://www.ibtimes.com/coronavirus-usa-death-toll-nears-10000-experts-say-us-undercounting-2953054)
    -   [Issues with undercounting & CDCs lag](https://www.cnn.com/2020/04/06/health/us-coronavirus-death-count-cdc-explainer/index.html)
    -   [Trump Tweet about Flu](https://twitter.com/realdonaldtrump/status/1237027356314869761)
    -   [COVID-19 mutating less so than flu](https://www.msn.com/en-gb/health/other/coronavirus-seems-to-mutate-much-slower-than-seasonal-flu/ar-BB12e9ci?li=AAJt1k3)
 
## Useful quotes

* "But another 200 city residents are now dying at home each day, compared to 20 to 25 such deaths before the pandemic, said Aja Worthy-Davis, a spokeswoman for the medical examiner’s office. And an untold number of them are unconfirmed"
* "The FDNY says it responded to 2,192 cases of deaths at home between March 20th and April 5th, or about 130 a day, an almost 400 percent increase from the same time period last year. (In 2019, there were just 453 cardiac arrest calls where a patient died, according to the FDNY.) "
* “a subset of the whole testing fiasco.” 
* "Meanwhile, city and hospital morgues and refrigerated trucks used to supplement them are nearing capacity, and first responders continue to answer unprecedented numbers of 911 calls every day. They’re averaging more than 6,400 a day over the last 11 days, compared to 4,500 before the pandemic, according to union officials. "
