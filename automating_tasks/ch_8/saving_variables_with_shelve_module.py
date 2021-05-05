import shelve


shelf_file = shelve.open('/home/neeraj/mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelf_file['cat'] = cats
shelf_file.close()

# reopen and retrieve the data from shelf file
shelf_file = shelve.open('/home/neeraj/mydata')
print(type(shelf_file))
print(shelf_file['cat'])
shelf_file.close()

# shelf 'keys()' and 'values()' method
shelf_file = shelve.open('/home/neeraj/mydata')
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
print('\n')
print(shelf_file.keys())
print(shelf_file.values())
shelf_file.close()
