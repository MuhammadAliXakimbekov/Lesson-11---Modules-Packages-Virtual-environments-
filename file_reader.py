def read_file(file_path):
    with open(file_path, 'r') as a:
        return a.read()
    
print(read_file('requerement.txt'))