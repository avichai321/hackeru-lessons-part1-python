print("******** into file_read.py ********")

# r = read - open for read content from file..
# open the file for read >> if not exist get ERROR (FileNotFoundError)

print("******** .readlines() ********")
file = open('file_read.txt', 'r')
file_lines = file.readlines()
file.close()

print(file_lines)
print( type(file_lines) )  # <class 'list'>



print("******** .read() ********")
file1 = open('file_read.txt', 'r')
file_lines1 = file1.read()
file1.close()

print( file_lines1 )
print( type(file_lines1) ) # <class 'str'>

print("******** read form pythone  ********")
file = open('file_read.py', 'r')
file_lines = file.readlines()
file.close()

print(file_lines)

print("******** for in my_file ********")
my_file = open('file_read.txt', 'r')
for i in my_file:
    print(i)



print("******** read form pythone  ********")
file = open('file_read.py', 'r')
file_lines = file.readlines()
file.close()

print(file_lines)
