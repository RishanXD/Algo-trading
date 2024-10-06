from urllib import response
from kite_trade import *
import time
import internet
import UI
import telegram
import requests
import zerodha_login
def kite_login():
    try:
        file=open(r"important_data\\enctoken.txt","r")
        enctoken=file.read()
    except FileNotFoundError:
        open(r"important_data\\enctoken.txt","w")
        with open(r"important_data\\enctoken.txt","r") as file:
            enctoken=file.read()


    kite=KiteApp(enctoken=enctoken)
    if kite.profile()!=None:
        print("Successfully logged into zerodha session using enctoken")
        return kite
    elif kite.profile()==None:
        print("Failed to log into zerodha session using enctoken")
        enctoken = zerodha_login.get_enctoken()
        kite=KiteApp(enctoken=enctoken)
        with open(r"important_data\\enctoken.txt","w") as file:
                file.write(enctoken)
        if kite.profile()!=None:
            print("Successfully logged in to the zerodha session using enctoken")
            return kite
        
        elif kite.profile()==None:
            print("Invalid Token, try to refresh the zerodha session")
            UI.errorbox("Invalid token, exiting the program")
            exit()
    return kite


def internet_check_and_fix():
    for i in range(2):
        if not internet.is_internet_connected():
            internet.search_and_connect_to_wifi("Airtel_9301131150_5GHz")

def is_market_open():
    headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}
    response=requests.get("https://www.nseindia.com/api/marketStatus",headers=headers,timeout=5)
    # return (response.json()["marketState"][0]["marketStatus"])
    if (response.json()["marketState"][0]["marketStatus"])=="Closed" or (response.json()["marketState"][0]["marketStatus"])=="Close":
        return False
    if (response.json()["marketState"][0]["marketStatus"])=="Open":
        return True
    else:
        return True

def telegram_send(message):
    """used to send telegram notification"""
    base_url = rf"https://api.telegram.org/bot6278715208:AAHuQBLJUWxOILF0MJyqToslQIr2LhXoG2k/sendMessage?chat_id=-903007971&text={message}"
    requests.get(base_url)
    print(f"Sent telegram message: {message}")
    return None