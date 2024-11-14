def write_file(file_path, content):
    with open(file_path, 'w') as a:
         a.write(content)
    
print(write_file('example.txt', 'Hello Uzbekistan'))