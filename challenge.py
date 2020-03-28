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

# number = input('何か値を入力してください:')
# number = int(number)

# if number % 15 == 0:
#     print('FizzBuzz')
# elif number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# else:
#     print(number)

# names = ['一色', 'かわさき', '遠藤']
# target = 'かわさき'

# for name in names:
#     if target in name:
#         print(f'発見: {name}')
#         break
# else:
#     print('見つかりませんでした')

# names = ['一色', 'かわさき', 'かわさきしんじ', '遠藤']
# target = 'かわさき'

# for name in names:
#     if target in name:
#         print(f'発見: {name}')
#         break
#     print('繰り返し処理を継続します')
# else:
#     print('見つかりませんでした')

# names = ['一色', 'かわさき', 'かわさきしんじ', '遠藤']
# target = 'かわさき'

# for name in names:
#     if target in name:
#         print(f'発見: {name}')
#         continue
#     print('繰り返し処理を継続します')
# else:
#     print('見つかりませんでした')

# names = ['一色', 'かわさき', 'かわさきしんじ', '遠藤']
# target = 'かわさき'
# found = False

# for name in names:
#     if target in name:
#         found = True
#         print(f'発見: {name}')
#         continue
#     print('繰り返し処理を継続します')
    
#     if not found:
#         print('見つかりませんでした')

# def hello(whom):
#     message = 'Hello' + str(whom)
#     print(message)

# hello(' World')

# def get_ans4ultimateQ():
    # return 42
    # print('can not reach this line')

# result = get_ans4ultimateQ()
# print(get_ans4ultimateQ())
# print(result)

# def myfunc(param1, param2, param3):
#     return f'param1: {param1}, param2: {param2}, param3: {param3}'

# print(myfunc(param3=1, param2='string', param1=0.5))
# print(myfunc(*'abc'))
# print(myfunc(1, *'23'))
# print(myfunc(*'12', 3))
# arg_dict = {'param3': 'param3', 'param2': 2, 'param1': 1.0}
# print(myfunc(**arg_dict))

# def myfunc(param1='param1', param2='parm2', param3='param3'):
#     return f'param1: {param1}, param2: {param2}, param3: {param3}'

# print(myfunc())
# print(myfunc(1))
# print(myfunc(param2=2))

# def myfunc(param1='param1', param2, param3):
#     return f'param1: {param1}, param2: {param2}, param3: {param3}'

# print(myfunc(param2=2, param3=3))

# def myfunc(param1, param2, *args):
#     return f'param1: {param1}, param2: {param2}, other: {args}'

# print(myfunc(1, 2))
# print(myfunc(1, 2, 3))
# print(myfunc(1, 2, 3, 4))

# def myfunc(param1, param2, *args):
#     tmp = f'param1: {param1}, param2: {param2}'
#     index = 3
#     for item in args:
#         tmp += f', param{index}: {item}'
#         index += 1
#     return tmp

# print(myfunc(1, 2))
# print(myfunc(1, 2, 3))
# print(myfunc(1, 2, 3, 4))
# print(myfunc(1, 2, 2, 3, 4))

# def myfunc(*args, param1):
#     return f'param1: {param1}, others: {args}'

# print(myfunc(1, param1='2'))

# def myfunc(param1, **kwargs):
#     return f'param1: {param1}, others: {kwargs}'

# print(myfunc(param4='param2', param1=1, fool='foo'))

def myfunc(param1, **kwargs):
    tmp = f'param1: {param1}'
    for item in kwargs.items():
        tmp += f', {item[0]}: {item[1]}'
    return tmp

print(myfunc(param2='param2', param1=1, foo='foo'))