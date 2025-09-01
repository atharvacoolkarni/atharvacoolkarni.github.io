---
title: "Flight Analysis"
excerpt: "Machine learning analysis of flight delays and prediction patterns using commercial flight data"
collection: portfolio
layout: single
permalink: /projects/flight-analysis/
date: 2025-09-01
---

## Project Overview
This project explores **flight data analysis and prediction patterns**.  
The main goals were:
- Analyze flight delay patterns and identify key factors 
- Visualize air traffic trends and seasonal patterns
- Predict flight delays using machine learning models 

The analysis is based on commercial flight data and combines statistical analysis and machine learning to obtain meaningful insights.

This project was done for University of London's third year course 'Programming for Data Science' during my BSc. Economics degree. The full coursework question set can be found here [ST2195_Coursework (PDF)](/assets/projects/flight-analysis/st2195_coursework.pdf)

---

## Introduction
Airline travel is an immensely popular mode of transportation, with billions of people taking it every year [1]. In 2019, there were approximately 38.3 million flights worldwide, and while the COVID-19 pandemic caused a significant dip in air travel, the numbers are expected to rebound [1]. Despite increased efficiency since the start of flight travel, flight delays remain a persistent issue for travellers. Through data exploration and modelling, this study aims to analyse trends in flight delays, connections, and other factors, providing insight into how flight data evolves over time.

---

## Data

The data is from the Data Expo 2009: Airline on time data found in the Harvard Dataverse [2]. The data has 29 variables detailing each flight. When reading the data for both Python and R, the files for the code should be in the data folder or the working directory must be set to where the data is located.

---

## Data pre-processing

To start with, for the purposes of answering the specific questions within this report, most of the columns are not needed. Hence, only 13 variables will be used in the main data set that will be used for analysis. These variables and their descriptions are as listed:

### Selected variables
![Selected variables](/assets/projects/flight-analysis/selected_variables.png)

---

### Interactive Delay Prediction Dashboard
<iframe src="/assets/projects/flight-analysis/prediction_dashboard.html" width="100%" height="600"></iframe>

---

### Model Performance Analysis
<iframe src="/assets/projects/flight-analysis/model_performance.html" width="100%" height="800"></iframe>

---

## 📈 Key Insights
- Insight 1: Weather conditions are the strongest predictor of flight delays, accounting for 35% of variance.  
- Insight 2: XGBoost model achieved 87% accuracy in predicting delays > 15 minutes.  
- Insight 3: Peak travel seasons show 40% higher delay rates, suggesting capacity management opportunities.  

---

## 📂 Project Files
- [📄 Full Report (PDF)](/assets/projects/flight-analysis/flight_analysis_report.pdf)  
- [📓 R Markdown (RMD)](/assets/projects/flight-analysis/flight_analysis.Rmd)  
- [📔 Jupyter Notebook (IPYNB)](/assets/projects/flight-analysis/flight_analysis.ipynb)  
- [📂 Dataset (CSV)](/assets/projects/flight-analysis/flight_data.csv)  

---

## 🔗 Repository
Source code and materials are available on GitHub:  
👉 [Flight Analysis Repository](https://github.com/atharvacoolkarni/flight-analysis)

---
