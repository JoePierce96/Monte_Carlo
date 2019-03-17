# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 21:10:59 2019

@author: Joe
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
ibm_data = pd.read_csv('IBMtimeseries.csv')

prices = ibm_data['close']
StockReturns = prices[:-1].values / prices[1:] - 1

#random walk of IBM returns

mu = np.mean(StockReturns)
vol = np.std(StockReturns)
T = 252
S0 = 10
rand_rets = np.random.normal(mu, vol, T) + 1
forecasted_values = S0*(rand_rets).cumprod()
plt.plot(forecasted_values)
#Monte Carlo

for i in range(100):
    rand_rets = np.random.normal(mu, vol, T) + 1
    forecasted_values = S0*(rand_rets).cumprod()
    plt.plot(range(T), forecasted_values)
plt.show

#VaR(99)
sim_returns = []
for i in range(100):
    rand_rets2 = np.random.normal(mu, vol, T)
    sim_returns.append(rand_rets2)
var_99 = np.percentile(sim_returns, 1)
print("Parametric VaR(99): ", round(100*var_99, 2), "%")