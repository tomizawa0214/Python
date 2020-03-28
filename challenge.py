# coding:utf-8

##print([i for i in range(10)])
##print([i * 3 for i in range(10)])
##print([i * 3 for i in range(10) if i % 2 == 0])

# print(i * 3 for i in range(10) if i % 2 == 0)
# print({i * 3 for i in range(10) if i % 2 == 0})

# number = input('何か値を入力してください:')
# number = int(number)

# if number % 2 == 0:
#     print('even')

number = input('何か値を入力してください:')
number = int(number)

if number % 15 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)
