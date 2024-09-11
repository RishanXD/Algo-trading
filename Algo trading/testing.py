def rsi(stock_name,time):
    if time=="Monthly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_MONTH
        )
        return(obj.get_analysis().indicators["RSI"])
    if time=="Daily":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_DAY
        )
        return(obj.get_analysis().indicators["RSI"])
    if time=="Weekly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_WEEK
        )
        return(obj.get_analysis().indicators["RSI"])





def sma20(stock_name,time):
    if time=="Monthly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_MONTH
        )
        return(obj.get_analysis().indicators["SMA20"])
    if time=="Daily":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_DAY
        )
        return(obj.get_analysis().indicators["SMA20"])
    if time=="Weekly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_WEEK
        )
        return(obj.get_analysis().indicators["SMA20"])





def high(stock_name,time):
    if time=="Monthly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_MONTH
        )
        return(obj.get_analysis().indicators["high"])
    elif time=="Daily":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_DAY
        )
        return(obj.get_analysis().indicators["high"])
    elif time=="Weekly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_WEEK
        )
        return(obj.get_analysis().indicators["high"])




def volume(stock_name,time):
    if time=="Monthly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_MONTH
        )
        return(obj.get_analysis().indicators["volume"])
    elif time=="Daily":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_DAY
        )
        return(obj.get_analysis().indicators["volume"])
    elif time=="Weekly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_WEEK
        )
        return(obj.get_analysis().indicators["volume"])
    



def UBB(stock_name,time):
    if time=="Monthly":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_MONTH
        )
        return(stock.get_analysis().indicators['BB.upper'])
    elif time=="Daily":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_DAY
        )
        return(stock.get_analysis().indicators['BB.upper'])
    elif time=="Weekly":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_WEEK
        )
        return(stock.get_analysis().indicators['BB.upper'])




def get_data(stock_name,time):
    if time=="Monthly":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_MONTH
        )
        return(stock.get_analysis().indicators)
    if time=="Daily":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_DAY
        )
        return(stock.get_analysis().indicators)
    if time=="Weekly":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_WEEK
        )
        return(stock.get_analysis().indicators)
from tradingview_ta import TA_Handler, Interval, Exchange
