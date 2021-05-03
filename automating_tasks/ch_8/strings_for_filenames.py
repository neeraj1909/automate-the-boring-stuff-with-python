import os


print(os.path.join('usr', 'bin', 'spam'))

my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for file_name in my_files:
    print(os.path.join('/home/neeraj/asweigart', file_name))


# Current Working Directory
print(os.getcwd())

os.chdir('/home/neeraj/Code/automate-the-boring-stuff-with-python/automating_tasks/ch_7')
print(os.getcwd())

os.chdir('/home/neeraj/ThisFolderDoesNotExist')
