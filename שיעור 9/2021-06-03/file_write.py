print("******** into file_write.py ********")

# w = write - change the content to new one..
# open the file for write contact, if not exist create new one


my_file1 = open('demo_files/demo_write_to_file.txt', 'w')
my_file1.write('hola class we create NEW File and write in file.. \nPython.. :) ')
my_file1.close()



my_file1 = open('demo_files/demo_write_to_file1.txt', 'w')
my_file1.write('בוקר טוב עולם מה שלום כולם.. \nPython.. :) ')
my_file1.close()

my_file1 = open('demo_files/demo_write_to_file2.txt', 'w',encoding='utf-8')
my_file1.write('בוקר טוב עולם מה שלום כולם.. \nPython.. :) ')
my_file1.close()

my_file1 = open('demo_files/demo_write_to_file3.py', 'w')
my_file1.write("""print('Hola')""")
my_file1.close()

