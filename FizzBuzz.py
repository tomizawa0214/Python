# if number % 3 == 0 and number % 5 == 0:
#     print('FizzBuzz')
# elif number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# else:
#     print(number)

def fizzbuzz(number):
    result = str(number)
    if number % 3 == 0 and number % 5 == 0:
        result = 'FizzBuzz'
        # print('FizzBuzz')
        # return 'FizzBuzz'
    elif number % 3 == 0:
        result = 'Fizz'
        # print('Fizz')
        # return 'Fizz'
    elif number % 5 == 0:
        result = 'Buzz'
        # print('Buzz')
        # return 'Buzz'
    return result
    # else:
        # print(str(number))
        # return (number)

number = input('何か数値を入力してください:')
number = int(number)

print(fizzbuzz(number))