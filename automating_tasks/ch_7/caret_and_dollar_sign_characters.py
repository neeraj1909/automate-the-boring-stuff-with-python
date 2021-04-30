import re


begins_with_hello = re.compile(r'^Hello')
mo1 = begins_with_hello.search('Hello world!')
print(mo1)

mo2 = begins_with_hello.search('He said hello.')
print(mo2 == None)

ends_with_number = re.compile(r'\d$')
mo3 = ends_with_number.search('Your number is 42')
print(mo3)

mo4 = ends_with_number.search('Your number is forty two.')
print(mo4 == None)

whole_string_is_num = re.compile(r'^\d+$')
mo5 = whole_string_is_num.search('1234567890')
print(mo5)

mo6 = whole_string_is_num.search('12345xyz67890')
print(mo6 == None)

mo7 = whole_string_is_num.search('12  34567890')
print(mo7 == None)

