import re


greedy_Ha_regex = re.compile(r'(Ha){3,5}')
mo1 = greedy_Ha_regex.search('HaHaHaHaHa')
print(mo1.group())

nongreedy_Ha_regex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedy_Ha_regex.search('HaHaHaHaHa')
print(mo2.group())
