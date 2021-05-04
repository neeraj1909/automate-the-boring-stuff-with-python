import os


# opening the file
hello_file = open('/home/neeraj/hello.txt', 'r')

# reading the contents of file
hello_content = hello_file.read()
print(hello_content)

# read file using readlines() method
sonnet_file = open('/home/neeraj/sonnet29.txt')
print(sonnet_file.readlines())

# writing to files
bacon_file = open('/home/neeraj/bacon.txt', 'w')
print(bacon_file.write('Hello world!\n'))
bacon_file.close()

bacon_file = open('/home/neeraj/bacon.txt', 'a')
print(bacon_file.write('Bacon is not a vegetable.'))
bacon_file.close()

bacon_file = open('/home/neeraj/bacon.txt')
content = bacon_file.read()
bacon_file.close()
print(content)
