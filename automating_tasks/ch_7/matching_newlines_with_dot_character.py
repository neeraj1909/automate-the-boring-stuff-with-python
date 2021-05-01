import re


no_newline_regex = re.compile(r'.*')
mo1 = no_newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo1.group())

newline_regex = re.compile('.*', re.DOTALL)
mo2 = newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo2.group())
