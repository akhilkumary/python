with open('my_file.txt', mode='r') as f:
    contents = f.read()
    print(contents)

with open('new_file.txt', mode='w') as f:
    f.write('New Text')

with open('new_file.txt', mode='a') as f:
    f.write('\n......')
