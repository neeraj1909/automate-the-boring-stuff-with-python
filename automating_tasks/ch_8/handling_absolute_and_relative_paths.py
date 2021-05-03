import os


print(os.path.abspath('.'))
print(os.path.abspath('./ch_7'))
print('\n')
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))
print('\n')
print(os.path.relpath('/home/neeraj/Code/automate-the-boring-stuff-with-python/automating_tasks/ch_8', '/home/neeraj/Code/automate-the-boring-stuff-with-python/automating_tasks'))
print(os.path.relpath('/home/neeraj/Code/automate-the-boring-stuff-with-python/automating_tasks/ch_8', '/home/neeraj/Code/automate-the-boring-stuff-with-python/'))
print(os.getcwd())
print('\n')

# Dir-name and Base-name
path = '/home/neeraj/Code/automate-the-boring-stuff-with-python/automating_tasks/ch_8'
print(os.path.dirname(path))
print(os.path.basename(path))
print(os.path.split(path))
print(path.split(os.path.sep))
