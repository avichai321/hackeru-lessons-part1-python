print("******** into file_append.py ********")

# a = append - add the content to the end of content..
# open the file for append contact, if not exist create new one

my_file1 = open('demo_files/demo_append_to_file1.txt', 'a')
my_file1.write('\n hola class we create NEW File and write in file.. \nPython.. :) ')
my_file1.close()

# Example - append to file with Hebrew
my_file2 = open("demo_files/demo_append_to_file2.txt", 'a', encoding='utf-8')
my_file2.write("שורה חדשה התווספה.. \n")    # encoding='utf-8'
my_file2.close()


# Example - append to python file
my_file3 = open('demo_files/demo_append_to_python_file.py', 'a')
my_file3.write("""print('Hola')\n""")
my_file3.close()

