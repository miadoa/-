# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:17:12 2018

@author: miadoa
@e-mail:hagezi@qq.com

"""

from scipy.cluster import hierarchy
import pandas as pd
from pylab import mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['SimHei']

def get_data(file):
    df = pd.read_csv(file, encoding='gbk', index_col=0)
    df.fillna(0, inplace=True)
    
    return df

def cluster(df):
    Z = hierarchy.linkage(df, method ='ward',metric='euclidean')
    plt.figure(figsize=(14,6))
    return hierarchy.dendrogram(Z,labels = df.index)
    
df = get_data('jx.csv')
cluster(df)
plt.savefig('image.jpg', dpi=300)