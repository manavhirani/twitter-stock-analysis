import pandas as pd
import regex as re
import string
import nltk
from nltk.corpus import stopwords

#Removing usernames from the tweet:
def remove_username(text):
    text = re.sub('@[^\s]+', '', text)
    return text


#Function for removing URL's from the tweet
def remove_url(text):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'', text)

#Removing the Hash-tag word in its entirety from the tweet
def remove_hastag(text):
    remove_hash = ""
    for word in text:
        if "#" not in word:
            remove_hash += word
    return remove_hash

#removing punctuations from the data for further cleaning
remove_punctuations_from_data = [',', '"', ':', ')', '(','?', '|', ';', "'", '$', '&', '/', '[', ']', '>', '%', '=', '#', '*', '+', '\\', '~', '@','·', '_', '{', '}','^', '®', '`', '<', '>', '″', '\'', '“', '”', '-','═', ':','⋅', '‘','`','-','’','—','.','!']
def remove_punctuations(text):
    for punctuation in remove_punctuations_from_data:
        text = text.replace(punctuation, '')
    return text


#removing New Line Characters
remove_newLineCharacters_from_data = ['\n', '\t']
def remove_newlinecharacters(text):
    for punctuation in remove_newLineCharacters_from_data:
        text = text.replace(punctuation, ' ')
    return text

#decorating text for efficient NLP
def decontraction(text):
    text = re.sub(r"won\'t", " will not", text)
    text = re.sub(r"won\'t've", " will not have", text)
    text = re.sub(r"can\'t", " can not", text)
    text = re.sub(r"don\'t", " do not", text)

    text = re.sub(r"can\'t've", " can not have", text)
    text = re.sub(r"ma\'am", " madam", text)
    text = re.sub(r"let\'s", " let us", text)
    text = re.sub(r"ain\'t", " am not", text)
    text = re.sub(r"shan\'t", " shall not", text)
    text = re.sub(r"sha\n't", " shall not", text)
    text = re.sub(r"o\'clock", " of the clock", text)
    text = re.sub(r"y\'all", " you all", text)
    text = re.sub(r"n\'t", " not", text)
    text = re.sub(r"n\'t've", " not have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'d've", " would have", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ll've", " will have", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)
    text = re.sub(r"\'re", " are", text)
    return text

#removing stop words from the text
def remove_stopwords(text):
    text = ' '.join([word for word in text.split() if word not in (stopwords.words('english'))])
    return text

#removing html tags from the text
def remove_html(text):
    html=re.compile(r'<.*?>')
    return html.sub(r'', text)

#seperate alphanumeric 
def seperate_alphanumeric(text):
    words = text
    words = re.findall(r"[^\W\d_]+|\d+", words)
    return " ".join(words)

def cont_rep_char(text):
    tchr = text.group(0)
    if len(tchr) > 1:
        return tchr[0:2]

def unique_char(rep, text):
    substitute = re.sub(r'(\w)\1+', rep, text)
    return substitute

def char(text):
    substitute = re.sub(r'[^a-zA-Z]', ' ', text)
    return substitute

#remove emojis
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

#data preprocessing
def data_preprocessing(data, stock):
    #data = pd.read_csv(r"./output/" + "TITN" + ".csv" , encoding = 'utf8')
    # print(stock)
    # print(data['text'])
    data = data.dropna()
    #CLEANING THE DATA
    data['text'] = data['text'].apply(lambda x : remove_username(x))
    data['text'] = data['text'].apply(lambda x : remove_url(x))
    data['text'] = data['text'].apply(lambda x : remove_emoji(x))
    data['text'] = data['text'].apply(lambda x : remove_html(x))
    data['text'] = data['text'].apply(lambda x: remove_newlinecharacters(x))
    data['text'] = data['text'].apply(lambda x : decontraction(x))
    data['text'] = data['text'].apply(lambda x : seperate_alphanumeric(x))
    data['text'] = data['text'].apply(lambda x : unique_char(cont_rep_char,x))
    data['text'] = data['text'].apply(lambda x : char(x))
    data['text'] = data['text'].apply(lambda x : x.lower())
    data['text'] = data['text'].apply(lambda x : remove_stopwords(x))
    data['text'] = data['text'].apply(lambda x : remove_punctuations(x))

    # print("Data after Removing punctuations: \n")
    # print(data['text'])
    #CONVERTING THE DATA TO CSV TO FORMAT
    data.to_csv("./output/" + "cleaned_" + stock + ".csv")
    #Returning the cleaned data
    return data