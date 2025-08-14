#!/usr/bin/env python3
import pandas as pd, numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("data/stock.csv",parse_dates=["date"])
df['t'] = (df['date']-df['date'].min()).dt.days
X = df[['t']]
y = df['close']
Xtr,Xte,ytr,yte = train_test_split(X,y,shuffle=False,test_size=0.2)
m = LinearRegression().fit(Xtr,ytr)
pred = m.predict(Xte)
print("MAE:", mean_absolute_error(yte,pred))
