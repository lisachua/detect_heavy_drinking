# Detect Heavy Drinking Episodes Using Smartphone Accelerometer Data

## Abstract/ Summary:
Just-in-time adaptive interventions (JITAIs) are a promising area of research in health domains, and have been used to detect heavy drinking episodes before their onset. This projects aims to improve on the study "Learning to Detect Heavy Drinking Episodes Using Smartphone Accelerometer Data" [Killian et al., 2019]. The study provides smartphone accelerometer data from 13 participants before and after a bar crawl and their blood alcohol content via transdermal alcohol concentration (TAC). Given a 10 second window of non-zero accelerometer data, I predict whether the TAC is above 0.08 (intoxicated). 

During preprocessing, I resampled the accelerometer data in order to have a reading for every millisecond between a subject's minimum to maximum timestamp. I engineered features at the 10 second window level using a two-tiered windowing approach similar to the technique used in the original study. My final dataset for modeling had 135 features and 72,521 rows. The class balance was around 36% intoxicated and 64% not intoxicated. <b> My best classifier (a stacked ensemble) detected "intoxication" with accuracy 0.86 and F1 score 0.81, surpassing the original study's best model performance. </b>

### Objective: 
Given a 10 second window of non-zero accelerometer data, predict whether the TAC is above 0.08 (intoxicated). Report accuracy and F1 scores.

### Data:
Downloaded from https://archive.ics.uci.edu/ml/datasets/Bar+Crawl%3A+Detecting+Heavy+Drinking.


### Data Preprocessing:
Preprocessing the data was the most time-consuming part of this project, but had the largest effect on performance metrics.

### Feature Engineering:


### Feature Importance:

### Model Performance:

Model | Accuracy | F1 Score
--- | --- | --- 
Baseline RF (sklearn) | 0.8563 | 0.7987
XGBoost (H2O AutoML) | 0.8549 | 0.8066
<b>Stacked Ensemble (H2O AutoML)</b> | <b>0.8598</b> | <b>0.8140</b>

Best model performance of original study: Accuracy 0.7748, F1 score 0.6815.

## How to run:

