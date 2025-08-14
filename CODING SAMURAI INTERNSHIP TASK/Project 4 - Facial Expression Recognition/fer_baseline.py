#!/usr/bin/env python3
import pandas as pd, numpy as np
from PIL import Image
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

meta = pd.read_csv("data/labels.csv")
X,y=[],[]
for _,r in meta.iterrows():
    img = Image.open(r['file']).convert('L')
    X.append(np.array(img).flatten())
    y.append(r['label'])
X = np.array(X)/255.0
Xtr,Xte,ytr,yte = train_test_split(X,y,test_size=0.2)
clf = LogisticRegression(max_iter=500).fit(Xtr,ytr)
print("Score:", clf.score(Xte,yte))
