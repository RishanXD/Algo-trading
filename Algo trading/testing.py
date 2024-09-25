def rsi(stock_name,time):
    if time=="Monthly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_MONTH
        )
        return(obj.get_analysis().indicators["RSI"]) # type: ignore # type: ignore
    if time=="Daily":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_DAY
        )
        return(obj.get_analysis().indicators["RSI"]) # type: ignore # type: ignore
    if time=="Weekly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_WEEK
        )
        return(obj.get_analysis().indicators["RSI"]) # type: ignore # type: ignore





def sma20(stock_name,time):
    if time=="Monthly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_MONTH
        )
        return(obj.get_analysis().indicators["SMA20"]) # type: ignore
    if time=="Daily":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_DAY
        )
        return(obj.get_analysis().indicators["SMA20"]) # type: ignore
    if time=="Weekly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_WEEK
        )
        return(obj.get_analysis().indicators["SMA20"]) # type: ignore





def high(stock_name,time):
    if time=="Monthly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_MONTH
        )
        return(obj.get_analysis().indicators["high"]) # type: ignore
    elif time=="Daily":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_DAY
        )
        return(obj.get_analysis().indicators["high"]) # type: ignore
    elif time=="Weekly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_WEEK
        )
        return(obj.get_analysis().indicators["high"]) # type: ignore




def volume(stock_name,time):
    if time=="Monthly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_MONTH
        )
        return(obj.get_analysis().indicators["volume"]) # type: ignore
    elif time=="Daily":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_DAY
        )
        return(obj.get_analysis().indicators["volume"]) # type: ignore
    elif time=="Weekly":
        obj = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_WEEK
        )
        return(obj.get_analysis().indicators["volume"]) # type: ignore # type: ignore
    



def UBB(stock_name,time):
    if time=="Monthly":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_MONTH
        )
        return(stock.get_analysis().indicators['BB.upper']) # type: ignore
    elif time=="Daily":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_DAY
        )
        return(stock.get_analysis().indicators['BB.upper']) # type: ignore
    elif time=="Weekly":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_WEEK
        )
        return(stock.get_analysis().indicators['BB.upper']) # type: ignore # type: ignore




def get_data(stock_name,time):
    if time=="Monthly":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_MONTH
        )
        return(stock.get_analysis().indicators) # type: ignore
    if time=="Daily":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_DAY
        )
        return(stock.get_analysis().indicators) # type: ignore
    if time=="Weekly":
        stock = TA_Handler(
            symbol=stock_name,
            screener="india",
            exchange="NSE",
            interval=Interval.INTERVAL_1_WEEK
        )
        return(stock.get_analysis().indicators) # type: ignore
from tradingview_ta import TA_Handler, Interval, Exchange
