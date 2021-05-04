import os


print(os.path.getsize('/home/neeraj/Code/automate-the-boring-stuff-with-python/automating_tasks/ch_8/strings_for_filenames.py'))
print(os.listdir('/home/neeraj/Code/automate-the-boring-stuff-with-python/automating_tasks/ch_8'))


# calculate total size of a folder
total_size = 0

for file_name in os.listdir('/home/neeraj/Code/automate-the-boring-stuff-with-python/automating_tasks/ch_8'):
    total_size = total_size + os.path.getsize(os.path.join('/home/neeraj/Code/automate-the-boring-stuff-with-python/automating_tasks/ch_8', file_name))
    
print(total_size)
