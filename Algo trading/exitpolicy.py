import time
from kiteconnect import KiteTicker
from final_workflow import kite_login
from kite_trade import *
from testing import *
from doublescreener import *
from Screener import *
from entrypolicy import *


def sell(kite):
    stoploss=-15
    target_profit=30
    global ltp_dict
    ltp_dict = {}


    def on_ticks(ws, ticks):
        global ltp_dict
        for tick in ticks:
            instrument_token = tick['instrument_token']
            ltp = tick['last_price']
            ltp_dict[instrument_dict[instrument_token]] = ltp

    net_holdings=kite.holdings()
    for i in net_holdings:
        tradingsymbol=i["tradingsymbol"]
        df=read_instruments_dataframe()
        if tradingsymbol in list(df['tradingsymbol']):
            pass
        else:
            # print(f"{tradingsymbol} is not listed on NSE")
            net_holdings.remove(i)

    stock=[]
    for i in net_holdings:
        stock.append(i["tradingsymbol"])
    with open(r"important_data\enctoken.txt") as file:
        enctoken = file.read()
    user_id=kite.profile()["user_id"]
    kws = KiteTicker(api_key="your_api_key", access_token=f"{enctoken}&user_id={user_id}")

    instrument_dict={}

    for i in stock:
        instrument_token=get_data_zerodha(kite=kite,stock=i,df=read_instruments_dataframe())["instrument_token"]
        instrument_dict[instrument_token]=i


    kws.on_ticks = on_ticks # type: ignore
    kws.connect(threaded=True)
    while not kws.is_connected():
        time.sleep(1)
    print("WebSocket : Connected")

    kws.subscribe(list(instrument_dict.keys()))
    (kws.set_mode(kws.MODE_LTP, [instrument_token]))
    time.sleep(1)

    try:


        Do_not_sell=["AARNAV"]




        if net_holdings==[]:
            print("There are no stocks in your portfolio")
            return None
        while True:
            print("Sell operation active")
            net_holdings=kite.holdings()
            for i in net_holdings:
                with open(r"important_data\bought_by_bot.txt","r") as file:
                    bought_by_bot = file.read()
                tradingsymbol=i["tradingsymbol"]
                if tradingsymbol in list(df['tradingsymbol']):
                    pass
                else:
                    # print(f"{tradingsymbol} is not listed on NSE")
                    net_holdings.remove(i)
                
            for i in net_holdings:
                if tradingsymbol not in bought_by_bot:
                    net_holdings.remove(i)

                    
            
            for i in net_holdings:
    
    
                order_placed=False
                tradingsymbol=i["tradingsymbol"]

                quantity=(i["quantity"])
                if quantity==0:
                    quantity=i["t1_quantity"]
                if quantity==0:
                    continue

                if i['tradingsymbol'] in Do_not_sell:
                    continue
    
                net_positions=kite.positions()["net"]

                for i in net_positions:
                    quantity=0
                    order_placed=False
                    tradingsymbol=i['tradingsymbol']
                    for j in kite.orders():
                        if tradingsymbol==j["tradingsymbol"]:
                                if j['transaction_type']=="SELL":
                                    if j['status']=='COMPLETE':
                                        if i["quantity"]==0:
                                            order_placed=True





                try:
                    if i["tradingsymbol"] in ltp_dict:
                        ltp=ltp_dict[i["tradingsymbol"]]
                        unrealised_profit=((ltp-i["average_price"])/i["average_price"])*100
                        # print(round(unrealised_profit,2))
                        if unrealised_profit>target_profit and order_placed==False:
                            order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                exchange=kite.EXCHANGE_NSE,
                                tradingsymbol=tradingsymbol,
                                transaction_type=kite.TRANSACTION_TYPE_SELL,
                                quantity=quantity,
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
                            # order="test"


                            print(f"Placed a selling order for {int(quantity)} shares of {tradingsymbol}- {order} as its profit has crossed the target profit of {target_profit}%")
                            time.sleep(1)
                            continue


                        if unrealised_profit<stoploss and order_placed==False:
                            order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                exchange=kite.EXCHANGE_NSE,
                                tradingsymbol=tradingsymbol,
                                transaction_type=kite.TRANSACTION_TYPE_SELL,
                                quantity=quantity,
                                product=kite.PRODUCT_CNC,
                                order_type=kite.ORDER_TYPE_MARKET,
                                price=None,
                                validity=kite.VALIDITY_IOC,
                                disclosed_quantity=None,
                                trigger_price=None,
                                squareoff=None,
                                stoploss=None,
                                trailing_stoploss=None,
                                tag="bot"
                                )
                            # order="test"
                            print(f"Placed a selling order for {int(quantity)} shares of {tradingsymbol}- {order} as its loss has crossed the stoploss value of {stoploss}%") 
                            time.sleep(1)
                            continue     


                except KeyboardInterrupt:
                    kws.unsubscribe([instrument_token])
                    exit("Keyboard interrupt")








                if order_placed==False and quantity>0:
                    try:
                        daily=get_data(tradingsymbol,"Daily")
                        hourly=get_data(stock_name=tradingsymbol,time="1h")
                    except Exception:
                        # print(f"{tradingsymbol} is not listed on NSE")
                        continue

                    if daily["RSI"]<50 and daily["close"] <= daily["EMA10"]: # type: ignore
                        if hourly["RSI"]<50 and hourly["close"] <= hourly["EMA10"]:  # type: ignore
                            print(f"Selling {quantity} of {tradingsymbol}")
                        
                            order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                        exchange=kite.EXCHANGE_NSE,
                                        tradingsymbol=tradingsymbol,
                                        transaction_type=kite.TRANSACTION_TYPE_SELL,
                                        quantity=quantity,
                                        product=kite.PRODUCT_CNC,
                                        order_type=kite.ORDER_TYPE_MARKET,
                                        price=None,
                                        validity=None,
                                        disclosed_quantity=None,
                                        trigger_price=None,
                                        squareoff=None,
                                        stoploss=None,
                                        trailing_stoploss=None,
                                        tag="bot")
                            # order="test"
                            print(f"Placed a selling order for {int(quantity)} shares of {tradingsymbol}- {order} as it met the exit conditions")
                            time.sleep(1)
            time.sleep(30)
    except KeyboardInterrupt:
        kws.unsubscribe([instrument_token])








# from final_workflow import kite_login
# from kite_trade import *
# from testing import *

# def sell(kite):
#     net_holdings=kite.holdings()


#     if net_holdings==[]:
#         print("There are no stocks in your portfolio")
#         return None
    
#     for i in net_holdings:
#         order_placed=False
#         tradingsymbol=i["tradingsymbol"]
#         quantity=(i["quantity"])
#         if quantity==0:
#             quantity=i["t1_quantity"]
#         if quantity==0:
#             continue
#         for j in kite.orders():
#             if tradingsymbol==j["tradingsymbol"]:
#                 order_placed=True

#         stoploss=-15
#         target_profit=30

#         for i in net_holdings:
#             unrealised_profit=(i["pnl"]/(i["average_price"]*quantity))*100

#             if unrealised_profit>target_profit:
#                 order = kite.place_order(variety=kite.VARIETY_REGULAR,
#                     exchange=kite.EXCHANGE_NSE,
#                     tradingsymbol=tradingsymbol,
#                     transaction_type=kite.TRANSACTION_TYPE_SELL,
#                     quantity=quantity,
#                     product=kite.PRODUCT_CNC,
#                     order_type=kite.ORDER_TYPE_MARKET,
#                     price=None,
#                     validity=kite.VALIDITY_IOC,
#                     disclosed_quantity=None,
#                     trigger_price=None,
#                     squareoff=None,
#                     stoploss=None,
#                     trailing_stoploss=None,
#                     tag="Rishan")
#                 print(f"Placed a selling order for {int(quantity)} shares of {tradingsymbol}- {order} as its profit has crossed {target_profit}%")
#                 time.sleep(5)

#                 continue
                                
#             if unrealised_profit<stoploss:
#                 order = kite.place_order(variety=kite.VARIETY_REGULAR,
#                     exchange=kite.EXCHANGE_NSE,
#                     tradingsymbol=tradingsymbol,
#                     transaction_type=kite.TRANSACTION_TYPE_SELL,
#                     quantity=quantity,
#                     product=kite.PRODUCT_CNC,
#                     order_type=kite.ORDER_TYPE_MARKET,
#                     price=None,
#                     validity=kite.VALIDITY_IOC,
#                     disclosed_quantity=None,
#                     trigger_price=None,
#                     squareoff=None,
#                     stoploss=None,
#                     trailing_stoploss=None,
#                     tag="Rishan")
#                 print(f"Placed a selling order for {int(quantity)} shares of {tradingsymbol}- {order} as its profit has crossed {stoploss}%") 
#                 time.sleep(5)
  
#                 continue             




#         if order_placed==False:
#             daily=get_data(tradingsymbol,"Daily")
#             if daily["RSI"]<50 and daily["close"] <= daily["EMA10"]: # type: ignore
                
#                 order = kite.place_order(variety=kite.VARIETY_REGULAR,
#                             exchange=kite.EXCHANGE_NSE,
#                             tradingsymbol=tradingsymbol,
#                             transaction_type=kite.TRANSACTION_TYPE_SELL,
#                             quantity=quantity,
#                             product=kite.PRODUCT_CNC,
#                             order_type=kite.ORDER_TYPE_MARKET,
#                             price=None,
#                             validity=None,
#                             disclosed_quantity=None,
#                             trigger_price=None,
#                             squareoff=None,
#                             stoploss=None,
#                             trailing_stoploss=None,
#                             tag="Rishan")
#                 print(f"Placed a selling order for {int(quantity)} shares of {tradingsymbol}- {order}")
#                 time.sleep(5)


