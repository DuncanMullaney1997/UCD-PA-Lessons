# cdf_income = Cdf(gss['realinc'])
#
# # Calculate the 75th percentile
# percentile_75th = cdf_income.inverse(0.75)
#
# # Calculate the 25th percentile
# percentile_25th = cdf_income.inverse(0.25)
#
# # Calculate the interquartile range
# iqr = percentile_75th - percentile_25th
#
# # Print the interquartile range
# print(iqr)
# *
# ------------------------------------------------
# # Select realinc
# income = gss['realinc']
#
# # Make the CDF
# cdf_income = Cdf(income)
#
# # Plot it
# cdf_income.plot()
#
# # Label the axes
# plt.xlabel('Income (1986 USD)')
# plt.ylabel('CDF')
# plt.show()
# *
# ------------------------------------------------

# educ =gss['educ']
#
# cdfObj =Cdf(educ) #b is the cdf object
#
# cdfObj.plot()
#
# plt.show()
#
# print(cdfObj(12)) # returns 0.5322611710323575
# *
# ------------------------------------------------
# # Select educ
# educ = gss['educ']
#
# # Bachelor's degree
# bach = (educ >= 16)
#
# # Associate degree
# assc = (educ >= 14) & (educ < 16)
#
# # High school (12 or fewer years of education)
# high = (educ <= 12)
# print(high.mean())
# *
# ------------------------------------------------
# income = gss['realinc']
#
# # Plot the CDFs
# Cdf(income[high]).plot(label='High school')
# Cdf(income[assc]).plot(label='Associate')
# Cdf(income[bach]).plot(label='Bachelor')
#
# # Label the axes
# plt.xlabel('Income (1986 USD)')
# plt.ylabel('CDF')
# plt.legend()
# plt.show()
# *
# ------------------------------------------------
# MODELLING
# ------------------------------------------------
# # Extract realinc and compute its log
# income = gss['realinc']
# log_income = np.log10(income)
#
# # Compute mean and standard deviation
# mean = log_income.mean()
# std = log_income.std()
# print(mean, std)
#
# # Make a norm object
# from scipy.stats import norm
# dist = norm(mean, std)
# *
# ------------------------------------------------
# # Extract realinc and compute its log
# log_income = np.log10(gss['realinc'])
#
# # Compute mean and standard deviation
# mean, std = log_income.mean(), log_income.std()
#
# # Make a norm object
# from scipy.stats import norm
# dist = norm(mean, std)

# # Evaluate the model CDF
# xs = np.linspace(2, 5.5)
# ys = dist.cdf(xs)
#
# # Plot the model CDF
# plt.clf()
# plt.plot(xs, ys, color='gray')
#
# # Create and plot the Cdf of log_income
# Cdf(log_income).plot()
#
# # Label the axes
# plt.xlabel('log10 of realinc')
# plt.ylabel('CDF')
# plt.show()
# *
# ------------------------------------------------
# Evaluate the normal PDF using dist, which is a norm object with the same mean and standard deviation as the data.
# Make a KDE plot of the logarithms of the incomes, using log_income, which is a Series object.

# # Evaluate the normal PDF
# xs = np.linspace(2, 5.5)
# ys = dist.pdf(xs)
#
# # Plot the model PDF
# plt.clf()
# plt.plot(xs, ys, color='gray')
#
# # Plot the data KDE
# sns.kdeplot(log_income)
#
# # Label the axes
# plt.xlabel('log10 of realinc')
# plt.ylabel('PDF')
# plt.show()
# *
# ------------------------------------------------
# ------------------------------------------------