#%% Importing Libraries
import pandas as pd  #
import matplotlib.pyplot as plt
import yfinance as yf

#%%
Data_SP = pd.read_excel('SP500ReturnData.xlsx')
Data_SP['Date'] = Data_SP['Year'].apply(str)+'-'+Data_SP["Month"].apply(str)+"-"+str(1)
Data_SP['Date'] = pd.to_datetime(Data_SP['Date']).dt.date



#%%
start = "2016-01-01"
end = "2020-12-31"
Apple = yf.download('AAPL',start,end)


#%%
Apple.to_excel(r'C:\Users\Abdul Basit Aftab\Desktop\Freelance WorK\NewerOnes\RefShazz-DataAnalyticsStocksPrice\AppleStocks.xlsx', index = False)

#%% Time Series Plots of Opening Prices
plt.figure()
Apple['Open'].plot(label = 'Apple', figsize = (15,7))
plt.ylabel("Apple Stocks: Opening Prices")
plt.title('Stock Prices of Apple')

#%% Times Series Plots of Total Volume Traded
plt.figure()
Apple['Volume'].plot(label = 'Apple', figsize = (15,7))
plt.ylabel("Volume")
plt.title('Volume of Stock Traded')

#%% Market Capitalization
Apple['MarketCap'] = Apple['Open'] * Apple['Volume']
plt.figure()
Apple['MarketCap'].plot(label = 'Apple', figsize = (15,7))
plt.ylabel("MarketCap")
plt.title('MarketCap')

#%% Moving Averages of 50 Days and 200 Days
Apple['MA50'] = Apple['Open'].rolling(50).mean()
Apple['MA200'] = Apple['Open'].rolling(200).mean()
plt.figure()
Apple['Open'].plot(label = 'Apple', figsize = (15,7))
Apple['MA50'].plot()
Apple['MA200'].plot()
plt.legend()


#%% Percentage Stock Returns
Apple['returns'] = (Apple['Close']/Apple['Close'].shift(1)) -1


#%% Apple Stocks Returns Graph
plt.figure()
Apple['returns'].plot()
plt.xlabel("Date")
plt.ylabel("Return %")
plt.title("Apple Stock Returns %")


#%% Market Returns
plt.figure()
plt.plot(Data_SP['Date'],Data_SP['Return'],label="Market Returns")
plt.xlabel("Date")
plt.ylabel("Return %")
plt.title("Market Returns %")


#%% Both Graphs on The same figure
plt.figure()
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.plot(Apple['returns'],label="Apple Stocks Returns")
plt.plot(Data_SP['Date'],Data_SP['Return'],label="Market Returns")
plt.legend()
plt.xlabel("Date")
plt.ylabel("Return %")
plt.title("Returns of Apple Stocks Compared to Market Return")



#%%
plt.figure()
Apple['returns'].hist(bins = 100, label = 'Apple', alpha = 0.5, figsize = (15,7))
Data_SP['Return'].hist(bins = 100, label = 'Market Returns', alpha = 0.5)
plt.legend()
plt.title("Volatility")

