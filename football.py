# coding: utf-8
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np
# 输入数据
data = pd.read_csv('footballdata.csv', encoding='gbk')
train_x = data[["2019年国际排名", "2018世界杯", "2015亚洲杯"]]
print(train_x)
df = pd.DataFrame(train_x)
print(df)
# kmeans = KMeans(n_clusters=3)

kmeans = KMeans(n_clusters=5)
# 规范化到 [0,1] 空间
# min_max_scaler = preprocessing.MinMaxScaler()
# train_x = min_max_scaler.fit_transform(train_x)

ss = preprocessing.StandardScaler()
train_x = ss.fit_transform(train_x)
# kmeans 算法
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
print(predict_y)
# 合并聚类结果，插入到原数据中
result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
result.rename({0: u'聚类'}, axis=1, inplace=True)
print(result)
