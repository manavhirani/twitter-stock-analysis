from getSentiment import getSentiment
import matplotlib.pyplot as plt

#Plotting the datafram and saving it to the root folder
def plotting(dataframe,stock):
    analysis = ["text_blob", "vader_sentiment", "Real_time Stock"]
    dataframe.plot(x='date', y=analysis, kind = 'line', title=stock).get_figure().savefig(stock)
    plt.grid(which="major", alpha=0.6)
    plt.grid(which="minor", alpha=0.3)
    plt.show()

#Entry point
if __name__ == "__main__":
    #Printing a prompt to take input from the user
    print("CIS-600 Social Media Data Mining Final Project:\nPerforming sentiment analysis on stock tickers using mined data from Twitter\n")
    print("Choose from the following sample list of stock tickers or enter your stock ticker\n Tickers for:\n")
    sample_stocks = ['Nvidia is NVDA', 'Microsoft is MSFT', 'Apple.Inc is AAPL', 'Roblox.Inc is RBLX']
    for i in range(len(sample_stocks)):
        print((i+1),".", sample_stocks[i])
    #Taking the input of the stock ticker
    stock = input("Enter stock ticker: \n")
    #Passing the stock to the getSentime() method and storing it in dataframe
    dataframe = getSentiment(stock)
    #renaming dataframe
    dataframe.rename(columns = {'Adj Close':'Real_time Stock'}, inplace = True)
    #plotting the graph
    plotting(dataframe,stock)
    print("Exited")
    #End of Program