# The simpler way of doing this
# my_file = open('InputOutput/iotest.txt')

# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.close()

# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

# The better way of doing this
# with open('InputOutput/iotest.txt') as my_file:
#     print(my_file.read())

# with open('InputOutput/new-file.txt', 'w') as my_file:
#     text = my_file.write('Name Surname')

# Regular expressions
import re

text = 'Python is a high-level, general-purpose programming language.'

search = re.search('is', text)

print(search.span())
print(search.start())
print(search.end())
print(search.group())