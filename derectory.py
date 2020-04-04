import os
# print(os.getcwd())

os.chdir('..')
# print(os.getcwd())
os.chdir('/Users/jtomi/Python')
# print(os.getcwd())

# print('using os.listdir')
# for name in os.listdir():
#     if os.path.isfile(name):
#         print(f'file: {name}')
#     else:
#         print(f'dir: {name}')

# print('using os.scandir')
# for entry in os.scandir():
#     if entry.is_file():
#         print(f'file: {entry.name}')
#     else:
#         print(f'dir: {entry.name}')

# os.mkdir('aaa')
# os.mkdir('xxx')
# os.system('echo aaa > aaa/aaa.txt')
# os.system('echo xxx > xxx/xxx.txt')

# os.rename('aaa/aaa.txt', 'xxx/aaa.txt')
# os.rename('xxx/aaa.txt', 'aaa/bbb.txt')
# os.rename('aaa/bbb.txt', 'xxx/xxx.txt')

# os.makedirs('top/aaa/bbb')
# os.makedirs('top/xxx/yyy')
# os.system('echo aaa > top/aaa/aaa.txt')
# os.system('echo bbb > top/aaa/bbb/bbb.txt')
# os.system('echo xxx > top/xxx/xxx.txt')
# os.system('echo yyy > top/xxx/yyy/yyy.txt')

for dirpath, dirnames, filenames in os.walk('top', topdown=False):
    print(f'now in {dirpath}')
    print(f'dirs in {dirpath}: {dirnames}')
    print(f'files in {dirpath}: {filenames}')