from sklearn import tree
import sys
import os
import graphviz
import numpy as np
os.environ["PATH"] += os.pathsep+'C:/Program Files (x86)/Graphviz2.38/bin'

# 创建数据[红，大]，1==是，0==否
data = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
# 数据标注为，1==好苹果，0==坏苹果
target = np.array([1, 1, 0, 0])

clf = tree.DecisionTreeClassifier() # 创建决策树分类器模型
clf = clf.fit(data, target)  # 拟合数据

# 最后利用graphviz库打印出决策树图
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("tree")# 在同目录下生成tree.pdf
