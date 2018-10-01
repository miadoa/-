import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
计算相关性系数和P值
"""
#df3=df [df['average']!=0] [['average','sum','entropy']]
#df4=df.iloc[:,9:22]
#df4['average']=df['average']
#df4['sum']=df['sum']
#df4['entropy']=df['entropy']
#df4=df4[df4['average']!=0]
#x=df4['average']
#y=df4['entropy']
#z=df4['sum']
#corr=df4.corr()
#pearsonr=stats.pearsonr(x,y)
#pearsonr2=stats.pearsonr(x,z)
#print(pearsonr)
#print(pearsonr2)
#print(pearsonr[1]<0.01)
#print(pearsonr2[1]<0.01)
#corr.to_excel('cor_drop_1000.xlsx')

"""
绘制散点图
"""
def plot_scatter():
    fig_scatter=plt.figure(figsize=(8,4))
    df_plot=df[df['average']>0][['average','公司企']]
    fig_q1_1 = plt.figure(figsize = (8,4))
    plt.scatter(df_plot['average'],df_plot['公司企'])
    plt.show()

if __name__=='__main__':
    df=pd.read_excel('sum_drop_1000_TableToExcel.xls')
    plot_scatter()










