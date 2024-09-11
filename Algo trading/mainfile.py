from kite_trade import *
from Screener import *
from exitpolicy import *
from entrypolicy import *
from testing import *
import time
import multiprocessing as mp #https://www.youtube.com/watch?v=GT10PnUFLlE
from multiprocessing import Process, Queue
import schedule #https://www.geeksforgeeks.org/python-schedule-library/
from final_workflow import *
import datetime

def setup():
    """
    This function runs only once.
    """
    try:
        global kite
        kite = kite_login()
        get_instruments_dataframe(kite=kite)
    except requests.exceptions.ConnectionError:
        print("Internet connection lost.")
        internet_check_and_fix()



def is_market_open_wrapper(market_open):
    """
    Wrapper function to run the market status check in a separate process.
    Continuously checks and updates the market status.
    """
    from datetime import datetime, time

    # Define market opening and closing times
    market_open_time = time(9, 15)
    market_close_time = time(15, 30)
    
    # Get the current time
    current_time = datetime.now().time()
    if market_open_time <= current_time <= market_close_time:
        market_open.value=is_market_open()
    else:
        market_open.value=False

    # market_open.value=True





def buy_wrapper(kite, market_open):
    """
    Wrapper to handle buy operations with market status check.
    """
    while True:
        try:
            if market_open.value:
                print("Buy operation active")
                while True:
                    buy(kite)
                    time.sleep(300)
            else:
                print("Market is closed, buy operation paused.")
            time.sleep(5)  # Check every 300 seconds
        except requests.exceptions.RequestException:
            print("Internet connection lost during buy operation.")
            internet_check_and_fix()

def sell_wrapper(kite, market_open):
    """
    Wrapper to handle sell operations with market status check.
    """
    while True:
        try:
            if market_open.value:
                print("Sell operation active")
                sell(kite)
            else:
                print("Market is closed, sell operation paused.")
            time.sleep(5)  # Check every 60 seconds
        except requests.exceptions.RequestException:
            print("Internet connection lost during sell operation.")
            internet_check_and_fix()

def main():
    # Setup and initialization
    setup()

    # Shared variable for inter-process communication
    market_open = mp.Value('b', False)

    # Create and start the market status process
    market_process = mp.Process(target=is_market_open_wrapper, args=(market_open,))
    market_process.start()

    # Wait until the market is open before starting buy and sell processes
    while not market_open.value:

        # Get the current time as a struct_time object
        current_time = time.localtime()

        # Format the current time as HH:MM:SS
        formatted_time = time.strftime("%H:%M:%S", current_time)


        print(f"\rWaiting for the market to open... {formatted_time} ", end='',flush=True)
        time.sleep(30)

    # Create and start buy and sell processes
    buy_process = mp.Process(target=buy_wrapper, args=(kite, market_open))
    sell_process = mp.Process(target=sell_wrapper, args=(kite, market_open))
    
    buy_process.start()
    sell_process.start()

    # Join processes
    market_process.join()
    buy_process.join()
    sell_process.join()

if __name__ == "__main__":
    main()
