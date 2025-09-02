import yfinance as yf

ticker = 'AAPL'
print(f"Getting stock data for {ticker}...")

stock_data = yf.download(ticker, period="1y", auto_adjust=True, progress=False)

if stock_data is None or stock_data.empty:
    print(f"Error: Could not retrieve data for {ticker}")
    exit(1)

# Show the last 5 days of data
print(f"\nLast 5 days of data for {ticker}:")
recent_data = stock_data.tail(5)
print(recent_data)

latest_price = stock_data['Close'].iloc[-1].item() # .iloc[-1] is used for getting the last element
yesterday_price = stock_data['Close'].iloc[-2].item() # .iloc[-2] is used for getting the second to last element

print(f"\nLatest closing price: ${latest_price:.2f}") # :.2f formats the float to 2 decimal places

# Calculate daily change
daily_change = latest_price - yesterday_price
change_percent = (daily_change / yesterday_price) * 100

print(f"Daily change: ${daily_change:.2f} ({change_percent:+.2f}%)") 

if daily_change > 0:
    print("Stock went up today")
elif daily_change < 0:
    print("Stock went down today")
else:
    print("Stock stayed the same today")