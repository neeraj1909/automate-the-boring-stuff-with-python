import re


vowel_regex = re.compile(r'[aeiouAEIOU]')
mo1 = vowel_regex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo1)

constant_regex = re.compile(r'[^aeiouAEIOU]')
mo2 = constant_regex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo2)
