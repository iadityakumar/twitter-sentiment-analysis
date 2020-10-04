# Install Libraries
# pip install -U textblob
# pip install pandas
# pip install numpy
# pip install plotly
# pip install seaborn
# pip install matplotlib
# pip install wordcloud

# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
from textblob import TextBlob
from wordcloud import WordCloud
import plotly.graph_objects as go
import plotly.express as px

# Reading both the csv files
def find_pol(review):
    return TextBlob(review).sentiment.polarity


Trump_reviews = pd.read_csv('trump_data.csv', encoding = 'utf-8')
Trump_reviews['Sentiment_Polarity'] = Trump_reviews['text'].apply(find_pol)
Trump_reviews['Expression Label'] = np.where(Trump_reviews['Sentiment_Polarity']>0,'positive', 'negative')
Trump_reviews['Expression Label'][Trump_reviews.Sentiment_Polarity ==0] = "Neutral"
Trump_reviews.tail()
Trump_reviews.to_csv('trump_data_with_senti.csv')


Biden_reviews = pd.read_csv('biden_data.csv', encoding = 'utf-8')
Biden_reviews['Sentiment_Polarity'] = Biden_reviews['text'].apply(find_pol)
Biden_reviews['Expression Label'] = np.where(Biden_reviews['Sentiment_Polarity']>0,'positive', 'negative')
Biden_reviews['Expression Label'][Biden_reviews.Sentiment_Polarity ==0] = "Neutral"
Biden_reviews.tail()
Biden_reviews.to_csv('biden_data_with_senti.csv')