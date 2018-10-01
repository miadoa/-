import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#写入文件
df=pd.read_excel('image.xls')
df.index=df['fid']
df=df.drop('fid',axis=1)


#数据清洗


#相关性分析
corr=df.corr()
corr.to_excel('城市意象相关性.xlsx')

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(14, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
#ax.set_xticklabels(corr.index,rotation=90)
ax.set_yticklabels(ax.get_yticklabels(),rotation=45)
ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
plt.yticks(rotation=450)

sns.heatmap(corr,mask=mask,cmap=cmap,vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

plt.show()
