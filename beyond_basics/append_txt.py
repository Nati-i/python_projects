from datetime import datetime
files = 'file1.txt file2.txt file3.txt'.split()


with open(files[0],'r') as file1:
    file1 = file1.read()
with open(files[1],'r') as file2:
    file2 = file2.read()
with open(files[2],'r') as file3:
    file3 = file3.read()

content = [file1,file2,file3]

with open((str(datetime.now().strftime('%b %d,%Y')) + '.txt'),'w') as f:
    for filecontent in content:
        f.write(filecontent + '\n')
