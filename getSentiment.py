from data_pre_processing import data_preprocessing
from twitter_tweet_Extraction import getTweets
from sentiment_analysis import sentiment_analysis
from getRealStock import getRealStock
import pandas as pd

#Performing sentiment analysis after pre-processing the data
def getSentiment(stock):
    #Mining the tweets from the last 7 days and storing it into a dataframe
    data = getTweets(stock)
    #Passing the data for cleaning
    cleaned_data = data_preprocessing(data, stock)
    cleaned_data['date'] = pd.to_datetime(cleaned_data['created_at']).dt.normalize()
    #Performing textblob and vader analysis on the cleaned data
    sentimented_data = sentiment_analysis(cleaned_data, stock)
    #Appending the real stock data to the data frame
    result_data = getRealStock(sentimented_data, stock)
    return result_data