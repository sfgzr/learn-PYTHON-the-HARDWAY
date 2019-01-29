# -*- coding:utf-8 -*-
print "How old are you?",  #加逗号不会输出换行符,在同一行
age=raw_input()
print "How tall are you?"
height=raw_input()
print "How much do you weight?"
weight=raw_input()

print "So,you're %s old,%s tall and %s heavy."%(age,height,weight)

#当输入为纯数字时
	#input返回的是数值类型，如int,float
    #raw_inpout返回的是字符串类型，string类型
#输入字符串为表达式
	#input会计算在字符串中的数字表达式，而raw_input不会。
