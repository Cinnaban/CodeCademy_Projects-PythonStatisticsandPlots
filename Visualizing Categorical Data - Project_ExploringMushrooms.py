'''
Question 1
Take a look at plot.py where we’ve loaded mushroom_data.csv. It contains 23 columns of data describing thousands of mushrooms. In the web browser on the right, data about five different mushrooms is shown.
Read through this table to get a sense of the type(s) of variables in the data and the structure of the table. It may also be helpful to read through the information on Kaggle.
Before you move on to plotting any of this data, answer the following questions:
  What type(s) of variables does mushroom_data.csv contain?
  How many of the variables can we visualize effectively with a bar graph?
  Click the hint to see our answers.

Question 2
There are 23 variables in this dataset (one for each column). Graphing each one individually would be tedious; luckily, you will use loops.
If you look at plot.py, you will see an attribute called columns. This attribute returns the name of each variable in mushroom_data.csv.
Create a loop that traverses each column in the columns list.
Print each column in columns while iterating through the loop. This is to check

Question 3
In the terminal, you should see 23 column names pop up starting with class and ending with habitat.
Great! Your for loop is working, so feel free to comment out your print statement.
You can now plot your data using the .countplot() method from the seaborn library. Follow these steps:
Call .countplot() in the for loop
Use column and the df pandas DataFrame to graph the value counts of each variable in mushroom_data.csv.
Please wait until the next task to use plt.show(). Since you are creating 23 plots in the browser, you will need an additional line of code.

Question 4
At the end of your for loop, add the following lines of code to show your plots:
  plt.show()
  plt.clf()
The .show() Matplotlib method should look familiar from previous lesson, but .clf() might be unfamiliar. This method is also from the Matplotlib library. It clears any previous figure formatting. This will keep any graphs you are plotting from bunching up on each other. Instead, your plots will be neatly stacked on top of each other will spacing ideal for viewing.

Question 5
After using plt.show() and plt.clf(), 23 plots should appear in the web browser on the right. We recommend that you click this button in the top right of the web browser to expand it for best viewing:
Fullscreen icon that sits in the top right of the learning environnment
Scroll through each of the graphs, and see what sort of trends you immediately see.
  What variables have an obvious mode?
  Do any of them have a notably diverse array of values?
  What habitat are you most likely to find mushrooms in?
What questions did you have before seeing the graphs? What questions are popping up now that you see them?
When you want to go back to your original view of the code editor and tasks, click the icon again.
Feel free to do this throughout the project if you want to take a closer look at your graphs and want to continue your analysis! In the next few steps, you will clean up the graphs and make them more readable and useful for finding patterns.

Question 6
As you scroll through the graphs, you may notice some imperfections. For example, some of the x-axis labels overlap each other. The font size for the labels along the x-axis is also pretty small, making them tough to read.
Let’s fix these up with two lines of code.
Following your .countplot() method, add the following two lines of code in your for loop:
  # rotates the value labels slightly so they don’t overlap, also slightly increases font size
  plt.xticks(rotation=30, fontsize=10)
  # increases the variable label font size slightly to increase readability
  plt.xlabel(column, fontsize=12)
Click the hint to check the code in your for loop up to this point.

Question 7
One more thing you can do to increase readability is to add an informative title. Using .title() from the Matplotlib library, give your graph the following title:
  {Variable Name} Value Counts
Use column to capture each variable name. Be sure to call this method after .countplot() inside of your for loop.

Question 8
The graphs are readable, but you can take it another step further.
Add the order parameter to your .countplot() method.
Set this parameter so that the value counts in each column are in descending order.
You will need to use the .value_counts() pandas method and the .index pandas object.

Question 9
Great job! In relatively few lines of code, you have created 23 informative plots. Now that they are titled, labeled clearly, and ordered, you can really dive in on your analysis.
Think about how someone could best use these visualizations. It is easy to tell which features of mushrooms are common and rare, and we get insights into the variety of mushrooms in the fungi kingdom.
Spend some time looking over the graphs. Write down exciting insights you find. Here are some examples to get you started:

  It is a roughly equal split between mushrooms that are edible vs. poisonous.
  The majority of mushrooms in this dataset have a scaly surface.
  There are a non-insignificant amount of mushrooms that give off an almond scent?!!!
  Most top surfaces of mushrooms in this dataset are scaly rather than smooth.
Some of your analysis may also require research into mushroom features for any of the x-labels. We hope you enjoy continuing to explore the world of these fun guys!

Question 10
Feel free to play around with the graphs and customize them any way you want to help in your analysis! Here are some ideas to get yourself started:
  Turn any bar graph with less than six bars into a pie chart (hint: use a conditional statement!).
  Create your bar charts using a list comprehension instead of a for loop.
  Change the color theme of your graphs using the seaborn color or palette parameters.
  Remove any graphs you find uninformative.
  Change around the current title or label formatting.
Happy Coding! :)
'''

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

for column in columns:
  sns.countplot(df[column], order=df[column].value_counts().index)
  plt.title(column + ' Value Counts')
  #print(column)
  plt.show()
  plt.clf() # Make sure plt.show is within the loop!!
  plt.xticks(rotation=30, fontsize=10)
  plt.xlabel(column, fontsize=12)










