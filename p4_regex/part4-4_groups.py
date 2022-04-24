# import re
#
# sentiment_analysis=['Just got ur newsletter, those fares really are unbelievable. '
# 'Write to statravelAU@gmail.com or statravelpo@hotmail.com. They have amazing prices',
# 'I should have paid more attention when we covered photoshop in my webpage design class in undergrad. ' \
# 'Contact me Hollywoodheat34@msn.net.', 'hey missed ya at the meeting. Read your email! msdrama098@hotmail.com']
#
# # Write a regex that matches email
# regex_email = r"\s([A-Za-z0-9]+)@\S+"
#
# for tweet in sentiment_analysis:
#     # print(tweet)
#     # Find all matches of regex in each tweet
#     email_matched = re.findall(regex_email, tweet)
#
#     # Complete the format method to print the results
#     print("Lists of users found in this tweet: {0}".format(email_matched))
# ------------------------------------------------------------------------
# flight='Subject: You are now ready to fly. Here you have your boarding pass IB3723 AMS-MAD 06OCT'
# # Import re
# import re
#
# # Write regex to capture information of the flight
# regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"
#
# # Find all matches of the flight information
# flight_matches = re.findall(regex, flight)
#
# # Print the matches
# print("Airline: {} Flight number: {}".format(flight_matches[0][0], flight_matches[0][1]))
# print("Departure: {} Destination: {}".format(flight_matches[0][2], flight_matches[0][3]))
# print("Date: {}".format(flight_matches[0][4]))
# ------------------------------------------------------------------------

# sentiment_analysis=['I totally love the concert The Book of Souls World Tour. It kinda amazing!',
# 'I enjoy the movie Wreck-It Ralph. I watched with my boyfriend.',
# "I still like the movie Wish Upon a Star. Too bad Disney doesn't show it anymore."]
#
# # Write a regex that matches sentences with the optional words
# regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."
#
# for tweet in sentiment_analysis:
#     # print(tweet)
#     # Find all matches of regex in tweet
#     positive_matches = re.findall(regex_positive, tweet)
#
#     # Complete format to print out the results
#     print("Positive comments found {}".format(positive_matches))
# ------------------------------------------------------------------------
# import re
# sentiment_analysis=['That was horrible! I really dislike the movie The cabin and the ant. So boring.',
# "I disapprove the movie Honest with you. It's full of cliches.",
# 'I dislike very much the concert After twelve Tour. The sound was horrible.']
#
# # Write a regex that matches sentences with the optional words
# regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)\s(.*?)\."
#
# for tweet in sentiment_analysis:
#     # Find all matches of regex in tweet
#     negative_matches = re.findall(regex_negative, tweet)
#
#     # Complete format to print out the results
#     print("Negative comments found {}".format(negative_matches))
# ------------------------------------------------------------------------
# contract='Provider will invoice Client for Services performed within 30 days of performance.  ' \
#          'Client will pay Provider as set forth in each Statement of Work within 30 days of receipt ' \
#          'and acceptance of such invoice. It is understood that payments to Provider for services ' \
#          'rendered shall be made in full as agreed, without any deductions for taxes of any kind ' \
#          'whatsoever, in conformity with Provider’s status as an independent contractor. Signed on 03/25/2001.'
# import re
# # Write regex and scan contract to capture the dates described
# regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
# dates = re.search(regex_dates, contract)
#
# # Assign to each key the corresponding match
# signature = {
# 	"day": dates.group(2),
# 	"month": dates.group(1),
# 	"year": dates.group(3)
# }
# # Complete the format method to print-out
# print("Our first contract is dated back to {data[year]}. "
#       "Particularly, the day {data[day]} of the month {data[month]}.".format(data=signature))

# each capturing group is assigned a number according to its position in the regex.
# Only if you use .search() and .match(), you can use .group() to retrieve the groups.
# ------------------------------------------------------------------------
# html_tags=[
# '<body>Welcome to our course! It would be an awesome experience</body>',
# '<article>To be a data scientist, you need to have knowledge in statistics and mathematics</article>',
# '<nav>About me Links Contact me!'
# ]
# import re
#
# for string in html_tags:
#     # Complete the regex and find if it matches a closed HTML tags
#     match_tag = re.match(r"<(\w+)>.*?</\1>", string)
#
#     if match_tag:
#         # If it matches print the first group capture
#         print("Your tag {} is closed".format(match_tag.group(1)))
#     else:
#         # If it doesn't match capture only the tag
#         notmatch_tag = re.match(r"<(\w+)>", string)
#         # Print the first group capture
#         print("Close your {} tag!".format(notmatch_tag.group(1)))
# ------------------------------------------------------------------------
# sentiment_analysis=[
#     '@marykatherine_q i know! I heard it this morning and wondered the same thing. Moscooooooow is so behind the times',
#     'Staying at a friends house...neighborrrrrrrrrryyyrrrrs are so loud-having a party',
#     'Just woke up an already have read some e-mail'
# ]
# import re
#
# # Complete the regex to match an elongated word
# regex_elongated = r"\w*(\w)\1\w*"
#
# for tweet in sentiment_analysis:
#     # Find if there is a match in each tweet
#     match_elongated = re.search(regex_elongated, tweet)
#
#     if match_elongated:
#         # Assign the captured group zero
#         elongated_word = match_elongated.group(0)
#
#         # Complete the format method to print the word
#         print("Elongated word found: {word}".format(word=elongated_word))
#     else:
#         print("No elongated word found")

# ------------------------------------------------------------------------
# import re
# sentiment_analysis='You need excellent python skills to be a data scientist. Must be! Excellent python'
# # Positive lookahead
# look_ahead = re.findall(r"\w+(?=\spython)", sentiment_analysis)
#
# # Print out
# print(look_ahead)
#
# # Positive lookbehind
# look_behind = re.findall(r"(?<=[Pp]ython\s)\w+", sentiment_analysis)
#
# # Print out
# print(look_behind)
# ------------------------------------------------------------------------
import re
cellphones=['4564-646464-01', '345-5785-544245', '6476-579052-01']

for phone in cellphones:
	# Get all phone numbers not preceded by area code
	number = re.findall(r"(?<!\d{3}-)\d{4}-\d{6}-\d{2}", phone)
	print(number)

for phone in cellphones:
	# Get all phone numbers not followed by optional extension
	number = re.findall(r"\d{3}-\d{4}-\d{6}(?!-\d{2})", phone)
	print(number)
