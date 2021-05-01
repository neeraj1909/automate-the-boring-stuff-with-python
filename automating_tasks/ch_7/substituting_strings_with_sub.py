import re


names_regex = re.compile(r'Agent \w+')
mo1 = names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo1)

agent_names_regex = re.compile(r'Agent (\w)\w*')
mo2 = agent_names_regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo2)
