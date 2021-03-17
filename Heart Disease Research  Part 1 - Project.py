'''
Question 1
The full dataset has been loaded for you as heart, then split into two subsets:

yes_hd, which contains data for patients with heart disease
no_hd, which contains data for patients without heart disease
For this project, we’ll investigate the following variables:

chol: serum cholestorol in mg/dl
fbs: An indicator for whether fasting blood sugar is greater than 120 mg/dl (1 = true; 0 = false)
To start, we’ll investigate cholesterol levels for patients with heart disease. Use the dataset yes_hd to save cholesterol levels for patients with heart disease as a variable named chol_hd.

Question 2
In general, total cholesterol over 240 mg/dl is considered “high” (and therefore unhealthy). Calculate the mean cholesterol level for patients who were diagnosed with heart disease and print it out. Is it higher than 240 mg/dl?

Question 3
Do people with heart disease have high cholesterol levels (greater than or equal to 240 mg/dl) on average? Import the function from scipy.stats that you can use to test the following null and alternative hypotheses:

Null: People with heart disease have an average cholesterol level equal to 240 mg/dl
Alternative: People with heart disease have an average cholesterol level that is greater than 240 mg/dl
Note: Unfortunately, the scipy.stats function we’ve been using does not (at the time of writing) have an alternative parameter to change the alternative hypothesis for this test. Therefore, you’ll have to run a two-sided test. However, since you calculated earlier that the average cholesterol level for heart disease patients is greater than 240 mg/dl, you can calculate the p-value for the one-sided test indicated above simply by dividing the two-sided p-value in half.

Question 4
Run the hypothesis test indicated in task 3 and print out the p-value. Can you conclude that heart disease patients have an average cholesterol level significantly greater than 240 mg/dl? Use a significance threshold of 0.05.

Question 5
Repeat steps 1-4 in order to run the same hypothesis test, but for patients in the sample who were not diagnosed with heart disease. Do patients without heart disease have average cholesterol levels significantly above 240 mg/dl?

Question 6
Let’s now return to the full dataset (saved as heart). How many patients are there in this dataset? Save the number of patients as num_patients and print it out.

Question 7
Remember that the fbs column of this dataset indicates whether or not a patient’s fasting blood sugar was greater than 120 mg/dl (1 means that their fasting blood sugar was greater than 120 mg/dl; 0 means it was less than or equal to 120 mg/dl).

Calculate the number of patients with fasting blood sugar greater than 120. Save this number as num_highfbs_patients and print it out.

Question 8
Sometimes, part of an analysis will involve comparing a sample to known population values to see if the sample appears to be representative of the general population.

By some estimates, about 8% of the U.S. population had diabetes (diagnosed or undiagnosed) in 1988 when this data was collected. While there are multiple tests that contribute to a diabetes diagnosis, fasting blood sugar levels greater than 120 mg/dl can be indicative of diabetes (or at least, pre-diabetes). If this sample were representative of the population, approximately how many people would you expect to have diabetes? Calculate and print out this number.

Is this value similar to the number of patients with a resting blood sugar above 120 mg/dl — or different?

Question 9
Does this sample come from a population in which the rate of fbs > 120 mg/dl is equal to 8%? Import the function from scipy.stats that you can use to test the following null and alternative hypotheses:

Null: This sample was drawn from a population where 8% of people have fasting blood sugar > 120 mg/dl
Alternative: This sample was drawn from a population where more than 8% of people have fasting blood sugar > 120 mg/dl

Question 10
Run the hypothesis test indicated in task 9 and print out the p-value. Using a significance threshold of 0.05, can you conclude that this sample was drawn from a population where the rate of fasting blood sugar > 120 mg/dl is significantly greater than 8%?

'''

# import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import binom_test
# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

# View the data sets
'''
print(yes_hd.head())
print(no_hd.head())
'''
#Assign heart disease patients cholestorol to the variable chol_hd
chol_hd = yes_hd.chol

# What is the average cholestorol level of patients with heart disease?
chol_hd_mean = np.mean(chol_hd)
print("Cholestorol with heart disease average: " + str(chol_hd_mean)) #251.47

# Test the Null and Alternative Hypotheses
tstat, pval = ttest_1samp(chol_hd, 240)
print("Cholestorol with heart disease p-value: " + str(pval)) # 0.00708 needs to be divided by 2 to get the p-value
# Since 0.0035 is less than 0.05, there is a significance with HD patients and average cholestorol levels

# Repeating to evaluate if not having heart disease has a significance on cholestorol levels
chol_no_hd = no_hd.chol
chol_no_hd_mean = np.mean(chol_no_hd)
print("Cholestorol without heart disease average: " + str(chol_no_hd_mean)) # 242.640243
tstat, pval = ttest_1samp(chol_no_hd, 240)
print("Cholestorol without heart disease p-value: " + str(pval)) # 0.5279
# Since 0.25 is larger than 0.05, there is not a significance with no HD patients and average cholestorol levels

# How many patients are in the total dataset?
num_patients = len(heart)
print(num_patients) # 303 patients

# Calculate the number of patients with fasting blood sugar greater than 120
num_highfbs_patients = np.sum(heart.fbs)
print(num_highfbs_patients) # 45 patients 

# How many patients have diabetes in the sample if 8% of the population has diabetes?
patients_DB = 0.08 * num_patients
print("Based on the estimates, we can expect: " + str(patients_DB) + " of people to have diabetes from the sample size")

pval = binom_test(num_highfbs_patients, num_patients, .08, alternative='greater')
print(pval) # 0.00000468 indicates there is a significance between fasting blood sugar levels and diabetes 










