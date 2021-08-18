import matplotlib.pyplot as plt   # download matplotlib
import numpy as np                # download numpy
import pandas as pd               # download pandas
import seaborn as sns             # download seaborn
import os
import warnings                    # filter warnings
warnings.filterwarnings('ignore')

mussel_mm = pd.read_csv('Mussel Data.csv')      # import dataset
pd.options.display.max_rows = 200                # show 200 rows
pd.options.display.max_columns = 8               # show up to 8 columns
print(mussel_mm)

#----------------------------------------------------------------------
mussel_mm.info()                   #change column name
mussel_mm.columns = (['CohortDate', 'AvgLength', 'AvgArea', 'CohortNumber',\
                    'Avg_pH', 'Avg_Temp'])
mussel_mm.info()                   # verify column names were changed
                                   # change columns to categories
mussel_mm.CohortNumber = mussel_mm.CohortNumber.astype('category')
mussel_mm.CohortDate = mussel_mm.CohortDate.astype('category')
mussel_mm.info()
                                  #round dataframe
mussel_mm = mussel_mm.round(3)
print(mussel_mm)
                                   #round 1st then change to category
mussel_mm.Avg_pH = mussel_mm.Avg_pH.astype('category')
mussel_mm.Avg_Temp = mussel_mm.Avg_Temp.astype('category')
mussel_mm.info

#---------------------------------------------------------------------
for date in mussel_mm.CohortDate.cat.categories:   #get list of cohort dates
    print(date)
                               # average lenghts for dates of cohorts
mussel_mm['AvgCohLength'] = mussel_mm.groupby(['CohortDate']).AvgLength.transform('mean')
print(mussel_mm)
                               #average area for dates of cohorts
mussel_mm['AvgCohArea'] = mussel_mm.groupby(['CohortDate']).AvgArea.transform('mean')
print(mussel_mm)
                              # round whole dataset again
mussel_mm = mussel_mm.round(3)
print(mussel_mm)

#---------------------------------------------------------------------
# Graph Avg_pH vs AvgLength
                                #set style
sns.set(style = "whitegrid", palette = 'muted', color_codes = True)
                                #plot box space
ax = sns. boxplot(data=mussel_mm, x ='Avg_pH', y = 'AvgLength', color ="gray")
plt.setp(ax, alpha = 0.5)
                                # add in points for lengths
sns.stripplot(data = mussel_mm, x ='Avg_pH', y = 'AvgLength')
ax.axes.set_title('Correlation between Average pH and Juvenile Length', fontsize = 20)
ax.set_ylabel('Average Length (mm)', fontsize = 20)
ax.set_xlabel('Average pH (total scale)', fontsize = 20)
plt.show()

# Graph Avg_pH vs AvgArea
                                #set style
sns.set(style = "whitegrid", palette = 'muted', color_codes = True)
                                #plot box space
ax = sns. boxplot(data=mussel_mm, x ='Avg_pH', y = 'AvgArea', color ="gray")
plt.setp(ax, alpha = 0.5)
                                # add in points for area
sns.stripplot(data = mussel_mm, x ='Avg_pH', y = 'AvgArea')
ax.axes.set_title('Correlation between Average pH and Juvenile Area', fontsize = 20)
ax.set_ylabel('Average Area (mm^2)', fontsize = 20)
ax.set_xlabel('Average pH (total scale)', fontsize = 20)
plt.show()

# Graph Avg_Temp vs AvgLength
                                #set style
sns.set(style = "whitegrid", palette = 'muted', color_codes = True)
                                #plot box space
ax = sns. boxplot(data=mussel_mm, x ='Avg_Temp', y = 'AvgLength', color ="lightgray")
plt.setp(ax, alpha = 0.5)
                                #add in points for length
sns.stripplot(data = mussel_mm, x ='Avg_Temp', y = 'AvgLength')
ax.axes.set_title('Correlation between Average Temperature and Juvenile Length', fontsize = 20)
ax.set_ylabel('Average Length (mm)', fontsize = 20)
ax.set_xlabel('Average Temperature (°C)', fontsize = 20)
plt.show()

# Graph Avg_Temp vs AvgArea
                                #set style
sns.set(style = "whitegrid", palette = 'muted', color_codes = True)
                                #plot box space
ax = sns. boxplot(data=mussel_mm, x ='Avg_Temp', y = 'AvgArea', color ="lightgray")
plt.setp(ax, alpha = 0.5)
                                # add in points for area
sns.stripplot(data = mussel_mm, x ='Avg_Temp', y = 'AvgArea')
ax.axes.set_title('Correlation between Average Temperature and Juvenile Area', fontsize = 20)
ax.set_ylabel('Average Area (mm^2)', fontsize = 20)
ax.set_xlabel('Average Temperature (°C)', fontsize = 20)
plt.show()

#-----------------------------------------------------------------------------
                                #create subpots for cohort averages
f, axes = plt.subplots(2)
axes[0].scatter(y = mussel_mm['AvgCohLength'], x = mussel_mm['Avg_Temp'], color = "green")
axes[1].scatter(y = mussel_mm['AvgCohArea'], x = mussel_mm['Avg_Temp'])
axes[1].set_xlabel('Average Temperature (°C)', fontsize = 20)
axes[0].set_ylabel('Average Length (mm)', fontsize = 15)
axes[1].set_ylabel('Average Area (mm^2)', fontsize = 15)
axes[0].title.set_text('Correlation between Temperature and Length')
axes[1].title.set_text('Correlation between Temperature and Area')
plt.show()


f, axes = plt.subplots(2)
axes[0].scatter(y = mussel_mm['AvgCohArea'], x = mussel_mm['Avg_pH'])
axes[1].scatter(y = mussel_mm['AvgCohLength'], x = mussel_mm['Avg_pH'], color = "green")
axes[1].set_xlabel('Average pH (total scale)', fontsize = 20)
axes[0].set_ylabel('Average Area (mm^2)', fontsize = 15)
axes[1].set_ylabel('Average Length (mm)', fontsize = 15)
axes[0].title.set_text('Correlation between pH and Area')
axes[1].title.set_text('Correlation between pH and Length')
plt.show()
#----------------------------------------------------------------------------
                                # create 3-D graph for pH vs temp cohort avg
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
axes = fig.add_subplot(111, projection = '3d')
x = mussel_mm['Avg_pH']
y = mussel_mm['Avg_Temp']
z = mussel_mm['AvgCohLength']

axes.scatter(x,y,z, marker ='x', color ='red' )
axes.set_xlabel('Average pH (total scale)')
axes.set_ylabel('Average Temperature (°C)')
axes.set_zlabel('Average Length (mm)')

plt.show()

fig2=plt.figure()
axes = fig2.add_subplot(111, projection = '3d')
x = mussel_mm['Avg_pH']
y = mussel_mm['Avg_Temp']
z = mussel_mm['AvgCohArea']

axes.scatter(x,y,z, marker ='x', color ='blue' )
axes.set_xlabel('Average pH (total scale)')
axes.set_ylabel('Average Temperature (°C)')
axes.set_zlabel('Average Area (mm^2)')

plt.show()
