from nsepython import *
import datetime
from datetime import date
import pandas
import pandas_datareader.data as web
import datetime

def collect_data(stock):
    symbol = stock
    print(symbol)
    series = ".NS"
    start = datetime.datetime(2000,1,1)
    end = date.today()
    global df
    df = web.DataReader(str(symbol)+'.NS','yahoo',start,end)
    df  = df.sort_values(by=['Date'])
    df['Date'] = df.index
    ohlc_dict = {                                                                                                             
    'Open':'first',                                                                                                    
    'High':'max',                                                                                                       
    'Low':'min',                                                                                                        
    'Close': 'last'                                                                                                   
    }
    df = df.loc[:,['Open','High','Low','Close']]
    df = df.resample('1M').apply(ohlc_dict)
    df['New_High'] = ''
    for i in range(len(df)):
        if i == 0:
            df['New_High'].iloc[i] = 'NEW HIGH'
            highest = df['High'][i]
        else:
            if df['High'][i]>highest:
                df['New_High'].iloc[i] = 'NEW HIGH'
                highest = df['High'][i]
               
    df.to_csv(str(stock)+'.csv')
    return df


stocks_list = input('Enter the stocks list\nEnter:')
stocks_list = stocks_list.split(",")
for i in range(len(stocks_list)):
    stock = stocks_list[i]
    try:
        collect_data(stock)
    except Exception as e:
        print("something is wrong with this stock")
        print(e)
        
