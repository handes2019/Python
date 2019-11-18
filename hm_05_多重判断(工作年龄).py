"""
需求：
    如果年龄小于18.为童工，不合法；
    如果年龄18-60岁之间，为合法工作年龄
    如果年龄大于60为退休年龄
"""

"""
步骤：
    1、用户输入自己的年龄，保存变量 -- str
    2、if做判断 elif
    3、输出提示信息：您输入的年龄是X,合法与否

"""

age = int(input('请输入您的年龄:'))
# 童工
if age < 18:
    print(f'您输入的年龄是{age},童工')
# 18-60 合法
elif (age >= 18) and (age <= 60):
    print(f'您输入的年龄是{age},合法')
# 大于60 退休年龄
elif age > 60:
    print(f'您输入的年龄是{age},退休年龄')
