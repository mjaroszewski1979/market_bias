import talib
import numpy as np
import pandas_datareader as pdr
import pandas as pd

spy = pdr.get_data_yahoo('^GSPC')
spy.drop(['Volume', 'Close'], axis = 1, inplace=True) 
o = spy['Open']
h = spy['High']
l = spy['Low']
c = spy['Adj Close']
cp = spy['Adj Close'][-1]
t = 200


# Trend filter #
adx = talib.ADX(h, l, c, 14)
adx = adx[-1]

# Indicators #
upperband, middleband, lowerband = talib.BBANDS(c, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
bblow = lowerband
dema = talib.DEMA(c, t)
ema = talib.EMA(c, t)
ht = talib.HT_TRENDLINE(c)
kama = talib.KAMA(c, t)
mama, fama = talib.MAMA(c, fastlimit=0.5, slowlimit=0.05)
sar = talib.SAR(h, l, acceleration=0.020, maximum=0.2)
sma = talib.SMA(c, t)
t3 = talib.T3(c, t, vfactor=0.7)
wma = talib.WMA(c, t)
trima = talib.TRIMA(c, t)

indis = [bblow, dema, ema, ht, kama, fama, sar, sma, t3, trima, wma]
res_i = []
for x in indis:
    res_i.append(x[-1])
id_i = ['Bollinger Bands', 'Double Exponential Moving Average', 'Exponential Moving Average','Hilbert Transform - Instantaneous Trendline', 'Kaufman Adaptive Moving Average',
'MESA Adaptive Moving Average', 'Parabolic SAR', 'Simple Moving Average', 'Triple Exponential Moving Average', 'Triangular Moving Average', 'Weighted Moving Average']
val_i = []
for _ in range(len(res_i)):
    val_i.append(cp)
num_i = range(len(res_i))

# Oscillators #
cci = talib.CCI(h, l, c, t)
macd, macdsignal, macdhist = talib.MACD(c, fastperiod=12, slowperiod=26, signalperiod=9)
macd = macdhist
mom = talib.MOM(c, t)
roc = talib.ROC(c, t)
rsi = talib.RSI(c, 100)
slowk, slowd = talib.STOCH(h, l, c, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
stoch = slowd
willr = talib.WILLR(h, l, c, 14)

oscs = [cci, macd, mom, roc, rsi, stoch, willr]
res_o = []
for y in oscs:
    res_o.append(y[-1])
id_o = ['Commodity Channel Index', 'MACD', 'Momentum', 'Rate of Change', 'Relative Strength Index', 'Stochastic', "Williams' %R"]
val_o = [0, 0, 100, 0, 50, 50, -50]
num_o = range(len(res_o))

# Patterns #
baby = talib.CDLABANDONEDBABY(o, h, l, c, penetration=0)
belt = talib.CDLBELTHOLD(o, h, l, c)
b_away = talib.CDLBREAKAWAY(o, h, l, c)
closing = talib.CDLCLOSINGMARUBOZU(o, h, l, c)
counter = talib.CDLCOUNTERATTACK(o, h, l, c)
dragon = talib.CDLDRAGONFLYDOJI(o, h, l, c)
engulfing = talib.CDLENGULFING(o, h, l, c)
gap = talib.CDLGAPSIDESIDEWHITE(o, h, l, c)
hammer = talib.CDLHAMMER(o, h, l, c)
harami = talib.CDLHARAMI(o, h, l, c)
har_cross = talib.CDLHARAMICROSS(o, h, l, c)
hikkake = talib.CDLHIKKAKE(o, h, l, c)
inside_up = talib.CDL3INSIDE(o, h, l, c)
kick = talib.CDLKICKING(o, h, l, c)
ladder = talib.CDLLADDERBOTTOM(o, h, l, c)
long_line = talib.CDLLONGLINE(o, h, l, c)
ma_low = talib.CDLMATCHINGLOW(o, h, l, c)
mat_hold = talib.CDLMATHOLD(o, h, l, c)
marubozu = talib.CDLMARUBOZU(o, h, l, c)
mor_doji = talib.CDLMORNINGDOJISTAR(o, h, l, c)
mor_star = talib.CDLMORNINGSTAR(o, h, l, c)
outside_up = talib.CDL3OUTSIDE(o, h, l, c)
piercing = talib.CDLPIERCING(o, h, l, c)
pigeon = talib.CDLHOMINGPIGEON(o, h, l, c)
river = talib.CDLUNIQUE3RIVER(o, h, l, c)
sep_lines = talib.CDLSEPARATINGLINES(o, h, l, c)
soldiers = talib.CDL3WHITESOLDIERS(o, h, l, c)
south = talib.CDL3STARSINSOUTH(o, h, l, c)
stick = talib.CDLSTICKSANDWICH(o, h, l, c)
swallow = talib.CDLCONCEALBABYSWALL(o, h, l, c)
takuri = talib.CDLTAKURI(o, h, l, c)
tasuki = talib.CDLTASUKIGAP(o, h, l, c)
three_met = talib.CDLRISEFALL3METHODS(o, h, l, c)
tlstrike = talib.CDL3LINESTRIKE(o, h, l, c)
tristar = talib.CDLTRISTAR(o, h, l, c)
u_gap = talib.CDLXSIDEGAP3METHODS(o, h, l, c)

patts = [baby, belt, b_away, closing, swallow, counter, dragon, engulfing, gap, hammer, harami, har_cross, hikkake, pigeon, kick, ladder, long_line, marubozu, ma_low, mat_hold,
mor_doji, mor_star, piercing, three_met, sep_lines, stick, takuri, tasuki, inside_up, tlstrike, south, soldiers, outside_up, tristar, river, u_gap]

res_p = []
for z in patts:
    res_p.append(z[-1])
id_p = ['Abandoned Baby', 'Belt-hold', 'Breakaway', 'Closing Marubozu', 'Concealing Baby Swallow', 'Counterattack', 'Dragonfly Doji', 'Engulfing Pattern', 'Up-gap Side-by-Side White Lines',
'Hammer', 'Harami', 'Harami Cross', 'Hikkake', 'Homing Pigeon', 'Kicking', 'Ladder Bottom', 'Long Line', 'Marubozu', 'Matching Low', 'Mat Hold', 'Morning Doji Star', 'Morning Star',
'Piercing', 'Rising Three Methods', 'Separating Lines', 'Stick Sandwich', 'Takuri', 'Tasuki Gap', 'Three Inside Up', 'Three-Line Strike', 'Three Stars In The South',
'Three Advancing White Soldiers', 'Three Outside Up/Down','Tristar', 'Unique 3 River', 'Upside Gap Three Methods']
num_p = range(len(res_p))
