from final_workflow import *
import testing
def get_data(stock_name,time):
    if time=="1m":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_MINUTE 
        )
        return(stock.get_analysis().indicators)# type: ignore
    if time=="15m":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_15_MINUTES 
        )
        return(stock.get_analysis().indicators)# type: ignore

    if time=="1h":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_HOUR
        )
        return(stock.get_analysis().indicators)# type: ignore
    
    if time=="Monthly":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_MONTH
        )
        return(stock.get_analysis().indicators)# type: ignore
    if time=="Daily":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_DAY
        )
        return(stock.get_analysis().indicators)# type: ignore
    if time=="Weekly":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_WEEK
        )
        return(stock.get_analysis().indicators)# type: ignore


    


from tradingview_ta import TA_Handler, Interval, Exchange, get_multiple_analysis
import time


# Your list of Nifty stocks
file=open(r"important_data\\Nifty500.txt","r")
Nifty=eval(file.read())

# Prefix the stock symbols with "NSE:" to create the full symbols
Nifty = [f"NSE:{symbol}" for symbol in Nifty]


# Nifty=["TATAMTRDVR","SBIN","ASIANPAINT","WIPRO","ITC",'ICICIBANK',"HDFCBANK","RITES","KOTAKBANK","SIEMENS"]
# Nifty=['SBIN',"BHARATFORG","HINDZINC","TATAMTRDVR","KOTAKBANK","VGUARD","SIEMENS","ABB",'ITC',"RELIANCE","VEDL","MARICO","JWL","TIMKEN","FINPIPE","CGPOWER","BEML","ADANIPOWER","BDL","ATGL","TATAMOTORS"]
# Nifty=["HINDZINC"]

# def screening():
#     Screened=[]
#     for stock in Nifty:
#         if high(stock,"Daily") >= UBB(stock,"Daily"):
#             # print("1")
#             if high(stock,"Weekly") >= UBB(stock,"Weekly"):
#                 # print("2")
#                 if high(stock,"Monthly") >= UBB(stock,"Monthly"):
#                     # print("3")
#                     if high(stock,"Daily") >= UBB(stock,"Weekly"):
#                         # print("4")
#                         if high(stock,"Daily") >= UBB(stock,"Monthly"):
#                             # print("5")
#                             if rsi(stock,"Daily")>=50.0:
#                                 # print("6")
#                                 if rsi(stock,"Weekly")>=60.0:
#                                     # print("7")
#                                     if rsi(stock,"Monthly")>=60.0:
#                                         # print("8")
#                                         if (volume(stock,"Daily") / sma20(stock,"Daily")) > 3.0:
#                                             # print("9")
#                                             Screened.append(stock)
#     return Screened




# daily=get_data("TATAMTRDVR","Daily")
# print(daily["UBB"])





def screening():
    Screened=[]
    Not_Screened=[]
    # Fetch multiple analyses for the Nifty stocks
    print("Getting data...")
    daily_all = get_multiple_analysis(screener="india", interval=Interval.INTERVAL_1_DAY , symbols=Nifty)
    weekly_all = get_multiple_analysis(screener="india", interval=Interval.INTERVAL_1_WEEK , symbols=Nifty)
    monthly_all = get_multiple_analysis(screener="india", interval=Interval.INTERVAL_1_MONTH , symbols=Nifty)
    
    # print("\033[A\033[K", end="") # this code deletes previous printed line and prints the new line in place of it
    
    for stock in Nifty:


        try:


            daily=daily_all[stock].indicators # type: ignore
            
            if daily["high"] >= daily["BB.upper"]:# type: ignore
                # print("1")
                weekly=weekly_all[stock].indicators



                if weekly["high"] >= weekly["BB.upper"]:# type: ignore
                    # print("2")
                    monthly=monthly_all[stock].indicators



                    if monthly["high"] >= monthly["BB.upper"]:# type: ignore
                        # print("3")



                        if daily['high'] >= weekly["BB.upper"]:# type: ignore
                            # print("4")



                            if daily['high'] >= monthly["BB.upper"]:# type: ignore
                                # print("5")



                                if daily["RSI"]>=50.0:# type: ignore
                                    # print("6")



                                    if weekly["RSI"]>=60.0:# type: ignore
                                        # print("7")



                                        if monthly["RSI"]>=60.0:# type: ignore
                                            # print("8")



                                            if daily["change"]  < 8 and daily["change"]>0:# type: ignore
                                                # print("9")
                                                
                                                if daily["open"]<daily["BB.upper"]:# type: ignore
                                                    # print(10)
                                                    stock=stock.replace("NSE:", "")
                                                    Screened.append(stock)
                                                    
        except:
            stock=stock.replace("NSE:", "")
            Not_Screened.append(stock)

    return Screened,Not_Screened