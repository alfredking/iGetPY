
#import scikit-learn

# 输入输出 代码缩进在 Python 中是一种语法
#name = input("What's youy name")
sum = 100+100
#print('hello ,%s' %name)
print('sum=%d' %sum)


#判断语句 if else

score = 70
print(score)
if score>=90:
   print ('Excellent')
else:
   if score<60:
     print ('Fail')
   else:
     print ('Good Job')

#循环语句 for in
sum = 0
for number in range(11): #从0到10
    sum = sum + number
print(sum)

#循环语句 while
sum = 0
number = 1
while number<11:
    sum = sum + number
    number = number +1
print(sum)

#列表 []
lists = ['a','b','c']
lists.append('d')
print(lists)
print(len(lists))
lists.insert(0,'mm')
print(lists)
lists.pop()
print(lists)


#元组(tuple)
tuples = ('tupleA','tupleB')
print(tuples[0])

#字典

score = {'guanyu':95,'zhangfei':96}
score['zhaoyun'] = 98
print(score)
score.pop('zhangfei')
print(score)
print('guanyu' in score)
print('zhangfei' in score)

print(score.get('guanyu'))
print(score.get('yase',99))
print(score)


#字典 set
s = set(['a','b','c'])
print(s)
s.add('d')
print(s)
s.remove('b')
print(s)
print('c' in s)

'''
注释
注释
注释
# 导入一个模块
import model_name
# 导入多个模块
import module_name1,module_name2
# 导入包中指定模块 
from package_name import moudule_name
# 导入包中所有模块 
from package_name import *


'''

#函数 def
def addone(score):
    return score+1
print(addone(99))

'''
#A+B problem
line = input()
a = line.split()
print(int(a[0])+int(a[1]))
'''

sum = 0
for number in range(1,100,2): #从1开始到99 步长为2
    sum = sum + number
    print(number)
print(sum)