from sklearn import preprocessing
import numpy as np

# 初始化数据，每一行表示一个样本，每一列表示一个特征
x = np.array([[0., -3.,  1.],
              [3.,  1.,  2.],
              [0.,  1., -1.]])
# 将数据进行 [0,1] 规范化
min_max_scaler = preprocessing.MinMaxScaler()
minmax_x = min_max_scaler.fit_transform(x)
print(minmax_x)  # 列是同一个指标才有比较的意义


# 初始化数据
x = np.array([[0., -3.,  1.],
              [3.,  1.,  2.],
              [0.,  1., -1.]])
# 将数据进行 Z-Score 规范化
scaled_x = preprocessing.scale(x)
print(scaled_x)


# 初始化数据
x = np.array([[0., -3.,  1.],
              [3.,  1.,  2.],
              [0.,  1., -1.]])
# 小数定标规范化
j = np.ceil(np.log10(np.max(abs(x))))
print(np.max(abs(x)))
print(np.log10(np.max(abs(x))))
scaled_x = x/(10**j)
print(scaled_x)

income = np.array([[5000, -3.,  1.],
              [16000,  1.,  2.],
              [58000,  1., -1.]])
# 将数据进行 [0,1] 规范化
minmax_x = min_max_scaler.fit_transform(income)
print(minmax_x)  # 列是同一个指标才有比较的意义