# two_cities='It was the best of times, it was the worst of times, it was the age of wisdom, ' \
#            'it was the age of foolishness, it was the epoch of belief, it was the epoch of ' \
#            'incredulity, it was the season of Light, it was the season of Darkness, it was ' \
#            'the spring of hope, it was the winter of despair, we had everything before us, ' \
#            'we had nothing before us, we were all going direct to Heaven, we were all going ' \
#            'direct the other way – in short, the period was so far like the present period, ' \
#            'that some of its noisiest authorities insisted on its being received, for good ' \
#            'or for evil, in the superlative degree of comparison only.'
# # Import the required packages
# from textblob import TextBlob
#
# # Create a textblob object
# blob_two_cities = TextBlob(two_cities)
#
# # Print out the sentiment
# print(blob_two_cities.sentiment)
# ------------------------------------------------------------------------
# annak='Happy families are all alike; every unhappy family is unhappy in its own way'
# catcher='If you really want to hear about it,the first thing you''ll probably want ' \
#         'to know is where I was born, and what my lousy childhood was like, and how ' \
#         'my parents were occupied and all before they had me, and all that David ' \
#         'Copperfield kind of crap, but I don''t feel like going into it, if you want ' \
#         'to know the truth.'
# # Import the required packages
# from textblob import TextBlob
#
# # Create a textblob object
# blob_annak = TextBlob(annak)
# blob_catcher = TextBlob(catcher)
#
# # Print out the sentiment
# print('Sentiment of annak: ', blob_annak.sentiment)
# print('Sentiment of catcher: ', blob_catcher.sentiment)
# ------------------------------------------------------------------------
# Import the required packages
# from textblob import TextBlob
#
# # Create a textblob object
# blob_titanic = TextBlob(titanic)
#
# # Print out its sentiment
# print(blob_titanic.sentiment)
#
# titanic='big lon string of text that is either positive or negative'
# ------------------------------------------------------------------------
# wordclouds

# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# ------------------------------------------------------------------------
# east_of_eden='I remember my childhood names for grasses and secret flowers. ' \
#              'I remember where a toad may live and what time the birds awaken ' \
#              'in the summer—and what trees and seasons smelled like—how people ' \
#              'looked and walked and smelled even. The memory of odors is very rich.'

# # Generate the word cloud from the east_of_eden string
# cloud_east_of_eden = WordCloud(background_color="white").generate(east_of_eden)
#
# # Create a figure of the generated cloud
# plt.imshow(cloud_east_of_eden, interpolation='bilinear')
# plt.axis('off')
# # Display the figure
# plt.show()
# ------------------------------------------------------------------------
# illuminated='I am not sad, he would repeat to himself over and over, I am not sad. As if he might one day convince ' \
#             'himself or convince others -- the only thing worse than being sad is for others to know that you are ' \
#             'sad. I am not sad.'
# # Generate the word cloud from the east_of_eden string
# cloud_east_of_eden = WordCloud(background_color="white").generate(illuminated)
#
# # Create a figure of the generated cloud
# plt.imshow(cloud_east_of_eden, interpolation='bilinear')
# plt.axis('off')
# # Display the figure
# plt.show()
# ------------------------------------------------------------------------
# BAG OF WORDS (BOW)
# Import the required function
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
# ------------------------------------------------------------------------
annak = ['Happy families are all alike;', 'every unhappy family is unhappy in its own way']

# Build the vectorizer and fit it
anna_vect = CountVectorizer()
anna_vect.fit(annak)

# Create the bow representation
anna_bow = anna_vect.transform(annak)

# Print the bag-of-words result
print(anna_bow.toarray())

# Create the bow representation
X_df=pd.DataFrame(anna_bow.toarray(), columns=anna_vect.get_feature_names_out())
print(X_df.head())
