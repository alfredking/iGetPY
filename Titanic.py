import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
# 数据加载
train_data = pd.read_csv('./Titanic_Data/train.csv')
test_data = pd.read_csv('./Titanic_Data/test.csv')
# 数据探索
print(train_data.info())
print('-'*30)
print(train_data.describe())
print('-'*30)
print(train_data.describe(include=['O']))
print('-'*30)
print(train_data.head())
print('-'*30)
print(train_data.tail())

# 使用平均年龄来填充年龄中的 nan 值
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)
# 使用票价的均值填充票价中的 nan 值
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(), inplace=True)

print(train_data['Embarked'].value_counts())
# 使用登录最多的港口来填充登录港口的 nan 值
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)

# 特征选择
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]


dvec = DictVectorizer(sparse=False)
print("show train_features dvec.fit_transform")
print(train_features)
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
print(train_features)
print(dvec.feature_names_)

# 构造 ID3 决策树
clf = DecisionTreeClassifier(criterion='entropy')
# 决策树训练
clf.fit(train_features, train_labels)

# fit_transform()干了两件事：fit找到数据转换规则，并将数据标准化
# transform()可以直接把转换规则拿来用，所以并不需要fit_transform()，否则，两次标准化后的数据格式就不一样了
print("show test_features vdvec.transform")
print(test_features)
test_features = dvec.transform(test_features.to_dict(orient='record'))
print(test_features)
# 决策树预测
pred_labels = clf.predict(test_features)


# AdaBoost 分类器
dt_stump = DecisionTreeClassifier(max_depth=1, min_samples_leaf=1)
ada = AdaBoostClassifier(base_estimator=dt_stump, n_estimators=200)
ada.fit(train_features, train_labels)
# AdaBoost 分类器准确率更高
print(u'AdaBoost 分类器准确率为 %.4lf' % np.mean(cross_val_score(ada, train_features, train_labels, cv=10)))

# 得到决策树准确率
acc_decision_tree = round(clf.score(train_features, train_labels), 6)
print(u'score 准确率为 %.4lf' % acc_decision_tree)


# 使用 K 折交叉验证 统计决策树准确率
print(u'cross_val_score 准确率为 %.4lf' % np.mean(cross_val_score(clf, train_features, train_labels, cv=10)))
