# ------------------------------------------------------------------------
# from sklearn.feature_extraction.text import CountVectorizer
#
# # Build the vectorizer, specify token sequence and fit
# vect = CountVectorizer(ngram_range=(1, 2))
# vect.fit(reviews.review)
#
# # Transform the review column
# X_review = vect.transform(reviews.review)
#
# # Create the bow representation
# X_df = pd.DataFrame(X_review.toarray(), columns=vect.get_feature_names())
# print(X_df.head())
# ------------------------------------------------------------------------
#Import the vectorizer
# from sklearn.feature_extraction.text import CountVectorizer
#
# # Build the vectorizer, specify max features and fit
# vect = CountVectorizer(max_features=1000, ngram_range=(2, 2), max_df=500)
# vect.fit(reviews.review)
#
# # Transform the review
# X_review = vect.transform(reviews.review)
#
# # Create a DataFrame from the bow representation
# X_df = pd.DataFrame(X_review.toarray(), columns=vect.get_feature_names())
# print(X_df.head())
# ------------------------------------------------------------------------
# Tokenize a string
import nltk

# GoT='Never forget what you are, for surely the world will not. Make it ' \
#     'your strength. Then it can never be your weakness. Armour yourself ' \
#     'in it, and it will never be used to hurt you.'
# # Import the required function
# from nltk import word_tokenize
# # nltk.download('punkt')
#
# # Transform the GoT string to word tokens
# print(word_tokenize(GoT))

# ------------------------------------------------------------------------
# avengers=["Cause if we can't protect the Earth, you can be d*** sure we'll avenge it"
#     , 'There was an idea to bring together a group of remarkable people, to see if '
#       'we could become something more', "These guys come from legend, Captain. They're basically Gods."]
#
# # Import the word tokenizing function
# from nltk import word_tokenize
#
# # Tokenize each item in the avengers
# tokens_avengers = [word_tokenize(item) for item in avengers]
#
# print(tokens_avengers)
# ------------------------------------------------------------------------
# foreign='L''histoire rendu était fidèle, excellent, et grande.'
# # Import the language detection function and package
# from langdetect import detect_langs
#
# # Detect the language of the foreign string
# print(detect_langs(foreign))
# ------------------------------------------------------------------------
# sentences=["L'histoire rendu était fidèle, excellent, et grande.",
# 'Excelente muy recomendable.',
# 'It had a leak from day one but the return and exchange process was very quick.']
# from langdetect import detect_langs
#
# languages = []
#
# # Loop over the sentences in the list and detect their language
# for sentence in sentences:
#     languages.append(detect_langs(sentence))
#
# print('The detected languages are: ', languages)
# ------------------------------------------------------------------------
# from langdetect import detect_langs
# languages = []
#
# # Loop over the rows of the dataset and append
# for row in range(len(non_english_reviews)):
#     languages.append(detect_langs(non_english_reviews.iloc[row, 1]))
#
# # Clean the list by splitting
# languages = [str(lang).split(':')[0][1:] for lang in languages]
#
# # Assign the list to a new feature
# non_english_reviews['language'] = languages
#
# print(non_english_reviews.head())
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
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------