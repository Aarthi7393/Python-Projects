import requests
import os
proxy= os.environ.get("PROXY")
os.environ['http_proxy']=proxy
os.environ['HTTP_PROXY']=proxy
os.environ['https_proxy']=proxy
os.environ['HTTPS_PROXY']=proxy

bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
bot_chatID = os.environ.get("TELEGRAM_BOT_CHAT_ID")
