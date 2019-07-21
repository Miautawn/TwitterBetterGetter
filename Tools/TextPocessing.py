import re
from urllib.request import urlopen
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize


def RefactorSearchStream(status):
    text = None
    if "extended_tweet" in status._json:
        text = status._json["extended_tweet"]["full_text"]
    elif "retweeted_status" in status._json:
        text = status._json["retweeted_status"]["text"]
    else:
      text = status._json["text"]
    clean_text = extractURLs(text)
    clean_text = TextCleaning(clean_text)
    f = open("TimeStamp.txt", "w").write(str(status.created_at))
    return clean_text


def RefactorSearchResults(search):  # filters old tweets and gets only text
    clean_results = []
    f = open("TimeStamp.txt", "r").read()
    fresh_results = [tweet for tweet in search if str(tweet.created_at) > str(f)]
    for tweet in fresh_results:
        text = None
        if "retweeted_status" in tweet._json:
            text = (tweet._json["retweeted_status"]["full_text"])
        else:
            text = (tweet._json["full_text"])

        clean_text = extractURLs(text)
        clean_text = TextCleaning(clean_text)
        clean_results.append(clean_text)
    f = open("TimeStamp.txt", "w").write(str(search[0].created_at))
    return clean_results

def extractURLs(text):    #Extracts provided urls and cleans them from text, stores them into scraper
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    if(len(urls) == 0):
        return text
    else:
        text_withoutUrls = text
        text_URLs = set({})
        Real_URLs = set({})
        #f = open("UrlsForScraper.txt", "a")
        for url in urls:
            text_URLs.add(url)
            text_withoutUrls = text_withoutUrls.replace(url, "")
        #for url in text_URLs:  #check if urls are accessable
            #try:
                #res = urlopen(url)
                #Real_url = res.geturl()
                #Real_URLs.add(Real_url)
            #except:
                #print("Invalid url: " + url)
        #for url in Real_URLs:
            #f.write(url + "\n")
        return text_withoutUrls

def TextCleaning(text):    #This will clean the text of any hashtags emojies ect.
    clean_text = text
    for match in re.findall("\#|\@\w+|\W", text):
        if (match not in [" ", ".", ",", "?", "!", "'", "$", "%"]):
            clean_text = clean_text.replace(match, " ")
    clean_text = clean_text.strip()
    return clean_text


def PerformSentimentAnalysis(text):    #This will return simple VADER polarity score with value and compound percenta
    sid = SentimentIntensityAnalyzer()
    sentences = sent_tokenize(text)
    score = 0
    counter = 0
    for x in sentences:
        ss = sid.polarity_scores(x)
        score += ss["compound"]
        counter += 1
    final_score = score / counter
    if (final_score >= 0.30):
        return {"positive":final_score}
    elif (final_score <= -0.30):
        return {"negative": final_score}
    else:
        return {"neutral": final_score}