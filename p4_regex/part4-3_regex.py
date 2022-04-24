# sentiment_analysis = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
# # Import the re module
# import re
#
# # Write the regex
# regex = r"@robot\d\W"
#
# # Find all matches of regex
# # print(re.findall(regex, sentiment_analysis))
# # ------------------------------------------------------------------------
# sentiment_analysis='Unfortunately one of those moments wasn''t a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7'
# # Write a regex to obtain user mentions
# print(re.findall(r"User_mentions:\d", sentiment_analysis))
#
# # Write a regex to obtain number of likes
# print(re.findall(r"likes:\s\d", sentiment_analysis))
#
# # Write a regex to obtain number of retweets
# print(re.findall(r"number\sof\sretweets:\s\d", sentiment_analysis))
# # ------------------------------------------------------------------------
# sentiment_analysis='He#newHis%newTin love with$newPscrappy. #8break%He is&newYmissing him@newLalready'
#
# # Write a regex to match pattern separating sentences
# regex_sentence = r"\W\dbreak\W"
#
# # Replace the regex_sentence with a space
# sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)
#
# # Write a regex to match pattern separating words
# regex_words = r"\Wnew\w"
#
# # Replace the regex_words and print the result
# sentiment_final = re.sub(regex_words, " ", sentiment_sub)
# print(sentiment_final)
# ------------------------------------------------------------------------

# import pandas as pd
# # Import re module
# import re
# items = ['Boredd. Colddd @blueKnight39 Internet keeps stuffing up. Save me! https://www.tellyourstory.com',
# 'I had a horrible nightmare last night @anitaLopez98 @MyredHat31 which affected my sleep, now I''m really tired',
# 'im lonely  keep me company @YourBestCompany! @foxRadio https://radio.foxnews.com 22 female, new york']
# sentiment_analysis = pd.Series(items)
# for tweet in sentiment_analysis:
#     print(tweet)
#
#     # Write regex to match http links and print out result
#     print(re.findall(r"http.+\.com", tweet))
#
#     # Write regex to match user mentions and print out result
#     print(re.findall(r"@\w+\d?", tweet))
#     print('---')
# # ------------------------------------------------------------------------
# sentiment_analysis='ITS NOT ENOUGH TO SAY THAT IMISS U #MissYou #SoMuch #Friendship #Forever'
# # Write a regex matching the hashtag pattern
# regex = r"#\w+"
#
# # Replace the regex by an empty string
# no_hashtag = re.sub(regex, "", sentiment_analysis)
#
# # Get tokens by splitting text
# print(re.split(r"\s+", no_hashtag))
# # ------------------------------------------------------------------------
# import pandas as pd
# # Import re module
# import re
# items = ['AIshadowhunters.txt aaaaand back to my literature review. At least i have a friendly cup of coffee to keep me company',
# 'ouMYTAXES.txt I am worried that I won''t get my $900 even though I paid tax last year']
# sentiment_analysis = pd.Series(items)
# # Write a regex to match text file name
# regex = r"\w+[^!&@%#]{1,}\.txt"
#
# for text in sentiment_analysis:
#     # print(sentiment_analysis)
#     # Find all matches of the regex
#     print(re.findall(regex, text))
#
#     # Replace all matches with empty string
#     print(re.sub(regex, "", text))
# ------------------------------------------------------------------------
# emails=['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
# # Write a regex to match a valid email address
# regex = r"[A-Za-z0-9!#%&*$\.]+@\w+\.com"
# import re
# for example in emails:
#   	# Match the regex to the string
#     if re.match(regex, example):
#         # we use "match" above b/c we want to match from the beginning of the string
#         # Complete the format method to print out the result
#       	print("The email {email_example} is a valid email".format(email_example=example))
#     else:
#       	print("The email {email_example} is invalid".format(email_example=example))
# ------------------------------------------------------------------------]
# Write a regex to check if the password is valid
# passwords=['Apple34!rose', 'My87hou#4$', 'abc123']
# import re
# regex = r"[a-zA-Z0-9*#$%!&\.]{8,20}"
#
# for example in passwords:
#   	# Scan the strings to find a match
#     if re.search(regex, example):
#         # Complete the format method to print out the result
#       	print("The password {pass_example} is a valid password".format(pass_example=example))
#     else:
#       	print("The password {pass_example} is invalid".format(pass_example=example))
# we used the .search() method. The reason is that we want to scan the string to match the
# pattern. We are not interested in where the regex finds the match
# ------------------------------------------------------------------------
# string='I want to see that <strong>amazing show</strong> again!'
# # Import re
# import re
#
# # Write a regex to eliminate tags (non-lazy!, so elements in middle do not get removed)
# string_notags = re.sub(r"<.+?>", "", string)
#
# # Print out the result
# print(string_notags)
# ------------------------------------------------------------------------
# Import re
# import re
# sentiment_analysis='Was intending to finish editing my 536-page novel manuscript ' \
#                    'tonight, but that will probably not happen. And only 12 pages are left'
# # Write a greedy regex expression
# numbers_found_lazy = re.findall(r"\d+?", sentiment_analysis)
# print(numbers_found_lazy)
#
# # Write a greedy regex expression
# numbers_found_greedy = re.findall(r"\d+", sentiment_analysis)
# print(numbers_found_greedy)
# # ------------------------------------------------------------------------
# sentiment_analysis='Put vacation photos online (They were so cute) a few yrs ago. ' \
#                    'PC crashed, and now I forget the name of the site (I''m crying).'

# ------------------------------------------------------------------------

