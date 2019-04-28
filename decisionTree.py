
from sklearn import tree
import graphviz
import os

os.environ["PATH"] += os.pathsep+'C:/Program Files (x86)/Graphviz2.38/bin'
'''
import numpy as np
# 创建数据[红，大]，1==是，0==否
data = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
# 数据标注为，1==好苹果，0==坏苹果
target = np.array([1, 1, 0, 0])

clf = tree.DecisionTreeClassifier()  # 创建决策树分类器模型
clf = clf.fit(data, target)  # 拟合数据

# 最后利用graphviz库打印出决策树图
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("tree")  # 在同目录下生成tree.pdf
'''

'''
这里我们使用 Seaborn 中自带的 iris 数据集，这个数据集也叫鸢尾花数据集。鸢尾花可以分成 Setosa、Versicolour 和 Virginica 
三个品种，在这个数据集中，针对每一个品种，都有 50 个数据，每个数据中包括了 4 个属性，分别是花萼长度、花萼宽度、花瓣长度
和花瓣宽度。通过这些数据，需要你来预测鸢尾花卉属于三个品种中的哪一种。CART 只支持二叉树,X[3] <= 0.75,这个0.75的选择最简
单的实现就是遍历，选择基尼系数最小的一个数值。
'''

# encoding=utf-8
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris


# 准备数据集
iris = load_iris()
print("iris")
print(iris)
'''
# 获取特征集和分类标识
features = iris.data
print("features")
print(features)
labels = iris.target
print("labels")
print(labels)
# 随机抽取 33% 的数据作为测试集，其余为训练集
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33,
                                                                            random_state=0)
print("train_features")
print(train_features)
print("test_features")
print(test_features)
print(test_features.size)
print("train_labels")
print(train_labels)
print("test_labels")
print(test_labels)

# 创建 CART 分类树
clf = DecisionTreeClassifier(criterion='gini')
# 拟合构造 CART 分类树
clf = clf.fit(train_features, train_labels)
# 用 CART 分类树做预测
test_predict = clf.predict(test_features)
# 预测结果与测试集结果作比对
score = accuracy_score(test_labels, test_predict)
print("CART 分类树准确率 %.4lf" % score)
# 最后利用graphviz库打印出决策树图


dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris_tree")  # 在同目录下生成iris_tree.pdf
'''

'''

CRIM：城镇人均犯罪率。

ZN：住宅用地超过 25000 sq.ft. 的比例。

INDUS：城镇非零售商用土地的比例。

CHAS：查理斯河空变量（如果边界是河流，则为1；否则为0）。

NOX：一氧化氮浓度。

RM：住宅平均房间数。

AGE：1940 年之前建成的自用房屋比例。

DIS：到波士顿五个中心区域的加权距离。

RAD：辐射性公路的接近指数。

TAX：每 10000 美元的全值财产税率。

PTRATIO：城镇师生比例。

B：1000（Bk-0.63）^ 2，其中 Bk 指代城镇中黑人的比例。

LSTAT：人口中地位低下者的比例。

MEDV：自住房的平均房价，以千美元计。


预测平均值的基准性能的均方根误差（RMSE）是约 9.21 千美元。
'''

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.datasets import load_digits
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.tree import DecisionTreeRegressor
# 准备数据集
boston = load_boston()
print(boston)
# 探索数据
print(boston.feature_names)
# 获取特征集和房价
features = boston.data
prices = boston.target
# 随机抽取 33% 的数据作为测试集，其余为训练集
train_features, test_features, train_price, test_price = train_test_split(features, prices, test_size=0.33)
# 创建 CART 回归树
dtr = DecisionTreeRegressor()
# 拟合构造 CART 回归树
dtr.fit(train_features, train_price)
# 预测测试集中的房价
predict_price = dtr.predict(test_features)
print("boston_predict_price")
print(predict_price)
# 测试集的结果评价
print('回归树二乘偏差均值:', mean_squared_error(test_price, predict_price))
print('回归树绝对值偏差均值:', mean_absolute_error(test_price, predict_price))

# 准备数据集
digits = load_digits()
print("digits")
print(digits)
# 获取特征集和分类标识
features = digits.data
print("features")
print(features)
labels = digits.target
print("labels")
print(labels)
# 随机抽取 33% 的数据作为测试集，其余为训练集
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33,
                                                                            random_state=0)
# 创建 CART 分类树
clf = DecisionTreeClassifier(criterion='gini')
# 拟合构造 CART 分类树
clf = clf.fit(train_features, train_labels)
# 用 CART 分类树做预测
test_predict = clf.predict(test_features)
# 预测结果与测试集结果作比对
score = accuracy_score(test_labels, test_predict)
print("CART 分类树准确率 %.4lf" % score)
# 最后利用graphviz库打印出决策树图

dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.view()

