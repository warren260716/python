# -*- coding: utf-8 -*-
for i in range(10):
    if(i <= 0):
        continue # i = i + 1的意思
    j = 1
    while 1: #1是true的意思，寫true也可以
        print(i, '*', j, '=', i*j, end='\t') #end='\t'：按一次tab鍵的意思
        j = j + 1
        if (j > 9):
            break
    print ()
print ()