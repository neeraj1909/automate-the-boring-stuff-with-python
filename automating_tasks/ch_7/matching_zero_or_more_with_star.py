import re

"""
    Match zero or more
"""
bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('The Adventures of Batman')
print(mo1.group())

mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = bat_regex.search('The Adventures of Batwowowowoman')
print(mo3.group())
