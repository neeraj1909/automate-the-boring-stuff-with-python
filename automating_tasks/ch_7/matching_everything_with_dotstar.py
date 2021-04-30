import re


at_regex = re.compile(r'.at')
mo1 = at_regex.findall('The cat in the hat sat on the flat mat')
print(mo1)

name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo2 = name_regex.search('First Name: Al Last Name: Sweigart')
print(mo2.group(1))
print(mo2.group(2))

non_greedy_regex = re.compile(r'<.*?>')
mo3 = non_greedy_regex.search('<To serve man> for dinner.>')
print(mo3.group())

greedy_regex = re.compile(r'<.*>')
mo4 = greedy_regex.search('<To serve man> for dinner.>')
print(mo4.group())
