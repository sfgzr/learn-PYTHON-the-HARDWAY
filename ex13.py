# -*- coding: utf-8 -*-

from sys import argv

#必须这样运行：python2 ex13.py first 2nd 3rd （4个参数）
#把argv解包（unpack），将所有参数依次赋值给左边的变量
script, first, second, third=argv

print "The script is called:",script
print "Your first variable is:",first
print "Your second variable is:",second
print "Your third variable is:",third
