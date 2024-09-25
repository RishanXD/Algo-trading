import doublescreener
from kite_trade import *
from Screener import *
from kite_trade import *
from doublescreener import *
import pandas as pd
from final_workflow import *
from kiteconnect import KiteTicker

def stocks_already_bought(kite):
    # Check if stocks are already bought
    stocks=[]
    for i in kite.holdings():
        stocks.append(i["tradingsymbol"])
    for i in kite.positions()["net"]:  
        stocks.append(i["tradingsymbol"])
    return stocks


def get_instruments_dataframe(kite):
    instruments=kite.instruments("NSE")
    df=pd.DataFrame(instruments)
    df.to_pickle(r'important_data\instruments.pkl')
    return df

def read_instruments_dataframe():
    df=pd.read_pickle(r'important_data\instruments.pkl')
    return df



def get_data_zerodha(kite,stock,df):
    Stock={}
    df=df.copy()
    df.set_index('tradingsymbol', inplace=True)
    result = df.loc[stock]
    Stock["Name"]=stock
    Stock["instrument_token"]=int(result["instrument_token"])
    return Stock




def ltp_value(kite,stock):
    """
    Gets the ltp of a stock using web socket
    """

    with open(r"important_data\enctoken.txt") as file:
        enctoken = file.read()
    user_id=kite.profile()["user_id"]
    kws = KiteTicker(api_key="your_api_key", access_token=f"{enctoken}&user_id={user_id}")
    def on_ticks(ws, ticks):
        global ltp_value_number
        if ticks:
            ltp_value_number = ticks[0]['last_price']
    instrument_token=get_data_zerodha(kite=kite,stock=stock,df=read_instruments_dataframe())["instrument_token"]
    kws.on_ticks = on_ticks # type: ignore
    kws.connect(threaded=True)
    while not kws.is_connected():
        time.sleep(1)
    print("WebSocket : Connected")
    kws.subscribe([instrument_token])
    (kws.set_mode(kws.MODE_LTP, [instrument_token]))
    time.sleep(0.5)
    kws.unsubscribe([instrument_token])

    return (ltp_value_number)


def buy(kite):
    global not_enough_funds
    not_enough_funds=[]
    Funds=kite.funds()["equity"]["available"]["live_balance"]
    
    if Funds>2500:
        screened_stocks=doublescreener.final_screening(kite=kite)
        
        df=read_instruments_dataframe()
        try:
            Funds_for_each_stock=Funds/(len(screened_stocks))
            for i in screened_stocks:  
                minute=get_data(stock_name=i,time="1m")
                if minute["high"]>Funds_for_each_stock: # type: ignore
                    if i not in not_enough_funds:
                        not_enough_funds.append(i)
                        continue
                if i in not_enough_funds:
                    continue

                if i in stocks_already_bought(kite=kite):
                    continue

                ltp=ltp_value(kite=kite,stock=i)
                
                if Funds_for_each_stock<ltp:
                    print(f"Insufficient funds for buying {i}")
                    continue
                

                order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                    exchange=kite.EXCHANGE_NSE,
                                    tradingsymbol=i,
                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                    quantity=int(Funds_for_each_stock//ltp) if ((Funds_for_each_stock)//ltp) else None,
                                    product=kite.PRODUCT_CNC,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    price=None,
                                    validity=kite.VALIDITY_IOC,
                                    disclosed_quantity=None,
                                    trigger_price=None,
                                    squareoff=None,
                                    stoploss=None,
                                    trailing_stoploss=None,
                                    tag="bot")
                print(f"Placed a buying order for {int((Funds//len(screened_stocks))//ltp)} shares of {i}- {order}")
                telegram_send(f"Placed a buying order for {int((Funds//len(screened_stocks))//ltp)} shares of {i}- {order}")
                with open(r"important_data\bought_by_bot.txt","r") as file:
                    bought_by_bot = dict(eval(file.read()))
                    if i not in bought_by_bot.keys():
                        bought_by_bot[i]=int((Funds//len(screened_stocks))//ltp)
                    if i in bought_by_bot.keys():
                        bought_by_bot[i]+=int((Funds//len(screened_stocks))//ltp)
                with open(r"important_data\bought_by_bot.txt","w") as file:
                    file.write(str(bought_by_bot))
                if len(screened_stocks)>1:
                    time.sleep(1)
        except ZeroDivisionError:
            pass
