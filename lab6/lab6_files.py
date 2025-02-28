#task1
import os
def list_directories(path):
    directories = []
    for i in os.listdir(path):
        i_path = os.path.join(path,i)
        if os.path.isdir(i_path):
            directories.append(i)
    return directories
path = "C:/Users/nitro5"
print(list_directories(path))

#task2
import os
path = input()
if os.access(path,os.F_OK):
    print("Exist")
    if os.access(path,os.R_OK):
        print("Readable")
    if os.access(path,os.W_OK):
        print("Writeable")
    if os.access(path,os.X_OK):
        print("Executable")
else:
    print("Does not exist")

#task3
import os
path = input()
if os.path.exists(path):
    dir_name = os.path.dirname(path)
    file_name = os.path.basename(path)
    print(f"dirname: {dir_name}\nfilename: {file_name}")
else:
    print("does not exist")

#task4
with open("text.txt","r") as File:
    a = File.readlines()
    print(len(a))

#task5
with open("text.txt","w") as write_file:
    a = input().split()
    for i in a:
        write_file.write(i+'\n')
print("write successfully")

#task6
for i in range(26):
    pattern = chr(65 + i)
    with open(f"{pattern}.txt","x"):
        pass

#task7
import shutil
shutil.copyfile("text.txt","new.txt")
print("Copied")

#task8
import os
path = input()
if os.access(path,os.F_OK):
    if os.path.exists(path):
        os.remove(path)
    print("Deleted")
else:
    print("This file does not exist")