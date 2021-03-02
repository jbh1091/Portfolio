#Goal: Find Buy/Sell patterns in stock prices using autocorrelation

#Step 1: load pandas, scipy, numpy, and matplotlib
import pandas as pd 
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt 

#Step 2: Define symbols of interest (here, airlines)
# - data acquired via csv files from yahoo finance
symbols = ["AAL", "ALK", "DAL", "JBLU", "LUV", "SAVE", "UAL"]

#Step 3: Extract data
basefolder = "C:/Users/jbh10/Documents/GitHub/Portfolio/StockOscillations/"
i = 0;
NormAC_Array = np.zeros((253, 7))
for symbol in symbols:
    filepath = basefolder + symbol + ".csv"
    df = pd.read_csv(filepath, header=0, index_col=0)
    df = df.rename(columns={"Adj Close": "AdjClose"})
    tempAC = df.AdjClose.to_numpy(copy=True)
    tempNorm = tempAC/tempAC[0]
    
    NormAC_Array[:,i] = tempNorm.copy()
    i = i + 1

#Plot return vs baseline
plt.plot(NormAC_Array)
plt.legend(symbols)
plt.xlabel('Day')
plt.ylabel('Normalized Change')
plt.title('Share price')
plt.show()

#Plot performance relative to sector

#corr = signal.correlate(NormAC,NormAC)
#lags = signal.correlation_lags(len(NormAC),len(NormAC))
#plt.plot(lags,corr)
#plt.xlabel('Lag (Days)')
#plt.title('DAL AutoCorrelation')