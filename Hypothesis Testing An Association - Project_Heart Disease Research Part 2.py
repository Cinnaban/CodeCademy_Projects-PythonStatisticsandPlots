'''
Question 1
The data has been saved as a dataframe named heart in script.py. It contains the following variables:
    age: age in years
    sex: sex assigned at birth; 'male' or 'female'
    trestbps: resting blood pressure in mm Hg
    chol: serum cholesterol in mg/dl
    cp: chest pain type ('typical angina', 'atypical angina', 'non-anginal pain', or 'asymptomatic')
    exang: whether the patient experiences exercise-induced angina (1: yes; 0: no)
    fbs: whether the patient’s fasting blood sugar is >120 mg/dl (1: yes; 0: no)
    thalach: maximum heart rate achieved in exercise test
    heart_disease: whether the patient is found to have heart disease ('presence': diagnosed with heart disease; 'absence': no heart disease)
Inspect the first few rows of data using the .head() method.

Question 2
Each of the patients in this dataset underwent an exercise test, during which their heart rate was monitored. For each patient, thalach gives us the highest heart rate that the patient achieved during this test.
Is thalach associated with whether or not a patient will ultimately be diagnosed with heart disease? Use sns.boxplot() to plot side by side box plots of thalach for patients who were and were not diagnosed with heart disease (indicated by the heart_disease variable). Do you think there is a relationship between these variables?

Question 3
In order to investigate this question further, save the values for thalach among patients who were diagnosed with heart disease as a variable named thalach_hd. Then save the values of thalach among patients who were not diagnosed with heart disease as thalach_no_hd. 

Question 4
Calculate and print the difference in mean thalach for patients diagnosed with heart disease compared to patients without heart disease. Then do the same for the median difference.

Question 5
We’d like to find out if the average thalach of a heart disease patient is significantly different from the average thalach for a person without heart disease.
Import the statistical test from scipy.stats that we would use to test the following null and alternative hypotheses:

    Null: The average thalach for a person with heart disease is equal to the average thalach for a person without heart disease.
    Alternative: The average thalach for a person with heart disease is NOT equal to the average thalach for a person without heart disease.

Question 6
Run the hypothesis test from task 5 and print out the p-value. Using a significance threshold of 0.05, is there a significant difference in average thalach for people with heart disease compared to people with no heart disease?

Question 7
Using the same process, investigate at least one other quantitative variable. Options include age, trestbps (resting blood pressure), and chol (cholesterol). Are any of these variables also significantly associated with heart disease?
Note: before every new plot that you make, be sure to use plt.clf() to clear the previous plot first, so that plots don’t get layered on top of each other. For example:
  # first box plot:
  sns.boxplot(x=heart.heart_disease, y=heart.thalach)
  plt.show()
  
  # second box plot:
  plt.clf()
  sns.boxplot(x=heart.heart_disease, y=heart.age)
  plt.show()

Question 8
Next, let’s investigate the relationship between thalach (maximum heart rate achieved during exercise) and the type of heart pain a person experiences. Create a set of side-by-side box plots of thalach for each chest pain type in the data. Make sure to use plt.clf() to clear the previous plots first!

Are there any chest pain types for which average thalach is significantly higher or lower (compared to other chest pain types)?

Question 9
To investigate this further, save the values of thalach for patients who experienced each type of chest pain as thalach_typical, thalach_asymptom, thalach_nonangin, and thalach_atypical, respectively.

Question 10
Run a single hypothesis test to address the following null and alternative hypotheses:
    Null: People with typical angina, non-anginal pain, atypical angina, and asymptomatic people all have the same average thalach.
    Alternative: People with typical angina, non-anginal pain, atypical angina, and asymptomatic people do not all have the same average thalach.
Save the resulting p-value as pval and print it out. Using a significance threshold of 0.05, is there at least one pair of chest pain categories for which people in those categories have significantly different thalach?

Question 11
If you completed the previous step correctly, you should have concluded that there is at least one pair of chest pain types (cp) for which people with those pain types have significantly different average max heart rates during exercise (thalach).
Run another hypothesis test to determine which of those pairs are significantly different. Use an overall type I error rate of 0.05 for all six comparisons.

Question 12
Finally, let’s investigate the relationship between the kind of chest pain a person experiences and whether or not they have heart disease. Create a contingency table of cp and heart_disease and save it as Xtab, then print it out.

Question 13
Run a hypothesis test for the following null and alternative hypotheses:

    Null: There is NOT an association between chest pain type and whether or not someone is diagnosed with heart disease.
    Alternative: There is an association between chest pain type and whether or not someone is diagnosed with heart disease.

Save the p-value as pval and print it out. Using a significance threshold of 0.05, is there a significant association between chest pain type and whether or not someone is diagnosed with heart disease?


'''
# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

# load data
heart = pd.read_csv('heart_disease.csv')

# Get an idea of the data 
print(heart.head())

# Does "thalach" have an association with heart disease diagnosis?
sns.boxplot(x = heart.heart_disease, y = heart.thalach)
plt.show()
plt.clf()

# Determine the thalach values for those with heart disease and those without heart disease
thalach_hd = heart.thalach[heart.heart_disease == 'presence']
thalach_no_hd = heart.thalach[heart.heart_disease == 'absence']
# Find the means for both
thalach_hd_mean = np.mean(thalach_hd)
thalach_no_hd_mean = np.mean(thalach_no_hd)
print("The average thalach value for those with heart disease is: " + str(thalach_hd_mean)) # 139.26
print("The average thalach value for those without heart disease is: " + str(thalach_no_hd_mean)) # 158.38

# Is there a statistically difference between those with heart disease and those without heart disease?
from scipy.stats import ttest_ind
tstat, pval = ttest_ind(thalach_hd, thalach_no_hd)
print("The statistical significance between thalach values of those with heart disease and those without is: " + str(pval)) # There is a statistical significant difference 0.00000000000003457 or 3.457e-14

# Repeat for another variable and see what you come up with
sns.boxplot(x = heart.heart_disease, y = heart.age)
plt.show()
plt.clf()

age_hd = heart.age[heart.heart_disease == 'presence']
age_no_hd = heart.age[heart.heart_disease == 'absence']

age_hd_mean = np.mean(age_hd) 
age_no_hd_mean = np.mean(age_no_hd) 
print("The average age for those with heart disease is: " + str(age_hd_mean)) # 56.259 
print("The average age for those without heart disease is: " + str(age_no_hd_mean)) # 52.5853

# Is there a statistically difference between the age of a patient and the diagnosis of heart disease?
tstat, pval = ttest_ind(age_hd, age_no_hd)
print("The statistical significance for age to heart disease is: " + str(pval)) # There appears to be a statistical significant difference of 0.0000896 or 8.96e-05 

# Is there a relationship between thalach and chest pain types?
sns.boxplot(x = heart.cp, y = heart.thalach)
plt.show() # both Typical Angina and Atypical Angina are higher than Asymptomatic and Non-Anginal pain
plt.clf()

# Separate each of the chest pain types into individual variables
thalach_typical = heart.thalach[heart.cp == 'typical angina']
thalach_asymptom = heart.thalach[heart.cp == 'asymptomatic']
thalach_nonangin = heart.thalach[heart.cp == 'non-anginal pain']
thalach_atypical = heart.thalach[heart.cp == 'atypical angina']

# Import f_oneway()
from scipy.stats import f_oneway
Fstat, pval = f_oneway(thalach_typical, thalach_asymptom, thalach_nonangin, thalach_atypical)
print("The significance between all variables for chest pain is: " + str(pval)) # there is a significance for chest pain and thalach!

# Which relationship is the significant one from the rest of the variables? 
from statsmodels.stats.multicomp import pairwise_tukeyhsd
results = pairwise_tukeyhsd(endog = heart.thalach, groups = heart.cp)
print(results)
''' The table below is the results!
 asymptomatic  atypical angina  21.7394  0.001  12.7439  30.735   True
    asymptomatic non-anginal pain  14.7264  0.001    7.258 22.1948   True
    asymptomatic   typical angina   15.276 0.0081   2.9702 27.5817   True
 atypical angina non-anginal pain   -7.013 0.2481 -16.7591   2.733  False
 atypical angina   typical angina  -6.4635 0.6069 -20.2707  7.3438  False
non-anginal pain   typical angina   0.5495    0.9  -12.315 13.4141  False
''' #The asymptomatic groups appear to all be true

# Create the Tabular table that can be used to evaluate the relationship between chest pain and heart disease
Xtab = pd.crosstab(heart.cp, heart.heart_disease)
print(Xtab)
''' 
heart_disease     absence  presence
cp                                 
asymptomatic           39       105
atypical angina        41         9
non-anginal pain       68        18
typical angina         16         7
'''

# Use the table created (Xtab) and answer the below questions
# What is the chance that there is not an association between chest pain type and heart disease? 
# What is the chance that there is an association between chest pain type and heart disease?
from scipy.stats import chi2_contingency
chi2, pval, dof, exp = chi2_contingency(Xtab)
print(pval) # 1.252e-17 shows there is a significant association between these chest pain and heart disease


