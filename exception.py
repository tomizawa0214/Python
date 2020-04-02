# import random
# answer = random.randint(1, 100)

# while True:
#     try:
#         number = int(input('100までの数値を入力してください:'))
#     except ValueError:
#         print('数字以外が入力されました。数字のみを入力してください')
#         continue
#     if answer < number:
#         print('もっと小さな数値です')
#     elif answer > number:
#         print('もっと大きな数値です')
#     else:
#         break

# print('素晴らしい！正解です！')

# while True:
#     try:
#         print()
#         print('1: ValueError例外を発生')
#         print('2: IndexError例外を発生')
#         print('3: 例外を発生させない')
#         print('4: 終了')
#         selection = int(input('どれにしますか:'))
#         if selection == 1:
#             tmp = int('foo')
#         elif selection == 2:
#             tmp = 'str'[5]
#         elif selection == 3:
#             print()
#             print('例外を発生させませんでした')
#         elif selection == 4:
#             print()
#             print('終了します')
#             break
#         else:
#             print(undefined_var)
#     except Exception as e:
#         print('Exception')
#         print(e.args)
#         print()
#     except ValueError as e:
#         print('Value Error')
#         print(e.args)
#         print()
#     except IndexError:
#         print('Index Error')
#         print()
#     print('try文の直後の行を実行しました')

# print('無限ループを終了しました')

# while True:
#     try:
#         print()
#         print('1: 例外を発生させる')
#         print('2: 例外を発生させない')
#         print('3: 終了')
#         selection = int(input('どれにしますか: '))
#         if selection == 1:
#             tmp = 'str'[5]
#         elif selection == 2:
#             print('例外を発生しませんでした')
#         elif selection == 3:
#             break
#     except IndexError:
#         print('IndexError例外が発生しました')
#     else:
#         print('else節を実行しました')
#     finally:
#         print('finally節を実行しました')

def raise_exception():
    try:
        raise ValueError()
    except IndexError:
        print('Index Error caught')
    finally:
        print('executing finally clause')

def call_raise_exception():
    try:
        raise_exception()
    except ValueError:
        print('Value Error caught')

def call_raise_exception2():
    raise_exception()

call_raise_exception()
call_raise_exception2()