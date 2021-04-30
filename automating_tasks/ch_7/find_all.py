import re


phone_num_regex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phone_num_regex1.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo1.group())

phone_num_regex2 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo2 = phone_num_regex2.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo2)

phone_num_regex3 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
mo3 = phone_num_regex3.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo3)
