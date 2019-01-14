import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from pandasql import sqldf, load_meat, load_births

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

# df2.to_excel('data.xlsx')
# score = DataFrame(pd.read_excel('data.xlsx'))
# score.to_excel('data1.xlsx')
# print(score)

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
score = score.apply(plus, axis=1, args=(2, 3))
# score = score.apply(plus, axis=0, args=(2, 3))
print(score)

df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
print(df1.describe())
df2 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2': range(5)})
df3 = pd.merge(df1, df2, on='name')
print(df3)
df3 = pd.merge(df1, df2, how='inner')
print(df3)
print('left')
df3 = pd.merge(df1, df2, how='left')
print(df3)
print('right')
df3 = pd.merge(df1, df2, how='right')
print(df3)
print('outer')
df3 = pd.merge(df1, df2, how='outer')
print(df3)

pysqldf = lambda sql : sqldf(sql, globals())
sql = "select * from df1 where name='ZhangFei'"
print(pysqldf(sql))

data = {'语文': [66, 95, 95, 90, 80, 80], '英语': [65, 85, 92, 88, 90, 90], '数学': [None, 98, 96, 77, 90, 90]}
exam = DataFrame(data)
exams = DataFrame(data, index=['张飞', '关羽', '赵云', '黄忠', '典韦', '典韦'], columns=['语文', '英语', '数学'])
print(exams)
exams = exams.drop_duplicates()
# exams = exams.replace(to_replace=None, value=0)
exams.fillna(0, inplace=True)
print(exams)


def sum(df):
    df['总和'] = (df[u'语文']+df[u'英语']+df[u'数学'])
    return df


exams = exams.dropna()
exams = exams.apply(sum, axis=1)
print(exams)

