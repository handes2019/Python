# 多行多个乘法表达式 x * x =x*x
"""
1、打印一个乘法表达式:x * x =x*x
2、一行打印多个表达式 -- 一行表达式的个数和行号数相等 -- 循环: 一个表达式
3、打印多行表达式 -- 循环：一行表达式 -- 换行

**** 一行表达式的个数和行号数相等

"""

j = 1
while j <= 9:
    #   一行的表达式开始
    i = 1
    while i <= j:

        print(f'{i} * {j} ={i*j}', end='\t')
        i += 1

    #   一行的表达式结束
    print()
    j += 1

