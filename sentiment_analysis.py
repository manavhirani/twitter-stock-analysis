from textblob_sentiment import textblob_senti
from vader_sentiment import vader_sentiment

#Performing textblob and vader sentiment analysis on the cleaned data
def sentiment_analysis(dataframe,stock):
    #Performing textblob sentimental analysis
    df1 = textblob_senti(dataframe)
    #Performing vader senttimental analysis
    df2 = vader_sentiment(dataframe)
    #Appending df1 and df2 to result_dataframe
    result_dataframe = df1
    result_dataframe['vader_sentiment'] = df2['vader_sentiment']
    result_dataframe.to_csv("./output/" + "sentiment_" + stock + ".csv")
    #Returninig result_dataframe
    return result_dataframe