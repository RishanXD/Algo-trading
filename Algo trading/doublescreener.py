from kite_trade import *
from Screener import *
import entrypolicy
from datetime import datetime, timedelta
import pandas as pd
import ta
with open(r"important_data\enctoken.txt","r") as file:
    enctoken = file.read()
kite = KiteApp(enctoken=enctoken)

# screened_stocks=['ADANIPORTS', 'ADANIPOWER', 'AEGISCHEM', 'ASHOKLEY', 'BEML', 'BALKRISIND', 'BDL', 'BEL', 'BHARTIARTL', 'BRIGADE', 'CENTURYTEX', 'COALINDIA', 'COCHINSHIP', 'CAMS', 'COROMANDEL', 'DIXON', 'EICHERMOT', 'ENGINERSIN', 'FINCABLES', 'FINPIPE', 'FORTIS', 'GRSE', 'GLAXO', 'HAVELLS', 'HINDALCO', 'HAL', 'HUDCO', 'IRFC', 'NAUKRI', 'INDIGO', 'KEI', 'LODHA', 'MAZDOCK', 'NHPC', 'PNCINFRA', 'POLYMED', 'RVNL', 'SJVN', 'MOTHERSON', 'SAREGAMA', 'SOBHA', 'SOLARINDS', 'UNOMINDA', 'VGUARD']
# screened_stocks=['ADANIPORTS', 'ADANIPOWER', 'AEGISCHEM', 'ARE_M', 'ASHOKLEY', 'BEML', 'BALKRISIND', 'BDL', 'BEL', 'BHARTIARTL', 'BRIGADE', 'CENTURYTEX', 'COALINDIA', 'COCHINSHIP', 'CAMS', 'COROMANDEL', 'DIXON', 'EICHERMOT', 'ENGINERSIN', 'FINCABLES', 'FINPIPE', 'FORTIS', 'GRSE', 'GLAXO', 'HAVELLS', 'HINDALCO', 'HAL', 'HUDCO', 'IRFC', 'NAUKRI', 'INDIGO', 'KEI', 'LODHA', 'MAZDOCK', 'NHPC', 'NAM_INDIA', 'PNCINFRA', 'POLYMED', 'RVNL', 'SJVN', 'MOTHERSON', 'SAREGAMA', 'SOBHA', 'SOLARINDS', 'UNOMINDA', 'VGUARD']

def sma20_vol(kite, screened_stocks):
    import pandas as pd
    not_scanned=[]
    Dict={}


    # Get the current date
    to_date = datetime.now().date()

    # Calculate the date 33 days ago
    days_ago = timedelta(days=33)
    from_date = datetime.now().date() - days_ago

    instruments=kite.instruments("NSE")
    df=pd.DataFrame(instruments)
    df.set_index('tradingsymbol', inplace=True)
    interval = "day"  # Can be 'minute', 'day', '3minute', etc.
    for i in screened_stocks:
        try:
            result = df.loc[i]
            instrument_token=result["instrument_token"]
            historical_data = kite.historical_data(instrument_token, from_date, to_date, interval)
            hd_df=pd.DataFrame(historical_data)

            mean_last_20 = hd_df['volume'].tail(20).mean()
            Dict[i]=mean_last_20
    
        except KeyError:
            try:
                i=i.replace("_","&")
                result = df.loc[i]
                instrument_token=result["instrument_token"]
                historical_data = kite.historical_data(instrument_token, from_date, to_date, interval)
                hd_df=pd.DataFrame(historical_data)
                mean_last_20 = hd_df['volume'].tail(20).mean()
                Dict[i]=mean_last_20
            except KeyError:
                try:
                    i=i.replace("&","-")
                    result = df.loc[i]
                    instrument_token=result["instrument_token"]
                    historical_data = kite.historical_data(instrument_token, from_date, to_date, interval)
                    hd_df=pd.DataFrame(historical_data)
                    mean_last_20 = hd_df['volume'].tail(20).mean()
                    Dict[i]=mean_last_20
                except:
                    not_scanned.append(i)




    return Dict,not_scanned




def sma5_vol(kite, screened_stocks):
    import pandas as pd
    not_scanned=[]
    Dict={}
    from datetime import datetime, timedelta

    # Get the current date
    to_date = datetime.now().date()

    # Calculate the date 33 days ago
    days_ago = timedelta(days=10)
    from_date = datetime.now().date() - days_ago

    instruments=kite.instruments("NSE")
    df=pd.DataFrame(instruments)
    df.set_index('tradingsymbol', inplace=True)
    interval = "day"  # Can be 'minute', 'day', '3minute', etc.
    for i in screened_stocks:
        try:
            result = df.loc[i]
            instrument_token=result["instrument_token"]
            historical_data = kite.historical_data(instrument_token, from_date, to_date, interval)
            hd_df=pd.DataFrame(historical_data)

            mean_last_20 = hd_df['volume'].tail(5).mean()
            Dict[i]=mean_last_20
    
        except KeyError:
            try:
                i=i.replace("_","&")
                result = df.loc[i]
                instrument_token=result["instrument_token"]
                historical_data = kite.historical_data(instrument_token, from_date, to_date, interval)
                hd_df=pd.DataFrame(historical_data)
                mean_last_5 = hd_df['volume'].tail(5).mean()
                Dict[i]=mean_last_5
            except KeyError:
                try:
                    i=i.replace("&","-")
                    result = df.loc[i]
                    instrument_token=result["instrument_token"]
                    historical_data = kite.historical_data(instrument_token, from_date, to_date, interval)
                    hd_df=pd.DataFrame(historical_data)
                    mean_last_20 = hd_df['volume'].tail(5).mean()
                    Dict[i]=mean_last_5
                except:
                    not_scanned.append(i)


    return Dict,not_scanned



def sma3(kite, screened_stocks):
    import pandas as pd
    not_scanned=[]
    Dict={}
    from datetime import datetime, timedelta

    # Get the current date
    to_date = datetime.now().date()

    # Calculate the date 33 days ago
    days_ago = timedelta(days=33)
    from_date = datetime.now().date() - days_ago

    instruments=kite.instruments("NSE")
    df=pd.DataFrame(instruments)
    df.set_index('tradingsymbol', inplace=True)
    interval = "day"  # Can be 'minute', 'day', '3minute', etc.
    for i in screened_stocks:
        try:
            result = df.loc[i]
            instrument_token=result["instrument_token"]
            historical_data = kite.historical_data(instrument_token, from_date, to_date, interval)
            hd_df=pd.DataFrame(historical_data)

            mean_last_20 = hd_df['volume'].tail(20).mean()
            mean_last_3 = hd_df['volume'].tail(3).mean()
            dict_temp={}
            
            dict_temp["SMA20"]=mean_last_20
            dict_temp["SMA3"]=mean_last_3


            Dict[i]=dict_temp
    
        except KeyError:
            try:
                i=i.replace("_","&")
                result = df.loc[i]
                instrument_token=result["instrument_token"]
                historical_data = kite.historical_data(instrument_token, from_date, to_date, interval)
                hd_df=pd.DataFrame(historical_data)

                mean_last_20 = hd_df['volume'].tail(20).mean()
                mean_last_5 = hd_df['volume'].tail(3).mean()
                dict_temp={}
                
                dict_temp["SMA20"]=mean_last_20
                dict_temp["SMA3"]=mean_last_3


                Dict[i]=dict_temp
            except KeyError:
                try:
                    i=i.replace("&","-")
                    result = df.loc[i]
                    instrument_token=result["instrument_token"]
                    historical_data = kite.historical_data(instrument_token, from_date, to_date, interval)
                    hd_df=pd.DataFrame(historical_data)

                    mean_last_20 = hd_df['volume'].tail(20).mean()
                    mean_last_3 = hd_df['volume'].tail(3).mean()
                    dict_temp={}
                    
                    dict_temp["SMA20"]=mean_last_20
                    dict_temp["SMA5"]=mean_last_3

                    Dict[i]=dict_temp
                except:
                    not_scanned.append(i)
        temp_dict=Dict[i]



    return Dict,not_scanned




def final_screening_testing(kite,screened_stocks):
    screened_stocks_tv=screened_stocks
    final_screened_stocks=[]
    sma_20_dict=sma20_vol(kite,screened_stocks)[0]
    for i in screened_stocks_tv:
        try:
            daily=get_data(i,"Daily")
            daily_volume=daily["volume"] # type: ignore
            if daily_volume/sma_20_dict[i]>1.25:
                final_screened_stocks.append(i)
        except KeyError as e:
            with open(r"important_data\tv_zerodha_issue.txt") as file:
                problems=eval(file.read())
            if i in problems:
                telegram_send(f"Problem with {i}, exception: {e}")
                problems.append(i)
                with open(r"important_data\tv_zerodha_issue.txt","w") as file:
                    file.write(problems)
            continue


    return final_screened_stocks


def final_screening_bb(kite,stocks):
    band_walking=[]

    to_date = datetime.now().date()
    # Calculate the date 100 days ago
    days_ago = timedelta(days=100)
    from_date = datetime.now().date() - days_ago
    instruments=kite.instruments("NSE")
    df=pd.DataFrame(instruments)
    df_i=df.copy()

    df_i.set_index('tradingsymbol', inplace=True)
    interval = "day"  # Can be 'minute', 'day', '3minute', etc.
    for i in stocks:
        try:
            result = df_i.loc[i]
            instrument_token=result["instrument_token"]
            historical_data = kite.historical_data(instrument_token, from_date, to_date, interval)
            df=pd.DataFrame(historical_data)


            # Calculate Bollinger Bands
            bb_indicator = ta.volatility.BollingerBands(close=df['close'], window=20, window_dev=2) # type: ignore
            df['bb_upper'] = bb_indicator.bollinger_hband()
            df['bb_middle'] = bb_indicator.bollinger_mavg()
            df['bb_lower'] = bb_indicator.bollinger_lband()

            # Define a threshold for "band walking" (e.g., price within 3% of upper band)
            band_walk_threshold = 0.03

            # Check if the close price is within the threshold of the upper Bollinger Band
            df['band_walking'] = (df['close'] >= df['bb_upper'] * (1 - band_walk_threshold))

            if df['band_walking'].iloc[-2:].all():
                band_walking.append(i)
        except:
            print(f"{i} not scanned")
    return band_walking



def final_screening(kite):
    screened_stocks,not_screened_stocks=screening()
    with open(r"logs\unscreened_stocks.txt",'a+') as file:
        data= f"{datetime.now()} : {not_screened_stocks}\n"
        file.write(data)
    # final_screened_stocks=final_screening_testing(kite,screened_stocks=screened_stocks)
    final_screened_stocks_after_bb=final_screening_bb(kite=kite,stocks=screened_stocks)

    print(f"final_screened_stocks: {final_screened_stocks_after_bb}")
    return final_screened_stocks_after_bb




# screened_stocks,not_screened_stocks=screening()
# with open(r"logs\unscreened_stocks.txt",'a+') as file:
#     data= f"{datetime.now()} : {not_screened_stocks}\n"
#     file.write(data)

# print(screened_stocks)
# print(final_screening_testing(kite,screened_stocks=screened_stocks))

