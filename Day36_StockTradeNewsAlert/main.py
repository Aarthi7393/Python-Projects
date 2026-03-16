import requests
import os
from twilio.rest import Client
import html
from deep_translator import GoogleTranslator

proxy= os.environ.get("PROXY")
os.environ['http_proxy']=proxy
os.environ['HTTP_PROXY']=proxy
os.environ['https_proxy']=proxy
os.environ['HTTPS_PROXY']=proxy


##TODO STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    NEWS_API = "https://newsapi.org/v2/everything?"
    NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
    COMPANY_NAME = "Rheinmetall"
    message_body = ""
    parameter1 = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "searchIn" :"title"
    }

    newsapi = requests.get(NEWS_API, params=parameter1)
    newsapi.raise_for_status()
    contents = newsapi.json()["articles"][:3]
    print(contents)
    contents = html.unescape(contents)
    for content in contents:
        title = content["title"]
        description = content["description"]
        title = GoogleTranslator(source='auto', target='en').translate(title)
        description = GoogleTranslator(source='auto', target='en').translate(description)
        message_body += f"Headline:{title}\nBrief:{description}\n"
    print(message_body)
    return message_body

## TODO STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_message(message_body):
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    account_sid = os.environ.get("TWILIO_ACC_SID")
    phone_no = "+15014346615"

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_body,
        from_=phone_no,
        to=os.environ.get("TO_PHONENUMBER")
    )
    print(message.sid)
    print(message.status)



##TODO STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

     # Helps to find the symbol :
     # https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=rheinmetall&apikey=YOUR_KEY
def check_percentage_change():
    STOCK = "RHM.DE"
    STOCK_API = "https://www.alphavantage.co/query"
    parameter = {
         "function": "TIME_SERIES_DAILY",
         "symbol": STOCK,
         "apikey": os.environ.get("ALPHAVANTAGE_API_KEY")
     }
    response = requests.get(STOCK_API, params=parameter)
    response.raise_for_status()
    data = response.json()
    recent_date = list(data["Time Series (Daily)"].keys())[0]
    previous_date =list(data["Time Series (Daily)"].keys())[1]

    recent_close = round(float(data["Time Series (Daily)"][recent_date]["4. close"]),2)
    previous_close = round(float(data["Time Series (Daily)"][previous_date]["4. close"]),2)


    diff_close = round(( previous_close - recent_close),2)
    #diff_close = round((recent_close - previous_close),2)

    percentage_close = diff_close / recent_close * 100
    print(percentage_close)
    return percentage_close

percentage_closure = check_percentage_change()
if percentage_closure < 1 :
    message = get_news()
    message_body = f"🔻{abs(percentage_closure)}%\n{message}"
    print(message_body)
    #send_message(message_body)

elif percentage_closure >1:
    message = get_news()
    message_body = f"🔺{abs(percentage_closure)}%\n{message}"
    print(message_body)
    #send_message(message_body)











#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

