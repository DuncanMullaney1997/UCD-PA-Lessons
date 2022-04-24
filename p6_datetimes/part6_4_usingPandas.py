# # Import pandas
# import pandas as pd
#
# # Load CSV into the rides variable
# rides = pd.read_csv('capital-onebike.csv',
#                     parse_dates = ['Start date','End date'])
#
# # Print the initial (0th) row
# print(rides.iloc[0])
# *

# ----------------------------------------------------------------
# # Subtract the start date from the end date
# ride_durations = rides['End date'] - rides['Start date']
#
# # Convert the results to seconds
# rides['Duration'] = ride_durations.dt.total_seconds()
#
# print(rides['Duration'].head())
# *
# ----------------------------------------------------------------
# # Create joyrides
# joyrides = (rides['Start station'] == rides['End station'])
#
# # Total number of joyrides
# print("{} rides were joyrides".format(joyrides.sum()))
#
# # Median of all rides
# print("The median duration overall was {:.2f} seconds"\
#       .format(rides['Duration'].median()))
#
# # Median of joyrides
# print("The median duration for joyrides was {:.2f} seconds"\
#       .format(rides[joyrides]['Duration'].median()))
# *
# ----------------------------------------------------------------
# # Import matplotlib
# import matplotlib.pyplot as plt
#
# # Resample rides to daily, take the size, plot the results
# rides.resample('D', on = 'Start date')\
#   .size()\
#   .plot(ylim = [0, 15])
#
# # Show the results
# plt.show()
# *
# using monthly ('M') resolution will
# eliminate the noise, and better show the trend
# ----------------------------------------------------------------
# # Resample rides to be monthly on the basis of Start date
# monthly_rides = rides.resample('M',on='Start date')['Member type']
#
# # Take the ratio of the .value_counts() over the total number of rides
# print(monthly_rides.value_counts() / monthly_rides.size())
# ----------------------------------------------------------------
# # Group rides by member type, and resample to the month
# grouped = rides.groupby('Member type')\
#   .resample('M', on='Start date')
#
# # Print the median duration for each group
# print(grouped['Duration'].median())
# *
# ----------------------------------------------------------------
# Localize the Start date column to America/New_York
# rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York',
#                                 						 ambiguous='NaT')
#
# # Print first value
# print(rides['Start date'].iloc[0])
#
# # Convert the Start date column to Europe/London
# rides['Start date'] = rides['Start date'].dt.tz_convert('Europe/London')
#
# # Print the new value
# print(rides['Start date'].iloc[0])
# *
# ----------------------------------------------------------------
# 1. Add a new column to rides called 'Ride start weekday', which is the weekday of the Start date.
# 2. Print the median ride duration for each weekday.

# # Add a column for the weekday of the start of the ride
# rides['Ride start weekday'] = rides['Start date'].dt.weekday_name
#
# # Print the median trip time per weekday
# print(rides.groupby('Ride start weekday')['Duration'].median())
# *
# ----------------------------------------------------------------
# 1. Calculate the difference in the Start date of the current row and the End date of the previous row and assign it to rides['Time since'].
# 2. Convert rides['Time since'] to seconds to make it easier to work with.
# 3. Resample rides to be in monthly buckets according to the Start date.
# 4. Divide the average by (60*60) to get the number of hours on average that W20529 waited in the dock before being picked up again.

# # Shift the index of the end date up one; now subract it from the start date
# rides['Time since'] = rides['Start date'] - (rides['End date'].shift(1))
#
# # Move from a timedelta to a number of seconds, which is easier to work with
# rides['Time since'] = rides['Time since'].dt.total_seconds()
#
# # Resample to the month
# monthly = rides.resample('M',on='Start date')
#
# # Print the average hours between rides each month
# print(monthly['Time since'].mean()/(60*60))
# *
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
