# Display the number of rows and columns
# nsfg.shape
#
# # Display the names of the columns
# nsfg.columns
#
# # Select column birthwgt_oz1: ounces
# ounces = nsfg['birthwgt_oz1']
#
# # Print the first 5 elements of ounces
# print(ounces.head())
#
# nsfg['outcome'].value_counts()
# # this will return how many 1's, 2's, 3's, etc... occured in 'outcome' column

# ------------------------------------------------
# # Replace the value 8 with NaN (one person decided not to answer, hence outlier)
# nsfg['nbrnaliv'].replace([8], np.nan, inplace=True)
#
# # Print the values and their frequencies
# print(nsfg['nbrnaliv'].value_counts())
# *
# ------------------------------------------------
# # Select the columns and divide by 100
# agecon = nsfg['agecon'] / 100
# agepreg = nsfg['agepreg'] / 100
#
# # Compute the difference
# preg_length = agepreg - agecon
#
# # Compute summary statistics
# print(preg_length.describe())
# *
# ------------------------------------------------
# # Plot the histogram
# plt.hist(agecon.dropna(),bins=20)
#
# # Label the axes
# plt.xlabel('Age at conception')
# plt.ylabel('Number of pregnancies')
#
# # Show the figure
# plt.show()
# *
#
# # Plot the histogram
# plt.hist(agecon, bins=20, histtype='step')#step hist, like stairs
#
# # Label the axes
# plt.xlabel('Age at conception')
# plt.ylabel('Number of pregnancies')
#
# # Show the figure
# plt.show()
# ------------------------------------------------
# # Create a Boolean Series for full-term babies
# full_term = nsfg['prglngth'] >= 37
#
# # Select the weights of full-term babies
# full_term_weight = birth_weight[full_term]
#
# # Compute the mean weight of full-term babies
# print(full_term_weight.mean())
# *
# ------------------------------------------------
# # Filter full-term babies
# full_term = nsfg['prglngth'] >= 37
#
# # Filter single births
# single = nsfg['nbrnaliv'] == 1
#
# # Compute birth weight for single full-term babies
# single_full_term_weight = birth_weight[single & full_term]
# print('Single full-term mean:', single_full_term_weight.mean())
#
# # Compute birth weight for multiple full-term babies
# mult_full_term_weight = birth_weight[~single & full_term]
# print('Multiple full-term mean:', mult_full_term_weight.mean())
# *
# ------------------------------------------------
# # Compute the PMF for year
# pmf_year = Pmf(gss['year'], normalize=False)
#
# # Print the result
# print(pmf_year)
# *
# ------------------------------------------------
# # Select the age column
# age = gss['age']
#
# # Make a PMF of age
# pmf_age = Pmf(age)
#
# # Plot the PMF
# pmf_age.bar(label='age')
#
# # Label the axes
# plt.xlabel('Age')
# plt.ylabel('PMF')
# plt.show()
# *

# https://pypi.org/project/empiricaldist/
