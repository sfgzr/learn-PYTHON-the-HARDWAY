# -*- coding: utf-8 -*-

from sys import argv

#把argv解包（unpack），将所有参数依次赋值给左边的变量
argv=raw_input("输入4个参数：")
script, first, second, third=argv

print "The script is called:",script
print "Your first variable is:",first
print "Your second variable is:",second
print "Your third variable is:",third

#argv：执行命令时输入
#raw_input：脚本运行过程中输入
