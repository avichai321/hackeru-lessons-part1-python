print("******** into file_create.py ********")

'''
Python File - working with files 
Create, Read, Update, Delete 

.open() / .close() 

x  - create file   
r  - read file (if file is not exist error - No such file or directory)
w  - write (if not exist will create new file )
a  - append to file (add to end of file)


wb - write binary file
rb - read binary file 
 
'''


# X = craete - create new file..
# open the file for read >> if exist get ERROR (FileExistsError)
# close - on the end to work with file..

file = open('demo_files/file_create2.txt', 'x')
file.close()