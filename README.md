# Detect Heavy Drinking Episodes Using Smartphone Accelerometer Data

## Solution

### Abstract:
<b>Objective: </b> Given a 10 second window of non-zero accelerometer data, predict whether the TAC is above 0.08 (intoxicated). Report accuracy and F1 scores.

### Data:
https://archive.ics.uci.edu/ml/datasets/Bar+Crawl%3A+Detecting+Heavy+Drinking

### Data Preprocessing:

### Feature Engineering:

### Model Performance:

Model | Accuracy | F1 Score
--- | --- | --- 
Baseline RF (sklearn) | 0.8563 | 0.7987
XGBoost (H2O AutoML) | 0.8549 | 0.8066
<b>Stacked Ensemble (H2O AutoML)</b> | <b>0.8598</b> | <b>0.8140</b>


## How to run:

