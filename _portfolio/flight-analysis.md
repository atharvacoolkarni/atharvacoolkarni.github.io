---
title: "Flight Analysis [work in progress]"
excerpt: "Machine learning analysis of flight delays and prediction patterns using commercial flight data"
collection: portfolio
layout: single
classes: wide
permalink: /projects/flight-analysis/
date: 2025-09-14
last_modified_at: 2025-09-15
---

<div class="notice">
  <strong>Note:</strong><br> 
  <br>
  This project only uses two years (2004 and 2005) out of all the years available in the dataset (1987 - 2008). I will be redoing this analysis for the entire dataset soon and updating it here. Few of the reference links have also shut down or moved away from their domain so the references used will also be updated soon.<br>
  <br>
  Stay tuned!
</div>

## Project Overview
This project explores **flight data analysis and prediction patterns**.  
The main goals were:
- Analyze flight delay patterns and identify key factors 
- Visualize air traffic trends and seasonal patterns
- Predict flight delays using machine learning models 

The analysis is based on commercial flight data and combines statistical analysis and machine learning to obtain meaningful insights.

This project was done for University of London's third year course 'Programming for Data Science' during my BSc. Economics degree. The full coursework question set can be found here [ST2195_Coursework (PDF)](/assets/projects/flight-analysis/st2195_coursework.pdf)

The questions are:
1. When is the 
    1. best time of day to fly to minimise delays?
    1. day of the week to fly to minimise delays?
    1. time of year to fly to minimise delays?
1. Do older planes suffer more delays?
1. How does the number of people flying between different locations change over time?
1. Can you detect cascading failures as delays in one airport create delays in others?
1. Use the available variables to construct a model that predicts delays.

## Introduction
Airline travel is an immensely popular mode of transportation, with billions of people taking it every year [[1]]. In 2019, there were approximately 38.3 million flights worldwide, and while the COVID-19 pandemic caused a significant dip in air travel, the numbers are expected to rebound [[1]]. Despite increased efficiency since the start of flight travel, flight delays remain a persistent issue for travellers. Through data exploration and modelling, this study aims to analyse trends in flight delays, connections, and other factors, providing insight into how flight data evolves over time.

## Data

The data is from the Data Expo 2009: Airline on time data found in the Harvard Dataverse [[2]]. The data has 29 variables detailing each flight. When reading the data for both Python and R, the files for the code should be in the data folder or the working directory must be set to where the data is located.

## Data pre-processing

To start with, for the purposes of answering the specific questions within this report, most of the columns are not needed. Hence, only 13 variables will be used in the main data set that will be used for analysis. These variables and their descriptions are listed below (Table 1).

| # | Variable            | Description (as stated / inferred)                               | Notes / Rationale |
|---|---------------------|------------------------------------------------------------------|-------------------|
| 1 | Year                | 1987 – 2008 (only 2004 and 2005 used)                            | Core temporal key |
| 2 | Month               | 1 – 12                                                           | Seasonality       |
| 3 | DayOfWeek           | 1 = Mon to 7 = Sun                                               | Day of week key   |
| 4 | DepTime             | Actual departure time (local, hhmm)                              | Delay calc        |
| 5 | CRSDepTime          | Scheduled departure time (local, hhmm)                           | Baseline schedule |
| 6 | ArrTime             | Actual arrival time (local, hhmm)                                | Delay calc        |
| 7 | CRSArrTime          | Scheduled arrival time (local, hhmm)                             | Baseline schedule |
| 8 | TailNum             | Plane tail number                                                | Join to plane data|
| 9 | ArrDelay            | Arrival delay, in minutes                                        | Target component  |
|10 | DepDelay            | Departure delay, in minutes                                      | Target component  |
|11 | Origin              | Origin airport code                                              | Network effects   |
|12 | Dest                | Destination airport code                                         | Network effects   |
|13 | Year of manufacture | The year the plane was manufactured (from plane-data file)       | Age analysis      |

_Table 1: Selected variables_

The reason for this selection is because these variables were the only ones determined to be crucial in answering the questions posed. We can also see that it is quite a large dataset since it is reading 3.5 gigabytes even when only 12 (actually 13 including plane manufacture year) variables were selected, so determining the important variables and selecting only those helps with reducing memory errors. The last variable, year of manufacture, is from the `plane-data` file.

![Data information](/assets/projects/flight_analysis/info.png)

_Table 2: Data information_

The main dataset is first checked for NA/missing values. There are missing values in the variables `DepTime`, `ArrTime`, `ArrDelay`, and `DepDelay`. We can check how many NA values there are and see the percentage of them compared to the total amount of data. As a rule of thumb, dropping NA values that are less than 5% of the respective observations is acceptable [[3]]. As we can see, the variables that have NA values have them for less than 5% of their observations and hence, the NA values will be dropped.

![NA percentage values](/assets/projects/flight_analysis/NA percentage.png)

_Table 2: NA percentage values_

Now that the data is set, we can start to do analysis on the data.

# Data Processing, Exploration and Modelling

## When is the best time of day, day of the week, and time of year to fly to minimise delays?

### The best time of the day

For Question 1 (best time of the day), to determine what is the best time of the day to fly, the variables `CRSDepTime` and `CRSArrTime` were selected. This is due to the fact that departure and arrival delays start at the scheduled departure and arrival timings. This would show the delays that are expected at a said scheduled time. 

For example, if the scheduled departure time is 06 hours (6 AM) and the mean departure delay is found out to be one hour then the observation is that there is an expected mean departure delay of an hour after 6 AM. If the actual departure time was taken, this would be inverse in interpretation since the actual departure time would already consider the delay. If the actual departure time is 07 hours (7 AM) and the mean departure delay is the same, then the delay ended at 7 AM. Hence, the variables `CRSDepTime` and `CRSArrTime` were selected.

As we can see in the hourly mean arrival and departure delay visualizations from both R and Python, the lowest arrival delay mean is in the morning, at 04:00 and 07:00 hours. The lowest departure delay mean is at 06:00 hours. The second lowest is at 05:00 hours.

The highest arrival delay mean is in the evening, at 18:00 to 23:00 (6 to 11 PM) which then also continues over into the next day at midnight (12 AM or 00 hours). This persists till 04:00 hours where it drops into the negatives. The highest departure delay mean is also in the evening, at 18:00 to 23:00 (6 to 11 PM) which then also continues over into the next day at midnight (12 AM or 00 hours).

<div class="full-width-block viz-container">
  <iframe src="/assets/projects/flight_analysis/hourly_delay_plot.html" width="100%" height="550px"></iframe>
</div>

_Figure 1: Interactive hourly mean delay_

In general, the time between 14:00 to 22:00 (2 PM to 10 PM) is when a lot of delays occur. There is also an abnormal increase at 03:00 to 04:00 in the early morning. Hence, the best time of the day to fly, in order to minimise delays, is during the early morning, from 05:00 to 06:00. In order to avoid peak delays, a person should avoid the evening hours of 17:00 to 21:00 and the early morning hour at 04:00.

### The best day of the week

Next, we have the day of the week. First, the weekly data frame is created by extracting the variables `DayOfWeek`, `ArrDelay`, and `DepDelay`. This allows us to focus on just those variables for this part of the question and makes it easier to handle the data as well. The same goes for the monthly data frame where only `Month`, `ArrDelay`, and `DepDelay` were used. For both weekly and monthly analysis, total delay (the sum of arrival and departure delay) was calculated due to the fact that on a timeframe like a week or as large as a month, looking at arrival and departure delay separately seems excessive. On such a timescale, there will be very nuanced changes between the two types of delays especially on a monthly timescale and hence total delay was taken for both weekly and monthly analysis.

The best day of the week, where total delays are the lowest, is Saturday. The total delay mean is close to ten minutes on Saturday while the second lowest is Tuesday where it is close to 12.5 minutes. The highest total delay mean is on Thursday and Friday with both having more than 17.5 minutes in the total delay mean. The next highest is Monday with just under 17.5 minutes.

<div class="full-width-block viz-container">
  <iframe src="/assets/projects/flight_analysis/weekly_delay_plot.html" width="100%" height="550px"></iframe>
</div>

_Figure 2: Weekly mean delay_

Hence, the best day of the week is Saturday. To avoid delays, it is best to avoid Thursdays, Fridays, and Mondays.

### The best time of the year (month)

The best time of the year to fly, by month, is September which has a mean of about six minutes. The next best month is April which has a mean of about seven minutes. The highest mean is during July, with December and June coming in 2nd and 3rd place for highest mean. This corresponds to the Summer and Winter break, hence the rise in delays. January also has high delays due to spill over from Winter break and New Year’s. It can also include the weather from winter season in December and January. The same can be seen in the R visualization.

<div class="full-width-block viz-container">
  <iframe src="/assets/projects/flight_analysis/monthly_delay_plot.html" width="100%" height="550px"></iframe>
</div>

_Figure 3: Monthly mean delay_

## Do older planes suffer more delays?

For Question 2, the `plane-data` dataset was used. The NA values were checked and removed. The variable `TailNum` was used which then allowed for the year of manufacture to be extracted.

There are two regression lines in each plot. This is done due to the sampling difference mentioned in the data pre-processing. It is helpful to split the data and plot them in two sections within the same plot.

The data is much more scattered in pre-1980s as opposed to post-1980s where there is much more data that results in a more gathered plot. Likewise, the confidence interval is much wider for pre-1980s as compared to post-1980s. Since there is a sampling issue with pre-1980s, we cannot reasonably apply the conclusion for all years. Hence, 1980 onwards, data points and analysis show that older planes did suffer more delays. We can see that there is a slow downward trend with much more scatter appearing below the trend line post-1990s and that there is much more scatter above the trend line during the 1980s. Meanwhile, pre-1980, the delays were increasing as seen by the upward sloping regression line.

<iframe src="/assets/projects/flight-analysis/plane_age_plot.html" width="100%" height="800"></iframe>

_Figure 9: Regression plot of total delay against year of manufacture (Python)_

_Figure 10: Regression plot of total delay against year of manufacture (R)_

## How does the number of people (number of flights) flying between different locations change over time?

For Question 3, the data was split in two: pre-1980 year of manufacture and post-1980 year of manufacture. This is due to the sampling variations between the two periods. There are about 8 million observations in post-1980 compared to the 500,000 in pre-1980. Hence, it wouldn’t give an accurate representation if the two were not separated.

In both visualizations, we can see that there is quite a lot of change for most of the connections. The largest change is between DTW - TYS (Detroit, Michigan – Knoxville, Tennessee) where more than 90% of total flights were in 2004 which dipped to less than 5% of total flights in 2005. The second largest change is between LAS – PVD (Las Vegas, Nevada – Warwick, Rhode Island) where it had a little over 10% of total flights in 2004 which then increased to more than 80%.

DTW – SBN (Detroit, Michigan – South Bend, Indiana) and LGA – STT (Queens, New York – St. Thomas, US Virgin Islands) have about the same amount of change, percentage wise. Both had just below 40% in 2004 which increased to more than 60% in 2005. AKN – DLG (King Salmon, Alaska – Dillingham, Alaska) had the opposite change with 60% in 2004 dropping to 40% in 2005.

<iframe src="/assets/projects/flight-analysis/route_analysis_plot.html" width="100%" height="800"></iframe>

_Figure 7: Top 5 connections by total flights (Python)_

The R visualization is quite interesting, almost resembling a step graph. The largest change is, of course, between MSY – SLC (New Orleans, Louisiana – Salt Lake, Utah) where the percentage change is 100% which means that the flights in 2005 are double of those in 2004. The second largest is between GSO – TPA (Greensboro, North Carolina – Port Alsworth, Alaska) where there was an increase from 25% to 75% of total flights. There is a similar increase between GRB – MQT (Green Bay, Wisconsin – Gwinn, Michigan) where it increased from about 30% to 70% from 2004 to 2005. The connection between AKN – ANC (King Salmon, Alaska – Anchorage, Alaska) had almost no change at all with the percentage increasing from just below 50% to just a little over 50% from 2004 to 2005. A similar change is noted in BDL – IAH (Windsor Locks, Connecticut – Houston, Texas) with the increase being from about 45% to 55%.

_Figure 8: Top 5 connections by total flights (R)_

## Can you detect cascading failures as delays in one airport create delays in others?

For Question 4, two different data subsets were taken for Python and R. For Python, the top 5 connections, in ascending order, with total flights between 100 and 500 were analysed while for R, the top 5 connections, in ascending order, with total flights between 1000 and 2500 were analysed. This was done due to the fact that at higher levels of total flights, there is very little change since the total flights number is so large. Hence, to find a greater change between 2004 and 2005, the data was filtered and analysed.

<iframe src="/assets/projects/flight-analysis/correlation_heatmap.html" width="100%" height="800"></iframe>

_Figure 13: Triangle correlation heatmap of top 5 airports (Python)_

_Figure 14: Triangle correlation heatmap of top 5 airports (R)_

It is possible to detect cascading failures as delays. The visualizations from Python and R both show the same information. We can see that there are indeed delays which cascade from one airport into another. There is perfect correlation between ORD (O’Hare airport, Chicago) and DFW (Dallas/Fort Worth airport, Dallas-Fort Worth) which means that the delays in ORD constantly cascade to DFW and result in delays in DFW. There are other similarly high correlations between other airports. PHL (Philadelphia airport, Philadelphia) and ATL (Hartsfield-Jackson airport, Atlanta) have a delay correlation of 0.95 while PHL has pretty much the same correlation with EWR (Newark Liberty airport, Newark) that has a correlation of 0.96. ORD and ATL have a correlation of 0.88 while EWR and DFW have a correlation of 0.8. The high positive correlations imply that delays in one airport, like PHL, do translate to or be associated with delays in the other airport, like ATL. This could be an indication that cascading failures are occurring between the airports. There is also much lower correlation such as 0.53 between ORD and EWR as well as 0.41 between PHL and ORD. This means that there is a moderately positive relationship in delays between the airports but does not necessarily mean that cascading failures are occurring. It is also to be noted that there is a correlation of 0.067, about 0, between EWR and ATL. This means that the delays in EWR do not affect the delays in ATL. There are also negative correlations between DFW and ATL, of -0.99, as well as between PHL and DFW, of -0.91. This means delays in DFW and PHL do not translate to delays in ATL and DFW, respectively.

As we saw, we can detect cascading failures as delays that start from one airport and lead to delays in other airports. Namely, there are indications of cascading failures between ORD – DFW, PHL – EWR, PHL – ATL, ORD – ATL, and EWR – DFW.

## Use the available variables to construct a model that predicts delays

For Question 5, the variables that immediately impact arrival and departure delay were taken. These are `CRSDepTime`, `CRSArrTime`, `DepTime`, `ArrTime`, `Origin`, and `Dest`. Total delay was calculated, and the 6 variables were used to model total delay. The sample size taken for both Python and R is 200,000. A large sample size results in greater accuracy within the model. For R, the variables `Origin` and `Dest` had to be dropped due to the “Factor has new levels” error that occurs from taking samples. Unfortunately, this results in lower accuracy but the error could not be solved. The only solution found was to take the entire dataset but this would be impossible due to the fact that the data has about 7 million rows. This will result in numerous memory errors and session aborts from R. Hence, the variables were dropped. The models used are logistic regression and gradient boosting in Python and linear regression, ridge regression, lasso regression, and random forests in R.

The train-test split is 80-20. A large sample was used in order to improve accuracy. We can see that we have an AUC score of 0.89 for the gradient boosting while the logistic regression has an AUC of 0.71. An AUC score tells us how well a model can predict classes correctly [[4]][[5]][[6]]. An AUC score of 0.71 means that the logistic regression model can distinguish and predict 71% of the classes correctly. This is already a good score. Gradient boosting has a score 0.89 which means that it can predict 89% of the classes correctly. This is a high score and is close to being very high since it is just 1% below 90%. We can improve on the model by adding more variables that contribute to the delay [[4]]. We can also change the train-test ratio and see if it can improve the model.

_Figure 15: Machine learning model (Python)_

On the left is the graph visualizing the various mean squared error (MSE) values for the regression models. The values for each model are given in the table below. As we can see, the MSE values vary quite a bit. The random forest model has the highest MSE with the most range as well. Its mean MSE value is 26.6. The second highest is the ridge regression without any tuning. The third highest is the lasso regression without any tuning. The lowest is the linear regression. A MSE value of zero would imply a perfect model [[7]]. We cannot conclude this with the linear regression as such a small value when variables like `Origin` and `Dest` were dropped. It also threw a warning message that the “prediction from a rank deficient fit may be misleading”. This means that the test data did not work well with the regression [[8]]. The ridge and lasso regressions without tuning are more believable but these are without tuning. Their penalty terms, also called lambdas, have not been calculated when benchmarking [[9]]. We can (see) with the penalty terms that their MSE values fall drastically. We can improve upon the model by including more variables, especially origin and destination.

_Figure 16: MSE values of regression models (R)_

# Conclusions

Overall, we were able to analyse when delays occur, changes in flight connections, cascading delays etc. There can be much more flight analysis done with this data. The entirety of the code, both in Python and R, took around 30 minutes to run and execute which is quite fast considering the samples taken in the machine learning models.

# References

1. The World of Air Transport in 2019. (n.d.). Retrieved March 25, 2023. Available at: [Link][1]  
2. Harvard Dataverse. (2008, October 6). Data Expo 2009: Airline On Time Data. Retrieved February 27, 2023. Available at: [Link][2]  
3. Mears, K., Montelpare, W. J., Read, E., McComber, T., Mahar, A., & Ritchie, K. (n.d.). Working with missing data. Retrieved April 3, 2023. Available at: [Link][3]  
4. Allwright, S. (2022, August 23). What is a good AUC score? Retrieved April 2, 2023. Available at: [Link][4]  
5. Google Developers. Classification: ROC curve and AUC. Retrieved April 1, 2023. Available at: [Link][5]  
6. Bhandari, A. (2023, March 28). Guide to AUC ROC curve in machine learning. Retrieved March 25, 2023. Available at: [Link][6]  
7. Allwright, S. (2022, December 6). What is a good MSE value? Retrieved April 2, 2023. Available at: [Link][7]  
8. ProgrammingR. Fix R warning: Prediction from a rank-deficient fit may be misleading. Retrieved April 1, 2023. Available at: [Link][8]  
9. Andrea Perlato. Ridge and lasso regression. Retrieved April 2, 2023. Available at: [Link][9]  

[1]: https://www2023.icao.int/annual-report-2019/Pages/the-world-of-air-transport-in-2019.aspx "The World of Air Transport in 2019"
[2]: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2FHG7NV7 "Data Expo 2009: Airline On Time Data (Harvard Dataverse)"
[3]: https://pressbooks.library.upei.ca/montelpare/chapter/working-with-missing-data/ "Working with Missing Data (Mears et al.)"
[4]: https://stephenallwright.com/good-auc-score/ "What is a Good AUC Score? (Allwright, 2022)"
[5]: https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc "Classification: ROC Curve and AUC (Google Developers)"
[6]: https://www.analyticsvidhya.com/blog/2020/06/auc-roc-curve-machine-learning/ "Guide to AUC ROC Curve (Bhandari, 2023)"
[7]: https://stephenallwright.com/good-mse-value/ "What is a Good MSE Value? (Allwright, 2022)"
[8]: https://www.programmingr.com/r-error-messages/prediction-from-a-rank-deficient-fit-may-be-misleading/ "Prediction from a Rank-Deficient Fit May Be Misleading (ProgrammingR)"
[9]: https://www.andreaperlato.com/theorypost/ridge-and-lasso-regression/ "Ridge and Lasso Regression (Andrea Perlato)"


## 📂 Project Files
- [📄 Full Report (PDF)](/assets/projects/flight-analysis/flight_analysis_report.pdf)  
- [📓 R Markdown (RMD)](/assets/projects/flight-analysis/flight_analysis.Rmd)  
- [📔 Jupyter Notebook (IPYNB)](/assets/projects/flight-analysis/flight_analysis.ipynb)  
- [📂 Dataset (CSV)](/assets/projects/flight-analysis/flight_data.csv)

## 🔗 Repository
Source code and materials are available on GitHub:  
👉 [Flight Analysis Repository](https://github.com/atharvacoolkarni/flight-analysis)
