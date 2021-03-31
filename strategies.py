import numpy as np
import pandas_datareader as pdr
import datetime

start = datetime.datetime(2020, 1, 1)
end = datetime.datetime.now()
stocks = ['^GSPC', '^IXIC', '^DJI', '^N225', '^FCHI', '^GDAXI', '^RUT', 'EPOL', 'EWC', 'TUR', '^NSEI', 'MCHI', 'EWY', 'EWT', 'EWZ', 'EWA', 'EWW', 'EWL', 'EWN', 'EZA', 'EWU']
data = pdr.get_data_yahoo(stocks, start, end)
data = data[['Adj Close']].pct_change(periods=252) * 100
data = round(data, 2)
data = data[['Adj Close']]
data = data.dropna()

sp500 = data['Adj Close']['^GSPC'][-1]
nasdq = data['Adj Close']['^IXIC'][-1]
dow = data['Adj Close']['^DJI'][-1]
nikkei = data['Adj Close']['^N225'][-1]
cac40 = data['Adj Close']['^FCHI'][-1]
dax = data['Adj Close']['^GDAXI'][-1]
russ = data['Adj Close']['^RUT'][-1]
pol = data['Adj Close']['EPOL'][-1]
can = data['Adj Close']['EWC'][-1]
tur = data['Adj Close']['TUR'][-1]
ind = data['Adj Close']['^NSEI'][-1]
chi = data['Adj Close']['MCHI'][-1]
kor = data['Adj Close']['EWY'][-1]
taiw = data['Adj Close']['EWT'][-1]
braz = data['Adj Close']['EWZ'][-1]
aus = data['Adj Close']['EWA'][-1]
mex = data['Adj Close']['EWW'][-1]
swi = data['Adj Close']['EWL'][-1]
net = data['Adj Close']['EWN'][-1]
safr = data['Adj Close']['EZA'][-1]
uk = data['Adj Close']['EWU'][-1]

indices = {
    'US/S&P 500' : sp500,
    'US/NASDAQ' : nasdq,
    'US/DOW JONES' : dow,
    'JAPAN/NIKKEI' : nikkei,
    'FRANCE/CAC 40' : cac40,
    'GERMANY/DAX' : dax,
    'US/RUSSELL 2000' : russ,
    'POLAND/MSCI' : pol,
    'CANADA/MSCI' : can,
    'TURKEY/MSCI' : tur,
    'INDIA/NIFTY' : ind,
    'CHINA/MSCI' : chi,
    'SOUTH KOREA/MSCI' : kor,
    'TAIWAN/MSCI' : taiw,
    'BRAZIL/MSCI' : braz,
    'AUSTRALIA/MSCI' : aus,
    'MEXICO/MSCI' : mex,
    'SWITZERLAND/MSCI' : swi,
    'NETHERLANDS/MSCI' : net,
    'SOUTH AFRICA/MSCI' : safr,
    'UK/MSCI' : uk
}

top_index = sorted([(v, k) for k, v in indices.items()], reverse=True)
nums = range(21)