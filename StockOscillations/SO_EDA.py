#Goal: Find Buy/Sell patterns in stock prices using crosscorrelation

#Step 1: load packages
import pandas as pd 
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt 
import seaborn as sns

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

AC_df = pd.DataFrame(NormAC_Array, columns = symbols)

#Plot return vs baseline
f1 = plt.plot(NormAC_Array)
plt.legend(symbols)
plt.xlabel('Day')
plt.ylabel('Normalized Change')
plt.title('Share price')
plt.show(f1)

# AAL and LUV have lowest 0-lag correlation and are therefore more likely than
# other pairs to show potential prediction
corr = signal.correlate(AC_df.AAL,AC_df.LUV)
lags = signal.correlation_lags(len(AC_df.AAL),len(AC_df.LUV))
f2  = plt.plot(lags,corr)
plt.xlabel('Lag (Days)')
plt.title('AAL-LUV X-correlation')
plt.show(f2)

#Plot correlation heatmap
sns.heatmap(AC_df.corr())

#Peak correlation is at 0, so it looks like daily close prices in airlines are 
#not predictive of each other. Given how advanced HFT firms are, there may be
#predictive effects at very short time frames. Retail investors probably
#can't compete on that level though.
