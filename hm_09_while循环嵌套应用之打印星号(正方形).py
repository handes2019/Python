"""
1、打印1个星星
2、一行5个：循环 -- 5个星星在一行显示
3、打印5行星星: 循环 -- 一行5个

"""
j = 0
while j < 5:
    # 一行星星开始
    i = 0
    while i < 5:
        print('*', end='')
        i += 1
    # 一行星星结束：换行显示下一行
    print()
    j += 1
