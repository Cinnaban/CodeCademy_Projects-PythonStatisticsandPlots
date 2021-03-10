'''
Question 1
In script.py, the data has been subsetted for you into two smaller datasets: games from 2010 (named nba_2010) and games from 2014 (named nba_2014). To start, let’s focus on the 2010 data.
Suppose you want to compare the knicks to the nets with respect to points earned per game. Using the pts column from the nba_2010 DataFrame, create two series named knicks_pts (fran_id = "Knicks") and nets_pts(fran_id = "Nets") that represent the points each team has scored in their games.

Question 2
Calculate the difference between the two teams’ average points scored and save the result as diff_means_2010. Based on this value, do you think fran_id and pts are associated? Why or why not?

Question 3
Rather than comparing means, it’s useful look at the full distribution of values to understand whether a difference in means is meaningful. Create a set of overlapping histograms that can be used to compare the points scored for the Knicks compared to the Nets. Use the series you created in the previous step (1) and the code below to create the plot. Do the distributions appear to be the same?

Question 4
Now, let’s compare the 2010 games to 2014. Replicate the steps from the previous three exercises using nba_2014. First, calculate the mean difference between the two teams points scored. Save and print the value as diff_means_2014. Did the difference in points get larger or smaller in 2014? Then, plot the overlapping histograms. Does the mean difference you calculated make sense?

Question 5
For the remainder of this project, we’ll focus on data from 2010. Let’s now include all teams in the dataset and investigate the relationship between franchise and points scored per game.
Using nba_2010, generate side-by-side boxplots with points scored (pts) on the y-axis and team (fran_id) on the x-axis. Is there any overlap between the boxes? Does this chart suggest that fran_id and pts are associated? Which pairs of teams, if any, earn different average scores per game?

Question 6
The variable game_result indicates whether a team won a particular game ('W' stands for “win” and 'L' stands for “loss”). The variable game_location indicates whether a team was playing at home or away ('H' stands for “home” and 'A' stands for “away”). Do teams tend to win more games at home compared to away?
Data scientists will often calculate a contingency table of frequencies to help them determine if categorical variables are associated. Calculate a table of frequencies that shows the counts of game_result and game_location.
Save your result as location_result_freq and print your result. Based on this table, do you think the variables are associated?

Question 7
Convert this table of frequencies to a table of proportions and save the result as location_result_proportions. Print your result.

Question 8
Using the contingency table created in the previous exercise (Ex. 7), calculate the expected contingency table (if there were no association) and the Chi-Square statistic and print your results. Does the actual contingency table look similar to the expected table — or different? Based on this output, do you think there is an association between these variables?

Question 9
For each game, 538 has calculated the probability that each team will win the game. In the data, this is saved as forecast. The point_diff column gives the margin of victory/defeat for each team (positive values mean that the team won; negative values mean that they lost). Did teams with a higher probability of winning (according to 538) also tend to win games by more points?
Using nba_2010, calculate the covariance between forecast (538’s projected win probability) and point_diff (the margin of victory/defeat) in the dataset. Save and print your result. Looking at the matrix, what is the covariance between these two variables?

Question 11
Generate a scatter plot of forecast (on the x-axis) and point_diff (on the y-axis). Does the correlation value make sense?

'''

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

#--------
knicks_pts = nba_2010.pts[nba.fran_id=='Knicks']
nets_pts = nba_2010.pts[nba.fran_id=='Nets']

knicks_mean_score = np.mean(knicks_pts)
nets_mean_score = np.mean(nets_pts)
diff_means_2010 = knicks_mean_score - nets_mean_score

plt.hist(knicks_pts, alpha=0.8, normed = True, label='knicks')
plt.hist(nets_pts, alpha=0.8, normed = True, label='nets')
plt.legend()
plt.title('NBA 2010')
plt.show()
# So it doesn't overlap the new plot
plt.clf()

knicks_pts2 = nba_2014.pts[nba.fran_id=='Knicks']
nets_pts2 = nba_2014.pts[nba.fran_id=='Nets']
knicks_mean_score2 = np.mean(knicks_pts2)
nets_mean_score2 = np.mean(nets_pts2)
diff_means_2014 = knicks_mean_score2 - nets_mean_score2

plt.hist(knicks_pts2, alpha=0.8, normed = True, label='knicks')
plt.hist(nets_pts2, alpha=0.8, normed = True, label='nets')
plt.legend()
plt.title('NBA 2014')
plt.show()
plt.clf()

sns.boxplot(data = nba_2010, x = 'pts', y = 'fran_id')
plt.show()
plt.clf()

location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)

location_result_proportions = location_result_freq/len(nba_2010)
print(location_result_proportions)

chi2, pval, dof, expected = chi2_contingency(location_result_proportions)
print(expected)
print("Chi2: " + str(chi2))

win_cov = np.cov(nba_2010.forecast, nba_2010.point_diff)
print("Win Cov: " + str(win_cov))

point_corr = pearsonr(nba_2010.point_diff, nba_2010.forecast)
print("Point Correlations: " + str(point_corr))

plt.scatter(nba_2010.forecast, nba_2010.point_diff)
plt.xlabel("Forecast")
plt.ylabel("Point Diff")
plt.title("NBA 2010 Score Forecast")
plt.show()




