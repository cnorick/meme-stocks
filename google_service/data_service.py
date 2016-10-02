#!flask/bin/python
from pytrends.request import TrendReq
import sys
import time
from googleapiclient.discovery import build

meme_list = ["good guy greg", "grumpy cat", "bad luck brian", "business cat", "batman slap robin",
    "blurry mr krabs", "dat boi", "willy wonka", "philosoraptor", "high expectations asian father",
    "kermit the frog drinking tea", "harambe", "petty skai", "pepe the frog", "y u no",
    "one does not simply", "futurama fry", "sad papaw", "what if i told you",
    "the most interesting man in the world"]

def get_result_count(meme_name):
    service = build("customsearch", "v1", developerKey="AIzaSyDj_UD-dK3-4mTyOUeD2JUABDVLpUi2gho")

    result = service.cse().list(
            q=str(meme_name),
            cx='003037442946977428462:dnodeoe0sta'
        ).execute()

    return result["searchInformation"]["totalResults"]

def get_score(meme_name):
    maxvalue = get_result_count(meme_name)
    google_username = "danqjones@gmail.com"
    google_password = "volhacks"

    pytrend = TrendReq(google_username, google_password, custom_useragent = 'Volhacks 2016')

    trend_payload = {'q': meme_name, 'date': '01/2011 69m'}

    trend = pytrend.trend(trend_payload, return_type = 'dataframe')
    time.sleep(10)
    print(trend)
    #for date in trend.index:
        #print date
        #print trend.at[date,meme_name]
    date = trend.index[-1]
    score = trend.at[date,meme_name] * int(maxvalue)
    score = score / float(100)
    print str(date) + " " + str(score)
    return score

def get_high_score():
    maximum = 0
    max_meme = ""
    for meme in meme_list:
        meme_score = get_score(meme)
        if meme_score > maximum:
            maximum = meme_score
            max_meme = meme
    print "Maximum is " + max_meme + " " + str(maximum)
    return (max_meme, maximum)
