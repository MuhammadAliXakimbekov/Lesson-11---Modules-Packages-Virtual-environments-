
def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()  
    
print(read_file('requirements.txt'))
   