import pandas as pd

def get_nifty_500_stocks():
    try:
        # Path to the locally saved CSV file
        csv_file_path = r"C:\Users\DELL\Downloads\EQUITY_L.csv"
        # Read the CSV file
        nifty_500 = pd.read_csv(csv_file_path)
        # Extract the symbol column
        return nifty_500['SYMBOL'].tolist()
    except Exception as e:
        print("An error occurred:", e)
        return []

nifty_500_stocks = get_nifty_500_stocks()
print(nifty_500_stocks)
print(len(nifty_500_stocks))