#Standard

import numpy as np

import pandas as pd

from numpy.random import randn

from pandas import Series, DataFrame

#Stats

from scipy import stats

#Matplotlib

import matplotlib as mpl

import matplotlib.pyplot as plt

#Seaborn

import seaborn as sns

#Draw

sns.set() #設定繪圖改為seaborn繪製

df = sns.load_dataset("tips")

sns.scatterplot(data=df, x="total_bill", y="tip", hue="size", size="size", sizes=(5, 500), legend="full")

plt.xlabel('this is x')

plt.ylabel('this is y')

plt.title('this is a demo')

plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0) #bbox_to_anchor(1, 1)是圖的右上方點，這裡表示圖例要在圖的那個位置，borderaxespad預設是0.5，這是表示基於bbox_to_anchor再位移多少

plt.tight_layout() #使子圖合適的跟圖形匹配。如果未呼叫 tight_layout()，則圖例框將被裁剪。

plt.show() #繪圖