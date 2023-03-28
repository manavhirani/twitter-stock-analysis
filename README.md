## **PERFORMING SENTIMENT ANALYSIS ON STOCK TICKERS USING DATA MINING ON TWITTER**

### 1. Project description
- The rise in social media usage and the power of its influence has created new perspectives towards the traditional investment strategies in investing in stock market. Using hashtags of stock tickers, e.g. TSLA, NASDAQ, NVIDIA, on twitter, we can interpret the trend in the stocks performance over a certain period of time. This project uses sentiment analysis to measure this trend by mining tweets using twitters Twitter API and comparing them to real time data collected from Yahoo Finance (yfinance)

- We used tweepy to extract tweets from twitter and store them into a pandas data frame. This data frame is then passed on to a pre processor that further cleans the data into a form that can be used for Natural Language Processing (NLP), particularly sentimental analysis. 

- To perform the sentimental analysis, we have used the textblob and VADER (Valence Aware Dictionary and sEntiment Reasoner). These methods work differently on different types of tweets, textblob is better for more formal tweets while VADER works better with emojis and informal language. 

### 2. Running the script

The project is written using Python 3.0 and the entry point can be found in exec.py

Make sure you have Python 3 installed on your system and add it to the environment variables

Go to the root folder of the project in your terminal and run

> $ python3 exec.py

### 3. Using this Project

Once executed you will be prompted to enter a stock ticker. After pressing enter it will take some time and output a graph with the name of the stock ticker and save it to the root folder. This graph shows the results of TextBlob, VADER and real-life results for the last 7 days for the input stock ticker.
