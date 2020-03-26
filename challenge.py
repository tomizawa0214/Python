# coding:utf-8

##def is_even(n):
##    return n % 2 == 0

##print(list(filter(is_even, range(10))))

print(list(filter(lambda n: n % 2 ==0, range(10))))
