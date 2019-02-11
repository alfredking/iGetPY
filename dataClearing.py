import pandas as pd
from pandas import Series, DataFrame

'''
foods = DataFrame(pd.read_excel('food.xlsx'))

foods['ounces'].fillna(foods['ounces'].mean(), inplace=True)
foods.to_excel('foodNew.xlsx')


ounces_maxf = foods['ounces'].value_counts().index[0]
print(foods['ounces'].value_counts())
foods['ounces'].fillna(ounces_maxf, inplace=True)
print(foods)


print(foods)
# 删除全空的行
# foods.dropna(how='all', inplace=True)
# 删除含空的行
foods.dropna(inplace=True)
print('after dropna')
print(foods)


# 获取 weight 数据列中单位为 lbs 的数据
rows_with_lbs = foods['weight'].str.contains('lbs').fillna(False)
print(rows_with_lbs)
print(foods[rows_with_lbs])
# 将 lbs 转换为 kgs, 2.2lbs=1kgs
for i, lbs_row in foods[rows_with_lbs].iterrows():
	# 截取从头开始到倒数第三个字符之前，即去掉 lbs。
	weight = float(lbs_row['weight'][:-3])/2.2
	foods.at[i,'weight'] = '{}kgs'.format(weight)
print(foods)



# 删除非 ASCII 字符
print(foods)
foods['food'].replace({r'[^\x00-\x7F]+': 'AK'}, regex=True, inplace=True)
print('删除非 ASCII 字符之后')
print(foods)


# 切分名字，删除源数据列
#foods[['first_name', 'last_name']] = foods['food'].str.split()
#print(foods)

foods[['first_name', 'last_name']] = foods['food'].str.split(expand=True)
print(foods)
foods.drop('food', axis=1, inplace=True)
print(foods)


# 删除重复数据行
foods.drop_duplicates(['first_name', 'last_name'], inplace=True)
'''

foods = DataFrame(pd.read_excel('foodExercise.xlsx'))

# 合法性：ounces列数据存在负值
foods['ounces'] = foods['ounces'].apply(lambda x: abs(x))

# 完整性：ounces 列数据中存在NAN
foods['ounces'].fillna(foods['ounces'].mean(), inplace=True)

# 全面性：food列数据中存在大小写不一致问题
foods['food'] = foods['food'].str.lower()

# 唯一性：food列数据存在重复
foods.drop_duplicates(['food', 'ounces', 'animal'], inplace=True)
# foods.drop_duplicates(['food'], inplace=True)
print(foods)
# newFood = foods.groupby(by='food').agg({'ounces': sum})
newFood = foods.groupby(['food', 'animal']).agg({'ounces': sum})
print(newFood)
foods.to_excel('foodNew.xlsx')
