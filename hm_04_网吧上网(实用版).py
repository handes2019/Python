# 系统可以用户输入年龄，用这个年龄做条件判断
"""
1、用户输入
2、保存用户输入的年龄
3、if
****** 注意一个点
"""

age = input('请输入您的年龄：')

if age.isdigit():
    if int(age) >= 18:
        print(f'您的年龄是{age}，已经成年，可以上网')
    else:
        print(f'您的年龄是{age}，小朋友，回家写代码')
else:
    print('输入有误')
print('结束')
