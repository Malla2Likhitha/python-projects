# file = open('hello.txt')
# contents = file.read()
# print(contents)
# file.close()

# # need not close, with keyword will close once this indented block is run
# # only one mode at a time
# # default mode = 'r'
# with open('hello.txt') as file:
#     contents = file.read()
#     print(contents)

# # write - overwrites
# with open('hello.txt', mode='w') as file:
#     file.write('Yayyyyy!!')
#
# with open('hello.txt') as file:
#     contents = file.read()
#     print(contents)

# # append - adds text rather than overwrite
# with open('hello.txt', mode='a') as file:
#     file.write('\nYayyyyy!!')
#
# with open('hello.txt') as file:
#     contents = file.read()
#     print(contents)

# # create - open a new file
# with open('new_file.txt', mode='w') as file:
#     file.write('Lalalala!!')

# # This gives an error, creating cn be done with write mode only
# with open('new.txt') as file:
#     print(file.read())

# yo.txt in desktop
# not working bcuz our code is in E dir, can't reach C(root)
# with open('/Users/Ramanaji/Desktop/yo.txt') as file:
# yo.txt in E - works as E is reachable
with open('../../../yo.txt') as file:
    contents = file.read()
    print(contents)

# import os
# # print(os.getcwd())
# ROOT_DIR = os.path.dirname(os.path.abspath(os.curdir))
# print(ROOT_DIR)
