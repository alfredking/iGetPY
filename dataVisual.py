import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties

'''
# 数据准备
N = 1000
x = np.random.randn(N)

print(x)
y = np.random.randn(N)
print("np.random.randn(N)")
print(y)
# 用 Matplotlib 画散点图
plt.scatter(x, y, marker='x')
plt.show()

plt.scatter(x, y, marker='>')
plt.show()

plt.scatter(x, y, marker='o')
plt.show()
# 用 Seaborn 画散点图
df = pd.DataFrame({'x': x, 'y': y})
sns.jointplot(x="x", y="y", data=df, kind='scatter');
plt.show()


# 数据准备
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]
# 使用 Matplotlib 画折线图
plt.plot(x, y)
plt.show()
# 使用 Seaborn 画折线图
df = pd.DataFrame({'x': x, 'y': y})
sns.lineplot(x="x", y="y", data=df)
plt.show()

# 数据准备
a = np.random.randn(100)
s = pd.Series(a)

print("hist")
print(s)
# 用 Matplotlib 画直方图
plt.hist(s)
plt.show()
# 用 Seaborn 画直方图
sns.distplot(s, kde=False)
plt.show()
sns.distplot(s, kde=True)
plt.show()


# 数据准备
x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
y = [5, 4, 8, 12, 7]
# 用 Matplotlib 画条形图
plt.bar(x, y)
plt.show()
# 用 Seaborn 画条形图
sns.barplot(x, y)
plt.show()


# 数据准备
# 生成 0-1 之间的 10*4 维度数据
data = np.random.normal(size=(10, 4))
print("data = np.random.normal(size=(10, 4))")
print(data)
lables = ['A', 'B', 'C', 'D']
# 用 Matplotlib 画箱线图
plt.boxplot(data, labels=lables)
plt.show()
# 用 Seaborn 画箱线图
df = pd.DataFrame(data, columns=lables)
sns.boxplot(data=df)
plt.show()


# 数据准备
nums = [25, 37, 33, 37, 6]
labels = ['High-school', 'Bachelor', 'Master', 'Ph.d', 'Others']
# 用 Matplotlib 画饼图
plt.pie(x=nums, labels=labels)
plt.show()


# 数据准备
flights = sns.load_dataset("flights")
data = flights.pivot('year', 'month', 'passengers')
# 用 Seaborn 画热力图
sns.heatmap(data)
plt.show()



# 数据准备
labels = np.array([u" 推进 ", "KDA", u" 生存 ", u" 团战 ", u" 发育 ", u" 输出 "])
stats = [83, 61, 95, 67, 76, 88]
# 画图数据准备，角度、状态值
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
print("angles")
print(angles)
stats = np.concatenate((stats, [stats[0]]))
print(stats)
angles = np.concatenate((angles, [angles[0]]))
print(angles)
# 用 Matplotlib 画蜘蛛图
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
# ax.plot(angles, stats, 'x-', linewidth=2)
ax.fill(angles, stats, alpha=0.25)
# ax.fill(angles, stats, alpha=2)
# 设置中文字体
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
ax.set_thetagrids(angles * 180/np.pi, labels, FontProperties=font)
plt.show()


tips = sns.load_dataset("tips")
print(tips.head(10))
# 用 Seaborn 画二元变量分布图（散点图，核密度图，Hexbin 图）
sns.jointplot(x="total_bill", y="tip", data=tips, kind='scatter')
plt.show()
sns.jointplot(x="total_bill", y="tip", data=tips, kind='kde')
plt.show()
sns.jointplot(x="total_bill", y="tip", data=tips, kind='hex')
plt.show()


# 数据准备
iris = sns.load_dataset('iris')
# 用 Seaborn 画成对关系
sns.pairplot(iris)
plt.show()
'''

# 作业
car_crashes = sns.load_dataset('car_crashes')
print(car_crashes)
# 用 Seaborn 画成对关系
sns.pairplot(car_crashes)
plt.show()

# 用 Seaborn 画二元变量分布图（散点图，核密度图，Hexbin 图）
sns.jointplot(x="total", y="no_previous", data=car_crashes, kind='scatter')
plt.show()
sns.jointplot(x="total", y="no_previous", data=car_crashes, kind='kde')
plt.show()
sns.jointplot(x="total", y="no_previous", data=car_crashes, kind='hex')
plt.show()