import re


"""
    "wo)?" part of the regular expression means that 
    the pattern wo is an optional group
"""
bat_regex = re.compile(r'Bat(wo)?man')
mo1 = bat_regex.search('The Adventures of Batman')
print(mo1.group())

mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo2.group())


"""
    Regex Look for phone numbers hat do or do not have an area code.
"""
phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# print(phone_regex)
mo1 = phone_regex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phone_regex.search('My number is 555-4242')
print(mo2.group())
