# result = []
# for num1 in range(1, 10):
#     tmp = []
#     for num2 in range(1, 10):
#         tmp.append(f'{num1*num2:2}')
#     result.append(tmp)

# for row in result:
#     print(','.join(row))

# result = [[f'{num1*num2:2}' for num2 in range(1, 10)] for num1 in range(1, 10)]

# for count, row in zip(range(1, 10), result):
#     print(','.join(row))

# PI = 3.14
# r = 1
# print(2 * PI * r)
# print(PI * r ** 2)
# r = 2
# print(2 * PI * r)
# r += 1
# print(PI * r ** 2)

# print('It's')

# user_input = input('input some number:')
# result = user_input * 2
# print(result)

# user_input = input('input some number:')
# int_value = int(user_input)
# result = int_value * 2
# print(result)

# user_input = input('input some number:')
# int_value = int(user_input)
# result = str(int_value) + '*2=' + str(int_value*2)
# print(result)

sample_str = 'find,rfind,index,rindex'
print(sample_str.find('index'))
print(sample_str.rfind('index'))
print(sample_str.find('foo'))
print(sample_str.index('find'))
print(sample_str.rindex('find'))
print(sample_str.index('foo'))
