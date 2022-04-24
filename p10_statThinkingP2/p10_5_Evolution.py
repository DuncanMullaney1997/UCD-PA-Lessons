# # Create bee swarm plot
# import seaborn as sns
#
# _ = sns.swarmplot(x=df['year'],y=df['beak_depth'],data=df)
#
# # Label the axes
# _ = plt.xlabel('year')
# _ = plt.ylabel('beak depth (mm)')
#
# # Show the plot
# plt.show()
# *
# ---------------------------------------------
# # Compute ECDFs
# x_1975, y_1975 = ecdf(bd_1975)
# x_2012, y_2012 = ecdf(bd_2012)
#
# # Plot the ECDFs
# _ = plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# _ = plt.plot(x_2012, y_2012, marker='.', linestyle='none')
#
# # Set margins
# plt.margins(0.02)
#
#
# # Add axis labels and legend
# _ = plt.xlabel('beak depth (mm)')
# _ = plt.ylabel('ECDF')
# _ = plt.legend(('1975', '2012'), loc='lower right')
#
# # Show the plot
# plt.show()
# *
# ---------------------------------------------
# Compute the difference of the sample means.
# Take 10,000 bootstrap replicates of the mean for the 1975 beak depths using your
# draw_bs_reps() function. Also get 10,000 bootstrap replicates of the mean for the 2012 beak depths.
# Subtract the 1975 replicates from the 2012 replicates to get bootstrap replicates of the difference of means.
# Use the replicates to compute the 95% confidence interval.
# Hit submit to view the results!

# # Compute the difference of the sample means: mean_diff
# mean_diff = diff_of_means(bd_2012,bd_1975)
# #np.mean(bd_1975) - np.mean(bd_2012)#
#
# # Get bootstrap replicates of means
# bs_replicates_1975 = draw_bs_reps(bd_1975,np.mean,size=10000)
# bs_replicates_2012 = draw_bs_reps(bd_2012,np.mean,size=10000)
#
# # Compute samples of difference of means: bs_diff_replicates
# bs_diff_replicates = bs_replicates_2012 - bs_replicates_1975
#
# # Compute 95% confidence interval: conf_int
# conf_int = np.percentile(bs_diff_replicates,[2.5,97.5])
#
# # Print the results
# print('difference of means =', mean_diff, 'mm')
# print('95% confidence interval =', conf_int, 'mm')
# *
# ---------------------------------------------
# # Compute mean of combined data set: combined_mean
# combined_mean = np.mean(np.concatenate((bd_1975, bd_2012)))
#
# # Shift the samples
# bd_1975_shifted = bd_1975 - np.mean(bd_1975) + combined_mean
# bd_2012_shifted = bd_2012 - np.mean(bd_2012) + combined_mean
# # control_shifted = control - np.mean(control) + mean_count
# # treated_shifted = treated - np.mean(treated) + mean_count
#
# # Get bootstrap replicates of shifted data sets
# bs_replicates_1975 = draw_bs_reps(bd_1975_shifted,np.mean,size=10000)
# bs_replicates_2012 = draw_bs_reps(bd_2012_shifted,np.mean,size=10000)
#
# # Compute replicates of difference of means: bs_diff_replicates
# bs_diff_replicates = bs_replicates_2012 - bs_replicates_1975
#
# # Compute the p-value
# p = np.sum(bs_diff_replicates >= mean_diff) / len(bs_diff_replicates)
#
# # Print p-value
# print('p =', p)
# *
# ---------------------------------------------
import numpy as np
from numpy import polyfit
from matplotlib import pyplot as plt

from p10_2_bootstrapping import draw_bs_pairs_linreg, draw_bs_reps

from bird_beak_lengths import bl_1975, bd_1975, bl_2012, bd_2012

# Make scatter plot of 1975 data
_ = plt.plot(bl_1975, bd_1975, marker='.', linestyle='None', color='blue', alpha=0.5)

# Make scatter plot of 2012 data
_ = plt.plot(bl_2012, bd_2012, marker='.', linestyle='None', color='red', alpha=0.5)

# Label axes and make legend
_ = plt.xlabel('beak length (mm)')
_ = plt.ylabel('beak depth (mm)')
_ = plt.legend(('1975', '2012'), loc='upper left')

# Show the plot
# plt.show()
# ---------------------------------------------
# Compute the linear regressions
# slope_1975, intercept_1975 = np.polyfit(bl_1975, bd_1975, 1)
# slope_2012, intercept_2012 = np.polyfit(bl_2012, bd_2012, 1)

# Perform pairs bootstrap for the linear regressions
bs_slope_reps_1975, bs_intercept_reps_1975 = \
        draw_bs_pairs_linreg(bl_1975, bd_1975, size=1000)
bs_slope_reps_2012, bs_intercept_reps_2012 = \
        draw_bs_pairs_linreg(bl_2012, bd_2012, size=1000)

# Compute confidence intervals of slopes
slope_conf_int_1975 = np.percentile(bs_slope_reps_1975, [2.5, 97.5])
slope_conf_int_2012 = np.percentile(bs_slope_reps_2012, [2.5, 97.5])
intercept_conf_int_1975 = np.percentile(bs_intercept_reps_1975, [2.5, 97.5])
intercept_conf_int_2012 = np.percentile(bs_intercept_reps_2012, [2.5, 97.5])


# Print the results
# print('1975: slope =', slope_1975,
#       'conf int =', slope_conf_int_1975)
# print('1975: intercept =', intercept_1975,
#       'conf int =', intercept_conf_int_1975)
# print('2012: slope =', slope_2012,
#       'conf int =', slope_conf_int_2012)
# print('2012: intercept =', intercept_2012,
#       'conf int =', intercept_conf_int_2012)
# ---------------------
# Make scatter plot of 1975 data
_ = plt.plot(bl_1975, bd_1975, marker='.',
             linestyle='none', color='blue', alpha=0.5)

# Make scatter plot of 2012 data
_ = plt.plot(bl_2012, bd_2012, marker='.',
             linestyle='none', color='red', alpha=0.5)

# Label axes and make legend
_ = plt.xlabel('beak length (mm)')
_ = plt.ylabel('beak depth (mm)')
_ = plt.legend(('1975', '2012'), loc='upper left')

# Generate x-values for bootstrap lines: x
x = np.array([10, 17])

# Plot the bootstrap lines
for i in range(100):
    plt.plot(x, bs_slope_reps_1975[i]*x + bs_intercept_reps_1975[i],
             linewidth=0.5, alpha=0.2, color='blue')
    plt.plot(x, bs_slope_reps_2012[i]*x + bs_intercept_reps_2012[i],
             linewidth=0.5, alpha=0.2, color='red')

# Draw the plot again
plt.show()
# plt.clf()
# ---------------------------------------------
# Compute length-to-depth ratios
ratio_1975 = bl_1975/bd_1975
ratio_2012 = bl_2012/bd_2012

# Compute means
mean_ratio_1975 = np.mean(ratio_1975)
mean_ratio_2012 = np.mean(ratio_2012)

# Generate bootstrap replicates of the means
bs_replicates_1975 = draw_bs_reps(ratio_1975, np.mean, size=10000)
bs_replicates_2012 = draw_bs_reps(ratio_2012, np.mean, size=10000)

# Compute the 99% confidence intervals
conf_int_1975 = np.percentile(bs_replicates_1975,[0.5,99.5])
conf_int_2012 = np.percentile(bs_replicates_2012,[0.5,99.5])

# Print the results
print('1975: mean ratio =', mean_ratio_1975,
      'conf int =', conf_int_1975)
print('2012: mean ratio =', mean_ratio_2012,
      'conf int =', conf_int_2012)

# ---------------------------------------------
# Make scatter plots
_ = plt.plot(bd_parent_fortis, bd_offspring_fortis,
             marker='.', linestyle='none', color='blue', alpha=0.5)
_ = plt.plot(bd_parent_scandens, bd_offspring_scandens,
             marker='.', linestyle='none', color='red', alpha=0.5)

# Label axes
_ = plt.xlabel('parental beak depth (mm)')
_ = plt.ylabel('offspring beak depth (mm)')

# Add legend
_ = plt.legend(('G. fortis', 'G. scandens'), loc='lower right')

# Show plot
plt.show()
*
# ---------------------------------------------
def draw_bs_pairs(x, y, func, size=1):
    """Perform pairs bootstrap for a single statistic."""

    # Set up array of indices to sample from: inds
    inds = np.arange(len(x))

    # Initialize replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_replicates[i] = func(bs_x,bs_y,1)

    return bs_replicates
# -------------------
# Compute the Pearson correlation coefficients
r_scandens = pearson_r(bd_parent_scandens,bd_offspring_scandens)
r_fortis = pearson_r(bd_parent_fortis,bd_offspring_fortis)

# Acquire 1000 bootstrap replicates of Pearson r
bs_replicates_scandens = draw_bs_pairs(bd_parent_scandens,bd_offspring_scandens,pearson_r,1000)

bs_replicates_fortis = draw_bs_pairs(bd_parent_fortis,bd_offspring_fortis,pearson_r,1000)


# Compute 95% confidence intervals
conf_int_scandens = np.percentile(bs_replicates_scandens,[2.5,97.5])
conf_int_fortis = np.percentile(bs_replicates_fortis,[2.5,97.5])

# Print results
print('G. scandens:', r_scandens, conf_int_scandens)
print('G. fortis:', r_fortis, conf_int_fortis)

# ---------------------------------------------
def heritability(parents, offspring):
    """Compute the heritability from parent and offspring samples."""
    covariance_matrix = np.cov(parents, offspring)
    return covariance_matrix[1][0] / covariance_matrix[0][0]


# Compute the heritability
heritability_scandens = heritability(bd_parent_scandens, bd_offspring_scandens)
heritability_fortis = heritability(bd_parent_fortis, bd_offspring_fortis)

# Acquire 1000 bootstrap replicates of heritability
replicates_scandens = draw_bs_pairs(
    bd_parent_scandens, bd_offspring_scandens, heritability, size=1000)

replicates_fortis = draw_bs_pairs(
    bd_parent_fortis, bd_offspring_fortis, heritability, size=1000)

# Compute 95% confidence intervals
conf_int_scandens = np.percentile(replicates_scandens, [2.5, 97.5])
conf_int_fortis = np.percentile(replicates_fortis, [2.5, 97.5])

# Print results
print('G. scandens:', heritability_scandens, conf_int_scandens)
print('G. fortis:', heritability_fortis, conf_int_fortis)
*
# Remember that the Pearson correlation coefficient is the ratio of the covariance to the geometric mean of the
# variances of the two data sets. This is a measure of the correlation between parents and offspring, but might
# not be the best estimate of heritability. If we stop and think, it makes more sense to define heritability as
# the ratio of the covariance between parent and offspring to the variance of the parents alone. In this exercise,
# you will estimate the heritability and perform a pairs bootstrap calculation to get the 95% confidence interval.
#
# This exercise highlights a very important point. Statistical inference (and data analysis in general) is not
# a plug-n-chug enterprise. You need to think carefully about the questions you are seeking to answer with your
# data and analyze them appropriately. If you are interested in how heritable traits are, the quantity we defined
# as the heritability is more apt than the off-the-shelf statistic, the Pearson correlation coefficient.
#
# Remember, the data are stored in bd_parent_scandens, bd_offspring_scandens, bd_parent_fortis,
# and bd_offspring_fortis.
# ---------------------------------------------
# The heritability of beak depth in G. scandens seems low. It could be that this observed heritability
# was just achieved by chance and beak depth is actually not really heritable in the species. You will
# test that hypothesis here. To do this, you will do a pairs permutation test.
#
# Initialize your array of replicates of heritability. We will take 10,000 pairs permutation replicates.
# Write a for loop to generate your replicates.
# Permute the bd_parent_scandens array using np.random.permutation().
# Compute the heritability between the permuted array and the bd_offspring_scandens array using the heritability()
# function you wrote in the last exercise. Store the result in the replicates array.
# Compute the p-value as the number of replicates that are greater than the observed heritability_scandens you
# computed in the last exercise.

# Initialize array of replicates: perm_replicates
perm_replicates = np.empty(10000)

# Draw replicates
for i in range(10000):
    # Permute parent beak depths
    bd_parent_permuted = np.random.permutation(bd_parent_scandens)
    perm_replicates[i] = heritability(bd_parent_permuted,bd_offspring_scandens)


# Compute p-value: p
p = np.sum(perm_replicates >= heritability_scandens) / len(perm_replicates)

# Print the p-value
print('p-val =', p)
# You get a p-value of zero, which means that none of the 10,000 permutation pairs replicates you drew had a
# heritability high enough to match that which was observed. This strongly suggests that beak depth is heritable
# in G. scandens, just not as much as in G. fortis. If you like, you can plot a histogram of the heritability
# replicates to get a feel for how extreme of a value of heritability you might expect by chance.
# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------
