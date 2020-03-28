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