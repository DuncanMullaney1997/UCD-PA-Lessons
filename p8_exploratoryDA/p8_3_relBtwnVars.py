# # Extract age
# age = brfss['AGE']
#
# # Plot the PMF
# pmf_age = Pmf(age)
# pmf_age.bar()
#
# # Label the axes
# plt.xlabel('Age in years')
# plt.ylabel('PMF')
# plt.show()
# *
# ------------------------------------------------
# # Select the first 1000 respondents
# brfss = brfss[:1000]
#
# # Extract age and weight
# age = brfss['AGE']
# weight = brfss['WTKG3']
#
# # Make a scatter plot
# plt.plot(age, weight, 'o',alpha=0.1)
#
# plt.xlabel('Age in years')
# plt.ylabel('Weight in kg')
#
# plt.show()
# *
# By adjusting alpha we can avoid saturating the plot.
# ------------------------------------------------
# # Select the first 1000 respondents
# brfss = brfss[:1000]
#
# # Add jittering to age
# age = brfss['AGE'] + np.random.normal(0, 2.5, size=len(brfss))
# # Extract weight
# weight = brfss['WTKG3']
#
# # Make a scatter plot
# plt.plot(age,weight,'o',markersize=5,alpha=0.2)
#
# plt.xlabel('Age in years')
# plt.ylabel('Weight in kg')
# plt.show()
# *
# ------------------------------------------------
# # Drop rows with missing data
# data = brfss.dropna(subset=['_HTMG10', 'WTKG3'])
#
# # Make a box plot
# sns.boxplot(x='_HTMG10',y='WTKG3',data=data,whis=10)
#
# # Plot the y-axis on a log scale
# plt.yscale('log')
#
# # Remove unneeded lines and label axes
# sns.despine(left=True, bottom=True)
# plt.xlabel('Height in cm')
# plt.ylabel('Weight in kg')
# plt.show()
# *
# ------------------------------------------------
# # Extract income
# income = brfss['INCOME2']
#
# # Plot the PMF
# Pmf(income).bar()
#
# # Label the axes
# plt.xlabel('Income level')
# plt.ylabel('PMF')
# plt.show()
# *
# ------------------------------------------------
# # Drop rows with missing data
# data = brfss.dropna(subset=['INCOME2', 'HTM4'])
#
# # Make a violin plot
# sns.violinplot(x='INCOME2',y='HTM4',data=data,inner=None)
#
# # Remove unneeded lines and label axes
# sns.despine(left=True, bottom=True)
# plt.xlabel('Income level')
# plt.ylabel('Height in cm')
# plt.show()
# *
# ------------------------------------------------
# CORRELATION
# ------------------------------------------------
# # Select columns
# columns = ['AGE', 'INCOME2','_VEGESU1']
# subset = brfss[columns]
#
# # Compute the correlation matrix
# print(subset.corr())

#             AGE  INCOME2  _VEGESU1
# AGE       1.000   -0.015     -0.01
# INCOME2  -0.015    1.000      0.12
# _VEGESU1 -0.010    0.120      1.00

# The correlation between income and vegetable consumption is small, but it suggests
# that there is a relationship. But a correlation close to 0 does mean there is no relationship.
# ------------------------------------------------
# from scipy.stats import linregress
#
# # Extract the variables
# subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
# xs = subset['INCOME2']
# ys = subset['_VEGESU1']
#
# # Compute the linear regression
# res = linregress(xs,ys)
# print(res)
# *
# ------------------------------------------------
# # Plot the scatter plot
# plt.clf()
# x_jitter = xs + np.random.normal(0, 0.15, len(xs))
# plt.plot(x_jitter, ys, 'o', alpha=0.2)
#
# # Plot the line of best fit
# fx = np.array([xs.min(), xs.max()])
# fy = res.intercept + res.slope * fx
# plt.plot(fx, fy, '-', alpha=0.7)
#
# plt.xlabel('Income code')
# plt.ylabel('Vegetable servings per day')
# plt.ylim([0, 6])
# plt.show()
# *
