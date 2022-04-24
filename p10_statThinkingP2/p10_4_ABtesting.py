# # Construct arrays of data: dems, reps
# dems = np.array([True] * 153 + [False] * 91)
# reps = np.array([True] * 136 + [False] * 35)
#
# def frac_yea_dems(dems, reps):
#     """Compute fraction of Democrat yea votes."""
#     frac = np.sum(dems) / len(dems)
#     return frac
#
# # Acquire permutation samples: perm_replicates
# perm_replicates = draw_perm_reps(dems, reps, frac_yea_dems, size=10000)
#
# # Compute and print p-value: p
# p = np.sum(perm_replicates <= 153/244) / len(perm_replicates)
# print('p-value =', p)
# *
# Great work! This small p-value suggests that party identity had a
# lot to do with the voting. Importantly, the South had a higher
# fraction of Democrat representatives, and consequently also a more racist bias.
# ---------------------------------------------
# # Compute the observed difference in mean inter-no-hitter times: nht_diff_obs
# nht_diff_obs = diff_of_means(nht_dead,nht_live)
#
# # Acquire 10,000 permutation replicates of difference in mean no-hitter time: perm_replicates
# perm_replicates = draw_perm_reps(nht_dead, nht_live,diff_of_means, size=10000)
#
#
# # Compute and print the p-value: p
# p = np.sum(perm_replicates <= nht_diff_obs) / 10000
# print('p-val =', p)
# *
# Your p-value is 0.0001, which means that only one out of your 10,000
# replicates had a result as extreme as the actual difference between
# the dead ball and live ball eras. This suggests strong statistical
# significance. Watch out, though, you could very well have gotten zero
# replicates that were as extreme as the observed value. This just means
# that the p-value is quite small, almost certainly smaller than 0.001.

# from matplotlib import pyplot as plt
#
# x_dead, y_dead = ecdf(nht_dead)
# x_live, y_live = ecdf(nht_live)
#
# _ = plt.plot(x_dead,y_dead,marker='.', linestyle='none',color='blue', alpha=0.02)
# _ = plt.plot(x_live,y_live,marker='.', linestyle='none',color='red', alpha=0.02)
#
# plt.show()
# # ---------------------------------------------
def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat=np.corrcoef(x,y)


    # Return entry [0,1]
    return corr_mat[0,1]


# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_width,versicolor_petal_length)

# Print the result
print(r)
# # ---------------------------------------------
# # Compute observed correlation: r_obs
# r_obs = pearson_r(illiteracy, fertility)
#
# # Initialize permutation replicates: perm_replicates
# perm_replicates = np.empty(10000)
#
# # Draw replicates
# for i in range(10000):
#     # Permute illiteracy measurments: illiteracy_permuted
#     illiteracy_permuted = np.random.permutation(illiteracy)
#
#     # Compute Pearson correlation
#     perm_replicates[i] = pearson_r(illiteracy_permuted,fertility)
#
# # Compute p-value: p
# p = np.sum(perm_replicates > r_obs) / len(perm_replicates)
# print('p-val =', p)
# *
# ---------------------------------------------
# https://royalsocietypublishing.org/doi/10.1098/rspb.2016.0506
# BEE SPERM
# ---------------------------------------------
# Compute the difference in mean sperm count: diff_means
diff_means = diff_of_means(control,treated)

# Compute mean of pooled data: mean_count
mean_count = np.mean(np.concatenate((control,treated)))

# Generate shifted data sets
control_shifted = control - np.mean(control) + mean_count
treated_shifted = treated - np.mean(treated) + mean_count

# Generate bootstrap replicates
bs_reps_control = draw_bs_reps(control_shifted,
                       np.mean, size=10000)
bs_reps_treated = draw_bs_reps(treated_shifted,
                       np.mean, size=10000)

# Get replicates of difference of means: bs_replicates
bs_replicates = bs_reps_control - bs_reps_treated

# Compute and print p-value: p
p = np.sum(bs_replicates >= np.mean(control) - np.mean(treated)) \
            / len(bs_replicates)
print('p-value =', p)

# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------