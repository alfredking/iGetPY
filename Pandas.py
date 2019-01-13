import pandas as pd
import numpy as np
from pandas import Series, DataFrame

x1 = Series([1, 2, 3, 4])
x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(x1)
print(x2)

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
x3 = Series(d)
print(x3)

data = {'Chinese': [66, 95, 93, 90, 80], 'Englis': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'], columns=['Englis', 'Math', 'Chinese'])
print(df1)
print(df2)

#df2.to_excel('data.xlsx')
#score = DataFrame(pd.read_excel('data.xlsx'))
#score.to_excel('data1.xlsx')
#print(score)

df2 = df2.drop(columns=['Chinese'])
df2 = df2.drop(index=['ZhangFei'])
df2.rename(columns={'chinese': 'YuWen', 'Englis': 'Yingyu'}, inplace=True)
df2 = df2.drop_duplicates()
df2['Math'].astype(np.int64)
df2['Math'] = df2['Math'].astype('str')
print(df2['Math'])

# 删除左右两边空格
df2['Math'] = df2['Math'].map(str.strip)
# 删除左边空格
df2['Math'] = df2['Math'].map(str.lstrip)
# 删除右边空格
df2['Math'] = df2['Math'].map(str.rstrip)

df2['Math'] = df2['Math'].str.strip('$')


# 全部大写
df2.columns = df2.columns.str.upper()
# 全部小写
df2.columns = df2.columns.str.lower()
# 首字母大写
df2.columns = df2.columns.str.title()

print('case transform')

score = DataFrame(pd.read_excel('data.xlsx'))
print(score.isnull())
print(score.isnull().any())

# apply函数
score['姓名'] = score['姓名'].apply(str.upper)


def double_df(x):
    return 2*x


score[u'语文'] = score[u'语文'].apply(double_df)

print(score)


def plus(df, n, m):
    df['new1'] = (df[u'语文']+df[u'英语'])*m
    df['new2'] = (df[u'语文']+df[u'英语'])*n
    return df


print(score)
# score = score.apply(plus, axis=1, args=(2, 3))
score = score.apply(plus, axis=0, args=(2, 3))
print(score)
