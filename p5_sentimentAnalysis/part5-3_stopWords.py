# myFile = '/Users/duncan/Documents/programming/Python/myPyCharm/p5/text_tweet.txt'
# # with open(myFile) as f:
# #     lines = f.readlines()
#
# # open text file in read mode
# text_file = open(myFile, "r")
# # read whole file to a string
# text_tweet = text_file.read()
# # close file
# text_file.close()

# ------------------------------------------------------------------------

# Import the word cloud function
# from wordcloud import WordCloud
#
# # Create and generate a word cloud image
# my_cloud = WordCloud(background_color='white').generate(text_tweet)
#
# # Display the generated wordcloud image
# plt.imshow(my_cloud)
# plt.axis("off")
#
# # Don't forget to show the final image
# plt.show()
# ------------------------------------------------------------------------
# Import the word cloud function and stop words list
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDS
#
# # Define and update the list of stopwords
# my_stop_words = STOPWORDS.update(['airline', 'airplane'])
#
# # Create and generate a word cloud image
# my_cloud = WordCloud(stopwords=my_stop_words).generate(text_tweet)
#
# # Display the generated wordcloud image
# plt.imshow(my_cloud, interpolation='bilinear')
# plt.axis("off")
# # Don't forget to show the final image
# plt.show()
# ------------------------------------------------------------------------
# Import the stop words
# from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
#
# # Define the stop words
# my_stop_words = ENGLISH_STOP_WORDS.union(['airline', 'airlines', '@'])
#
# # Build and fit the vectorizer
# vect = CountVectorizer(stop_words=my_stop_words)
# vect.fit(tweets.text)
#
# # Create the bow representation
# X_review = vect.transform(tweets.text)
# # Create the data frame
# X_df = pd.DataFrame(X_review.toarray(), columns=vect.get_feature_names())
# print(X_df.head())
# *
# ------------------------------------------------------------------------
# Import the vectorizer and default English stop words list
# from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
#
# # Define the stop words
# my_stop_words = ENGLISH_STOP_WORDS.union(['airline', 'airlines', '@', 'am', 'pm'])
#
# # Build and fit the vectorizers
# vect1 = CountVectorizer(stop_words=my_stop_words)
# vect2 = CountVectorizer(stop_words=ENGLISH_STOP_WORDS)
# vect1.fit(tweets.text)
# vect2.fit(tweets.negative_reason)
#
# # Print the last 15 features from the first, and all from second vectorizer
# print(vect1.get_feature_names()[-15:])
# print(vect2.get_feature_names())
# *
# ------------------------------------------------------------------------
# Build and fit the vectorizer
# vect = CountVectorizer(token_pattern=r'\b[^\d\W][^\d\W]+\b').fit(tweets.text)
# vect.transform(tweets.text)
# print('Length of vectorizer: ', len(vect.get_feature_names()))
# *
# ------------------------------------------------------------------------
# Build the first vectorizer
# vect1 = CountVectorizer().fit(tweets.text)
# vect1.transform(tweets.text)
#
# # Build the second vectorizer
# vect2 = CountVectorizer(token_pattern=r'\b[^\d\W][^\d\W]').fit(tweets.text)
# vect2.transform(tweets.text)
#
# # Print out the length of each vectorizer
# print('Length of vectorizer 1: ', len(vect1.get_feature_names()))
# print('Length of vectorizer 2: ', len(vect2.get_feature_names()))
# Length
# of
# vectorizer
# 1: 3081
# Length
# of
# vectorizer
# 2: 332
# *
# ------------------------------------------------------------------------
# Import the word tokenizing package
# from nltk import word_tokenize
#
#
# # Tokenize the text column
# word_tokens = [word_tokenize(review) for review in tweets.text]
# print('Original tokens: ', word_tokens[0])
#
# # Filter out non-letter characters
# cleaned_tokens = [[word for word in item if word.isalpha()] for item in word_tokens]
# print('Cleaned tokens: ', cleaned_tokens[0])
# Original tokens:  ['@', 'VirginAmerica', 'What', '@', 'dhepburn', 'said', '.']
# Cleaned tokens:  ['VirginAmerica', 'What', 'dhepburn', 'said']
# *
# ------------------------------------------------------------------------
# from nltk import word_tokenize
# tweets_list=["@VirginAmerica it's really aggressive to blast obnoxious 'entertainment' in your guests' faces &amp; they have little recourse",
#              "@VirginAmerica Hey, first time flyer next week - excited! But I'm having a hard time getting my flights added to my Elevate account. Help?",
#              '@united Change made in just over 3 hours. For something that should have taken seconds online, I am not thrilled. Loved the agent, though.']
#
# # Create a list of lists, containing the tokens from list_tweets
# tokens = [word_tokenize(item) for item in tweets_list]
#
# # Remove characters and digits , i.e. retain only letters
# letters = [[word for word in item if word.isalpha()] for item in tokens]
# # Remove characters, i.e. retain only letters and digits
# let_digits = [[word for word in item if word.isalnum()] for item in tokens]
# # Remove letters and characters, retain only digits
# digits = [[word for word in item if word.isdigit()] for item in tokens]
#
# # Print the last item in each list
# print('Last item in alphabetic list: ', letters[2])
# print('Last item in list of alphanumerics: ', let_digits[2])
# print('Last item in the list of digits: ', digits[2])
# ------------------------------------------------------------------------
# STEMMING (may not be a valid root)/LEMMATIZATION (root is always valid)
# ------------------------------------------------------------------------
# Import the required packages from nltk
# from nltk.stem import PorterStemmer, WordNetLemmatizer
# from nltk import word_tokenize
#
# GoT='Never forget what you are, for surely the world will not. Make it your strength. ' \
#     'Then it can never be your weakness. Armour yourself in it, and it will never be used to hurt you.'
#
#
# porter = PorterStemmer()
# WNlemmatizer = WordNetLemmatizer()
#
# # Tokenize the GoT string
# tokens = word_tokenize(GoT)
#
# import time
#
# # Log the start time
# start_time = time.time()
#
# # Build a stemmed list
# stemmed_tokens = [porter.stem(token) for token in tokens]
#
# # Log the end time
# end_time = time.time()
#
# print('Time taken for stemming in seconds: ', end_time - start_time)
# print('Stemmed tokens: ', stemmed_tokens)
#
# # import time
#
# # Log the start time
# start_time = time.time()
#
# # Build a lemmatized list
# lem_tokens = [WNlemmatizer.lemmatize(token) for token in tokens]
#
# # Log the end time
# end_time = time.time()
#
# print('Time taken for lemmatizing in seconds: ', end_time - start_time)
# print('Lemmatized tokens: ', lem_tokens)
# ------------------------------------------------------------------------
# Import the language detection package
# import langdetect
#
#
# # Loop over the rows of the dataset and append
# languages = []
# for i in range(len(non_english_reviews)):
#     languages.append(langdetect.detect_langs(non_english_reviews.iloc[i, 1]))
#
# # Clean the list by splitting
# languages = [str(lang).split(':')[0][1:] for lang in languages]
# # Assign the list to a new feature
# non_english_reviews['language'] = languages
#
# # Select the Spanish ones
# filtered_reviews = non_english_reviews[non_english_reviews.language == 'es']
# # Import the required packages
# from nltk.stem.snowball import SnowballStemmer
# from nltk import word_tokenize
#
# # Import the Spanish SnowballStemmer
# SpanishStemmer = SnowballStemmer("spanish")
#
# # Create a list of tokens
# tokens = [word_tokenize(review) for review in filtered_reviews.review]
# # Stem the list of tokens
# stemmed_tokens = [[SpanishStemmer.stem(word) for word in token] for token in tokens]
#
# # Print the first item of the stemmed tokens
# print(stemmed_tokens[0])
# *
# ------------------------------------------------------------------------
# tweets=['@VirginAmerica What @dhepburn said.'
#  "@VirginAmerica plus you've added commercials to the experience... tacky."
#  "@VirginAmerica I didn't today... Must mean I need to take another trip!"
#  '@united he has no priority and Iove it'
#  '@united Pleased to be a Premier Platinum'
#  '@united how can you not put my bag on plane to Seattle. Flight 1212. Waiting  in line to talk to someone about my bag. Status should matter.']
#
# # Import the function to perform stemming
# from nltk.stem import PorterStemmer
# from nltk import word_tokenize
#
# # Call the stemmer
# porter = PorterStemmer()
#
# # Transform the array of tweets to tokens
# tokens = [word_tokenize(tweet) for tweet in tweets]
# # Stem the list of tokens
# stemmed_tokens = [[porter.stem(word) for word in tweet] for tweet in tokens]
# # Print the first element of the list
# print(stemmed_tokens[0])
# ------------------------------------------------------------------------
# Tfidf (Term frequency, Inverse document frequency)
# ------------------------------------------------------------------------
# Import the required function
# from sklearn.feature_extraction.text import TfidfVectorizer
#
# annak = ['Happy families are all alike;', 'every unhappy family is unhappy in its own way']
#
# # Call the vectorizer and fit it
# anna_vect = TfidfVectorizer(max_features=100).fit(annak)
#
# # Create the tfidf representation
# anna_tfidf = anna_vect.transform(annak)
#
# # Print the result
# print(anna_tfidf.toarray())
# ------------------------------------------------------------------------
# Import the required vectorizer package and stop words list
# from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
#
# # Define the vectorizer and specify the arguments
# my_pattern = r'\b[^\d\W][^\d\W]+\b'
# vect = TfidfVectorizer(ngram_range=(1, 2), max_features=100, token_pattern=my_pattern, stop_words=ENGLISH_STOP_WORDS).fit(tweets.text)
#
# # Transform the vectorizer
# X_txt = vect.transform(tweets.text)
#
# # Transform to a data frame and specify the column names
# X=pd.DataFrame(X_txt.toarray(), columns=vect.get_feature_names())
# print('Top 5 rows of the DataFrame: ', X.head())
# *
# ------------------------------------------------------------------------
# Import the required packages
# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
#
# # Build a BOW and tfidf vectorizers from the review column and with max of 100 features
# vect1 = CountVectorizer(max_features=100).fit(reviews.review)
# vect2 = TfidfVectorizer(max_features=100).fit(reviews.review)
#
# # Transform the vectorizers
# X1 = vect1.transform(reviews.review)
# X2 = vect2.transform(reviews.review)
# # Create DataFrames from the vectorizers
# X_df1 = pd.DataFrame(X1.toarray(), columns=vect1.get_feature_names())
# X_df2 = pd.DataFrame(X2.toarray(), columns=vect2.get_feature_names())
# print('Top 5 rows using BOW: \n', X_df1.head())
# print('Top 5 rows using tfidf: \n', X_df2.head())
# # *